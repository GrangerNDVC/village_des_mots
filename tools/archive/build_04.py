import json
M="gram-5e-mots-invariables"
S4="manuel-5e-f4-p14"; S5="manuel-5e-f5-p15"
CA,CB,CC="gram-5e-preposition-emploi","gram-5e-conjonction-types","gram-5e-adverbe-categories"
ex=[]
def add(t,f,c,d,cons,src,**kw):
    ex.append(dict(id=f"{M}-{len(ex)+1:03d}",type=t,forme=f,competence=c,difficulte=d,consigne=cons,**kw,source=src))
TOL={"casse":False,"accents":False}
def sais(f,c,d,cons,en,acc,expl,src): add("saisie",f,c,d,cons,src,enonce=en,reponses_acceptees=acc,tolerance=TOL,explication=expl)
def qcm(f,c,d,cons,ch,r,expl,src,en=None):
    kw=dict(choix=ch,reponse=r,explication=expl)
    if en: kw["enonce"]=en
    add("qcm",f,c,d,cons,src,**({"enonce":en} if en else {}),**kw) if False else add("qcm",f,c,d,cons,src,**({"enonce":en} if en else {}),choix=ch,reponse=r,explication=expl)
def vf(c,d,cons,en,r,expl,src): add("vrai_faux","reconnaitre",c,d,cons,src,enonce=en,reponse=r,explication=expl)
def clic(f,c,d,cons,mots,cib,expl,src): add("clic_mot",f,c,d,cons,src,mots=mots,cibles=cib,explication=expl)
def tri(f,c,d,cons,els,cats,sol,expl,src): add("tri",f,c,d,cons,src,elements=els,categories=cats,solution=dict(zip(els,sol)),explication=expl)
def trous(f,c,d,cons,en,tr,expl,src): add("texte_trous",f,c,d,cons,src,enonce=en,trous=[dict(id=i+1,choix=ch,reponse=r) for i,(ch,r) in enumerate(tr)],explication=expl)
def corr(c,d,cons,fa,ok,expl,src): add("corriger","corriger",c,d,cons,src,phrase_fautive=fa,corrections_acceptees=ok,explication=expl)

# ---- A : prépositions (f4 p14)
c=CA;s=S4
qcm("reconnaitre",c,1,"Quel mot est une préposition ?",["Plume","marche","vers","forêt"],2,"« vers » introduit le groupe « la forêt » et ne change jamais de forme : c’est une préposition.",s,"Plume marche vers la forêt.")
clic("reconnaitre",c,1,"Clique sur la préposition.",["Hugo","vit","chez","Léa"],[2],"« chez » introduit le nom « Léa » : c’est une préposition.",s)
vf(c,1,"Vrai ou faux ?","Une préposition se place devant un nom, un groupe nominal, un pronom ou un infinitif.",True,"Les prépositions (à, de, dans, pour, sans…) introduisent un nom, un groupe nominal, un pronom ou un infinitif.",s)
sais("produire",c,1,"Recopie la préposition de la phrase.","Les lutins dansent sans musique.",["sans"],"« sans » introduit le nom « musique » : c’est une préposition.",s)
trous("completer",c,2,"Complète avec les prépositions qui conviennent.","Hugo écrit {{1}} une plume et part {{2}} sa lanterne.",[(["avec","contre","jusqu’à"],0),(["sans","sur","contre"],0)],"On écrit « avec une plume » et on part « sans sa lanterne » : ce sont les seules prépositions qui donnent une phrase correcte.",s)
tri("reconnaitre",c,2,"Classe ces mots : préposition ou conjonction de coordination ?",["pour","car","avec","mais","chez","donc"],["préposition","conjonction de coordination"],[0,1,0,1,0,1],"Les prépositions (pour, avec, chez) introduisent un groupe de mots. Les conjonctions de coordination (car, mais, donc) relient des mots ou des propositions.",s)
qcm("reconnaitre",c,2,"Quelle expression est une locution prépositive ?",["près de","parce que","c’est pourquoi","tout à coup"],0,"« près de » est un groupe de mots invariable qui joue le rôle d’une préposition. « parce que » est une locution conjonctive, « c’est pourquoi » un adverbe de liaison, « tout à coup » une locution adverbiale.",s)
qcm("completer",c,2,"Quelle préposition complète la phrase ?",["jusqu’à","pendant","parce que","mais"],0,"On marche « jusqu’à » la lisière : « jusqu’à » est une préposition qui introduit le groupe nominal « la lisière ».",s,"Plume a marché … la lisière du bois.")
sais("transformer",c,2,"Remplace la préposition « devant » par « derrière ».","Le renard se cache devant la cabane.",["Le renard se cache derrière la cabane.","Le renard se cache derrière la cabane"],"On remplace seulement la préposition : « Le renard se cache derrière la cabane. »",s)
corr(c,2,"Corrige la phrase : il manque un mot à la locution prépositive.","Léa s’est assise à côté la fenêtre.",["Léa s’est assise à côté de la fenêtre."],"La locution prépositive « à côté de » se termine par « de » devant le groupe nominal « la fenêtre ».",s)
tri("contexte",c,3,"Le mot entre crochets est-il une préposition ou un adverbe ?",["Plume arrive [après] Hugo.","Plume arrive [après].","Hugo dort [devant] la porte.","Hugo regarde [devant].","Léa rentre [avant] la nuit.","Léa est venue [avant]."],["préposition","adverbe"],[0,1,0,1,0,1],"Une préposition introduit un groupe de mots (après Hugo, devant la porte, avant la nuit). Un adverbe est employé seul : il n’introduit rien (arrive après, regarde devant, venue avant).",s)
clic("contexte",c,3,"Clique sur toutes les prépositions.",["Après","le","dîner","Plume","part","chez","Hugo","pour","parler"],[0,5,7],"« Après », « chez » et « pour » introduisent chacune un mot, un groupe nominal ou un infinitif : ce sont des prépositions.",s)

