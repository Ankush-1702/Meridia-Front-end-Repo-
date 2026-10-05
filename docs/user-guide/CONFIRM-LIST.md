# Meridia User Guide – Open [CONFIRM] Questions

Compiled from all drafted articles (163 `[CONFIRM]` markers across 10 modules, de-duplicated into the questions below). Each item says **who can answer**, **what we assumed in the draft**, and **which articles change** once answered.

How to use: answer in the "Answer" column (or reply "OK as drafted"). After answers come back, the `[CONFIRM]` tags are removed and the HTML is regenerated.

Legend – **Owner**: PM = product owner · BE = backend/data team · FE = front-end developers · SUP = support/customer success · QA = verify in a running environment.

## Already decided (no action – for the record)
| Decision | Applied in |
|---|---|
| MTI, PurpleTRAC screening and Ask IQ are available only to entitled accounts/users | Vessels, Library, Fleets, Ports articles |
| Users without the **Meridia** feature see no Meridia content | Library, My Profile (on the Vessels PR branch) |
| Fleet cap is fixed at 1,000 vessels | Fleets |
| Events-tab 90-day window stays as is for now | Vessels |
| Note: the app shows a hover card with a **More about MTI / PurpleTRAC** link, not a "Contact us" box on click – articles describe the link | Vessels, Fleets |

## A. Product decisions (PM)
| # | Question | Draft assumption | Articles |
|---|---|---|---|
| A1 | **Company search (Beta)** has no entitlement check in the front end – the icon shows for any ownership name. Should it be limited to certain accounts? | Described as available to everyone, with a [CONFIRM] | Company search |
| A2 | Should locked sections (Berths, Inbound vessels, Congestion) show a **Contact us** path? Port articles say "locked sections lead to Contact us" but the code shows no such box in Ports. | Wording kept, flagged | Ports (congestion, berths, inbound, berth details, occupancy) |
| A3 | How does a customer **request a change** to their name, email or role? (earlier answer was "Yes" – need the actual process/contact) | "Contact your account administrator or support" | My Profile |
| A4 | What does a user see/do when the **Meridia feature isn't enabled** or they lack Library access (user said they see nothing)? Confirm the sentence to use. | "You won't be able to see Meridia content – contact your administrator or Pole Star" | Library, My Profile |
| A5 | **Dynamic fleets** and **custom-zone delete**, **port Details (WPI) tab** are switched off in the app. Are any planned for release? If yes, when (so we publish the held articles)? | Held in `_unpublished/`; not in KB | Fleets, Zones, Ports |
| A6 | Meridia IQ: how is access granted/requested by a customer? What may we say about what IQ can/can't answer, data used, accuracy, retention of chats (how long), and whether shared chat links open for other users? | Wording is neutral; app's own advice "We recommend verifying key information" quoted | Meridia IQ (all 4) |
| A7 | Rename: only possible via **Edit** (no standalone rename). Acceptable to document that way? | Documented via Edit | Fleets |
| A8 | Exports: which export types are customer-facing and what are the file formats/columns/names (events export, berths export, fleet list CSV, composition PNG, company vCard/CSV)? | Described as in the UI; columns marked | Vessels, Ports, Zones, Fleets, Notifications, Company search |

## B. Metric & term definitions (BE / data team) – needed for the glossary
| # | Term(s) | Where used |
|---|---|---|
| B1 | **MTI score**: how calculated, refresh frequency, meaning of colour/bands (UI shows a red→green gauge and a 0–5 scale; Meridia IQ table uses ≥3.5 green, ≥2.0 amber, else red) | Vessels (MTI), Meridia IQ, Fleets |
| B2 | **PurpleTRAC** results: meaning of **Ok / Warning / Critical / Unscored**, why a vessel is Unscored, whether runs are saved/limited | Vessels (PTRAC), Notifications (severity), Ports |
| B3 | Event definitions: **Area Arrival/Departure vs Arrival/Departure vs Berth Arrival/Departure**, **Zone Entry/Exit**, **AIS Gap**, **STS Pairing** (and STS Type values), **Positional Discrepancy**, **Port State Control** (Detained, Defects), **Draught Change** sign | Vessels, Ports, Zones, Fleets |
| B4 | **In port / inbound / in zone**: definitions; how a vessel is matched to a port; what "reported" destination means; ATA/ETA sources and freshness; Next Port (Destination/ETA) source | Ports, Zones, Vessels, Fleets |
| B5 | **Port congestion & utilisation** metrics: arrivals, unique arrivals per day (avg/max), dwell time at berth (avg/median), congestion; whether end date is included; Vessel Class values; "Visits" count rule | Ports, Zones |
| B6 | **Berth metrics**: units for Length, Max LOA, Max DWT, Depth (LW), dwell times (chart axis says hrs), Duration/Gap time; how gaps are computed; whether Daily/Weekly granularity is chosen by the server | Ports (berths) |
| B7 | **Fleet composition**: Average age, Total DWT, size bands in Class, Age profile, Share %, when bars turn grey, Dimensions units; fleet map marker colour list | Fleets |
| B8 | **Zone/Port data cut-off & schedule**: presets end "yesterday (UTC)"; new custom-zone banner says "24 hours… processed daily" (code uses 15 min on test) – what is the true schedule? | Zones, Ports |
| B9 | Navigational Status: numeric codes → text mapping; Location Type and Zone Type values; Vessel Type colours | Ports, Fleets, Vessels |
| B10 | Notifications: default events when **Enable Live Notifications** is switched on; email timing options; exact labels of **Show Notifications** (expected: All, last 7 days, last 24 hours); is Risk from PurpleTRAC Auto-Screening; do removed bell items stay on the page | Notifications |
| B11 | Notifications page: behaviour beyond the first 500 rows; how many recent exports are listed; where an export is requested (vessel/port/zone/fleet?) | Notifications |
| B12 | WPI data (port Details, if enabled): source, edition, update date, units, empty categories | Ports (held) |
| B13 | Custom zones: maximum file size for uploads; default 1000 m radius when a circle has no radius in a file (intended?); maximum number of zones per account; true list-page row cap/pagination | Zones |
| B14 | Company details (Beta): result contents/accuracy, whether the 160 s timeout matches the backend, what "Match Type / shell company" mean | Company search |
| B15 | Data sources and refresh frequency for vessel details fields (particulars, ownership) | Vessels |

