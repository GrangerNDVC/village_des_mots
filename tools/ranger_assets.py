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
PREFIXES = [
    (r"^plume_", "personnages/plume"), (r"^hibou_", "personnages/hibou"), (r"^(pate_|grand_pate)", "personnages/pates"),
    (r"^maman_souris_", "personnages/maman_souris"), (r"^chatte_", "personnages/chatte"),
    (r"^ecureuil_", "personnages/ecureuil"), (r"^lapin_", "personnages/lapin"),
    (r"^emb_", "decor/emblemes"), (r"^coffre_", "recompenses"), (r"^maison_", "maisons"), (r"^batiment_", "batiments"),
    (r"^(piece_|duplex_)", "pieces"), (r"^fond_", "fonds"), (r"^(couloir_)", "pieces"), (r".*_v2$", "variantes"),
]


def destination(stem):
    for motif, dest in PREFIXES:
        if re.match(motif, stem):
            return dest
    base = stem
    for s in SUFFIXES:
        if stem.endswith(s):
            base = stem[: -len(s)]
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
