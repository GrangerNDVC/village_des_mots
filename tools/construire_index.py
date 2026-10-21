#!/usr/bin/env python3
"""Reconstruit data/index.json à partir des modules de data/exercices/.
Usage : python tools/construire_index.py
"""
import json, os, glob

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DONNEES = os.path.join(RACINE, "data")
ORDRE_DOMAINES = ["grammaire", "orthographe", "conjugaison", "vocabulaire"]


def construire():
    modules = []
    for chemin in sorted(glob.glob(os.path.join(DONNEES, "exercices", "*", "*", "*.json"))):
        with open(chemin, encoding="utf-8") as f:
            m = json.load(f)
        exos = m.get("exercices", [])
        modules.append({
            "id": m["module"],
            "titre": m["titre"],
            "domaine": m["domaine"],
            "niveau": m["niveau"],
            "grade": m["grade"],
            "version": m["version"],
            "fichier": os.path.relpath(chemin, RACINE).replace(os.sep, "/"),
            "nb_exercices": len(exos),
            "competences": m.get("competences", []),
            "formes": sorted({e.get("forme") for e in exos if e.get("forme")}),
        })
    modules.sort(key=lambda x: (ORDRE_DOMAINES.index(x["domaine"]), -x["niveau"], x["id"]))
    return {
        "version": 1,
        "genere_par": "tools/construire_index.py",
        "domaines": ORDRE_DOMAINES,
        "niveaux": [6, 5, 4, 3],
        "totaux": {"modules": len(modules), "exercices": sum(x["nb_exercices"] for x in modules)},
        "modules": modules,
    }


if __name__ == "__main__":
    index = construire()
    with open(os.path.join(DONNEES, "index.json"), "w", encoding="utf-8") as f:
        json.dump(index, f, ensure_ascii=False, indent=2)
        f.write("\n")
    print("index.json reconstruit :", index["totaux"]["modules"], "module(s),", index["totaux"]["exercices"], "exercice(s)")
