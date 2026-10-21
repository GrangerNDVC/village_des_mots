# Conventions

## Identifiants (ne jamais les changer une fois publiés)

| Objet | Format | Exemple |
|---|---|---|
| Module | `<dom>-<niveau>e-<slug>` | `gram-6e-natures` |
| Exercice | `<module>-NNN` (3 chiffres, jamais réutilisé) | `gram-6e-natures-014` |
| Compétence | `<dom>-<niveau>e-<theme>-<precision>` | `gram-6e-nature-nom` |
| Image | `snake_case`, sans accent ni espace | `canape_face`, `maison_rose` |

Préfixes de domaine : `gram`, `ortho`, `conj`, `vocab`. Niveaux : 6, 5, 4, 3. Grades : page (6ᵉ), ecuyer (5ᵉ), chevalier (4ᵉ), maitre (3ᵉ).

## Emplacement des fichiers

- Un module : `data/exercices/<domaine>/<niveau>e/<module>.json`.
- Le champ `module` du fichier, son dossier et son nom de fichier doivent être cohérents (le validateur le vérifie).
- Un module contient 25 à 35 exercices. Au-delà, on le coupe en deux modules.

## Exercices

- Types : `qcm`, `vrai_faux`, `texte_trous`, `saisie`, `tri`, `clic_mot`, `association`, `ordre`, `corriger`.
- Formes (pour la variété et le transfert) : `reconnaitre`, `completer`, `produire`, `transformer`, `corriger`, `contexte`.
- Difficulté : 1 (facile), 2, 3. Les gains en pièces en dépendent (2, 4, 6).
- Une seule bonne réponse par défaut ; une `explication` est obligatoire ; la consigne est courte et sans ambiguïté.
- Chaque compétence : au moins 12 exercices répartis sur au moins 4 formes (objectif ; le validateur avertit en dessous de 5 exercices ou 4 formes).
- Les exercices sont **originaux**, inspirés des manuels et jamais recopiés. Le champ facultatif `source` garde la trace (`manuel-6e-p42`).
- Texte en UTF-8 ; apostrophe typographique ’ ; guillemets français « ».

## Versions

- Le champ `version` d’un module augmente quand son contenu change.
- On n’efface pas un identifiant d’exercice : on le retire et on garde le trou dans la numérotation.

## Images

- Jeu : WebP dans `assets/`. Sources : PNG dans `sources/images/`. Même arborescence.
- Meubles : `<id>_face`, `<id>_cote`, `<id>_dos`, `<id>_diag`, plus `_cote_droite` et `_diag_droite` (miroirs).
- Les images ne contiennent jamais de texte.

## Git

- Branche : `chantier/NN-slug`. Commits : `[NN] message court`.
- On fusionne dans `main` quand le validateur affiche 0 erreur.
