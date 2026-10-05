# How to read the zone events table

Use the Events tab to see when individual vessels entered or left a zone, search them, and export the full history.

## Before you begin

- Open the zone page. See "How to open and read a zone page".

## Steps

1. Select the **Events** tab.
   `[SCREENSHOT 1: Events tab with table]`
2. Open the **Event Type** dropdown. Both options are selected at first: **Entries** and **Exits**.
3. Tick or untick **Entries** or **Exits**, or use the select-all option, to filter the table.
   `[SCREENSHOT 2: Event Type dropdown]`
4. Type in **Search...** to filter the loaded rows. The search checks all fields, including the displayed time.
5. Read the line "Showing most recent ... events". For the full history, use **Export**.
6. Check "Updated ... ago". Select **Refresh** to reload now. The tab also reloads every 5 minutes.
7. Click a column heading to sort by it.
   `[SCREENSHOT 3: Table with sorted column]`
8. Select a row to open the vessel's page.
9. To export, select **Export**. In the window, choose event types, then a date range, and select **Request export**.
   `[SCREENSHOT 4: Export window]`
10. Wait for "Export queued", then select **Done**. **[CONFIRM]** where the finished file is delivered or downloaded.

## Expected result

The table lists the most recent events, newest first, for the event types you chose.

## Good to know

- The table loads the last 90 days only, and shows at most the 500 most recent events.
- Export date presets: **Today**, **Yesterday**, **Last 7 Days**, **Last 30 Days**, **Last 90 Days** and **Custom** (**From** and **To** dates). The default is **Last 30 Days**. Export timestamps are in UTC.
- Event badges read **Entry** and **Exit**.
- The timestamp heading shows **TimeStamp (UTC)** or **TimeStamp (System)** depending on your time zone setting; **Reported ETA** follows the same setting.
- Columns shown by default:

| Column | Meaning |
|---|---|
| **TimeStamp** | When the event happened |
| **Event** | **Entry** or **Exit** |
| **Vessel** | Vessel name with flag |
| **IMO** | IMO number |
| **Type** | Vessel type |
| **Flag** | Flag state |

- Columns hidden by default (shown through the table's column controls; **[CONFIRM]** how to reveal them):

| Column | Meaning |
|---|---|
| **Call Sign**, **MMSI** | Vessel identifiers |
| **Course**, **Heading**, **Speed** | Movement values reported with the event |
| **Draught** | Reported draught |
| **Latitude**, **Longitude** | Position at the event |
| **Navigational Status (status)**, **Navigational Status (code)** | Reported navigational status |
| **Reported Destination**, **Reported ETA** | Voyage details reported by the vessel |

- Empty values show "-". **[CONFIRM]** units for course, heading, speed and draught, and how an event is detected.
- Selecting a row opens the vessel page using its IMO number.

## Troubleshooting

| Problem | What to do |
|---|---|
| "No data available" | Check **Event Type** has a selection, clear **Search...**, then select **Refresh**. |
| The table is empty after an error | Select **Refresh**. **[CONFIRM]** whether an error message is shown. |
| **Request export** is unavailable | Select at least one event type and a valid date range. |
| An older event is missing | The table shows only the latest 500 from 90 days. Use **Export**. |
