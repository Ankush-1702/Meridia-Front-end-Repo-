# How to view live zone traffic on the map

Use the zone Overview tab to see which vessels are in the zone right now, where they are, and how traffic looked over the last 24 hours.

## Before you begin

- Open the zone page and stay on the **Overview** tab. See "How to open and read a zone page".

## Steps

1. Open the zone and select **Overview**.
2. Look at the top right of the page. It shows "Updated ... ago" with a **Refresh** link. The page also notes **Auto-updates every 5 minutes**.
   `[SCREENSHOT 1: Overview with the Updated ago line and Refresh link]`
3. Select **Refresh** to reload the vessels and charts at once. The link is unavailable while a refresh is running.
4. Read the **Vessels In Zone** card on the left. The number is the count of vessels in the zone.
5. Select the card to open the list. It is titled **In Zone**; each row shows the vessel name, type, IMO, an **ATA** time in UTC and the flag.
   `[SCREENSHOT 2: Expanded In Zone list]`
6. Select a vessel in the list to open its vessel page.
7. Select **Back** to return, or **View all** to go to the **Events** tab.
8. Below the card, read **Traffic (Previous 30 days)**: **Unique Entries per Day (avg)**, **Unique Entries per Day (max)**, **Total Entries** and **Total Exits**.
9. Select **View Traffic Analytics** to open the **Traffic** tab.
10. On the map, find the zone boundary and the vessels. The legend at top left shows **In Zone**.
   `[SCREENSHOT 3: Map with zone boundary, vessel markers and legend]`
11. Select a vessel marker to see a popup with name, IMO, vessel type, flag, reported destination and ETA, timestamp and speed/course. The popup says "Click vessel for more details". **[CONFIRM]** which fields appear for each marker.
12. Select the map style button (**Toggle Map Styles**) at top right. In **Map Style**, choose **Simple**, **Satellite** or **C-MAP**, and switch **Grid / Graticules** on or off.
   `[SCREENSHOT 4: Map Style panel]`
13. Scroll down to the charts: **Entries and Exits** (**Last 24 Hours**) and **Entries by Vessel Type** (**Last 24 Hours**).
   `[SCREENSHOT 5: Entries and Exits and Entries by Vessel Type charts]`

## Expected result

You see the current vessels in the zone on the map and in the list, the last 30 days summary, and the last 24 hours of entries and exits.

## Good to know

- While vessels are still loading, a progress bar shows "Loading ... of ..." vessels.
- Vessel positions are shown on the map; the count in the card may be higher than the number of markers. If vessels exist but none can be mapped, the list says "No mappable vessels currently in zone".
- If there are none, the list says "No vessels currently in zone".
- The **Vessels In Zone** card shows only the count until you select it; the list appears when it is expanded.
- The map shows custom zones from their saved shape, and other zones from the zone boundary. **[CONFIRM]** how boundaries are sourced.
- **[CONFIRM]** What counts as "in the zone" and how often positions update, since this depends on backend data.
- A custom-zone banner may appear at the top of the tab for newly created zones.

## Troubleshooting

| Problem | What to do |
|---|---|
| "Error loading vessel data" appears | Select **Refresh**. If it persists, reload the page. |
| The charts show "No data available" | Select **Refresh**; the message suggests adjusting the date range or filters or refreshing. |
| The map is blank | **[CONFIRM]** A message appears if the map service is not configured; contact your account manager. |
