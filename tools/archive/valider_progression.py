#!/usr/bin/env python3
"""Valide carte-notions.json / progression.json et simule les règles.
Usage : python3 tools/valider_progression.py  (depuis la racine du projet)"""
import json, random, re, math, sys, pathlib
R = pathlib.Path(__file__).resolve().parent.parent / "data"
carte = json.load(open(R/"carte-notions.json", encoding="utf-8"))
prog = json.load(open(R/"progression.json", encoding="utf-8"))
err = []

# ---- 1. validation de la carte
ids, mods = set(), set()
for nt in carte["notions"]:
    if nt["id"] in ids: err.append("notion en double " + nt["id"])
    ids.add(nt["id"])
    lv = [x["niveau"] for x in nt["niveaux"]]
    if lv != sorted(lv, reverse=True): err.append("niveaux non ordonnés " + nt["id"])
    for x in nt["niveaux"]:
        if x["module"] in mods: err.append("module en double " + x["module"])
        mods.add(x["module"])
        if not re.fullmatch(rf"(gram|conj|ortho|vocab)-{x['niveau']}e-[a-z0-9-]+", x["module"]): err.append("slug " + x["module"])
        if not x["source"]: err.append("source vide " + x["module"])
        if x["grade"] != prog["niveaux"]["grades"][str(x["niveau"])]: err.append("grade " + x["module"])
print(f"{len(ids)} notions, {len(mods)} modules")
by = {}
for nt in carte["notions"]:
    for x in nt["niveaux"]: by.setdefault(x["chantier"], 0); by[x["chantier"]] += 1
print("modules par chantier :", dict(sorted(by.items())), "| max", max(by.values()))
big = {c: m for c, m in by.items() if m > 6}
if big: print("  -> chantiers > 6 modules (à découper en plusieurs conversations) :", big)

# ---- 2. simulation des règles
S, M, V = prog["serie"], prog["maitrise"], prog["variete"]
def serie_score(p, rnd):
    pts = 0
    for _ in range(S["taille"]):
        if rnd.random() < p: pts += 1
        elif rnd.random() < p: pts += 0.5
    return pts / S["taille"]
def series_pour_maitriser(p, rnd, plafond=200):
    fen = []
    for i in range(1, plafond + 1):
        fen = (fen + [serie_score(p, rnd)])[-M["series_requises"]:]
        if len(fen) == M["series_requises"] and all(s >= M["seuil"] for s in fen): return i
    return None
rnd = random.Random(42)
print("\nSéries moyennes pour maîtriser un module (500 élèves simulés) :")
for p in (0.5, 0.65, 0.75, 0.85, 0.95):
    r = [series_pour_maitriser(p, rnd) for _ in range(500)]
    ok = [x for x in r if x]
    print(f"  réussite par question {p:.2f} : {sum(ok)/len(ok):5.1f} séries (échecs au plafond : {len(r)-len(ok)})")

# réserve de questions : 3 séries disjointes = 15 questions minimum
besoin = S["taille"] * M["series_requises"]
print(f"\nQuestions nécessaires par module pour 3 séries disjointes : {besoin} (un module de 2 compétences × 12 en fournit 24)")
if besoin > 24: err.append("réserve insuffisante")

# variété : élève qui reste sur la même notion
def propose(hist, cle, cfg, derniere):
    fen = hist[-cfg["fenetre_series"]:]
    return (len(fen) >= cfg["seuil_series"] and fen.count(cle) >= cfg["seuil_series"]
            and len(hist) - derniere > prog["variete"]["pause_apres_proposition_series"])
hist, derniere, props = [], -99, []
for i in range(1, 25):
    hist.append(("gram", "gram-pronom"))
    if propose([h[1] for h in hist], "gram-pronom", V["par_notion"], derniere):
        props.append(i); derniere = len(hist)
print("Élève collé à une notion : propositions aux séries", props, "(attendu : 6, 11, 16, 21)")
if props[:2] != [6, 11]: err.append("variété notion")

print("\nERREURS :", err if err else "aucune")
sys.exit(1 if err else 0)
