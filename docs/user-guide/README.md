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
| 7 | Fleets | `/analytics/fleet/new`, `/:id`, `/:id/edit` | Create/edit a fleet | Planned |
| 8 | Notifications | `/analytics/notifications` | View/manage notifications | Planned |
| 9 | Meridia IQ (chat) | `/analytics/chat2` | Start a chat, chat history | Planned |
| 10 | Company search | – | Search a company | Planned |

## Screenshot priority
1. **P1 (POC):** Login page, Login filled in, MFA code screen, Reset – enter email, Reset – code + new password (incl. requirements tooltip), success toast on Login, landing page after login.
2. **P2:** My Account → Security (Change password, MFA), Logout control.
3. **P3:** Every module's main screen, plus any modal, dropdown, filter panel or export dialog (these are the places users get stuck).

## Notes for customers audience
- No admin-only screens exist in the front end; admin-related content is limited to the read-only **Role** / **Account ID** on My Profile. MFA self-setup is commented out of the UI, so it is intentionally not documented.
- Product Fruits-ready output: `product-fruits/` (HTML articles + tour/checklist definitions).
- Screenshots: pending test-environment URL.

## Front-end issues spotted while drafting Zones / Custom Zones
- **Custom-zone Delete is switched off** (menu item commented out; no delete API call exists) – article held in `zones/_unpublished/`.
- Upload accepts only **GeoJSON / WKT** (`.geojson`, `.json`, `.wkt`, `.txt`) – not shapefile/KML. A circle/point with no radius silently defaults to 1000 m; LineString/MultiPoint are treated as polygons.
- Circle map tooltip typo "Ecapse to stop editing"; form banner says "drag to adjust radius" while the tooltip says "right click to edit circle".
- Banner after saving always says "24 hours", but the code uses 15 minutes when the API URL contains "test".
- Description rule (5–150 characters) has no inline field message; editing a non-custom zone by URL shows a blank form instead of an error.
- Zone page: **Details tab unreachable**; Export button and Arrivals/Departures tab commented out (CSV only); card title changes ("Vessels In Zone" → "In Zone"); map popup has placeholder fallbacks ("VESSEL NAME", "9999999", "Tug", "Panama").
- Zone events: a failed load silently shows an empty table; missing speed/course/heading/draught can show `0`.
- The PurpleTRAC Auto-Screening toggle (zone notifications) shows a lock + "Contact your account manager" tooltip to everyone, not only entitled users.
