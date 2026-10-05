# Meridia User Guide – Knowledge Base Drafts (Product Fruits)

Source of truth: `maritime-analytics-frontend-develop.zip` (v1.11.0). Steps are derived from the UI code (labels, validation rules, toasts), so wording matches the screen. Items marked **[CONFIRM]** depend on backend/email behaviour that cannot be verified from front-end code.

## Article format (one article per task)
Title → Before you begin → Numbered steps (one action each, UI labels in **bold**) → Expected result → Troubleshooting → `[SCREENSHOT n]` markers.

## Module map (proposed KB structure)
| # | Module | Route | Articles | Status |
|---|--------|-------|----------|--------|
| 1 | Authentication | `/login`, `/reset-password` | How to log in · How to log in with a verification code (MFA) · How to reset your password · How to log out (see My Profile → Sign out) | **POC done** |
| 2 | My Profile | `/analytics/account` | View profile · Time zone & theme · Notification pop-ups · Change password · Sign out | **Drafted** |
| 3 | Library (home) | `/`, `/analytics/library` | Getting started · Add to Library · Search filters · Search & change view · Fleets (optional) · Custom zones shortcut | **Drafted** |
| 4 | Vessels | `/analytics/vessel/:id` | Open & read a vessel page · Switch vessels · Vessel details & save to Library · Track on the map · Replay movements · Event timeline · View & filter events · Events table columns · MTI score · PurpleTRAC screening | **Drafted (10)** |
| 5 | Ports | `/analytics/port/:id` | Open & read a port page · Live traffic on the map · Congestion & utilisation · Inbound vessels · Port events table · Berths · Berth details & dwell time · Vessel occupancy at a berth. *Port Details/facilities (WPI) drafted in `ports/_unpublished/` – tab is switched off in the app.* | **Drafted (7 live + 1 held)** |
| 6 | Zones / Custom zones | `/analytics/zone/:id`, `/analytics/custom-zones` | Open & read a zone page · Live zone traffic on the map · Zone traffic charts · Zone events table · View & manage custom zones · Create a custom zone · Upload GeoJSON/WKT · Edit a custom zone. *Delete a custom zone held in `zones/_unpublished/` – the Delete action is commented out in the app.* | **Drafted (7 live + 1 held)** |
| 7 | Fleets | `/analytics/fleet/new`, `/:id`, `/:id/edit` | Create a fleet · Edit or delete a fleet · Open & read a fleet page · View your fleet on the map · Read fleet composition · View fleet events. *Filter-based vessel adding held in `fleets/_unpublished/` – it does not exist in the app (filters only narrow the view).* | **Drafted (6 live + 1 held)** |
| 8 | Notifications | `/analytics/notifications` | Open & read your notifications · Filter & manage the Notifications page · Turn notifications on for a port or zone · Download your exports | **Drafted (4)** |
| 9 | Meridia IQ (chat) | `/analytics/chat2` | Start a chat · Read answers, tables & maps · Manage chat history · Ask IQ about a vessel, port or zone. *Only the current version is documented; the older chat version is unreachable.* | **Drafted (4)** |
| 10 | Company search (Beta) | launched from the company icon beside ownership names on a vessel page | Open company search from a vessel page · Read company details (contacts, sources, export). *There is no standalone company search in the app.* | **Drafted (2)** |

## Screenshot priority
1. **P1 (POC):** Login page, Login filled in, MFA code screen, Reset – enter email, Reset – code + new password (incl. requirements tooltip), success toast on Login, landing page after login.
2. **P2:** My Account → Security (Change password, MFA), Logout control.
3. **P3:** Every module's main screen, plus any modal, dropdown, filter panel or export dialog (these are the places users get stuck).

## Notes for customers audience
- No admin-only screens exist in the front end; admin-related content is limited to the read-only **Role** / **Account ID** on My Profile. MFA self-setup is commented out of the UI, so it is intentionally not documented.
- Product Fruits-ready output: `product-fruits/` (HTML articles + tour/checklist definitions).
- Screenshots: pending test-environment URL.