# ---- B : conjonctions (f4 p14)
c=CB
qcm("reconnaitre",c,1,"Quel mot est une conjonction de coordination ?",["veut","mais","préfère","Hugo"],1,"« mais » relie deux propositions : c’est une conjonction de coordination.",s,"Hugo veut partir, mais Plume préfère rester.")
clic("reconnaitre",c,1,"Clique sur la conjonction de subordination.",["Plume","dort","quand","la","nuit","tombe"],[2],"« quand » introduit la subordonnée « quand la nuit tombe » : c’est une conjonction de subordination.",s)
vf(c,1,"Vrai ou faux ?","Le mot « car » est une conjonction de coordination.",True,"Les conjonctions de coordination sont : mais, ou, et, donc, or, ni, car.",s)
sais("produire",c,1,"Recopie la conjonction de subordination.","Hugo sourit puisque Léa arrive.",["puisque"],"« puisque » introduit la subordonnée « puisque Léa arrive » : c’est une conjonction de subordination.",s)
tri("reconnaitre",c,2,"Cette conjonction est-elle de coordination ou de subordination ?",["or","afin que","ni","tandis que","donc","dès que"],["coordination","subordination"],[0,1,0,1,0,1],"Coordination : mais, ou, et, donc, or, ni, car. Subordination : que, quand, lorsque, dès que, tandis que, afin que, parce que…",s)
trous("completer",c,2,"Complète avec les conjonctions de coordination qui conviennent.","Hugo n’aime {{1}} le froid {{2}} la pluie.",[(["ni","ou","mais"],0),(["ni","et","car"],0)],"« ni » est généralement redoublé : « ni le froid ni la pluie ».",s)
qcm("completer",c,2,"Quelle conjonction de subordination complète la phrase ?",["afin que","parce que","quand","alors que"],0,"« afin que » exprime le but et se construit avec le subjonctif (« puissent voir »). Les autres conjonctions ne conviennent pas ici.",s,"Plume allume sa lanterne … les lutins puissent voir le chemin.")
sais("transformer",c,2,"Relie les deux phrases avec « parce que ».","Les lutins rentrent. Le soir tombe.",["Les lutins rentrent parce que le soir tombe.","Les lutins rentrent parce que le soir tombe"],"« parce que » introduit la subordonnée « parce que le soir tombe ».",s)
corr(c,2,"Corrige la phrase : la négation « ni » doit être redoublée.","Plume ne mange ni pain ou fromage.",["Plume ne mange ni pain ni fromage."],"« ni » est généralement redoublé : « ni pain ni fromage ».",s)
qcm("contexte",c,2,"Dans quelle phrase « que » est-il une conjonction de subordination ?",["Je crois que tu as raison.","Le coffre que Hugo ouvre est vide.","Que cherches-tu ?","Voici le livre que Léa lit."],0,"Dans « Je crois que tu as raison », « que » relie deux propositions : c’est une conjonction de subordination. Dans « Le coffre que… » et « le livre que… », c’est un pronom relatif ; dans « Que cherches-tu ? », un pronom interrogatif.",s)
tri("contexte",c,3,"Le mot entre crochets est-il une conjonction de coordination ou de subordination ?",["Hugo dort [car] il est fatigué.","Hugo dort [puisque] Plume veille.","Plume veille [et] Hugo dort.","Plume veille [tandis que] Hugo dort.","Plume veille [mais] Hugo dort.","Plume veille [pendant que] Hugo dort."],["coordination","subordination"],[0,1,0,1,0,1],"« car », « et » et « mais » relient deux propositions de même niveau. « puisque », « tandis que » et « pendant que » introduisent une subordonnée.",s)
clic("contexte",c,3,"Clique sur toutes les conjonctions.",["Hugo","rit","quand","Plume","chante","mais","Léa","dort"],[2,5],"« quand » est une conjonction de subordination et « mais » une conjonction de coordination.",s)

