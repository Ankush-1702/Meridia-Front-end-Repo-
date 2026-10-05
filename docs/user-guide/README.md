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
| 5 | Ports | `/analytics/port/:id` | Port details, congestion | Planned |
| 6 | Zones / Custom zones | `/analytics/zone/:id`, `/analytics/custom-zones` | Open & read a zone page · Live zone traffic on the map · Zone traffic charts · Zone events table · View & manage custom zones · Create a custom zone · Upload GeoJSON/WKT · Edit a custom zone. *Delete a custom zone held in `zones/_unpublished/` – the Delete action is commented out in the app.* | **Drafted (7 live + 1 held)** |
| 7 | Fleets | `/analytics/fleet/new`, `/:id`, `/:id/edit` | Create a fleet · Edit or delete a fleet · Open & read a fleet page · View your fleet on the map · Read fleet composition · View fleet events. *Filter-based vessel adding held in `fleets/_unpublished/` – it does not exist in the app (filters only narrow the view).* | **Drafted (6 live + 1 held)** |
| 8 | Notifications | `/analytics/notifications` | Open & read your notifications · Filter & manage the Notifications page · Turn notifications on for a port or zone · Download your exports | **Drafted (4)** |
| 9 | Meridia IQ (chat) | `/analytics/chat2` | Start a chat, chat history | Planned |

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
