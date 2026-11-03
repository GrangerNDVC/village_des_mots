# Firebase : sauvegarde en ligne et suivi des élèves

## Mise en route (une seule fois)
1. Console Firebase : activer **Authentication** → méthodes de connexion : **Anonyme** et **E-mail/Mot de passe** (créer l’utilisateur `julie.granger.rennes@gmail.com`).
2. Authentication → Paramètres → **Domaines autorisés** : ajouter le nom d’hôte GitHub Pages (`pseudo.github.io`, sans `https://` ni chemin).
3. Realtime Database → **Règles** : coller `docs/firebase-rules.json` (le bloc `jeux/plume` est celui du jeu).
4. Dans `index.html`, compléter `FB_CFG` (apiKey, authDomain, databaseURL, projectId, appId). Cette configuration n’est pas secrète.

## Fonctionnement
- Élève : sur l’accueil, carte « Sauvegarde en ligne », numéro à 4 chiffres. Un numéro déjà pris propose de charger la partie ; le refuser n’écrase rien.
- Données : `/jeux/plume/<numéro>` = `{v, maj, donnees, resume}` (`donnees` < 60 000 caractères, `resume` < 2 000).
- Professeur : ✦ discret en bas de l’accueil, mot de passe du compte Firebase (aucun mot de passe dans le code). Le panneau « Suivi des élèves » liste les numéros, pièces, modules maîtrisés et détail par atelier.
- Sans `apiKey`, le jeu reste 100 % hors ligne.

## Limites connues
- Le numéro à 4 chiffres est devinable : un élève peut ouvrir ou écraser la partie d’un autre numéro. Acceptable en classe.
- La liste du professeur télécharge toutes les sauvegardes (`donnees` comprises) : correct pour une classe, à revoir pour de gros effectifs.
- Le mot de passe du compte professeur protège toutes les données : ne jamais le mettre dans le dépôt.