# ---- C : adverbes (f5 p15)
c=CC;s=S5
qcm("reconnaitre",c,1,"Quel mot est un adverbe ?",["hibou","vole","silencieusement","Le"],2,"« silencieusement » précise le verbe « vole » et ne change jamais de forme : c’est un adverbe.",s,"Le hibou vole silencieusement.")
clic("reconnaitre",c,1,"Clique sur l’adverbe d’intensité.",["Cette","tour","est","très","haute"],[3],"« très » précise l’adjectif « haute » et exprime l’intensité.",s)
vf(c,1,"Vrai ou faux ?","« Cependant » est un adverbe de liaison.",True,"Les adverbes de liaison (en effet, de plus, cependant, c’est pourquoi, d’abord, puis…) relient des phrases ou des idées.",s)
sais("produire",c,1,"Recopie l’adverbe circonstanciel de lieu.","Plume cherche son livre ici.",["ici"],"« ici » indique le lieu : c’est un adverbe circonstanciel de lieu.",s)
tri("reconnaitre",c,2,"Classe ces adverbes selon leur catégorie.",["demain","trop","cependant","jamais","vite","assez","puis","guère"],["circonstanciel","intensité ou quantité","liaison","négation"],[0,1,2,3,0,1,2,3],"Circonstanciels : demain (temps), vite (manière). Intensité ou quantité : trop, assez. Liaison : cependant, puis. Négation : jamais, guère.",s)
trous("completer",c,2,"Complète avec les adverbes de liaison qui conviennent.","Il pleut, {{1}} nous restons ici. {{2}}, nous jouerons aux cartes.",[(["c’est pourquoi","cependant","d’abord"],0),(["Ensuite","En effet","Cependant"],0)],"« c’est pourquoi » exprime la conséquence et « Ensuite » indique ce qui vient après.",s)
qcm("reconnaitre",c,2,"Quelle phrase contient un adverbe d’intensité ?",["Plume arrive demain.","Plume est très fatigué.","Plume ne dort pas.","Plume parle doucement."],1,"« très » précise l’adjectif « fatigué » : c’est un adverbe d’intensité. « demain » et « doucement » sont circonstanciels ; « ne… pas » est une négation.",s)
sais("transformer",c,2,"Remplace le groupe nominal « avec lenteur » par un adverbe en -ment.","Hugo marche avec lenteur.",["Hugo marche lentement.","Hugo marche lentement"],"« avec lenteur » exprime la manière : on peut le remplacer par l’adverbe « lentement ».",s)
sais("transformer",c,2,"Mets la phrase à la forme négative avec « ne… jamais ».","Hugo ment.",["Hugo ne ment jamais.","Hugo ne ment jamais"],"« ne » se place devant le verbe et « jamais » après lui : « Hugo ne ment jamais. »",s)
corr(c,2,"Corrige la phrase : il manque un mot de la négation.","Hugo sort plus la nuit.",["Hugo ne sort plus la nuit."],"Les adverbes de négation sont formés de « ne » devant le verbe et d’un second mot (plus, pas, jamais…).",s)
tri("contexte",c,3,"Dans chaque phrase, « plus » est-il un adverbe de négation ou de quantité ?",["Hugo ne mange plus de miel.","Hugo mange plus de miel.","Il n’y a plus de baies.","Plume est plus rapide que Hugo.","Léa ne veut plus partir.","Léa veut plus de temps."],["adverbe de négation","adverbe de quantité ou d’intensité"],[0,1,0,1,0,1],"« plus » est un adverbe de négation quand il s’associe à « ne » (ne… plus). Sans « ne », il exprime la quantité ou l’intensité.",s)
clic("contexte",c,3,"Clique sur tous les adverbes.",["Hier","Plume","a","très","bien","dormi","mais","Hugo","veille","encore"],[0,3,4,9],"« Hier », « très », « bien » et « encore » sont des adverbes. « mais » est une conjonction de coordination.",s)

