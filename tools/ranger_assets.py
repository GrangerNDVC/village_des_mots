#!/usr/bin/env python3
"""Range les images détourées livrées (PNG et WebP) dans le dépôt.
  - WebP  -> assets/<destination>/        (utilisé par le jeu)
  - PNG   -> sources/images/<destination>/ (haute définition, non déployé)
Usage : python tools/ranger_assets.py dossier_decompresse [--simuler]
Les dossiers « apercus » et les fichiers inconnus sont ignorés et signalés.
"""
import json, os, re, shutil, sys

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SUFFIXES = ["_cote_droite", "_diag_droite", "_face", "_cote", "_dos", "_diag"]


def charger(nom):
    with open(os.path.join(RACINE, "data", "catalogue", nom), encoding="utf-8") as f:
        return json.load(f)


MEUBLES = {m["id"]: m for m in charger("meubles.json")["meubles"]}
OBJETS = {o["id"]: o for o in charger("objets.json")["objets"]}
MAISONS = {m["id"]: m for m in charger("maisons.json")["maisons"]}


def destination(stem):
    m = re.match(r"^(plume|maman_souris|chatte|ecureuil|lapin)_(.*)$", stem)
    if m:
        nom, reste = m.groups()
        if nom == "plume":
            if reste.startswith("buste_"): sous = "expressions"
            elif reste.startswith("modele_"): sous = "modele"
            elif reste.startswith("tenue_") or reste == "sans_cape": sous = "tenues"
            else: sous = "postures"
        else:
            sous = "expressions" if reste.startswith("expr_") else "postures"
        return "personnages/" + nom + "/" + sous
    if stem.startswith("hibou_"): return "personnages/hibou"
    if re.match(r"^(pate_|grand_pate)", stem): return "personnages/pates"
    if stem.startswith("emb_"): return "ui/domaines"
    if re.match(r"^coffre_(ferme|ouvert)$", stem): return "recompenses"
    if stem.startswith("maison_"):
        info = MAISONS.get(stem)
        if info is None: return "maisons"
        if info.get("neige"): return "maisons/anciennes_avec_neige"
        return "maisons/rondes" if info["forme"].startswith("ronde") else "maisons/rectangulaires"
    if stem.startswith("batiment_"): return "batiments"
    if re.match(r"^(piece_|duplex_|couloir_)", stem): return "pieces"
    if stem.startswith("fond_"): return "fonds"
    if stem.endswith("_v2"): return "variantes"
    base = stem
    for suf in SUFFIXES:
        if stem.endswith(suf):
            base = stem[: -len(suf)]
            break
    if base in MEUBLES:
        return "meubles/" + MEUBLES[base]["pieces"][0]
    if stem in OBJETS:
        o = OBJETS[stem]
        return "tapis" if o["type"] == "tapis" else "objets/" + o["piece"]
    return None


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    entree, simuler = sys.argv[1], "--simuler" in sys.argv
    inconnus, n = [], 0
    for dossier, _, fichiers in os.walk(entree):
        if "apercus" in dossier.split(os.sep):
            continue
        for nom in sorted(fichiers):
            stem, ext = os.path.splitext(nom)
            ext = ext.lower()
            if ext not in (".png", ".webp"):
                continue
            dest = destination(stem)
            if dest is None:
                inconnus.append(nom); continue
            base = "assets" if ext == ".webp" else os.path.join("sources", "images")
            cible = os.path.join(RACINE, base, dest, nom)
            if not simuler:
                os.makedirs(os.path.dirname(cible), exist_ok=True)
                shutil.copy2(os.path.join(dossier, nom), cible)
            n += 1
    print(("Simulation : " if simuler else "") + str(n) + " fichier(s) rangé(s)")
    if inconnus:
        print("Sans destination connue (à ajouter aux catalogues) :")
        for x in inconnus: print("  ", x)


if __name__ == "__main__":
    main()
