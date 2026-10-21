# Plan des chantiers

**Une conversation = un chantier = une branche git.** Cela garde chaque échange léger et évite les conversations trop lourdes.

| N° | Chantier | Titre | Dépend de | Statut |
|---|---|---|---|---|
| 00 | [cadrage-images](chantiers/00-cadrage-images.md) | Cadrage et images de base | — | quasi terminé |
| 01 | [moteur-prototype](chantiers/01-moteur-prototype.md) | Moteur du prototype jouable | 00 | prochain |
| 02 | [atelier-variantes](chantiers/02-atelier-variantes.md) | Atelier de variantes de couleur | 01 | à faire |
| 03 | [grammaire-6e-5e](chantiers/03-grammaire-6e-5e.md) | Contenu : grammaire 6ᵉ et 5ᵉ | 01 | à faire |
| 04 | [grammaire-4e-3e](chantiers/04-grammaire-4e-3e.md) | Contenu : grammaire 4ᵉ et 3ᵉ | 03 | à faire |
| 05 | [orthographe-6e-5e](chantiers/05-orthographe-6e-5e.md) | Contenu : orthographe 6ᵉ et 5ᵉ | 01 | à faire |
| 06 | [orthographe-4e-3e](chantiers/06-orthographe-4e-3e.md) | Contenu : orthographe 4ᵉ et 3ᵉ | 05 | à faire |
| 07 | [conjugaison-6e-5e](chantiers/07-conjugaison-6e-5e.md) | Contenu : conjugaison 6ᵉ et 5ᵉ | 01 | à faire |
| 08 | [conjugaison-4e-3e](chantiers/08-conjugaison-4e-3e.md) | Contenu : conjugaison 4ᵉ et 3ᵉ | 07 | à faire |
| 09 | [vocabulaire-6e-5e](chantiers/09-vocabulaire-6e-5e.md) | Contenu : vocabulaire 6ᵉ et 5ᵉ | 01 | à faire |
| 10 | [vocabulaire-4e-3e](chantiers/10-vocabulaire-4e-3e.md) | Contenu : vocabulaire 4ᵉ et 3ᵉ | 09 | à faire |
| 11 | [evaluations](chantiers/11-evaluations.md) | Évaluations | 03, 05, 07, 09 | à faire |
| 12 | [univers-a-la-demande](chantiers/12-univers-a-la-demande.md) | Univers à la demande | 01 | en continu |
| 13 | [assemblage-publication](chantiers/13-assemblage-publication.md) | Assemblage, tests et publication | 01, 11 | à la fin |

## Protocole

**Au début d’une conversation** : coller `docs/CONVENTIONS.md` et le brief du chantier (`docs/chantiers/NN-slug.md`), puis joindre **uniquement** les fichiers listés dans « Entrées ». Rien d’autre.

**Pendant** : produire des fichiers (JSON, code, images), pas de longs textes. Valider avec `python tools/valider_donnees.py`.

**À la fin** : livrer les fichiers (ou un zip) ; mettre à jour `docs/JOURNAL.md` et le suivi des planches ; committer sur la branche du chantier.

## Règles pour garder les conversations légères

- Les chantiers de contenu (03 à 10) : au plus 6 modules par conversation. Si le programme est plus long, ouvrir `03b`, `03c`.
- Les images ne sont jamais jointes en masse : on joint seulement les planches à traiter.
- Une décision importante se note dans `docs/JOURNAL.md` ; on ne la rediscute pas dans un autre chantier.
- Quand une conversation devient lente, on livre l’état, on met à jour le journal et on ouvre la suivante.
