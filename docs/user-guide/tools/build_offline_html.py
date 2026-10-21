#!/usr/bin/env python3
"""Build ONE self-contained, offline HTML help centre from product-fruits/knowledge-base.
No network access needed: CSS, JS and all articles are inlined.
Usage (from docs/user-guide):  python3 tools/build_offline_html.py [out.html]"""
import os,re,sys,json,glob,html,datetime
sys.path.insert(0,os.path.dirname(__file__))
from md_to_pf_html import convert
ROOT="product-fruits/knowledge-base"
OUT=sys.argv[1] if len(sys.argv)>1 else "offline/Meridia-User-Guide.html"
JT={}  # journey folder -> title (from INDEX.md)
cur=None
for l in open(f"{ROOT}/INDEX.md",encoding="utf-8"):
    m=re.match(r"## (\d+) · (.+)",l)
    if m: JT[m.group(1)]=m.group(2).strip()
def clean(h):
    h=re.sub(r' style="[^"]*"','',h)                       # drop inline styles, use CSS classes
    h=re.sub(r'<p><strong>📷 Screenshot (\d+):</strong> (.*?)</p>',r'<div class="shot"><b>Screenshot \1</b> – \2</div>',h,flags=re.S)
    h=re.sub(r'(\[CONFIRM[^\]<]*\])',r'<mark class="confirm">\1</mark>',h)
    h=h.replace("<table>",'<div class="tw"><table>').replace("</table>","</table></div>")
    return h
arts=[]; journeys=[]
for jd in sorted(d for d in os.listdir(ROOT) if os.path.isdir(f"{ROOT}/{d}")):
    num=jd.split("-",1)[0]; j={"id":jd,"title":JT.get(num,jd),"articles":[]}
    for f in sorted(glob.glob(f"{ROOT}/{jd}/*.md")):
        title,body=convert(open(f,encoding="utf-8").read().splitlines())
        slug=os.path.basename(f)[:-3]; a={"id":f"{jd}/{slug}","journey":jd,"title":title,"html":clean(body)}
        a["text"]=re.sub(r"\s+"," ",html.unescape(re.sub(r"<[^>]+>"," ",body)))
        j["articles"].append(a["id"]); arts.append(a)
    journeys.append(j)
# link bold references like **How to log in** to the matching article
tl=[(a["title"].lower(),a["id"]) for a in arts]
def link(h):
    def rep(m):
        t=html.unescape(m.group(1)).strip().lower().rstrip(".")
        if not t.startswith("how to"): return m.group(0)
        c=[(tt,i) for tt,i in tl if tt==t] or sorted([(tt,i) for tt,i in tl if tt.startswith(t) or t.startswith(tt)],key=lambda x:len(x[0]))
        # exact match wins; otherwise the closest (shortest) title that starts with the reference
        return f'<a class="xref" href="#/{c[0][1]}">{m.group(1)}</a>' if c else m.group(0)
    return re.sub(r"<strong>([^<]+)</strong>",rep,h)
for a in arts: a["html"]=link(a["html"])
data=json.dumps({"journeys":journeys,"articles":{a["id"]:{"t":a["title"],"j":a["journey"],"h":a["html"],"x":a["text"]} for a in arts},
                 "built":datetime.date.today().isoformat()},ensure_ascii=False).replace("</","<\\/")
TEMPLATE=open(os.path.join(os.path.dirname(__file__),"offline_template.html"),encoding="utf-8").read()
out=TEMPLATE.replace("/*DATA*/",data)
os.makedirs(os.path.dirname(OUT) or ".",exist_ok=True)
open(OUT,"w",encoding="utf-8").write(out)
print(f"{OUT}: {len(arts)} articles, {len(journeys)} journeys, {len(out)//1024} KB")
