# How to view your fleet on the map

Use the **Overview** tab of a fleet page to see where each vessel in the fleet was last reported, and to open a vessel's details.

## Before you begin

- Open a fleet page (see "How to open and read a fleet page").
- The map shows only vessels that have a valid last position. A vessel without one is not drawn but still appears in the list view.

## Steps

1. Select the **Overview** tab. The map is the default view.
   `[SCREENSHOT 1: Fleet Overview map with vessel markers and the Legend]`
2. Look at the markers. Each arrow is one vessel. Its colour shows the vessel type and it points in the vessel's heading or course.
3. Hover over a marker. A card shows **Name**, **IMO**, **Vessel Type**, **Vessel Class**, **Flag**, **Speed**, **Course**, **Destination**, **ETA** and **Last Reported**.
   `[SCREENSHOT 2: Hover card on a vessel marker]`
4. Select **Legend** at the top left to open it. It lists the vessel types in your fleet with their colours.
5. Untick a type in the legend to hide those vessels. Tick it again to show them.
6. Select the map-style button at the top right (tooltip **Toggle Map Styles**) to open **Map Style**.
7. Choose **Simple**, **Satellite** or **C-MAP**. Turn **Grid / Graticules** on or off.
   `[SCREENSHOT 3: Map Style panel]`
8. Use the **Zoom in** and **Zoom out** buttons at the bottom right.
9. Move the pointer over the map to read its position in the box at the bottom left.
10. Select a vessel marker. A side panel opens with the vessel's details.
   `[SCREENSHOT 4: Vessel side panel opened from the map]`
11. Read the rows. See Good to know for what each one means.
12. Select the vessel name at the top of the panel, or **Full Details** at the bottom, to open the full vessel page.
13. Close the panel with the close button, the **Esc** key, or by clicking outside it.
14. To work with a subset of the fleet, use **Vessel Flag**, **Vessel Type**, **Vessel Class** or (if you have it) **MTI Score** above the map. The map updates to match.

## Expected result

The map shows one marker for each filtered vessel with a known position. Selecting a marker opens that vessel's panel.

## Good to know

- Panel rows: **Type**, **Class**, **MMSI**, **Callsign**, **Flag**, **Build year**, **Age**, **DWT**, **Registry status**, **PurpleTRAC screening**, **MTI score**, then **Latest position** (a small map) with **Nav Status**, **Coordinates**, **Speed**, **Course**, **Destination**, **ETA** (UTC), **Last reported** and **Source**. A dash (-) means no value.
- **PurpleTRAC screening** and **MTI score** need the matching access. Without it you see a lock with **Unlock**. Hover to read what it offers. **[CONFIRM]** the "Contact us" step that opens on click: in the code this is an "Available on request." card with a **More about PurpleTRAC** or **More about MTI** link.
- Marker colours come from the vessel type. Types without a set colour use a default. **[CONFIRM]** the full colour list.
- If the Ask IQ feature is enabled for you, an **Ask IQ** button appears in the vessel panel. Users without it see nothing.
- The legend currently offers a **Type** view only. The legend by flag is switched off in the code.
- Event markers do not appear on this map. They appear on the small map inside a fleet event's side panel. See "How to view fleet events".
- Hiding a type in the legend does not change the filters or the vessel count.
- Use **Refresh** to reload positions; data also reloads every 5 minutes.

## Troubleshooting

| Problem | What to do |
|---|---|
| The map is blank or shows a notice about a missing token | The map service is not configured. Contact support. **[CONFIRM]** |
| A vessel is missing from the map | It may have no valid position, or its type is unticked in the **Legend**. Check **List view**. |
| No markers after filtering | Select **Reset Filters**. |
| The panel does not open | Click the marker itself, not the hover card. |
