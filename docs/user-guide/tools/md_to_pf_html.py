#!/usr/bin/env python3
"""Convert a user-guide .md article into clean, paste-ready HTML for the
Product Fruits knowledge-base editor (semantic tags + inline styles only).

Usage: md_to_pf_html.py <in.md> <out.html>
"""
import html
import re
import sys

SHOT = re.compile(r"^`\[SCREENSHOT (\d+): (.*)\]`$")


def inline(t):
    t = html.escape(t, quote=False)
    t = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t)
    t = re.sub(r"(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)", r"<em>\1</em>", t)
    t = re.sub(r"`(.+?)`", r"<code>\1</code>", t)
    return t


def shot(m):
    return (
        '<p style="background:#fff7ed;border:1px dashed #ea580c;padding:8px 12px;'
        'border-radius:6px;color:#9a3412;">'
        f"<strong>📷 Screenshot {m.group(1)}:</strong> {inline(m.group(2))}</p>"
    )


def convert(lines):
    out, i, title = [], 0, ""
    while i < len(lines):
        ln = lines[i].rstrip()
        if not ln.strip():
            i += 1
        elif ln.startswith("# "):
            title = ln[2:].strip()
            i += 1
        elif ln.startswith("## "):
            out.append(f"<h2>{inline(ln[3:])}</h2>")
            i += 1
        elif ln.startswith("### "):
            out.append(f"<h3>{inline(ln[4:])}</h3>")
            i += 1
        elif ln.startswith("|"):
            rows = []
            while i < len(lines) and lines[i].startswith("|"):
                rows.append([c.strip() for c in lines[i].strip().strip("|").split("|")])
                i += 1
            head, body = rows[0], [r for r in rows[2:]]
            th = "".join(f'<th style="text-align:left;border:1px solid #d1d5db;padding:6px 10px;background:#f3f4f6;">{inline(c)}</th>' for c in head)
            tb = "".join(
                "<tr>" + "".join(f'<td style="border:1px solid #d1d5db;padding:6px 10px;">{inline(c)}</td>' for c in r) + "</tr>"
                for r in body
            )
            out.append(f'<table style="border-collapse:collapse;width:100%;"><thead><tr>{th}</tr></thead><tbody>{tb}</tbody></table>')
        elif re.match(r"^\d+\. ", ln):
            items = []
            while i < len(lines) and (re.match(r"^\d+\. ", lines[i]) or (lines[i].startswith("   ") and lines[i].strip())):
                cur = lines[i].rstrip()
                if re.match(r"^\d+\. ", cur):
                    items.append([inline(re.sub(r"^\d+\. ", "", cur)), []])
                else:
                    s = cur.strip()
                    m = SHOT.match(s)
                    items[-1][1].append(("shot", shot(m)) if m else ("li", inline(s[2:])) if s.startswith("- ") else ("txt", inline(s)))
                i += 1
            html_items = []
            for text, subs in items:
                body, lis = text, [s for k, s in subs if k == "li"]
                extra = "".join(s for k, s in subs if k in ("shot", "txt"))
                if lis:
                    body += "<ul>" + "".join(f"<li>{x}</li>" for x in lis) + "</ul>"
                html_items.append(f"<li>{body}{extra}</li>")
            out.append("<ol>" + "".join(html_items) + "</ol>")
        elif ln.startswith("- "):
            items = []
            while i < len(lines) and lines[i].startswith("- "):
                items.append(inline(lines[i][2:].rstrip()))
                i += 1
            out.append("<ul>" + "".join(f"<li>{x}</li>" for x in items) + "</ul>")
        elif SHOT.match(ln.strip()):
            out.append(shot(SHOT.match(ln.strip())))
            i += 1
        else:
            out.append(f"<p>{inline(ln.strip())}</p>")
            i += 1
    return title, "\n".join(out)


if __name__ == "__main__":
    title, body = convert(open(sys.argv[1], encoding="utf-8").read().splitlines())
    open(sys.argv[2], "w", encoding="utf-8").write(f"<!-- Product Fruits KB article. Title: {html.escape(title)} -->\n{body}\n")
