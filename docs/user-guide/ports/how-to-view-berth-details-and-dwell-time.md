# How to view berth details and dwell time

Open a single berth from the **Berths** tab to see its key facts, a dwell-time chart, and what vessels used it.

## Before you begin
- Open a port page and select the **Berths** tab.
- This section is premium and visible only to entitled accounts. **[CONFIRM: entitlement behaviour]**

## Steps
1. In the **Berths** tab, open a terminal and select a berth row.
   `[SCREENSHOT 1: Berth row being selected]`
2. Wait while the page loads. The berth name shows at the top, next to **Back**.
   `[SCREENSHOT 2: Berth details page header with Back, date range and Vessel Flag]`
3. Read the **Berth Details** box on the left. It lists **Operator**, **Type**, **Handling**, **Length**, **Max LOA**, **Max DWT**, **Depth (LW)**, **Dwell time at berth (avg)** and **Dwell time at berth (median)**.
   `[SCREENSHOT 3: Berth Details box]`
4. Read the **Dwell time at berth** chart on the right. Its subtitle says, for example, "Daily avg and median dwell time". **[CONFIRM: Daily or Weekly is chosen by the system, not by you]**
   `[SCREENSHOT 4: Dwell time at berth line chart with legend]`
5. Hover over the lines to see the date for each point.
6. To change the period, select the date button (it shows **Previous 7 Days** by default) and choose a preset or **Custom**, then select **Apply**.
7. To narrow by flag, select **Vessel Flag** and tick or untick flags. Use **Select All** to tick or untick all.
8. To save the chart, select the menu icon at the top right of the chart, then **Export Data (CSV)** or **Export Image (PNG)**.
   `[SCREENSHOT 5: Chart menu with export options]`
9. Select **Back** to return to the berth list.

## Expected result
The page shows the berth facts, a line chart with two lines (average and median), and below it either the vessel occupancy timeline or a **Top vessels by dwell time** table.

## Good to know
- The chart has two lines: **Dwell time at berth (avg)** (solid) and **Dwell time at berth (median)** (dashed). The vertical axis is in hours ("hrs").
- If there is only one data point, it is shown as a dot.
- **Vessel Flag** is greyed out when no flags are available for the berth and period.
- The date range is shared with the **Berths** tab list.
- The CSV has the columns **Berth Name**, **Terminal type**, **Terminal Operator**, **Date**, **Dwell Time at berth (avg)** and **Dwell Time at berth (median)**. The file name uses the berth name and the dates. Image export is PNG.
- The **Top vessels by dwell time** table has the columns **Vessel**, **Type**, **Visits**, **Total Dwell** and **Avg Dwell**, with the note "ranked by total time at berth". Select a row to open that vessel's page. **[CONFIRM: when this table appears instead of the occupancy timeline; the choice comes from the data, not from a control]**
- How dwell time is calculated and its unit in the box and table are **[CONFIRM]**.

## Troubleshooting
| Problem | What to do |
|---|---|
| **No data available** in the box or chart | Adjust the date range or flags, or refresh the page. |
| The berth name reads "Unkown Berth" | The name could not be loaded. Go **Back** and reopen the berth. **[CONFIRM: spelling in the product is "Unkown"]** |
| The chart menu is greyed out | There is no chart data for the period. |
| **Vessel Flag** is greyed out | No flags are available for this berth and period. |
