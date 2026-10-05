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
| 6 | Zones / Custom zones | `/analytics/zone/:id`, `/analytics/custom-zones` | View zones, create/edit custom zone | Planned |
| 7 | Fleets | `/analytics/fleet/new`, `/:id`, `/:id/edit` | Create a fleet · Edit or delete a fleet · Open & read a fleet page · View your fleet on the map · Read fleet composition · View fleet events. *Filter-based vessel adding held in `fleets/_unpublished/` – it does not exist in the app (filters only narrow the view).* | **Drafted (6 live + 1 held)** |
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

## Front-end issues spotted while drafting Fleets
- **Only static fleets exist** – dynamic fleets are switched off (type hard-coded `static`); dynamic-only preview strings are unreachable.
- **Rename is not available** from the Library card or fleet page (a rename dialog exists but is not wired); renaming works only via Edit.
- Overview list **Export Data (CSV)** downloads a file named `berths-export.csv` (copy-paste from Berths). Composition **Export Image (PNG)** does nothing in "Show all" view for the Flag / Port of registry / Country of build / Builder charts; the Composition **Export** button is commented out.
- Composition "Based on X of Y vessels" compares against the whole fleet's count, not the filtered count.
- Ask IQ buttons on the fleet page and in the event panel header are commented out; the map legend **Flag** tab is commented out; the notify bell on fleet cards is commented out; no fleet notification settings exist.
- Locked MTI / PurpleTRAC rows show a hover card with an "Unlock" prompt, "Available on request." and a **More about …** link (external page) – there is no "Contact us" box on click in the app code.
- Events: failed fetch silently shows an empty table; Port State Control **Defects** may show blank instead of "-"; **Detained** shows "No" when missing; column named **Location Type** here but **Zone Type** in vessel events; tooltip typo "avaialble".
- Cancel while editing always opens the Discard dialog even with no changes; the Library delete modal's cancel button label is lowercase ("cancel").
- The 1,000-vessel cap is hard-coded, while preview text says "your N-vessel limit" **[CONFIRM plan limits]**.
