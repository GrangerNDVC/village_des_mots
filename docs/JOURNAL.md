# Journal du projet

## Chantier 0 : cadrage et images de base (terminé à l’exception des restes listés dans ASSETS.md)

- Concept : Plume, renard scribe, aide des amis en difficulté, construit un village et le meuble avec les pièces gagnées.
- Recentrage : on teste le moteur avec les assets existants, puis on ajoute maisons, amis et bâtiments à la demande.
- Neige produite par le code, jamais dessinée. Saisons uniquement sur les fonds.
- Animaux : personnages personnalisés (histoire, tenue avant/après, accessoire), pas de figurants.
- Maisons : rondes (une pièce ou duplex à escalier) et rectangulaires (1 à 5 pièces avec couloir de 2 à 5 portes).
- Meubles : inventaire partagé, quatre vues (face, côté, dos, diagonale) et six orientations, variantes de couleur par script. Meubles adossés au mur marqués `mural`.
- Une seule maison entièrement aménageable (celle de Plume, 6 pièces) ; les maisons d’amis ont une pièce meublée par une disposition modèle.

## Chantier 1 : moteur du prototype (à venir)

Premier module de test : `gram-6e-natures` (30 exercices).

## Fusion v0.8 (reprise du projet)

- Les 16 modules de la v0.8 (11 en 6e, 5 en 5e) sont rangés dans `data/exercices/grammaire/{6e,5e}/`, validés par `tools/valider_donnees.py` (0 erreur).
- `data/competences.json` : référentiel v0.8 (54 compétences) ; `gram-6e-natures` conservé.
- `data/jeu/` : fichiers propres au jeu v0.8 (carte-notions, progression, epreuves, catalogue-objets, economie). L’économie et le catalogue de `data/` (squelette initial) ne sont pas écrasés : à unifier.
- `tools/archive/` : scripts de fabrication de la v0.8 (build_04/05, gen_economie, valider_progression, controle_module).
- À faire : verser `source/tpl.html` et `build.py` (non encore dans le dépôt), puis Firebase.

## Jeu v0.8 versé dans le dépôt

- `index.html` = le jeu v0.8 complet (fichier unique autonome, récupéré de l’artifact claude.ai). `modules.html` = ancienne page provisoire (liste des modules).
- Le fichier source (`source/tpl.html`) et `build.py` restent à verser : tant qu’ils manquent, toute modification passe par `index.html` directement.
