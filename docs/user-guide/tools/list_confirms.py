#!/usr/bin/env python3
"""Flat list of every [CONFIRM] item, in knowledge-base (user journey) order. Run from docs/user-guide."""
import re,glob,os,csv
root="product-fruits/knowledge-base"
def clean(l):
    l=l.strip()
    l=re.sub(r"^\d+\.\s+","",l); l=re.sub(r"^-\s+","",l)
    if l.startswith("|"):
        cells=[c.strip() for c in l.strip("|").split("|")]; l="  —  ".join(c for c in cells if c)
    l=re.sub(r"\*\*(\[CONFIRM[^\]]*\])\*\*",r"\1",l)
    l=l.replace("**","").replace("`","")
    return re.sub(r"\s+"," ",l)
def title(p): return open(p,encoding="utf-8").readline().lstrip("# ").strip()
rows=[]
journeys=sorted(d for d in os.listdir(root) if os.path.isdir(f"{root}/{d}"))
for j in journeys:
    jn=j.split("-",1)[1].replace("-"," ")
    for f in sorted(glob.glob(f"{root}/{j}/*.md")):
        for i,l in enumerate(open(f,encoding="utf-8"),1):
            if "CONFIRM" in l: rows.append((jn,title(f),clean(l),os.path.relpath(f,root)))
held=[]
for f in sorted(glob.glob("*/_unpublished/*.md")):
    for l in open(f,encoding="utf-8"):
        if "CONFIRM" in l: held.append(("(held article)",title(f),clean(l),f))
allr=rows+held
out=["# All open [CONFIRM] items – one list\n",
 f"Total: **{len(allr)}** ({len(rows)} in published articles + {len(held)} in held articles). Order = knowledge-base user-journey order. Each line: what is unconfirmed, then the article it is in. Write your answer after the item or in the CSV (`CONFIRM-ITEMS.csv`).\n",
 "Owner key – PM = product · BE = backend/data · FE = front-end dev · SUP = support · QA = check in running app (see CONFIRM-LIST.md for the grouped view on branch confirm-list).\n"]
for n,(j,t,txt,f) in enumerate(allr,1):
    out.append(f"{n}. **{t}** ({j}) — {txt}")
open("CONFIRM-ITEMS.md","w",encoding="utf-8").write("\n".join(out)+"\n")
with open("CONFIRM-ITEMS.csv","w",newline="",encoding="utf-8") as fh:
    w=csv.writer(fh); w.writerow(["#","Journey","Article","Item to confirm","File","Owner","Answer"])
    for n,(j,t,txt,f) in enumerate(allr,1): w.writerow([n,j,t,txt,f,"",""])
print(len(allr),len(rows),len(held))
