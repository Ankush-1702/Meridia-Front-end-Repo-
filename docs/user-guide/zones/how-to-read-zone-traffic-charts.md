# How to read zone traffic charts

Use the Traffic tab to analyse how many vessels enter and exit a zone over a period, and which vessels visit repeatedly.

## Before you begin

- Open the zone page. See "How to open and read a zone page".
- Select the **Traffic** tab.

## Steps

1. Select the **Traffic** tab.
   `[SCREENSHOT 1: Traffic tab with filters and charts]`
2. Choose the time range with the calendar button. It shows **Previous 30 Days** at first. Options: **Previous 7 Days**, **Previous 30 Days**, **Previous 90 Days**, **Previous 12 Months**, **Custom**.
3. For **Custom**, enter a **Start date** and **End date** and apply. **[CONFIRM]** the exact apply button label, which is outside this page's code. The date picker accepts dates within the last two years.
   `[SCREENSHOT 2: Time range options with Custom dates]`
4. Narrow the data with **Vessel Flag**, **Vessel Type** and **Vessel Class**. Each has **Select All**; **Vessel Flag** also has a **Search Flags** box.
5. Note that **Vessel Class** is greyed out until at least one vessel type is selected.
   `[SCREENSHOT 3: Vessel Flag, Vessel Type and Vessel Class filters]`
6. Wait about a second after changing filters; the charts reload automatically.
7. Select **Refresh** to reload all charts and the table.
8. Read **Key Metrics**: **Entries**, **Exits**, **Unique Entries per Day (avg)** and **Unique Entries per Day (max)**.
9. Read the **Entries and Exits** line chart. Its subtitle reads "Totals per Day" (or Week, Month, Quarter).
10. Change **Group By** with the dropdown on the chart (shows **Daily**, **Weekly**, **Monthly** or **Quarterly**). Choose **Day**, **Week**, **Month** or **Quarter**.
   `[SCREENSHOT 4: Group By dropdown]`
11. Read **Entries** - "By Vessel Type, Totals" (donut chart) and **Entries** - "By Vessel Type, Per [Day/Week/Month/Quarter]" (bar chart, with its own **Group By**).
12. Scroll to **Top Visiting Vessels** and read the table (columns below). Select a row to open that vessel's page.
   `[SCREENSHOT 5: Top Visiting Vessels table]`
13. To export, open the three-dot download menu on a chart or table and choose **Export Data (CSV)**, or **Export Image (PNG)** where offered.

## Expected result

The charts and table update to your time range and filters, and exports download with the zone name and dates in the file name.

## Good to know

- **Group By** options depend on the range: up to 7 days allows **Day** only; up to 60 days adds **Week**; up to 90 days adds **Month**; longer ranges add **Quarter**. Unavailable options are greyed out, and the selection moves to an allowed one when the range changes.
- Your filters and **Group By** choices are remembered in your browser.
- Export options: **Key Metrics** and **Top Visiting Vessels** offer **Export Data (CSV)** only; **Entries and Exits** and both **Entries** charts offer **Export Data (CSV)** and **Export Image (PNG)**. A download menu is unavailable while there is no data.
- The **Top Visiting Vessels** information icon says: "Showing repeat visiting vessels only. Single visit vessels are excluded." It shows a count next to the title and loads 20 rows at a time.
- **Top Visiting Vessels** columns:

| Column | Meaning |
|---|---|
| **Vessel** | Vessel name |
| **IMO** | The vessel's IMO number |
| **Flag** | Flag state |
| **Type** | Vessel type |
| **Class** | Vessel class, or "-" if none |
| **Visits** | Number of visits **[CONFIRM]** how a visit is counted |

- **[CONFIRM]** How entries, exits and unique entries per day are calculated, whether the end date is included, and the data cut-off (the presets end yesterday).
- **[CONFIRM]** What the **Vessel Class** values mean for each type.
- An **Export** button exists in the code but is switched off, so only the per-chart menus export.
- Newly created custom zones show a banner about analytics being available after 24 hours.

## Troubleshooting

| Problem | What to do |
|---|---|
| "No data available" in a panel | Widen the time range, reset filters, or select **Refresh**. |
| **Vessel Class** cannot be opened | Select at least one vessel type first. |
| **Group By** option is greyed out | Choose a longer time range. |
| "No recurring vessels found for the selected period" | No vessel visited more than once; widen the range or filters. |
