# Update notes – UI research answers applied (2026-10-21)

**Source:** `Meridia-UI-Testcases and Observations.xlsx` (161 rows of questions with the team's answers). A copy is kept in `research/ui-testcases-observations.csv`. All 161 `[CONFIRM]` markers were resolved: answers are folded into the article text, the "Draft edition" banner is gone, and screenshot placeholders are hidden by default in the offline guide (they remain in the Markdown/HTML for the writer to replace).

## What changed, by chapter
| Chapter | Notable changes |
|---|---|
| Getting started | Login troubleshooting lists the three server messages ("Invalid user credentials", "User with the specified email address not found.", "Inactive user state, Please ask account admin to activate your account"). MFA code is delivered by email. |
| Your account | Email cannot be changed; role is changed by the account administrator. |
| Library | Items are removed from the Library on the item's own page (menu → Remove from Library). |
| Vessels | MTI factors and daily refresh; Zone Type, STS Type and draught-change sign values; PurpleTRAC results saved for 24 h, "Unscored" explained; no vessel notifications/export on the Overview tab; company search is available on request only; error-page text. |
| Ports | Units (metres, tons, hours); dwell time = departure minus arrival; presets end 00:00 UTC previous day; inbound view has no side panel; berth timeline vs top-vessels table depends on the date period; features tied to the Meridia feature tag. |
| Zones / Custom zones | Traffic data is built on a previous-day basis (available 24 h after creation); visits = entry/exit pair, unique = by IMO; limit of 100 custom zones per user; uploads up to 1 MB; Polygon or Circle; circles must include a radius. |
| Fleets | CSV is named after the fleet; no list-view actions, no fleet alerts; Fleets need the fleet feature; location types and event definitions added. |
| Notifications | Any entity page can request an export; 100 downloads shown per page; Show Notifications options confirmed. |
| Meridia IQ | Access via account administrator; answers come from its connected database and aren't guaranteed correct; "No response text" means no information on the query; chat links are private; history grouped by period; chats kept as long as possible. |
| Held articles | Port Details/facilities, custom-zone delete and fleet filters stay unpublished (features not available). |

## Needs a product decision (articles word these cautiously)
| Row | Question |
|---|---|
| 3 | Answer says users can change their own name; the My Profile screen shows read-only details. Article says only that email and role can't be changed by the user. |
| 10 | Vessel switcher "Library" tab and grid/list page size ("discuss") – no limit is stated in the article. |
| 19, 25, 31 | Answers TBC/TBD: how an in-progress arrival looks, whether a failed event type shows an error, how positional discrepancies are detected. |
| 33 | Course/Heading showing 0 – answer says they should not; article only notes values may be missing. |
| 35 | MTI band mapping: answer says green = low and light green = very low risk, but the gauge runs light green → green with a higher score meaning lower risk. Article names red/orange/yellow bands and says "the two green shades mark the lower-risk bands". |
| 38 | PurpleTRAC answer is the five MTI risk bands; the screen shows Ok / Warning / Critical / Unscored. Meaning of each result is not published. |
| 66 | "Same route" for berth-event export is ambiguous. |
| 75 | "Expand All" greyed with no filter is called unintended – troubleshooting row removed. |
| 77 | Berth dwell chart: "system default as well user defined" – confirm a grouping control exists. |
| 78 / 82 / 88 | 90-day boundary for occupancy timeline vs top-vessels table (answers differ); article says "up to 90 days" = timeline. |
| 86 | Berths export columns may differ from the table ("maybe"). |
| 96 / 122 | Blank-map advice: "contact your account manager" vs "contact support" – align. |
| 110 | The 1000 m default circle radius is not intended – articles tell users to always include a radius. |
| 124 | Fleet composition calculations ("ignore") remain undocumented. |
| 143 / 147 | Meridia IQ "Error:" and blank-map advice unsure/"depends". |
| 144 | Meridia IQ score colours: answer is the five MTI bands; app uses 3.5 / 2.0 thresholds (three colours). |
| 151 | Chat groups: answer says Last 7 / 30 days; screen also shows Today and Older. |

## Not yet covered (in the product outline, not in the v1.11.0 code analysed)
Global Map View (global search, entity toggles, "Show global data", "In View" counter, map styles Simple / Satellite / C-MAP), dynamic fleets, **Port group** and **Zone group** creation, and the Library "Last updated" fleet column. Add once a build or branch containing them is available.

## For the product / development team (from the answers)
- "Unkown Berth" typo – should read "Unknown Berth" (row 80).
- "Expand All / Collapse All" disabled when no filter is active (row 75).
- Course / Heading display 0 when missing (row 33).
- No message when one event type fails to load (rows 25, 67).
- Port page has no port switcher – proposal to add one like vessels (row 48).
- Default 1000 m radius for circles without a radius (row 110).
- Composition "Export Image (PNG)" does nothing in "Show all" view (row 125).
