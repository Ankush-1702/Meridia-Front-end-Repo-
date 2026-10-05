# How to read the port events table

Use the **Events** tab on a port page to see recent arrivals, departures and berth events at that port, and to filter, search and export them.

## Before you begin
- Open a port page (`/analytics/port/:id`).
- The **Historic** view covers the last 90 days. There is no date picker. Use **Export** for other periods.

## Steps
1. Select the **Events** tab.
   `[SCREENSHOT 1: Events tab on a port page with Historic selected]`
2. Make sure **Historic** is selected (the other choice is **Inbound Vessels**).
3. Wait for the spinner to finish.
4. Select **Event Type** to open the list of types.
5. Tick or untick **Area Arrivals**, **Arrivals**, **Berth Arrivals**, **Berth Departures**, **Departures** and **Area Departures**. Use **Select All** to tick all at once.
   `[SCREENSHOT 2: Event Type dropdown]`
6. Type in **Search...** to narrow the rows. It matches any value in the row, including dates as shown.
7. Select a column heading to sort. Select it again to reverse the order.
8. To show more columns, use the side panel of the table and tick the columns you want. **[CONFIRM: side panel label]**
   `[SCREENSHOT 3: Optional columns]`
9. Select a row to open that vessel's page.
10. Select **Export** to request a file (see Good to know).
   `[SCREENSHOT 4: Export panel]`
11. Select **Refresh** at the top right to reload.

## Expected result
The table lists events, newest first. Text beside the search box says, for example, "Showing most recent 120 events".

## Good to know
- Default columns:


| Column | Meaning |
|---|---|
| **TimeStamp (UTC)** or **TimeStamp (System)** | When the event happened. Follows your time-zone setting. |
| **Event** | The event type, shown as a coloured badge. |
| **Vessel** | Vessel name with flag icon. |
| **IMO** | Vessel IMO number. |
| **Type** | Vessel type. |
| **Flag** | Flag country. |

- Optional columns: **Berth**, **Call Sign**, **Course**, **MMSI**, **Draught**, **Heading**, **Latitude**, **Longitude**, **Navigational Status (status)**, **Navigational Status (code)**, **Reported Destination**, **Reported ETA (UTC)** or **Reported ETA (System)**, and **Speed**. A dash (-) means no value. **Berth** is filled only for berth events.
- Event types: **Area Arrival** and **Area Departure** relate to the port area, **Arrival** and **Departure** to the port, and **Berth Arrival** and **Berth Departure** to a berth. **[CONFIRM: exact definitions and how area differs from port]**
- The table shows at most 500 recent events. Use **Export** for the full dataset. Export timestamps are in UTC.
- In **Export** you choose **Event type** and **Date range** (**Today**, **Yesterday**, **Last 7 Days**, **Last 30 Days**, **Last 90 Days** or **Custom**), then select **Request export**. When ready it appears under **Notifications** then **Downloads**. A note says berth events are not included, so export those separately. **[CONFIRM: berth export route and file format]**
- The page reloads every 5 minutes. **Updated ... ago** shows the age of the data.
- Hover over a cell to see its full value. All times use your time-zone setting.
- The **Inbound Vessels** view has its own filters. See "How to view inbound vessels".

## Troubleshooting
| Problem | What to do |
|---|---|
| **No data available** | Tick more event types and clear **Search...**. |
| Some events are missing | Berth and port events load separately. Select **Refresh** if one set is missing. **[CONFIRM: no error message is shown]** |
| I need data older than 90 days | Use **Export** with a longer **Date range**. |
| **Refresh** is greyed out | A refresh is already running. |
| **Request export** is greyed out | Choose at least one event type and a valid date range. |
