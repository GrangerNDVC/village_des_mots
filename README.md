# Le village des mots

**Chapitre 1 : La Quête de Plume.**

Serious game de français (grammaire, orthographe, conjugaison, vocabulaire) de la 6ᵉ à la 3ᵉ, en HTML, jouable sur PC, tablette et smartphone.
Plume, un jeune renard scribe, réchauffe des amis, bâtit un village et le meuble grâce aux bonnes réponses.

## Arborescence

```
village-des-mots/
├─ README.md
├─ index.html                      point d’entrée du jeu (provisoire : liste les modules)
├─ docs/
│  ├─ CHANTIERS.md                 plan des chantiers et protocole (à lire en premier)
│  ├─ chantiers/NN-slug.md         un brief par chantier = une conversation
│  ├─ CONVENTIONS.md               identifiants, noms, formats, règles de qualité
│  ├─ DIRECTION-ARTISTIQUE.md      palette, style, règles des images
│  ├─ ASSETS.md                    où va chaque image, état des livraisons
│  └─ JOURNAL.md                   décisions et état d’avancement
├─ data/
│  ├─ index.json                   catalogue des modules (GÉNÉRÉ, ne pas modifier à la main)
│  ├─ competences.json             référentiel des compétences
│  ├─ economie.json                gains, prix, raretés, variantes de couleur
│  ├─ schema/                      schémas JSON (module, exercice)
│  ├─ exercices/
│  │  └─ <domaine>/<niveau>e/<module>.json     1 fichier = 1 module de 25 à 35 exercices
│  ├─ evaluations/                 test de placement, boss, bilans
│  └─ catalogue/                   objets du jeu : meubles, objets, maisons, pièces, personnages, bâtiments
├─ assets/                         images WebP utilisées par le jeu
│  ├─ personnages/<nom>/  maisons/  batiments/  pieces/  tapis/  fonds/  recompenses/  ui/  variantes/
│  ├─ meubles/<piece>/    objets/<piece>/    decor/emblemes/
├─ sources/images/                 PNG haute définition (non déployés), même structure que assets/
├─ src/
│  ├─ css/   js/                   moteur du jeu (chantier 01)
├─ tools/
│  ├─ valider_donnees.py           contrôle tous les modules et l’index
│  ├─ construire_index.py          régénère data/index.json
│  ├─ nouveau_module.py            crée le squelette d’un module au bon endroit
│  └─ ranger_assets.py             range les zips d’images détourées dans assets/ et sources/
└─ .github/workflows/              validation automatique et publication GitHub Pages
```

## Démarrage

```
python tools/valider_donnees.py          # doit afficher 0 erreur
python -m http.server 8000                # puis ouvrir http://localhost:8000
```

## Ajouter du contenu

1. Un nouveau module : `python tools/nouveau_module.py grammaire 6 sujet "Le sujet du verbe"`, puis écrire les exercices.
2. Régénérer l’index : `python tools/construire_index.py`.
3. Valider : `python tools/valider_donnees.py`.
4. De nouvelles images : décompresser le zip livré, puis `python tools/ranger_assets.py dossier_decompresse`.

## Méthode de travail

Une conversation = un chantier = une branche `chantier/NN-slug`. Voir `docs/CHANTIERS.md`.
