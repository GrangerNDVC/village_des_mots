import json
M="gram-5e-expansions-nom"
S6="manuel-5e-f6-p16"; S7="manuel-5e-f7-p18"
CA,CB,CC="gram-5e-epithete-place","gram-5e-cdn-nature","gram-5e-relative-reperer"
ex=[]
def add(t,f,c,d,cons,src,**kw):
    ex.append(dict(id=f"{M}-{len(ex)+1:03d}",type=t,forme=f,competence=c,difficulte=d,consigne=cons,**kw,source=src))
TOL={"casse":False,"accents":False}
def sais(f,c,d,cons,en,acc,expl,src): add("saisie",f,c,d,cons,src,enonce=en,reponses_acceptees=acc,tolerance=TOL,explication=expl)
def qcm(f,c,d,cons,ch,r,expl,src,en=None): add("qcm",f,c,d,cons,src,**({"enonce":en} if en else {}),choix=ch,reponse=r,explication=expl)
def vf(c,d,cons,en,r,expl,src): add("vrai_faux","reconnaitre",c,d,cons,src,enonce=en,reponse=r,explication=expl)
def clic(f,c,d,cons,mots,cib,expl,src): add("clic_mot",f,c,d,cons,src,mots=mots,cibles=cib,explication=expl)
def tri(f,c,d,cons,els,cats,sol,expl,src): add("tri",f,c,d,cons,src,elements=els,categories=cats,solution=dict(zip(els,sol)),explication=expl)
def trous(f,c,d,cons,en,tr,expl,src): add("texte_trous",f,c,d,cons,src,enonce=en,trous=[dict(id=i+1,choix=ch,reponse=r) for i,(ch,r) in enumerate(tr)],explication=expl)
def corr(c,d,cons,fa,ok,expl,src): add("corriger","corriger",c,d,cons,src,phrase_fautive=fa,corrections_acceptees=ok,explication=expl)

# A : épithète (f6 p16)
c=CA;s=S6
qcm("reconnaitre",c,1,"Quel mot est l’épithète du nom « pousse » ?",["frêle","devient","arbre","robuste"],0,"« frêle » qualifie directement le nom « pousse » : c’est son épithète. « robuste » est l’épithète d’un autre nom, « arbre ».",s,"La frêle pousse devient un arbre robuste.")
clic("reconnaitre",c,1,"Clique sur tous les adjectifs épithètes.",["Des","feuilles","brunes","couvrent","le","sol","mouillé"],[2,6],"« brunes » qualifie « feuilles » et « mouillé » qualifie « sol » : ce sont des épithètes.",s)
vf(c,1,"Vrai ou faux ?","L’épithète est reliée au nom par un verbe d’état.",False,"L’épithète qualifie directement le nom, sans l’intermédiaire d’un verbe. Quand un verbe d’état relie l’adjectif au sujet, c’est un attribut.",s)
sais("produire",c,1,"Recopie le participe passé employé comme épithète.","Hugo ramasse des feuilles tombées.",["tombées"],"« tombées » qualifie directement le nom « feuilles » : c’est un participe passé employé comme épithète.",s)
tri("reconnaitre",c,2,"Cette épithète est-elle un adjectif ou un participe passé ?",["un chemin étroit","des feuilles fanées","un hibou silencieux","une lanterne allumée","un lutin curieux","un village endormi"],["adjectif","participe passé"],[0,1,0,1,0,1],"L’épithète peut être un adjectif (étroit, silencieux, curieux) ou un participe passé employé comme adjectif (fanées, allumée, endormi).",s)
qcm("reconnaitre",c,2,"Quelle phrase contient deux épithètes du même nom ?",["Le vent froid souffle sur la tour.","Un vent froid et violent souffle.","Le vent froid souffle sur la tour haute.","Le vent souffle fort."],1,"Dans « Un vent froid et violent souffle », « froid » et « violent » qualifient tous deux « vent ». Dans « la tour haute », « haute » qualifie un autre nom.",s)
trous("completer",c,2,"Complète avec le sens qui convient.","Dans « un grand homme », « grand » signifie {{1}} ; dans « un homme grand », il signifie {{2}}.",[(["important, admirable","de haute taille"],0),(["important, admirable","de haute taille"],1)],"Pour certains adjectifs, le sens change selon la place : avant le nom, « grand » exprime l’importance ; après le nom, il indique la taille.",s)
sais("transformer",c,2,"Remplace « qui est fermée » par une épithète.","une porte qui est fermée",["une porte fermée"],"« qui est fermée » peut être remplacé par le participe passé « fermée », épithète de « porte ».",s)
corr(c,2,"Corrige l’épithète qui ne convient pas.","Des fleurs sauvages et parfumé bordent le chemin.",["Des fleurs sauvages et parfumées bordent le chemin."],"Les deux épithètes qualifient « fleurs » (féminin pluriel) : « sauvages » et « parfumées » s’accordent avec lui.",s)
qcm("contexte",c,2,"Dans quelle phrase « pauvre » est-il une épithète qui signifie « qui a peu d’argent » ?",["Ce lutin est pauvre.","Le pauvre lutin se lamente.","Un lutin pauvre frappe à la porte.","Pauvre Plume !"],2,"Dans « Un lutin pauvre », l’adjectif suit le nom et signifie « qui a peu d’argent ». « Le pauvre lutin » signifie « digne de pitié » ; dans « Ce lutin est pauvre », « pauvre » est attribut.",s)
tri("contexte",c,3,"Dans chaque phrase, le mot « calme » est-il une épithète ?",["Un hibou calme veille.","Ce hibou est calme.","Le calme du village me plaît.","Une rivière calme coule.","La forêt semble calme.","Plume traverse un lac calme."],["épithète","pas une épithète"],[0,1,1,0,1,0],"« calme » est épithète quand il qualifie directement un nom. Ce n’est pas une épithète quand il est attribut (est calme, semble calme) ou quand il est un nom (le calme).",s)
clic("contexte",c,3,"Clique sur toutes les épithètes.",["Les","lutins","fatigués","restent","calmes","devant","un","feu","mourant"],[2,8],"« fatigués » et « mourant » qualifient directement un nom : ce sont des épithètes. « calmes » est relié au sujet par « restent » : c’est un attribut.",s)