## Front-end issues spotted while drafting Company search
- **No standalone company search, result list, company profile or fleet view exists** – only a Beta "company contact details" lookup launched from the company icon on the five Ownership rows (Operator, Registered owner, Technical manager, Ship manager, Group beneficial owner) of the vessel details panel (Overview tab). The sidebar **Search** has no company tab.
- **No entitlement gate in the front end** – the icon shows for any non-empty ownership name (conflicts with the "entitled accounts only" decision – please confirm).
- The "DOC company" row in Registry has no company icon; the Export menu is hidden for empty results but Refresh is still shown; results are cached in the browser for 24 hours per company name + IMO; the address map silently disappears if geocoding fails; requests time out after about 160 s.

## Front-end issues spotted while drafting Vessels (for the product/dev team)
- PurpleTRAC screening starts automatically each time the section is expanded; there is no Run button, and it times out after 160 s with a generic error.
- Missing Speed/Course/Heading/Draught can display as `0` instead of `-` in the Events table; a missing Detained value shows "No".
- Events tab silently drops an event type if its fetch fails; fixed 500-row limit, no paging; fixed 90-day window (no date picker on the tab).
- Per-event-type column definition files (Port/Zone/STS/AIS gap/Discrepancy/PSC) are unused – the Events tab uses one unified table.
- Product decisions (confirmed): MTI, PurpleTRAC and Ask IQ are visible only to entitled accounts/users; locked boxes are described as leading to Contact us details – note the code actually shows a hover card with a **More about MTI / PurpleTRAC** link (external page), so the Vessels articles say that and carry a [CONFIRM]; users without the Meridia feature see no Meridia content; the Events tab's fixed 90-day window is not ideal but stays as-is for now.
- Toast says "bookmarks" while the UI says "Library".
- MTI gauge never shows the score date although the API returns `updated_at`; "Unlock … / Available on request." upsell boxes also show for users who do have access.
- Tooltip typo "avaialble" in the events panel; "Skip to start" replay button is very faint; several icon buttons lack `aria-label`.
- Draught track option disabled ("Coming soon"); Risk/Transparency sidebar sections commented out; "Set as Homepage" not implemented.
## Front-end issues spotted while drafting Ports
- **Details tab (WPI port facilities) is commented out** – not visible to users; article held in `ports/_unpublished/`.
- Berths tab: **Expand All / Collapse All** are disabled when no filter is active (all filters are on by default); "Unkown Berth" typo; back button from a berth opened via Congestion returns to Congestion, not the Berths list.
- Congestion tab: Export button, "Hourly Averages" and group-by tab are commented out; CSV-only exports; "Specialsed Carrier" typo (internal value); custom start date limited to 2 years back.
- Group By popup says Day/Week/Month/Quarter while the button says Daily/Weekly/Monthly/Quarterly.
- Port Events: Reset-columns button missing; a failed berth/port request is silently dropped; missing Speed/Course/Heading/Draught show `0`; Navigational Status shows a raw numeric code; Event Type labels plural in dropdown, singular in badges.
- Dead code: `inboundVesselsMock.ts` (1970 dates), standalone `InboundVessels` table, `utils/ColDefs.tsx`, `createBerthEventsColDef`, `portsData.ts` (likely).
- Toast says "bookmarks" (UI says "Library"), and its wording may be inverted after add/remove.
- Overview "Performance (Previous 30 days)" excludes today; port page has no port switcher.
## Front-end issues spotted while drafting Notifications
- **No vessel or fleet notification settings** – the settings button is deliberately hidden on Vessel and Fleet pages (ports and zones only).
- No read/unread state, no mark-as-read, no per-row delete, no sorting/search on the Notifications page; only the **All / Ports / Zones** tabs. Dismiss (**x**) only clears the local bell panel / pop-ups.
- Clicking a bell item, a pop-up, **View All** or **Refresh** clears the local list, pop-ups and bell count; **View All** also empties the bell's Downloads list.
- Pressing Enter on a pop-up does not call "dismiss all", unlike a click.
- PurpleTRAC Auto-Screening toggle is locked with "Contact your account manager" for accounts without the `ptrac-vessel-screening` / `auto-screening` group.
- Show Notifications option labels are loaded from the backend (**[CONFIRM]** exact wording).


