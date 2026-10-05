# How to view live port traffic on the map

Use the port Overview to see vessels in port and inbound, a live map, recent performance and the last 24 hours of arrivals and departures.

## Before you begin

- Open a port page and select the **Overview** tab. See "How to open and read a port page".

## Steps

1. Select the **Overview** tab.
2. Note the line "Updated ... ago" with a **Refresh** link at the top right. Select **Refresh** to reload all Overview data. Next to the tabs, the page also says "Auto-updates every 5 minutes".
   `[SCREENSHOT 1: Overview tab with the Updated ago line and Refresh link]`
3. If a progress bar appears reading "Loading ... vessels", wait for it to finish. It shows how many vessels have loaded.
4. In the left column, read the **Vessels In Port** card. The number is the count of vessels currently in port.
5. Select **Vessels In Port** to open the list titled **In Port**. Each row shows the vessel name, type, IMO and **ATA** (a UTC date and time).
   `[SCREENSHOT 2: In Port list expanded]`
6. Select a vessel row to open that vessel's page.
7. Select **View all** to open the **Events** tab on **Historic**, or **Back** to return to the cards.
8. Read the **Vessels Inbound** card. Its title shows the time frame, for example "next 24h", or "All".
9. Select **Vessels Inbound** to open the **Inbound** list. Each row shows name, type, IMO and **ETA**.
10. In the **Inbound** list, under **Within next**, choose **24h**, **7d**, **30d** or **All** to change the time frame.
   `[SCREENSHOT 3: Inbound list with the Within next time frames]`
11. Select **View all Events** to open the **Events** tab on **Inbound Vessels**.
12. Read the **Performance (Previous 30 days)** card: **Unique Arrivals per Day (avg)**, **Unique Arrivals per Day (max)**, **Dwell time at berth (avg)** and **Dwell time at berth (median)** (in hrs).
13. Select **View congestion and utilisation analytics** to open that tab.
14. On the map, check the legend at top left. **In Port** (orange) marks vessels in port and **Inbound** (teal) marks inbound vessels. The port boundary is also drawn.
   `[SCREENSHOT 4: Map with legend, port boundary and vessel markers]`
15. Select the map style button (tooltip **Toggle Map Styles**) at top right. In **Map Style**, choose **Simple**, **Satellite** or **C-MAP**, and switch **Grid / Graticules** on or off.
16. Use the zoom controls at bottom right. The map also shows cursor coordinates.
17. Scroll down to the charts **Arrivals and Departures** (**Last 24 Hours**) and **Arrivals by Vessel Type** (**Last 24 Hours**).
   `[SCREENSHOT 5: Arrivals and Departures charts]`

## Expected result

You see current vessel counts, a map of vessels in and heading to the port, and charts for the last 24 hours.

## Good to know

- The legend only lists a group (**In Port**, **Inbound**) when that group has vessels, and is hidden when there are none.
- "Commercial vessels only" appears beside the charts. Its tooltip says all data uses commercial vessel data only and excludes passenger, fishing and tug vessels.
- Empty states: "No vessels currently in port", "No mappable vessels currently in port" and "No inbound vessels".
- The **Inbound** time frame you pick is remembered on your device.
- **[CONFIRM]** how "in port" and "inbound" are defined, and the data sources and freshness of ATA and ETA.
- **[CONFIRM]** how the Performance figures and the arrival and departure counts are calculated.
- **[CONFIRM]** map marker interactions (hover or click) as they depend on shared map code.

## Troubleshooting

| Problem | What to do |
|---|---|
| Charts or Performance show "No data available" | Select **Refresh**, or reload the page. The message suggests adjusting filters or refreshing. |
| The map is blank or shows a missing-token notice | Contact support. **[CONFIRM]** wording and cause. |
| The vessel count differs from the markers on the map | The "No mappable vessels" message means some vessels have no usable position. **[CONFIRM]** |
| Data looks old | Check the "Updated ... ago" time, then select **Refresh**. |
