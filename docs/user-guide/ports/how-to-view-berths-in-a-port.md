# How to view berths in a port

Use the **Berths** tab on a port page to see the port's berths grouped by terminal, filter them, and export the list.

## Before you begin
- Open a port page (`/analytics/port/:id`).
- Berth information is part of a premium section. It is visible only to entitled accounts. If you do not see the **Berths** tab, contact your Meridia administrator or use **Contact us**. **[CONFIRM: exact entitlement and what non-entitled users see]**

## Steps
1. Select the **Berths** tab, next to **Congestion and Utilisation** and **Events**.
   `[SCREENSHOT 1: Berths tab selected on a port page]`
2. Wait for the cards and table to load. A loading indicator shows while data is being fetched.
3. Select the date button at the top left (it shows **Previous 7 Days** by default) and choose **Previous 7 Days**, **Previous 30 Days**, **Previous 90 Days**, **Previous 12 Months** or **Custom**.
   `[SCREENSHOT 2: Date range menu with preset options]`
4. For **Custom**, enter a **Start date** and an **End date**, then select **Apply**.
5. Select **Berth Type** and tick or untick the types you want. Use **Select All** to tick or untick everything.
   `[SCREENSHOT 3: Berth Type dropdown]`
6. Select **Terminal Name** and tick or untick the terminals you want.
7. Check the four cards above the table: **Total Berths**, **Min Dwell Time**, **Max Dwell Time** and **Terminal Operators**.
   `[SCREENSHOT 4: KPI cards above the berth table]`
8. In the table, select a terminal row to open it and see its berths. Select **Expand All** to open every terminal, or **Collapse All** to close them.
   `[SCREENSHOT 5: Berth table grouped by terminal]`
9. Select a berth row to open its details (see "How to view berth details and dwell time").
10. To clear your filters, select **Reset Filters**. It is greyed out when no filter is applied. **[CONFIRM: whether Reset Filters restores all options or clears them]**
11. To download the list, select **Export** (see Good to know).

## Expected result
The table lists terminals, and each terminal opens to show its berths. The cards update to match your date range and filters.

## Good to know
- The berth table columns are:

| Column | Meaning |
|---|---|
| **Berth** | Berth name. |
| **Type** | Berth type. |
| **Vessel types** | A coloured bar showing the mix of vessel types. Hover over it to see each type and its percentage. |
| **Handling** | Berth handling facility. |
| **Length** | Berth length. **[CONFIRM: unit, shown as metres in the data]** |
| **Max LOA** | Maximum vessel length overall the berth takes. **[CONFIRM: unit]** |
| **Max DWT** | Maximum deadweight the berth takes. **[CONFIRM: unit]** |
| **Depth (LW)** | Depth at low water. **[CONFIRM: unit]** |
| **Min dwell**, **Avg dwell**, **Median dwell**, **Max dwell** | Minimum, average, median and maximum dwell time for the selected period. **[CONFIRM: unit (hours?) and how dwell time is calculated]** |

- A dash (-) means no value is available.
- A legend above the table names the vessel types present in the current results, with their colours.
- Your date range choice is remembered in your browser and is shared with the berth details page.
- Berth Type and Terminal Name options update each other, so you only see choices that still apply. The table refreshes shortly after you stop changing filters.
- **Export** downloads a file named berths-export.csv for the selected date range and filters. See "How to view vessel occupancy at a berth" for the export steps. **Export** is greyed out when there are no rows or an export is already running.
- There is no map of berths on this tab.

## Troubleshooting
| Problem | What to do |
|---|---|
| The **Berths** tab is missing | The section is premium. Contact your administrator or use **Contact us**. |
| **No data available** appears | Adjust the date range or filters, or refresh the page. |
| The table is empty after filtering | Tick more options in **Berth Type** and **Terminal Name**, or select **Reset Filters**. |
| **Expand All** is greyed out | It is disabled when no filter is applied. **[CONFIRM: this looks like unintended behaviour]** |