# B : complément du nom (f6 p16)
c=CB
qcm("reconnaitre",c,1,"Quel groupe est le complément du nom « bague » ?",["Léa","porte","en argent","une"],2,"« en argent » complète le nom « bague » : c’est un complément du nom, relié à lui par la préposition « en ».",s,"Léa porte une bague en argent.")
clic("reconnaitre",c,1,"Clique sur la préposition qui introduit le complément du nom.",["Hugo","aime","la","soupe","de","potiron"],[4],"« de » relie le nom « soupe » à son complément « potiron » : c’est une préposition.",s)
vf(c,1,"Vrai ou faux ?","Le complément du nom suit toujours le nom qu’il complète.",True,"Le complément du nom se place toujours après le nom, alors que l’épithète peut le précéder.",s)
sais("produire",c,1,"Recopie le complément du nom.","le chant des oiseaux",["des oiseaux"],"« des oiseaux » complète le nom « chant » : c’est le complément du nom.",s)
tri("reconnaitre",c,2,"Classe ces compléments du nom selon leur classe grammaticale.",["un panier de fruits","la cabane du bûcheron","le désir de voyager","le souci de ceux-ci","une tasse de thé","la clé de la tour"],["nom","groupe nominal","pronom","infinitif"],[0,1,3,2,0,1],"Le complément du nom peut être un nom (de fruits, de thé), un groupe nominal (du bûcheron, de la tour), un pronom (de ceux-ci) ou un infinitif (de voyager).",s)
qcm("reconnaitre",c,2,"Quelle phrase contient un complément du nom ?",["Plume part dans la forêt.","Plume lit un livre de contes.","Plume lit pour se détendre.","Plume rentre avec Hugo."],1,"Dans « un livre de contes », « de contes » complète le nom « livre ». Dans les autres phrases, les groupes complètent le verbe ou la phrase.",s)
trous("completer",c,2,"Complète avec les prépositions contractées qui conviennent.","Plume mange un gâteau {{1}} chocolat et une tarte {{2}} pommes.",[(["au","aux","du"],0),(["au","aux","du"],1)],"« au » est la forme contractée de « à le » et « aux » de « à les » : « un gâteau au chocolat », « une tarte aux pommes ».",s)
sais("transformer",c,2,"Ajoute le complément du nom « de pierre » au groupe nominal.","un vieux pont",["un vieux pont de pierre"],"Le complément du nom se place après le nom : « un vieux pont de pierre ».",s)
corr(c,2,"Corrige la phrase : la préposition et l’article doivent se contracter.","Plume mange un gâteau à les pommes.",["Plume mange un gâteau aux pommes."],"« à les » se contracte en « aux » : « un gâteau aux pommes ».",s)
qcm("contexte",c,2,"Quelle information le complément du nom apporte-t-il ?",["le temps","la possession","la matière","le lieu"],3,"« de montagne » indique où se trouve la cabane : le complément du nom exprime le lieu.",s,"Plume habite une cabane de montagne.")
tri("contexte",c,3,"Quelle information chaque complément du nom apporte-t-il ?",["une statue de marbre","le courrier du matin","le coffre de Plume","un hibou de la forêt"],["temps","lieu","possession","matière"],[3,0,2,1],"« de marbre » : la matière. « du matin » : le temps. « de Plume » : la possession. « de la forêt » : le lieu.",s)
clic("contexte",c,3,"Clique sur tous les mots des compléments du nom.",["Le","chant","des","oiseaux","réveille","la","fille","du","meunier"],[2,3,7,8],"« des oiseaux » complète « chant » et « du meunier » complète « fille » : ce sont deux compléments du nom.",s)

