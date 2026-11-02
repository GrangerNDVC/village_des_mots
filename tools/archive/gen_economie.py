#!/usr/bin/env python3
"""Genere data/economie.json et data/surfaces-pose.json (sources des chiffres : ce fichier).
Usage : python3 tools/gen_economie.py  (depuis la racine du projet)"""
import json, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
D = pathlib.Path(__file__).resolve().parent.parent / "data"
cat = json.load(open(D/"catalogue-objets.json", encoding="utf-8"))

# ------------------------------------------------------------ prix (pieces)
BASE = dict(chaise_bois=25, chaise_metal=25, chaise_rotin=35, canape=90, fauteuil=60, fauteuil_rotin=70,
            commode=55, meuble_TV=140, meuble_PC=120, lit=80, pouf=35,
            coussin=12, coussin2=12, jouet_dino=25, jouet_train=25, jouet_anneaux=20, cubes_jouets=10,
            poulet=20, gateau=20, part_gateau=10, hamburger=15, bol_legumes=15)
MAXEX = dict(chaise_bois=4, chaise_metal=4, chaise_rotin=4, canape=2, fauteuil=2, fauteuil_rotin=2, commode=2,
             meuble_TV=1, meuble_PC=1, lit=2, pouf=3, coussin=4, coussin2=4, jouet_dino=1, jouet_train=1,
             jouet_anneaux=1, cubes_jouets=3, poulet=2, gateau=2, part_gateau=4, hamburger=4, bol_legumes=4)
FACTEUR_COLOR = 2.5
def r5(x): return int(round(x/5.0)*5)
ids = [o["id"] for o in cat["objets"]]
objets = {}
for o in cat["objets"]:
    i, v = o["id"], o.get("variante_de")
    if v:
        # coussin_colorable -> coussin, coussin_colorable2 -> coussin2 : la variante_de du catalogue le dit deja
        objets[i] = dict(prix=r5(BASE[v]*FACTEUR_COLOR), max_exemplaires=MAXEX[v], variante_de=v, colorable=True)
    else:
        objets[i] = dict(prix=BASE[i], max_exemplaires=MAXEX[i], colorable=False)

# ------------------------------------------------------------ pieces et maisons
def piece(pid, nom, prix, mob, statut="propose"):
    return dict(id=pid, nom=nom, prix=prix, mobilier=mob, statut_contenu=statut)
maisons = [
 dict(id="maison-1", nom="Chaumière du Page", niveau=6, grade="page", colorisation=False, pieces=[
   piece("m1-p1","Salon",0,["canape","fauteuil","coussin","coussin2","commode","meuble_TV"]),
   piece("m1-p2","Chambre",150,["lit","pouf","jouet_dino","jouet_train","jouet_anneaux","cubes_jouets"]),
   piece("m1-p3","Cuisine",250,["chaise_bois","chaise_metal","poulet","gateau","part_gateau","hamburger","bol_legumes"]),
   piece("m1-p4","Bureau",350,["meuble_PC"])]),
 dict(id="maison-2", nom="Maison de l'Écuyer", niveau=5, grade="ecuyer", colorisation=True, pieces=[
   piece("m2-p1","Salon moderne",600,["canape_colorable","fauteuil_colorable","coussin_colorable","coussin_colorable2","commode_colorable","meuble_TV_colorable"]),
   piece("m2-p2","Chambre claire",400,["lit_colorable","pouf_colorable","jouet_dino_colorable","fauteuil_rotin"]),
   piece("m2-p3","Salle à manger",500,["chaise_bois_colorable","chaise_metal_colorable","chaise_rotin","chaise_rotin_colorable"]),
   piece("m2-p4","Bureau moderne",600,["meuble_PC_colorable","fauteuil_rotin_colorable"])]),
 dict(id="maison-3", nom="Manoir du Chevalier", niveau=4, grade="chevalier", colorisation=True, statut="a_creer",
      pieces=[piece("m3-p1","(à créer)",1200,[],"a_creer"),piece("m3-p2","(à créer)",800,[],"a_creer"),
              piece("m3-p3","(à créer)",1000,[],"a_creer"),piece("m3-p4","(à créer)",1200,[],"a_creer")]),
 dict(id="maison-4", nom="Château du Maître", niveau=3, grade="maitre", colorisation=True, statut="a_creer",
      pieces=[piece("m4-p1","(à créer)",2000,[],"a_creer"),piece("m4-p2","(à créer)",1400,[],"a_creer"),
              piece("m4-p3","(à créer)",1700,[],"a_creer"),piece("m4-p4","(à créer)",2000,[],"a_creer")]),
]
DOMS = ["grammaire","conjugaison","orthographe","vocabulaire"]
paliers = []
for m in maisons:
    for d in DOMS:
        paliers.append(dict(id=f"palier-{m['niveau']}e-{d}", niveau=m["niveau"], domaine=d,
            condition="tous les modules (notion, %de) du domaine sont a l'etat maitrise" % m["niveau"],
            recompense=dict(personnage_offert=f"perso-{m['niveau']}e-{d}", pieces=0),
            effet="ouvre a l'achat la piece suivante de la maison (n-ieme palier de domaine -> piece n+1) ; au 4e palier : niveau complet"))
