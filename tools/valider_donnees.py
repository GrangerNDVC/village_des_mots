#!/usr/bin/env python3
"""Valide tous les modules d'exercices et vérifie que data/index.json est à jour.
Usage : python tools/valider_donnees.py        (code de sortie 1 en cas d'erreur)
"""
import glob, json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import construire_index

RACINE = construire_index.RACINE
DONNEES = construire_index.DONNEES
TYPES = {"qcm", "vrai_faux", "texte_trous", "saisie", "tri", "clic_mot", "association", "ordre", "corriger"}
FORMES = {"reconnaitre", "completer", "produire", "transformer", "corriger", "contexte"}
PREFIXES = {"grammaire": "gram", "orthographe": "ortho", "conjugaison": "conj", "vocabulaire": "vocab"}
GRADES = {6: "page", 5: "ecuyer", 4: "chevalier", 3: "maitre"}
erreurs, avertissements = [], []


def rel(f):
    return os.path.relpath(f, RACINE).replace(os.sep, "/")


def err(f, msg):
    erreurs.append(rel(f) + " : " + msg)


def warn(f, msg):
    avertissements.append(rel(f) + " : " + msg)


def liste_str(v, mini=1):
    return isinstance(v, list) and len(v) >= mini and all(isinstance(x, str) and x.strip() for x in v)


def verifier_exercice(f, mod, e, comps_ref, vus):
    eid = e.get("id", "?")
    pre = "exercice " + str(eid) + " : "
    if not re.fullmatch(re.escape(mod["module"]) + r"-\d{3}", str(eid)):
        err(f, pre + "identifiant invalide (attendu " + mod["module"] + "-NNN)")
    if eid in vus:
        err(f, pre + "identifiant en double")
    vus.add(eid)
    if e.get("type") not in TYPES:
        err(f, pre + "type inconnu " + str(e.get("type"))); return
    if e.get("forme") not in FORMES:
        err(f, pre + "forme inconnue " + str(e.get("forme")))
    if e.get("difficulte") not in (1, 2, 3):
        err(f, pre + "difficulte doit valoir 1, 2 ou 3")
    for champ in ("consigne", "explication"):
        if not isinstance(e.get(champ), str) or not e[champ].strip():
            err(f, pre + "champ " + champ + " manquant")
    c = e.get("competence")
    if c not in mod.get("competences", []):
        err(f, pre + "competence " + str(c) + " absente de la liste du module")
    if c not in comps_ref:
        err(f, pre + "competence " + str(c) + " absente de data/competences.json")
    t = e["type"]
    if t == "qcm":
        ch = e.get("choix")
        if not liste_str(ch, 2): err(f, pre + "choix invalides")
        elif not isinstance(e.get("reponse"), int) or not 0 <= e["reponse"] < len(ch): err(f, pre + "reponse hors des choix")
        elif len(set(ch)) != len(ch): err(f, pre + "choix en double")
    elif t == "vrai_faux":
        if not isinstance(e.get("enonce"), str): err(f, pre + "enonce manquant")
        if not isinstance(e.get("reponse"), bool): err(f, pre + "reponse doit être true ou false")
    elif t == "texte_trous":
        en, tr = e.get("enonce", ""), e.get("trous")
        if not isinstance(tr, list) or not tr: err(f, pre + "trous manquants"); return
        ids = set()
        for x in tr:
            if not isinstance(x.get("id"), int): err(f, pre + "trou sans id entier"); continue
            ids.add(x["id"])
            ch = x.get("choix")
            if not liste_str(ch, 2): err(f, pre + "choix du trou " + str(x["id"]) + " invalides")
            elif not isinstance(x.get("reponse"), int) or not 0 <= x["reponse"] < len(ch): err(f, pre + "reponse du trou " + str(x["id"]) + " hors des choix")
        marques = {int(m) for m in re.findall(r"\{\{(\d+)\}\}", en)}
        if marques != ids: err(f, pre + "les marques {{n}} de l'énoncé ne correspondent pas aux trous")
    elif t == "saisie":
        if not liste_str(e.get("reponses_acceptees")): err(f, pre + "reponses_acceptees invalides")
    elif t == "tri":
        el, ca, so = e.get("elements"), e.get("categories"), e.get("solution")
        if not liste_str(el, 2) or not liste_str(ca, 2) or not isinstance(so, dict): err(f, pre + "tri mal formé"); return
        if set(so) != set(el): err(f, pre + "solution et elements ne correspondent pas")
        if any(not isinstance(v, int) or not 0 <= v < len(ca) for v in so.values()): err(f, pre + "indice de catégorie invalide")
    elif t == "clic_mot":
        mo, ci = e.get("mots"), e.get("cibles")
        if not liste_str(mo, 2) or not isinstance(ci, list) or not ci: err(f, pre + "clic_mot mal formé"); return
        if any(not isinstance(i, int) or not 0 <= i < len(mo) for i in ci): err(f, pre + "cible hors des mots")
    elif t == "association":
        p = e.get("paires")
        if not isinstance(p, list) or len(p) < 2 or any(not liste_str(x, 2) or len(x) != 2 for x in p): err(f, pre + "paires invalides"); return
        if len({x[0] for x in p}) != len(p): err(f, pre + "éléments de gauche en double")
    elif t == "ordre":
        a, b = e.get("elements_melanges"), e.get("reponse")
        if not liste_str(a, 2) or not liste_str(b, 2): err(f, pre + "ordre mal formé"); return
        if sorted(a) != sorted(b): err(f, pre + "elements_melanges et reponse n'ont pas les mêmes éléments")
        if a == b: warn(f, pre + "les éléments mélangés sont déjà dans l'ordre")
    elif t == "corriger":
        if not isinstance(e.get("phrase_fautive"), str) or not liste_str(e.get("corrections_acceptees")): err(f, pre + "corriger mal formé")
        elif e["phrase_fautive"] in e["corrections_acceptees"]: err(f, pre + "la phrase fautive figure parmi les corrections")


