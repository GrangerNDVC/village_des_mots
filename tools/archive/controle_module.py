import json, re, collections, sys
mod_path, comp_path = sys.argv[1], sys.argv[2]
comp = json.load(open(comp_path, encoding="utf-8")); m = json.load(open(mod_path, encoding="utf-8"))
cids = {c["id"] for c in comp["competences"]}; err=[]; seen=set(); by=collections.defaultdict(list)
for k,e in enumerate(m["exercices"],1):
    i=e["id"]
    if i!=f"{m['module']}-{k:03d}": err.append("id "+i)
    if i in seen: err.append("doublon "+i)
    seen.add(i)
    if e["competence"] not in m["competences"] or e["competence"] not in cids: err.append("comp "+i)
    if e["difficulte"] not in (1,2,3): err.append("diff "+i)
    if not e.get("explication") or not e.get("consigne"): err.append("texte "+i)
    by[e["competence"]].append(e); t=e["type"]
    if t=="qcm":
        if not 0<=e["reponse"]<len(e["choix"]) or len(set(e["choix"]))!=len(e["choix"]): err.append("qcm "+i)
    elif t=="clic_mot":
        if not e["cibles"] or any(not 0<=c<len(e["mots"]) for c in e["cibles"]): err.append("clic "+i)
    elif t=="vrai_faux":
        if not isinstance(e["reponse"],bool): err.append("vf "+i)
    elif t=="saisie":
        if not e["reponses_acceptees"]: err.append("saisie "+i)
    elif t=="tri":
        if set(e["solution"])!=set(e["elements"]) or len(set(e["elements"]))!=len(e["elements"]) or any(not 0<=v<len(e["categories"]) for v in e["solution"].values()): err.append("tri "+i)
    elif t=="texte_trous":
        if sorted(int(x) for x in re.findall(r"\{\{(\d+)\}\}",e["enonce"]))!=sorted(tr["id"] for tr in e["trous"]): err.append("trous "+i)
        for tr in e["trous"]:
            if not 0<=tr["reponse"]<len(tr["choix"]): err.append("trou borne "+i)
    elif t=="association":
        if len({p[0] for p in e["paires"]})!=len(e["paires"]) or len({p[1] for p in e["paires"]})!=len(e["paires"]): err.append("assoc "+i)
    elif t=="ordre":
        if sorted(e["elements_melanges"])!=sorted(e["reponse"]) or e["elements_melanges"]==e["reponse"]: err.append("ordre "+i)
    elif t=="corriger":
        if not e["corrections_acceptees"] or e["phrase_fautive"] in e["corrections_acceptees"]: err.append("corriger "+i)
    else: err.append("type "+t)
if "'" in open(mod_path,encoding="utf-8").read(): err.append("apostrophe droite")
for c in m["competences"]:
    l=by[c]; print(c,len(l),"ex | formes",len({e['forme'] for e in l}),"| diff",dict(sorted(collections.Counter(e['difficulte'] for e in l).items())),"| types",len({e['type'] for e in l}))
    if len(l)!=12 or len({e['forme'] for e in l})<4: err.append("couverture "+c)
print("total",len(m["exercices"]),"| ERREURS:",err or "aucune")
