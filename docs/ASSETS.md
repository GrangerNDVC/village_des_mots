# Assets : où va chaque image

Les images sont livrées en zips de PNG transparents et WebP. `tools/ranger_assets.py` les range automatiquement.

| Préfixe ou famille | Destination |
|---|---|
| `plume_*` | `personnages/plume` |
| `hibou_*`, `pate_*`, `grand_pate` | `personnages/hibou`, `personnages/pates` |
| `maman_souris_*`, `chatte_*`, `ecureuil_*`, `lapin_*` | `personnages/<nom>` |
| `emb_*` | `decor/emblemes` |
| `coffre_*` | `recompenses` |
| `maison_*`, `batiment_*` | `maisons`, `batiments` |
| `piece_*`, `duplex_*`, `couloir_*` | `pieces` |
| meubles (liste dans `data/catalogue/meubles.json`) | `meubles/<piece>` |
| objets (liste dans `data/catalogue/objets.json`) | `objets/<piece>` ou `tapis` |
| `fond_*` | `fonds` |

## Zips livrés pendant le chantier 0

`chantier0_images_detourees.zip` (planches A à G), `planche_N1_detouree.zip`, `lot2_planches_detourees.zip`, `lot3_planches_detourees.zip`, `lot4_pieces_et_S6.zip`, `lot5_personnages_detoures.zip`, `lot6_maisons_batiments_pieces_rondes.zip`.

## Encore à générer

Couloirs à 2, 3, 4 portes et couloir à 5 portes refait ; six maisons de départ sans neige ; tapis vus du dessus (T1) ; décor du village (D1, D2) ; récompenses (R1) ; bâtiments de réserve (B2) ; gammes de meubles à la demande.

Le suivi détaillé est dans la page « Suivi des planches ».
