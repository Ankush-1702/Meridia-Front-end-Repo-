#!/usr/bin/env python3
"""Copy every user-guide article into product-fruits/knowledge-base/<journey>/NN-name.md
following the customer journey order, and write an INDEX.md. Run from docs/user-guide."""
import os,re,shutil,glob
J=[
("01-Getting-started","Sign in and stay secure",[
 "authentication/how-to-log-in","authentication/how-to-log-in-with-verification-code-mfa","authentication/how-to-reset-password","my-profile/how-to-sign-out"]),
("02-Your-account","Set up your account (My Profile)",[
 "my-profile/how-to-view-your-profile","my-profile/how-to-change-time-zone-and-theme","my-profile/how-to-manage-notification-popups","my-profile/how-to-change-password-from-my-profile"]),
("03-Library","Build and use your Library",[
 "library/how-to-navigate-the-library","library/how-to-add-to-library","library/how-to-use-search-filters","library/how-to-search-and-filter-your-library"]),
("04-Vessels","Research a vessel",[
 "vessels/how-to-open-and-read-a-vessel-page","vessels/how-to-switch-between-vessels","vessels/how-to-view-vessel-details-and-save-a-vessel",
 "vessels/how-to-view-a-vessels-track-on-the-map","vessels/how-to-replay-a-vessels-movements","vessels/how-to-read-the-event-timeline",
 "vessels/how-to-view-and-filter-vessel-events","vessels/how-to-read-the-events-tables","vessels/how-to-understand-the-mti-score","vessels/how-to-run-ptrac-screening",
 "company-search/how-to-open-company-search-from-a-vessel-page","company-search/how-to-read-company-details"]),
("05-Ports","Research a port",[
 "ports/how-to-open-and-read-a-port-page","ports/how-to-view-live-port-traffic-on-the-map","ports/how-to-read-port-congestion-and-utilisation",
 "ports/how-to-view-inbound-vessels","ports/how-to-read-the-port-events-table","ports/how-to-view-berths-in-a-port",
 "ports/how-to-view-berth-details-and-dwell-time","ports/how-to-view-vessel-occupancy-at-a-berth"]),
("06-Zones","Research a zone",[
 "zones/how-to-open-and-read-a-zone-page","zones/how-to-view-live-zone-traffic-on-the-map","zones/how-to-read-zone-traffic-charts","zones/how-to-read-the-zone-events-table"]),
("07-Custom-zones","Create and manage your own zones",[
 "library/how-to-create-custom-zone-shortcut","zones/how-to-view-and-manage-custom-zones","zones/how-to-create-a-custom-zone","zones/how-to-upload-a-zone-shape-file-or-geojson","zones/how-to-edit-a-custom-zone"]),
("08-Fleets","Create and monitor fleets",[
 "library/how-to-manage-fleets-in-library","fleets/how-to-create-a-fleet","fleets/how-to-open-and-read-a-fleet-page","fleets/how-to-view-your-fleet-on-the-map",
 "fleets/how-to-read-fleet-composition","fleets/how-to-view-fleet-events","fleets/how-to-edit-or-delete-a-fleet"]),
("09-Notifications","Stay informed",[
 "notifications/how-to-open-and-read-your-notifications","notifications/how-to-filter-and-manage-notifications-page","notifications/how-to-turn-notifications-on-for-a-port-or-zone","notifications/how-to-download-your-exports"]),
("10-Meridia-IQ","Ask Meridia IQ",[
 "meridia-iq/how-to-start-a-chat-with-meridia-iq","meridia-iq/how-to-read-meridia-iq-answers-and-maps","meridia-iq/how-to-ask-iq-about-a-vessel-port-or-zone","meridia-iq/how-to-manage-your-chat-history"]),
]
root="product-fruits/knowledge-base"
if os.path.isdir(root): shutil.rmtree(root)
os.makedirs(root)
mapped=set(); idx=["# Meridia Knowledge Base – articles by user journey\n",
 "Paste order for Product Fruits: go folder by folder, file by file (numbers show the order). Each file is Markdown; the matching paste-ready HTML is in `../articles/<file name without the NN- prefix>.html`. Screenshot placeholders look like `[SCREENSHOT n: …]`. `[CONFIRM]` tags mark open questions (see `../../CONFIRM-ITEMS.md`).\n"]
for folder,title,items in J:
    os.makedirs(f"{root}/{folder}")
    idx.append(f"\n## {folder.split('-',1)[0]} · {title}\n")
    for n,src in enumerate(items,1):
        mapped.add(src); name=os.path.basename(src)
        dst=f"{root}/{folder}/{n:02d}-{name}.md"
        shutil.copy(f"{src}.md",dst)
        t=open(f"{src}.md",encoding="utf-8").readline().lstrip("# ").strip()
        idx.append(f"{n}. [{t}]({folder}/{n:02d}-{name}.md)")
allmd={f[:-3] for f in glob.glob("*/*.md") if "/_unpublished/" not in f and not f.startswith("product-fruits")}
missing=allmd-mapped; extra=mapped-allmd
assert not missing and not extra,(missing,extra)
open(f"{root}/INDEX.md","w",encoding="utf-8").write("\n".join(idx)+"\n")
print(len(mapped),"articles in",len(J),"journeys")