## Front-end issues spotted while drafting Fleets
- **Only static fleets exist** – dynamic fleets are switched off (type hard-coded `static`); dynamic-only preview strings are unreachable.
- **Rename is not available** from the Library card or fleet page (a rename dialog exists but is not wired); renaming works only via Edit.
- Overview list **Export Data (CSV)** downloads a file named `berths-export.csv` (copy-paste from Berths). Composition **Export Image (PNG)** does nothing in "Show all" view for the Flag / Port of registry / Country of build / Builder charts; the Composition **Export** button is commented out.
- Composition "Based on X of Y vessels" compares against the whole fleet's count, not the filtered count.
- Ask IQ buttons on the fleet page and in the event panel header are commented out; the map legend **Flag** tab is commented out; the notify bell on fleet cards is commented out; no fleet notification settings exist.
- Locked MTI / PurpleTRAC rows show a hover card with an "Unlock" prompt, "Available on request." and a **More about …** link (external page) – there is no "Contact us" box on click in the app code.
- Events: failed fetch silently shows an empty table; Port State Control **Defects** may show blank instead of "-"; **Detained** shows "No" when missing; column named **Location Type** here but **Zone Type** in vessel events; tooltip typo "avaialble".
- Cancel while editing always opens the Discard dialog even with no changes; the Library delete modal's cancel button label is lowercase ("cancel").
- The 1,000-vessel cap per fleet is fixed (confirmed by product); the preview text still says "your N-vessel limit", which could be reworded.

## Front-end issues spotted while drafting Zones / Custom Zones
- **Custom-zone Delete is switched off** (menu item commented out; no delete API call exists) – article held in `zones/_unpublished/`.
- Upload accepts only **GeoJSON / WKT** (`.geojson`, `.json`, `.wkt`, `.txt`) – not shapefile/KML. A circle/point with no radius silently defaults to 1000 m; LineString/MultiPoint are treated as polygons.
- Circle map tooltip typo "Ecapse to stop editing"; form banner says "drag to adjust radius" while the tooltip says "right click to edit circle".
- Banner after saving always says "24 hours", but the code uses 15 minutes when the API URL contains "test".
- Description rule (5–150 characters) has no inline field message; editing a non-custom zone by URL shows a blank form instead of an error.
- Zone page: **Details tab unreachable**; Export button and Arrivals/Departures tab commented out (CSV only); card title changes ("Vessels In Zone" → "In Zone"); map popup has placeholder fallbacks ("VESSEL NAME", "9999999", "Tug", "Panama").
- Zone events: a failed load silently shows an empty table; missing speed/course/heading/draught can show `0`.
- The PurpleTRAC Auto-Screening toggle (zone notifications) shows a lock + "Contact your account manager" tooltip to everyone, not only entitled users.
## Front-end issues spotted while drafting Meridia IQ
- Only the current version (`/analytics/chat2`) is reachable: `/analytics/chats/*` redirects to it, so the older chat UI and its "Switch to Meridia IQ 2.0" toggle are dead code; the V1/V2 switcher component is unused.
- **Ask IQ sends the prompt automatically** (it navigates with the prompt and sends it, no chance to edit first). Ask IQ buttons are commented out in the fleet page and fleet event panel header.
- The six "I can help you with things like…" prompts on the welcome screen are plain text, not clickable. No stop, regenerate, feedback, copy, search, rename or pin exists; the chat-list menu offers only **Delete**.
- Chat list fetch is limited to 20 with no paging (older chats may be unreachable); titles are cut to 19 characters + "…".
- Errors show raw server text ("Error: …"); an empty turn shows "No response text".
- `MARA2_API_URL` falls back to `http://localhost:8000` if the env var is missing; a stale sidebar "New Chat" item pointing to `/analytics/chats` exists (hidden when the sidebar is expanded).
- Access: group `meridia-iq` or `mara`; the article carries **[CONFIRM]** on how access is granted and on what IQ can answer.
