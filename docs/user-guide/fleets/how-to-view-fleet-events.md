# How to view fleet events

Use the **Events** tab to see recent port, zone and other events for every vessel in a fleet, open the detail of any event, and export a longer history.

## Before you begin

- Open a fleet page and select **Events**.
- The table always covers the last 90 days and has no date picker. Use **Export** for other periods.

## Steps

1. Select the **Events** tab.
   `[SCREENSHOT 1: Fleet Events tab with table]`
2. Wait for the table to load. A spinner shows while data loads.
3. Select **Event Type** to choose what to see.
4. Tick the types you want. They are grouped as **Port Events** (**Area Arrival**, **Arrival**, **Departure**, **Area Departure**), **Zone Events** (**Zone Entry**, **Zone Exit**) and **Other Events** (**AIS Gap**, **STS Pairing**, **Positional Discrepancy**, **Port State Control**). All are ticked at first.
   `[SCREENSHOT 2: Event Type dropdown]`
5. Type in **Search...** to narrow the rows. It matches any value, including the dates as you see them.
6. Select a column heading to sort. Select it again to reverse the order.
7. Open the column panel on the side of the table to add or hide columns. **[CONFIRM]** where it appears on screen.
8. To restore the standard columns, select **Reset columns**.
9. Select a row to open the **Event Details** side panel.
   `[SCREENSHOT 3: Event Details side panel]`
10. In the panel, read **Vessels**, **Location** and **Details**. Select a vessel or location card to see more. Use the back arrow to return.
11. Select **Full Details** inside a vessel or location view to open that vessel, port or zone page.
12. Close the panel with the close button, **Esc**, or by clicking outside it.
13. To reload, select **Refresh** next to "Updated ... ago".
14. To get a file, select **Export**.
15. In **Export**, choose **Event type** and **Date range** (**Today**, **Yesterday**, **Last 7 Days**, **Last 30 Days**, **Last 90 Days** or **Custom** with **From** and **To**).
16. Select **Request export**. When ready it appears in **Notifications** > **Downloads**.
   `[SCREENSHOT 4: Export window]`

## Expected result

The table lists the matching events, and the text beside the search box says, for example, "Showing most recent 120 events".

## Good to know

- Standard columns:

| Column | Meaning |
|---|---|
| TimeStamp (UTC) or (System) | When the event happened, in UTC or your system time zone. |
| Vessel | Vessel name with flag. |
| IMO | The vessel's IMO number. |
| Event | The event type. |
| Location | The port or zone linked to the event. |
| Country | Country of that location. |
| UN/LOCODE | The location's UN/LOCODE, where it has one. |
| Location Type | Kind of location. **[CONFIRM]** values. |
| Speed | Vessel speed in knots. |
| Course | Vessel course in degrees. |
| Duration (hours) | How long the event lasted, where that applies. |

- Optional columns come in groups: **Vessel identity** (**MMSI**, **Call Sign**, **Flag**, **Type**), **Position & movement** (**Heading**, **Draught**, **Navigational Status**, **Reported Destination**, **Reported ETA**), **Port State Control** (**Authority**, **Inspection Type**, **Inspection Date**, **Detained**, **Days Detained**, **No. Defects**, **Release Date**), **STS pairing** (**STS Type**, **Paired Vessel**, **Paired IMO**, **STS Ended**), **AIS gap** (**Gap Stopped**, **Gap Resumed**, **Draught Change**) and **Positional discrepancy** (**Has Ended**, **Started Latitude**, **Started Longitude**, **Stopped Timestamp**, **Stopped Latitude**, **Stopped Longitude**).
- **[CONFIRM]** the exact definitions of AIS Gap, STS Pairing, Positional Discrepancy and Area Arrival/Departure events.
- A dash (-) means no value. A tooltip beside the table says not every column applies to every event type.
- The table shows at most the 500 most recent events, 100 per page. Export timestamps are in UTC.
- In the panel, **Vessels** appears only for vessels found in the fleet. STS pairings show **Primary vessel** and **Paired vessel**. The **Location** section has a small map. Port State Control events have no map.
- On that map, STS pairings show a pairing marker. AIS gaps show a start and end marker joined by a dashed red line. Positional discrepancies show start and end markers joined by a dashed yellow line. Port and zone events show the vessel at the event position, the location pin and, for zones, the boundary.
- Location view shows **Last 24 hours**: **Arrivals**/**Entries**, **In port**/**In zone**, **Departures**/**Exits**.
- Data reloads every 5 minutes.
- There are no notification settings on the fleet page. **[CONFIRM]** whether fleet alerts exist elsewhere.

## Troubleshooting

| Problem | What to do |
|---|---|
| **No data available** | Tick more event types, clear **Search...**, or check later. |
| **Refresh** is greyed out | A refresh is already running. |
| I need data older than 90 days | Use **Export** with a longer **Date range**. |
| **Request export** is greyed out | Pick at least one event type and a valid date range. |
| A vessel card is missing in the panel | The vessel is not in the fleet's loaded list. Reload. |
