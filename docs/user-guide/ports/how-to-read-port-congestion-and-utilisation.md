# How to read port congestion and utilisation

Use the **Congestion and Utilisation** tab on a port page to see how many vessels arrive and depart, how long they stay at berth, and which vessels visit most often.

## Before you begin
- Open a port page (`/analytics/port/:id`).
- Everything on this tab uses commercial vessel data only. A note at the top right says **Commercial vessels only**; hover over the info icon beside it to read that passenger, fishing and tug vessels are excluded.
- The tab is only shown to accounts that have the Meridia feature. Locked sections lead to **Contact us** details. **[CONFIRM: exact entitlement behaviour for this tab]**

## Steps
1. Open a port and select the **Congestion and Utilisation** tab.
   `[SCREENSHOT 1: Congestion and Utilisation tab with filters and Key Metrics]`
2. Select the date button at the top left (it shows, for example, **Previous 30 Days**) to change the period.
3. Choose **Previous 7 Days**, **Previous 30 Days**, **Previous 90 Days** or **Previous 12 Months**.
   `[SCREENSHOT 2: Date range menu with presets and Custom]`
4. For your own dates, choose **Custom**, pick a **Start date** and an **End date**, then select **Apply**.
5. Use **Vessel Flag** to choose which flags to include. Search with **Search Flags**, or use **Select All**.
6. Use **Vessel Type** to choose vessel types (for example **Bulk Carrier**, **Container (FC)**, **Oil Tanker**).
7. Use **Vessel Class** to narrow within the chosen types, for example by size band. Each class shows its gross tonnage range.
   `[SCREENSHOT 3: Vessel Class menu grouped by vessel type]`
8. Read **Key Metrics**: **Arrivals**, **Departures**, **Unique Arrivals per Day (avg)**, **Unique Arrivals per Day (max)**, **Dwell time at berth (avg)** and **Dwell time at berth (median)**. Dwell times are shown in hours.
9. Read **Arrivals and Departures** (totals per day, week, month or quarter). The legend shows **Arrivals** and **Departures**.
10. To change the grouping on **Arrivals and Departures**, the per-period **Arrivals** chart or **Dwell time at berth**, select the grouping button (for example **Daily**), then choose **Day**, **Week**, **Month** or **Quarter** under **Group By**.
   `[SCREENSHOT 4: Group By menu with some options greyed out]`
11. Read the **Arrivals** donut (**By Vessel Type, Totals**). Hover over a segment to see the vessel type, count and percentage. Use the legend at the bottom to identify types.
12. Read the second **Arrivals** chart (**By Vessel Type, Per** day, week, month or quarter), a stacked bar chart with one colour per vessel type.
13. Read **Dwell time at berth**. A solid line shows the average and a dashed line shows the median. Use **Berth Type** to filter berths.
14. Scroll to **Top Visiting Vessels** and **Berth Summary** for tables (see Good to know).
15. To download a chart, select the menu icon on the chart, then **Export Data (CSV)** or **Export Image (PNG)**.
   `[SCREENSHOT 5: Chart download menu]`
16. To reload everything, select **Refresh** at the top right.

## Expected result
All charts and tables update to the chosen period and filters. Charts with no matching data show **No data available**.

## Good to know
- **Group By** options depend on the period: up to 7 days allows **Day** only; 8 to 60 days adds **Week**; 61 to 90 days adds **Month**; longer periods add **Quarter**. Unavailable options are greyed out. If you shorten the period, the grouping resets to a valid choice.
- Custom ranges cannot start before two years ago or end after today. If the range is longer than two years, the message **Date range cannot exceed two years from current date.** appears and **Apply** stays disabled.
- Preset periods end yesterday (UTC). **[CONFIRM: the time basis of the charts]**
- **Vessel Class** is greyed out until at least one **Vessel Type** is selected, and only lists classes for the selected types. A number badge on a filter shows how many items are selected.
- **Top Visiting Vessels** lists vessels with these columns: **Vessel**, **IMO**, **Flag**, **Type**, **Class** and **Visits**. The info icon says: "Showing repeat visiting vessels only. Single visit vessels are excluded." Select a row to open that vessel's page. The title shows the number of vessels.
- **Berth Summary** ("All berths — click any row for full detail") has the columns **Berth**, **Operator**, **Type**, **Avg Dwell** and **Median Dwell**. Select a row to open that berth's details on the **Berths** tab.
- **Key Metrics** and **Top Visiting Vessels** offer **Export Data (CSV)** only. The other charts offer CSV and PNG. The download menu is disabled when a chart has no data.
- Your date range, flags, vessel types, classes and grouping choices are remembered in your browser.
- How arrivals, unique arrivals, dwell time and congestion are calculated is not described in the app. **[CONFIRM: definitions of Arrivals, Unique Arrivals per Day and Dwell time at berth]**
- The same four figures (without **Arrivals**/**Departures**) appear on the port **Overview** tab under **Performance (Previous 30 days)**.

## Troubleshooting
| Problem | What to do |
|---|---|
| A chart says **No data available** | Widen the date range or loosen the flag, type or class filters, or select **Refresh**. |
| **Vessel Class** is greyed out | Select at least one **Vessel Type** first. |
| **Week**, **Month** or **Quarter** is greyed out | Choose a longer date range. |
| **Berth Type** is greyed out | No berth types are available for this port and period. |
| **Apply** is disabled for a custom range | Check both dates are set, the end is not before the start, and the range is under two years. |
| **Top Visiting Vessels** says **No recurring vessels found for the selected period** | Only vessels with repeat visits are shown. Try a longer period. |