# C : subordonnée relative (f7 p18)
c=CC;s=S7
qcm("reconnaitre",c,1,"Quel groupe est une subordonnée relative ?",["Plume ouvre le coffre","le coffre","que Hugo a trouvé","a trouvé"],2,"« que Hugo a trouvé » est introduite par le pronom relatif « que » et complète le nom « coffre » : c’est une subordonnée relative.",s,"Plume ouvre le coffre que Hugo a trouvé.")
clic("reconnaitre",c,1,"Clique sur le pronom relatif.",["Le","lutin","qui","dort","rêve"],[2],"« qui » reprend « le lutin » et introduit la subordonnée relative « qui dort ».",s)
vf(c,1,"Vrai ou faux ?","L’antécédent est toujours placé avant la subordonnée relative.",True,"Le nom que la relative complète s’appelle l’antécédent : il est toujours placé avant elle.",s)
sais("produire",c,1,"Recopie le pronom relatif.","Voici la tour où vit Hugo.",["où"],"« où » reprend « la tour » et introduit la subordonnée relative « où vit Hugo ».",s)
qcm("reconnaitre",c,2,"Quel est l’antécédent du pronom relatif ?",["Hugo","regarde","étoile","brille"],2,"« qui » reprend « l’étoile » : c’est l’antécédent, placé avant la relative « qui brille ».",s,"Hugo regarde l’étoile qui brille.")
tri("reconnaitre",c,2,"Ce pronom relatif est-il simple ou composé ?",["qui","lequel","dont","auxquelles","où","duquel"],["pronom relatif simple","pronom relatif composé"],[0,1,0,1,0,1],"Pronoms relatifs simples : qui, que, quoi, dont, où. Pronoms relatifs composés : lequel, auquel, duquel et leurs formes féminines et plurielles.",s)
trous("completer",c,2,"Complète avec les pronoms relatifs qui conviennent.","L’ami {{1}} chante est Hugo ; le livre {{2}} il parle est ancien.",[(["qui","que","dont"],0),(["que","dont","où"],1)],"« L’ami chante » : « qui » est sujet. « Il parle du livre » : le pronom relatif est « dont ».",s)
sais("transformer",c,2,"Réunis les deux phrases avec le pronom relatif « qui ».","Hugo tient une lanterne. La lanterne brille.",["Hugo tient une lanterne qui brille.","Hugo tient une lanterne qui brille"],"« qui » remplace « la lanterne », sujet de « brille » : « Hugo tient une lanterne qui brille. »",s)
corr(c,2,"Corrige le pronom relatif : il doit indiquer le lieu.","La forêt que vivent les lutins est sombre.",["La forêt où vivent les lutins est sombre.","La forêt dans laquelle vivent les lutins est sombre."],"Les lutins vivent dans la forêt : le pronom relatif indique le lieu, on emploie « où ».",s)
qcm("contexte",c,2,"Quelle est la fonction de la subordonnée relative ?",["sujet","COD","complément de l’antécédent","attribut"],2,"Une subordonnée relative est une expansion du nom : elle est complément de son antécédent, ici « la clé ».",s,"Plume cherche la clé que Hugo a perdue.")
tri("contexte",c,3,"Quelle est la fonction du pronom relatif entre crochets ?",["La pluie [qui] tombe me rend triste.","Les amis [que] Plume a invités arrivent.","Le livre [dont] tu parles est ancien.","La tour [où] dort Hugo est vieille.","Le lutin [qui] chante réveille Hugo.","Les baies [que] Léa cueille sont mûres."],["sujet","COD","COI","complément circonstanciel de lieu"],[0,1,2,3,0,1],"Le pronom relatif a sa fonction dans la relative : sujet (qui tombe), COD (que Plume a invités), COI (parles de : dont), complément de lieu (où dort Hugo).",s)
clic("contexte",c,3,"Clique sur tous les mots de la subordonnée relative.",["Plume","cherche","le","coffre","que","Hugo","a","caché"],[4,5,6,7],"La subordonnée relative est « que Hugo a caché », complément de l’antécédent « coffre ».",s)

