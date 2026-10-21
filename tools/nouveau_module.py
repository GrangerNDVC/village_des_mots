#!/usr/bin/env python3
"""Crée le squelette d'un nouveau module au bon endroit.
Usage : python tools/nouveau_module.py grammaire 6 sujet "Le sujet du verbe"
"""
import json, os, sys

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PREFIXES = {"grammaire": "gram", "orthographe": "ortho", "conjugaison": "conj", "vocabulaire": "vocab"}
GRADES = {6: "page", 5: "ecuyer", 4: "chevalier", 3: "maitre"}

if len(sys.argv) != 5 or sys.argv[1] not in PREFIXES or int(sys.argv[2]) not in GRADES:
    sys.exit("Usage : python tools/nouveau_module.py <grammaire|orthographe|conjugaison|vocabulaire> <6|5|4|3> <slug> \"Titre\"")
domaine, niveau, slug, titre = sys.argv[1], int(sys.argv[2]), sys.argv[3], sys.argv[4]
mid = PREFIXES[domaine] + "-" + str(niveau) + "e-" + slug
comp = mid.replace("-" + slug, "-" + slug + "-exemple")
chemin = os.path.join(RACINE, "data", "exercices", domaine, str(niveau) + "e", mid + ".json")
if os.path.exists(chemin):
    sys.exit("Ce module existe déjà : " + chemin)
modele = {
    "module": mid, "titre": titre, "domaine": domaine, "niveau": niveau, "grade": GRADES[niveau], "version": 1,
    "description": "À compléter.",
    "rappel": {"titre": titre, "points": [{"mot": "à compléter", "definition": "à compléter", "exemple": "à compléter"}]},
    "competences": [comp],
    "exercices": [{
        "id": mid + "-001", "type": "qcm", "forme": "reconnaitre", "competence": comp, "difficulte": 1,
        "consigne": "À compléter.", "enonce": "À compléter.", "choix": ["a", "b"], "reponse": 0,
        "explication": "À compléter."}],
}
os.makedirs(os.path.dirname(chemin), exist_ok=True)
with open(chemin, "w", encoding="utf-8") as f:
    json.dump(modele, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("Créé :", os.path.relpath(chemin, RACINE))
print("Ensuite : ajouter les compétences dans data/competences.json, écrire les exercices,")
print("puis python tools/construire_index.py et python tools/valider_donnees.py")
