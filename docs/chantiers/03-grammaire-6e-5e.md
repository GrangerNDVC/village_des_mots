# Chantier 03 — Contenu : grammaire 6ᵉ et 5ᵉ

**Statut** : à faire  
**Dépend de** : 01

## Mission
Écrire les modules de grammaire de 6ᵉ et 5ᵉ à partir des manuels.

## Entrées (les seules choses à fournir)
- Manuels 6ᵉ et 5ᵉ (table des matières + 2 à 3 pages d’exercices par chapitre)
- docs/CONVENTIONS.md
- data/competences.json

## Sorties
- data/exercices/grammaire/6e/*.json et 5e/*.json
- data/competences.json complété
- data/index.json régénéré

## Critères de fin
- Validateur à 0 erreur
- 25 à 35 exercices par module
- Chaque compétence : 12 exercices sur 4 formes minimum

## Démarrage de la conversation
Coller `docs/CONVENTIONS.md` et ce fichier. Joindre les entrées ci-dessus. Travailler sur la branche `chantier/03-grammaire-6e-5e`.

## Modules prévus (indicatifs, à affiner avec les manuels)

| Module | Contenu |
|---|---|
| `gram-6e-natures` | natures de mots (**fait**, 30 exercices) |
| `gram-6e-phrase-types` | types et formes de phrase |
| `gram-6e-sujet` | le sujet du verbe |
| `gram-6e-cod-coi` | compléments d’objet |
| `gram-6e-complements-circ` | compléments circonstanciels |
| `gram-5e-attribut` | l’attribut du sujet |
| `gram-5e-expansions-nom` | expansions du nom |
| `gram-5e-propositions` | juxtaposition et coordination |