## C. Front-end behaviour – confirm intended or fix (FE / PM)
| # | Observation (verified in code) | Draft treatment |
|---|---|---|
| C1 | Events tables show **0** instead of "–" for missing speed/course/heading/draught; Detained shows "No" when missing | Documented as shown, flagged |
| C2 | A failed events/berth/port fetch **silently drops** that event type (empty table) | Troubleshooting says "Refresh" |
| C3 | **PurpleTRAC starts automatically** whenever the section is expanded (no Run button); times out at 160 s with a generic error | Documented as behaviour |
| C4 | **Ask IQ auto-sends** the prompt (no edit step); welcome-screen example prompts aren't clickable | Documented as behaviour |
| C5 | Notifications: **View All / Refresh / clicking a bell item** clears the bell list, pop-ups and count; View All also empties the bell's Downloads list | Documented |
| C6 | Berths: **Expand All / Collapse All / Reset Filters** disabled when no filter is active (all selected by default) | Documented; likely bug |
| C7 | Fleet list **Export Data (CSV)** downloads `berths-export.csv`; Composition **Export Image (PNG)** does nothing in "Show all" view | Troubleshooting row |
| C8 | Replay: dragging the slider pauses; does it resume from the dragged point? | Marked |
| C9 | Gantt: arrival without departure draws as a thin tick; Gantt/replay button disabled when no events? | Marked |
| C10 | Zones: custom-zone polygon with 3 points may pass the form but fail the 4-point server rule; description (5–150 chars) has no inline message | Described as validation toast |
| C11 | Chat list loads only 20 chats – how to reach older ones? | Marked |
| C12 | "Library" tab in vessel switcher shows max 20 vessels | Marked |
| C13 | Toasts say "bookmarks"; UI says "Library" – and add/remove wording may be inverted | Articles say "Library" |
| C14 | Typos for dev team: "Unkown Berth", "Ecapse to stop editing", "avaialble", "Specialsed Carrier" (internal), "Harbor" (US) vs UK spellings | Not copied into articles |
| C15 | Placeholder text still in the app: "Enter the code sent to your **[2FA_METHOD]**" on reset password and change password | Articles say "email" |
| C16 | "OTP sent" screen appears even when sending the OTP failed | Not documented as a feature |
| C17 | Locked **Auto-Screening** toggle in zone/port notifications shows a lock to everyone without the group (not only entitled) | Documented |

## D. Support / wording (SUP / PM)
| # | Question | Articles |
|---|---|---|
| D1 | Exact text of the **login error** message (comes from the server) and of generic **error pages** ("An error page appears…" appears in vessel, port, zone, fleet articles) | Authentication, Vessels, Ports, Zones, Fleets |
| D2 | MFA code is sent by email only? (screen says "email") Any other channel? | Authentication |
| D3 | What to advise after "Error: …", "No response text" or a blank map in Meridia IQ; recommended action | Meridia IQ |
| D4 | Map not configured / missing map token notice: wording and what customers should do ("contact support" assumed) | Vessels, Ports, Zones, Fleets |
| D5 | Other ways to remove an item from the Library besides the **Added to Library** toggle | Library |
| D6 | What do users without fleet management see on a direct fleet URL? Does the Library list view offer fleet actions? | Fleets |

## E. Verify in a running environment (QA) – will be resolved when screenshots are captured
| # | Item | Articles |
|---|---|---|
| E1 | Where the **Columns** side panel appears on screen (events tables on vessel, port, zone, fleet) and how to reveal hidden columns | Vessels, Ports, Zones, Fleets |
| E2 | Label of the header **refresh** control; apply-button label of the custom date picker | Vessels, Zones |
| E3 | How a vessel/port/zone is found on the Library tabs (search box vs rows) | Vessels, Ports, Zones |
| E4 | Map marker hover/click popups – which fields show per marker | Ports, Zones, Fleets |
| E5 | Whether the company-search window re-opens automatically when a search completes | Company search |
| E6 | Is there a port/zone switcher? (none found in code) | Ports, Zones |
| E7 | Exact label for hidden-by-default columns, and what the Event Type dropdown plural/singular labels look like | Ports, Zones, Vessels |

## Suggested order
1. **PM** – A1–A8 (unblocks policy wording and the held articles).
2. **BE/data** – B1–B15 (create a shared glossary once; many articles reuse it).
3. **FE** – C1–C17 (decide "document as is" vs "fix first" – fixes would change the articles).
4. **SUP** – D1–D6 (copy-edit only).
5. **QA** – E1–E7 (resolved during the screenshot pass).