rappel={"titre":"Les prépositions, les conjonctions et les adverbes","points":[
{"mot":"préposition","definition":"La préposition se place devant un nom, un groupe nominal, un pronom, un infinitif ou un groupe infinitif. Elle est invariable. Quelques prépositions : à, de, dans, pour, sans, par, contre, vers, chez, avec. Certaines sont des groupes de mots, les locutions prépositives : près de, jusqu’à, à côté de.","exemple":"Plume part chez Hugo pour parler."},
{"mot":"conjonction de coordination","definition":"Les conjonctions de coordination mais, ou, et, donc, or, ni, car relient deux mots, deux groupes de mots ou deux propositions.","exemple":"Le gâteau est petit mais délicieux."},
{"mot":"conjonction de subordination","definition":"Les conjonctions de subordination introduisent une subordonnée conjonctive : que, quand, lorsque, dès que, après que, pendant que, tandis que, alors que, parce que, puisque, comme, pour que, afin que, quoique…","exemple":"Hugo sourit quand Plume arrive."},
{"mot":"adverbe","definition":"Les adverbes sont des mots invariables qui précisent, le plus souvent, le sens d’un adjectif ou d’une action.","exemple":"Un fruit bien mûr. Vous marchez vite."},
{"mot":"catégories d’adverbes","definition":"Adverbes circonstanciels : ici (lieu), toujours (temps), vite, facilement (manière). Adverbes d’intensité et de quantité : si, tant, tellement, très, plus, trop, assez. Adverbes de liaison : en effet, aussi, de plus, cependant, c’est pourquoi, d’abord, puis. Adverbes de négation : non, ne (généralement suivi de pas, plus, jamais, guère).","exemple":"Il pleut, c’est pourquoi nous ne sortons pas."}]}
mod=dict(module=M,titre="Prépositions, conjonctions, adverbes",domaine="grammaire",niveau=5,grade="ecuyer",version=1,
description="Reconnaître et employer les prépositions, distinguer les conjonctions de coordination et de subordination, reconnaître l’adverbe et sa catégorie (circonstanciel, intensité ou quantité, liaison, négation).",
rappel=rappel,competences=[CA,CB,CC],exercices=ex)
json.dump(mod,open(M+".json","w",encoding="utf-8"),ensure_ascii=False,indent=2)
comp=json.load(open("/mnt/project/competences.json",encoding="utf-8"))
assert len(comp["competences"])==48
for i,l in [(CA,"Reconnaître et employer les prépositions et les locutions prépositives"),(CB,"Distinguer et employer les conjonctions de coordination et de subordination"),(CC,"Reconnaître l’adverbe et sa catégorie (circonstanciel, intensité ou quantité, liaison, négation)")]:
    comp["competences"].append(dict(id=i,domaine="grammaire",niveau=5,libelle=l))
json.dump(comp,open("competences.json","w",encoding="utf-8"),ensure_ascii=False,indent=2)
print(len(comp["competences"]))