rappel={"titre":"L’épithète, le complément du nom et la subordonnée relative","points":[
{"mot":"expansion du nom","definition":"Une expansion complète un nom à l’intérieur du groupe nominal. Il en existe trois : l’épithète, le complément du nom et la subordonnée relative.","exemple":"un vieux pont de pierre que Plume traverse"},
{"mot":"épithète","definition":"L’épithète est un adjectif ou un participe qui qualifie directement un nom, sans verbe entre les deux. Elle suit le nom, mais peut aussi le précéder. Certains adjectifs changent de sens selon leur place.","exemple":"un homme grand, un grand homme"},
{"mot":"complément du nom","definition":"Le complément du nom suit toujours le nom. Il est généralement relié à lui par une préposition. Il peut être un nom, un groupe nominal, un pronom, un infinitif ou un groupe infinitif.","exemple":"les rues de la ville ; une bague en or"},
{"mot":"information apportée par le complément du nom","definition":"Le complément du nom apporte une information sur le nom : la possession, la matière, le temps, le lieu…","exemple":"le coffre de Plume ; une statue de marbre"},
{"mot":"subordonnée relative","definition":"La subordonnée relative est une expansion du nom. Le nom qu’elle complète est son antécédent, toujours placé avant elle. Elle est introduite par un pronom relatif simple (qui, que, quoi, dont, où) ou composé (lequel, auquel, duquel…).","exemple":"Il possède un objet auquel il est très attaché."},
{"mot":"fonctions","definition":"La subordonnée relative est complément de son antécédent. Le pronom relatif a sa propre fonction dans la relative : sujet, COD, COI, complément de lieu…","exemple":"L’animal qui figure sur cette photo est un lémurien. (qui : sujet de figure)"}]}
mod=dict(module=M,titre="Épithète, complément du nom, subordonnée relative",domaine="grammaire",niveau=5,grade="ecuyer",version=1,
description="Reconnaître l’épithète et sa place, le complément du nom (préposition, classe, sens) et la subordonnée relative (antécédent, pronom relatif, fonctions).",
rappel=rappel,competences=[CA,CB,CC],exercices=ex)
json.dump(mod,open(M+".json","w",encoding="utf-8"),ensure_ascii=False,indent=2)
comp=json.load(open("competences.json",encoding="utf-8"))
assert len(comp["competences"])==51
for i,l in [(CA,"Reconnaître l’épithète (adjectif ou participe), sa place et son effet sur le sens"),(CB,"Reconnaître le complément du nom, sa préposition, sa classe grammaticale et l’information qu’il apporte"),(CC,"Reconnaître la subordonnée relative, son antécédent, le pronom relatif et leurs fonctions")]:
    comp["competences"].append(dict(id=i,domaine="grammaire",niveau=5,libelle=l))
json.dump(comp,open("competences.json","w",encoding="utf-8"),ensure_ascii=False,indent=2)
print(len(comp["competences"]))
