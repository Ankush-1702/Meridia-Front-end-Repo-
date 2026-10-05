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
| 5 | Ports | `/analytics/port/:id` | Port details, congestion | Planned |
| 6 | Zones / Custom zones | `/analytics/zone/:id`, `/analytics/custom-zones` | View zones, create/edit custom zone | Planned |
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

## Front-end issues spotted while drafting Meridia IQ
- Only the current version (`/analytics/chat2`) is reachable: `/analytics/chats/*` redirects to it, so the older chat UI and its "Switch to Meridia IQ 2.0" toggle are dead code; the V1/V2 switcher component is unused.
- **Ask IQ sends the prompt automatically** (it navigates with the prompt and sends it, no chance to edit first). Ask IQ buttons are commented out in the fleet page and fleet event panel header.
- The six "I can help you with things like…" prompts on the welcome screen are plain text, not clickable. No stop, regenerate, feedback, copy, search, rename or pin exists; the chat-list menu offers only **Delete**.
- Chat list fetch is limited to 20 with no paging (older chats may be unreachable); titles are cut to 19 characters + "…".
- Errors show raw server text ("Error: …"); an empty turn shows "No response text".
- `MARA2_API_URL` falls back to `http://localhost:8000` if the env var is missing; a stale sidebar "New Chat" item pointing to `/analytics/chats` exists (hidden when the sidebar is expanded).
- Access: group `meridia-iq` or `mara`; the article carries **[CONFIRM]** on how access is granted and on what IQ can answer.