def verifier_module(f, comps_ref):
    try:
        with open(f, encoding="utf-8") as fh:
            m = json.load(fh)
    except Exception as ex:
        err(f, "JSON illisible : " + str(ex)); return
    for champ in ("module", "titre", "domaine", "niveau", "grade", "version", "rappel", "competences", "exercices"):
        if champ not in m:
            err(f, "champ " + champ + " manquant"); return
    mid, dom, niv = m["module"], m["domaine"], m["niveau"]
    if dom not in PREFIXES: err(f, "domaine inconnu"); return
    if not re.fullmatch(PREFIXES[dom] + r"-" + str(niv) + r"e-[a-z0-9-]+", mid): err(f, "identifiant du module incohérent avec domaine/niveau")
    if GRADES.get(niv) != m["grade"]: err(f, "grade incohérent avec le niveau (attendu " + str(GRADES.get(niv)) + ")")
    attendu = os.path.join(DONNEES, "exercices", dom, str(niv) + "e", mid + ".json")
    if os.path.abspath(f) != os.path.abspath(attendu): err(f, "emplacement attendu : " + rel(attendu))
    vus = set()
    par_comp = {}
    for e in m["exercices"]:
        verifier_exercice(f, m, e, comps_ref, vus)
        par_comp.setdefault(e.get("competence"), []).append(e)
    for c, liste in par_comp.items():
        formes = {e.get("forme") for e in liste}
        if len(liste) < 5: warn(f, "compétence " + str(c) + " : seulement " + str(len(liste)) + " exercice(s) (objectif 12 ou plus)")
        if len(formes) < 4: warn(f, "compétence " + str(c) + " : seulement " + str(len(formes)) + " forme(s) (objectif 4 ou plus)")


def main():
    with open(os.path.join(DONNEES, "competences.json"), encoding="utf-8") as fh:
        comps_ref = {c["id"] for c in json.load(fh)["competences"]}
    fichiers = sorted(glob.glob(os.path.join(DONNEES, "exercices", "**", "*.json"), recursive=True))
    for f in fichiers:
        verifier_module(f, comps_ref)
    chemin_index = os.path.join(DONNEES, "index.json")
    try:
        with open(chemin_index, encoding="utf-8") as fh:
            actuel = json.load(fh)
        if actuel != construire_index.construire():
            err(chemin_index, "obsolète : lancez python tools/construire_index.py")
    except FileNotFoundError:
        err(chemin_index, "absent : lancez python tools/construire_index.py")
    for a in avertissements: print("AVERTISSEMENT", a)
    for e in erreurs: print("ERREUR", e)
    print(str(len(fichiers)) + " module(s) vérifié(s), " + str(len(erreurs)) + " erreur(s), " + str(len(avertissements)) + " avertissement(s)")
    sys.exit(1 if erreurs else 0)


if __name__ == "__main__":
    main()
