# Assets : comment les images sont organisées

## PNG et WebP : à quoi ça sert

Chaque image existe en deux formats. Vous n’avez rien à trier à la main : `tools/ranger_assets.py` les range.

| Format | Rôle | Dossier |
|---|---|---|
| **PNG** | l’original transparent, haute définition. On le garde précieusement mais le jeu ne le charge pas. | `sources/images/` |
| **WebP** | la copie allégée, 5 à 10 fois plus légère. C’est celle que le jeu affiche. | `assets/` |

Les deux dossiers ont exactement la même arborescence.

## Où va chaque image

| Dossier de `assets/` | Contenu |
|---|---|
| `personnages/plume/modele/` | fiche modèle de Plume (4 vues, bustes de référence) |
| `personnages/plume/postures/` | poses de Plume, dont les versions « avant » (haillons) et « après » (cape verte) |
| `personnages/plume/tenues/` | tenues des 4 grades, sans cape, tenues bonus |
| `personnages/plume/expressions/` | bustes d’expressions |
| `personnages/<ami>/postures/` et `expressions/` | pour maman souris, la chatte, l’écureuil, le lapin : les postures (corps entier) séparées des expressions (bustes) |
| `personnages/hibou/`, `personnages/pates/` | mentor et adversaires |
| `maisons/rondes/`, `maisons/rectangulaires/` | maisons sans neige, classées par forme |
| `maisons/anciennes_avec_neige/` | premières maisons enneigées, à remplacer |
| `batiments/` | épicerie, café-boulangerie, cinéma, théâtre |
| `pieces/` | pièces vides, couloirs, pièces rondes et duplex |
| `meubles/<piece>/` | meubles orientables (4 vues + miroirs), classés par pièce principale |
| `objets/<piece>/` | petits objets, décor mural |
| `tapis/` | tapis |
| `recompenses/` | coffres, pièces, cadeaux, médailles |
| `ui/domaines/` | les quatre emblèmes des domaines : tour (grammaire), chêne (orthographe), sablier (conjugaison), livres (vocabulaire) |
| `ui/` | plus tard : boutons, icônes, étoiles, badges de grade (images d’interface à créer au chantier 1) |
| `fonds/` | fonds de la forêt et du village, avec les saisons |
| `variantes/` | variantes de couleur générées par script (chantier 2) et versions de secours |

## Les emblèmes et les coffres

- Les **emblèmes** (tour, chêne, sablier, livres) sont les icônes des quatre domaines : ils vont dans `assets/ui/domaines/`.
- Les **coffres** servent de récompense : ils vont dans `assets/recompenses/`.

## Ranger une nouvelle livraison

1. Décompresser le zip dans un dossier.
2. `python tools/ranger_assets.py dossier_decompresse --simuler` pour voir où chaque fichier ira.
3. Relancer sans `--simuler` pour copier.

## Zips livrés pendant le chantier 0

`chantier0_images_detourees.zip`, `planche_N1_detouree.zip`, `lot2_planches_detourees.zip`, `lot3_planches_detourees.zip`, `lot4_pieces_et_S6.zip`, `lot5_personnages_detoures.zip`, `lot6_maisons_batiments_pieces_rondes.zip`. Un seul zip, `images-rangees.zip`, les réunit déjà rangés.

## Encore à générer

Couloirs à 2, 3, 4 portes et couloir à 5 portes refait ; six maisons de départ sans neige ; tapis vus du dessus (T1) ; décor du village (D1, D2) ; récompenses (R1) ; bâtiments de réserve (B2) ; images d’interface ; gammes de meubles à la demande.
