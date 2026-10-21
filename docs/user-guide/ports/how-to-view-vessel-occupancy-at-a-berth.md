# How to view vessel occupancy at a berth

Use the **Vessel occupancy** timeline on a berth's details page to see when vessels were at the berth and when it was free.

## Before you begin
- Open a berth from the **Berths** tab (see "How to view berth details and dwell time").
- This section is available to accounts with the Meridia feature enabled. Your user must be tagged to the relevant feature.
- Whether you see the timeline or the **Top vessels by dwell time** table depends on the date period you choose. For periods of up to 90 days you see the vessel occupancy timeline; for longer periods you see the top visiting vessels.

## Steps
1. On the berth details page, scroll below the **Berth Details** box and the **Dwell time at berth** chart.
2. Find the **Vessel occupancy** heading. The dates beneath it show the period covered.
   `[SCREENSHOT 1: Vessel occupancy header with period and gap totals]`
3. Read **Gap time (total)** and **Gap time (avg)**, both in hours.
4. In the **Occupied** row, each block is a vessel at the berth. Hover over a block to see **Vessel**, **IMO**, **Flag**, **Type**, **From**, **To** and **Duration**.
   `[SCREENSHOT 2: Tooltip over an occupied block]`
5. Select a block to open that vessel's page. The tooltip says "Click for more vessel details".
6. In the **Gap** row, each block is a period with no vessel. Hover over it to see **From**, **To** and **Duration**.
   `[SCREENSHOT 3: Gap row with tooltip]`
7. Select **Next →** to move the window forward and **← Prev** to move it back.
8. To change what is shown, change the date range or **Vessel Flag** at the top of the page.

## Expected result
A timeline shows up to 15 days at a time, with date labels along the top. **Prev** and **Next** move by 7 days. Each button is greyed out at the start or end of the period.

## Good to know
- The timeline shows 15 days at a time. For longer periods, use **Prev** and **Next**.
- Names are shortened on narrow blocks. Hover over a block to see full details.
- Times in tooltips are shown in UTC.
- Gaps are shown in orange and vessels in red-orange. A time slot is shown as a gap when arrival or departure times are not available for it.
- **Duration** in the vessel tooltip is shown as a number of hours.

### Exporting the berth list
1. Open the **Berths** tab and set the date range and filters.
2. Select **Export**. A message says "Exporting CSV...".
3. Wait. The file downloads automatically as berths-export.csv and a message says "CSV Exported!".
   `[SCREENSHOT 4: Export button and success message]`
- While an export runs, **Export** is greyed out. It is also unavailable when the table is empty.
- The file is a CSV with one row per berth. Its columns include **Terminal Name**, **Berth**, **Type**, **Vessel types**, **Handling**, **Length**, **Max LOA**, **Max DWT**, **Depth (LW)**, **Min dwell**, **Avg dwell**, **Median dwell** and **Max dwell**. The exported file may contain different columns from the table.
- To download the dwell-time data for one berth instead, use the chart menu (see "How to view berth details and dwell time").

### Berth events
- Berth arrival and departure events appear in the port's **Events** tab as **Berth Arrivals** and **Berth Departures**. Extra details such as **Call Sign**, **Course**, **MMSI**, **Draught**, **Heading**, **Latitude**, **Longitude**, **Reported Destination**, **Reported ETA** and **Speed** are optional columns you can add.

## Troubleshooting
| Problem | What to do |
|---|---|
| **No data available** in place of the timeline | Adjust the date range or **Vessel Flag**, or refresh the page. |
| I see a table instead of a timeline | The page shows **Top vessels by dwell time** for this berth and period. This happens when the date period is longer than 90 days. |
| **Prev** or **Next** is greyed out | You are at the start or end of the period. |
| **Export** does not start | Wait for any running export to finish, and check the table has rows. |
| The export does not download | Allow downloads in your browser and try again. |
