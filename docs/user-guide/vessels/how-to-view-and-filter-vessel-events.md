# How to view and filter vessel events

Use the **Events** tab on a vessel page to see a table of that vessel's recent port, zone and other events, and to filter, search, sort and export them.

## Before you begin
- Open a vessel page (`/analytics/vessel/:id`).
- The table covers the last 90 days only. It has no date picker. Use **Export** for other periods. **[CONFIRM: that 90 days is the intended fixed window]**

## Steps
1. Select the **Events** tab, next to **Overview**.
   `[SCREENSHOT 1: Events tab selected on a vessel page]`
2. Wait for the table to load. A spinner shows while data is loading.
3. Select **Event Type** above the table to open the list of event types.
   `[SCREENSHOT 2: Event Type dropdown showing grouped options]`
4. Tick or untick the types you want. They are grouped as **Port Events** (**Area Arrival**, **Arrival**, **Departure**, **Area Departure**), **Zone Events** (**Zone Entry**, **Zone Exit**) and **Other Events** (**AIS Gap**, **STS Pairing**, **Positional Discrepancy**, **Port State Control**).
5. To tick or untick everything at once, use the select-all option at the top of the list.
6. Type in **Search...** to narrow the rows. It matches any value in the row, including the dates as you see them.
7. Select a column heading to sort by that column. Select it again to reverse the order.
8. To see more columns, open the **Columns** panel on the side of the table and tick the columns you want. **[CONFIRM: where the Columns tab appears on screen]**
   `[SCREENSHOT 3: Columns panel with optional columns]`
9. To go back to the standard columns, select **Reset columns**. It is greyed out until you change the columns.
10. Select a row to open the related port or zone page, if the row has one.
11. To get the data in a file, select **Export** (see Good to know).
   `[SCREENSHOT 4: Export window]`
12. To reload the data, select **Refresh** at the top right (next to **Updated ... ago**).

## Expected result
The table lists matching events with the newest first. The text beside the search box says, for example, "Showing most recent 120 events".

## Good to know
- The table shows at most the 500 most recent events. For the full dataset, use **Export**. Export times are in UTC.
- Pages of 100 rows are used; you can change the page size at the bottom of the table.
- The standard columns are **TimeStamp**, **Event**, **Location**, **Country**, **UN/LOCODE**, **Zone Type**, **Speed**, **Course** and **Duration (hours)**. The **TimeStamp** header shows **(UTC)** or **(System)**, following your time-zone setting. See "How to read the events tables" for what each column means.
- Not every column applies to every event type. A dash (-) means no value. A tooltip beside the table says the same.
- Hover over a cell to see its full value.
- Clicking a **Zone Entry** or **Zone Exit** row opens that zone's page. Clicking a port event row opens that port's page. Other event types do nothing when clicked. **[CONFIRM: that Area Arrival and Area Departure rows open the port page]**
- The data refreshes by itself every 5 minutes. **Updated ... ago** shows the age of the data.
- In **Export**, you choose **Event type** and **Date range** (**Today**, **Yesterday**, **Last 7 Days**, **Last 30 Days**, **Last 90 Days** or a custom range) and select **Request export**. When the file is ready it appears in Notifications or Downloads. **[CONFIRM: file format and whether the export covers other columns]**
- Berth events appear on the timeline and map but are not in this table's **Event Type** list.

## Troubleshooting
| Problem | What to do |
|---|---|
| The table says **No data available** | Tick more event types, clear **Search...**, or check again later. |
| A type seems missing | Each type is fetched separately. If one request fails, only that type is left out. Select **Refresh**. **[CONFIRM: no error message is shown for a failed type]** |
| I need data older than 90 days | Use **Export** and pick a longer **Date range**. |
| **Refresh** is greyed out | A refresh is already running. |
| Clicking a row does nothing | That event has no linked port or zone page. |
| **Request export** is greyed out | Choose at least one event type and a valid date range. |