economie = dict(
 version=1,
 note="Economie du jeu (pieces). Les chiffres sont calibres par tools/valider_economie.py. Tout est a valider ; maisons 3 et 4 = gabarit.",
 devise="pièces",
 depart=dict(pieces=50, maison="maison-1", piece_offerte="m1-p1", objets_offerts=[dict(id="fauteuil", n=1)]),
 gains=dict(
   note="Un peu d'argent pour avoir fini, plus pour avoir bien repondu. Serie de 5 : de 2 a 15 pieces.",
   serie_terminee=2,
   question=dict(bon_du_premier_coup=2, bon_au_second_essai=1, faux=0),
   serie_parfaite_bonus=3,
   maitrise_module=30,
   revision_reussie=10,
   variete_acceptee=5,
   test_placement_par_module_valide=15),
 jalons=dict(note="Cadeaux a chaque nombre de modules maitrises (tous domaines et niveaux confondus) : il y a toujours une marche proche.",
   liste=[dict(modules=1,pieces=20),dict(modules=3,objet="coussin"),dict(modules=6,pieces=40),
          dict(modules=10,objet="jouet_dino"),dict(modules=15,pieces=60),dict(modules=20,pieces=80),
          dict(modules=30,pieces=100),dict(modules=45,pieces=120),dict(modules=60,pieces=150)]),
 paliers_domaine=paliers,
 palier_niveau=dict(note="Quand les 4 paliers de domaine d'un niveau sont atteints.",
   recompense_pieces=100, effet="la maison suivante devient achetable ; la suivante encore apparait en silhouette"),
 apparition=dict(
   etats=["cache","silhouette","achetable","achetee"],
   regles=["La piece (ou maison) suivante a debloquer est toujours visible en silhouette grise, avec ses meubles en ombres.",
           "La suivante de celle-ci reste cachee.",
           "Une piece achetee ouvre la boutique de ses meubles.",
           "Les objets achetes sont a l'inventaire et placables dans toute piece achetee."]),
 colorisation=dict(
   disponible_a_partir_de="maison-2", facteur_prix=FACTEUR_COLOR,
   premiere_couleur_gratuite=True, prix_changement_couleur=10, mode="decalage de teinte depuis le rouge de base",
   palette=[dict(id="rouge",mode="base"),dict(id="orange",teinte=25),dict(id="jaune",teinte=48),dict(id="vert",teinte=110),
            dict(id="turquoise",teinte=170),dict(id="bleu",teinte=215),dict(id="violet",teinte=270),dict(id="rose",teinte=335,luminosite=+12),
            dict(id="marron",teinte=20,luminosite=-25),dict(id="blanc",mode="desature",luminosite=+55),
            dict(id="gris",mode="desature"),dict(id="noir",mode="desature",luminosite=-45)]),
 garde_fous=dict(
   note="Verifies par la simulation de tools/valider_economie.py.",
   ecart_max_modules_sans_achat_possible=2,
   prix_max_objet_en_modules=1.6,
   prix_max_piece_en_modules=4.5),
 objets=objets,
 maisons=maisons)
json.dump(economie, open(D/"economie.json","w",encoding="utf-8"), ensure_ascii=False, indent=1)
print("economie.json ecrit :", len(objets), "objets,", sum(len(m['pieces']) for m in maisons), "pieces")
