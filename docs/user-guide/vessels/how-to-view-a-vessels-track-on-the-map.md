# How to view a vessel's track on the map

See where a vessel has been and what happened along the way, for a period you choose.

## Before you begin

- Open the vessel page and stay on the **Overview** tab.

## Steps

1. Look at the map. The vessel's track is drawn as a coloured line and events appear as round markers.
   `[SCREENSHOT 1: Overview map with track and event markers]`
2. Select the date button in the toolbar above the map. It shows **Previous 30 days** by default.
3. Choose **Previous 7 days**, **Previous 14 days**, **Previous 30 days** or **Previous 90 days**.
4. For your own dates, choose **Custom range...** instead.
5. Pick a **Start date** and an **End date**.
6. Select **Apply**.
   `[SCREENSHOT 2: Date menu with Custom range open]`
7. Open the **Legend** box at the top left of the map.
8. Under **Track**, choose **Nav** or **Speed** to change how the line is coloured.
9. Under **Events**, tick or untick event types, or use **Show / Hide All**.
   `[SCREENSHOT 3: Legend open showing Events and Track]`
10. Hover over a marker to see its details. Click it to keep the details open.
11. Select the map style button at the top right (**Toggle Map Styles**) to open **Map Style**.
12. Choose **Simple**, **Satellite** or **C-MAP**, and switch **Grid / Graticules** on or off.
   `[SCREENSHOT 4: Map Style panel]`
13. Use the toolbar's ship icon (**Hide Vessel Details** / **Show Vessel Details**) to hide or show the left panel.
14. Use the list icon (**Show Event Timeline** / **Hide Event Timeline**) to open the event list on the right.

## Expected result

The map shows the track and events for your chosen dates.

## Good to know

- **Nav** colours: **Underway**, **Moored / Anchored**, **Other**. **Speed** colours: **Stopped (< 0.1 kn)**, **Slow (0.1–5 kn)**, **Medium (5–15 kn)**, **Fast (≥ 15 kn)**. A dashed line is **AIS Gap**.
- Event types: **Port Arrival**, **Port Departure**, **Zone Entry**, **Zone Exit**, **AIS Gap**, **STS Pairing**, **Discrepancy**, **PSC**. A type with no events in the period is greyed out ("events not available").
- Custom dates must lie within the last two years and cannot span more than two years. **Apply** stays off until they are valid.
- The toolbar shows the vessel's next port and **ETA** when available. **[CONFIRM]** data source.
- **Enter focus mode** (the expand icon, or Ctrl+/ or Cmd+/) hides panels so the map fills the page.
- The **Event Timeline** panel has a **Search events...** box.
- A **Loading** / **Loaded** note appears near the Legend while data loads. The **Draught** colour option is greyed out ("Coming soon").

## Troubleshooting

| Problem | What to do |
|---|---|
| No track appears | Try a longer period. **[CONFIRM]** how vessels with no positions are shown. |
| The replay bar says "No data available for selected range" | Choose a different date range. |
| Date message "Date range cannot exceed two years from current date." | Pick dates within two years. |
