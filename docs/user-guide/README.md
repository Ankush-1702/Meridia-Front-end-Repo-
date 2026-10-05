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
| 4 | Vessels | `/analytics/vessel/:id` | Search/view a vessel | Planned |
| 5 | Ports | `/analytics/port/:id` | Open & read a port page · Live traffic on the map · Congestion & utilisation · Inbound vessels · Port events table · Berths · Berth details & dwell time · Vessel occupancy at a berth. *Port Details/facilities (WPI) drafted in `ports/_unpublished/` – tab is switched off in the app.* | **Drafted (7 live + 1 held)** |
| 6 | Zones / Custom zones | `/analytics/zone/:id`, `/analytics/custom-zones` | Open & read a zone page · Live zone traffic on the map · Zone traffic charts · Zone events table · View & manage custom zones · Create a custom zone · Upload GeoJSON/WKT · Edit a custom zone. *Delete a custom zone held in `zones/_unpublished/` – the Delete action is commented out in the app.* | **Drafted (7 live + 1 held)** |
| 7 | Fleets | `/analytics/fleet/new`, `/:id`, `/:id/edit` | Create/edit a fleet | Planned |
| 8 | Notifications | `/analytics/notifications` | View/manage notifications | Planned |
| 9 | Meridia IQ (chat) | `/analytics/chat2` | Start a chat · Read answers, tables & maps · Manage chat history · Ask IQ about a vessel, port or zone. *Only the current version is documented; the older chat version is unreachable.* | **Drafted (4)** |
| 10 | Company search | – | Search a company | Planned |

## Screenshot priority
1. **P1 (POC):** Login page, Login filled in, MFA code screen, Reset – enter email, Reset – code + new password (incl. requirements tooltip), success toast on Login, landing page after login.
2. **P2:** My Account → Security (Change password, MFA), Logout control.
3. **P3:** Every module's main screen, plus any modal, dropdown, filter panel or export dialog (these are the places users get stuck).

## Notes for customers audience
- No admin-only screens exist in the front end; admin-related content is limited to the read-only **Role** / **Account ID** on My Profile. MFA self-setup is commented out of the UI, so it is intentionally not documented.
- Product Fruits-ready output: `product-fruits/` (HTML articles + tour/checklist definitions).
- Screenshots: pending test-environment URL.

## Front-end issues spotted while drafting Ports
- **Details tab (WPI port facilities) is commented out** – not visible to users; article held in `ports/_unpublished/`.
- Berths tab: **Expand All / Collapse All** are disabled when no filter is active (all filters are on by default); "Unkown Berth" typo; back button from a berth opened via Congestion returns to Congestion, not the Berths list.
- Congestion tab: Export button, "Hourly Averages" and group-by tab are commented out; CSV-only exports; "Specialsed Carrier" typo (internal value); custom start date limited to 2 years back.
- Group By popup says Day/Week/Month/Quarter while the button says Daily/Weekly/Monthly/Quarterly.
- Port Events: Reset-columns button missing; a failed berth/port request is silently dropped; missing Speed/Course/Heading/Draught show `0`; Navigational Status shows a raw numeric code; Event Type labels plural in dropdown, singular in badges.
- Dead code: `inboundVesselsMock.ts` (1970 dates), standalone `InboundVessels` table, `utils/ColDefs.tsx`, `createBerthEventsColDef`, `portsData.ts` (likely).
- Toast says "bookmarks" (UI says "Library"), and its wording may be inverted after add/remove.
- Overview "Performance (Previous 30 days)" excludes today; port page has no port switcher.


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
