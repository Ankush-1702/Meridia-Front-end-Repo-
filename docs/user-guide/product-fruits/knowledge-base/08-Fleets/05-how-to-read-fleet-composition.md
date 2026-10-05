# How to read fleet composition

Use the **Composition** tab to see how your fleet breaks down by vessel type, flag, build, size and more.

## Before you begin

- Open a fleet page and select **Composition**.
- Charts rebuild when you change filters, after a short delay of about one second.

## Steps

1. Select the **Composition** tab.
   `[SCREENSHOT 1: Composition tab with summary cards and charts]`
2. Read the four cards at the top: **Vessels**, **Average age**, **Total DWT** and **Flag states**.
3. Read **Vessels** as "X of Y". X is the vessels matching your filters. Y is the fleet total.
4. Narrow the data with **Vessel Flag**, **Vessel Type** and **Vessel Class**. Use the search box inside **Vessel Type** and **Vessel Class**.
   `[SCREENSHOT 2: Composition filter row]`
5. To clear your choices, select **Reset Filters**.
6. Scroll through the chart groups: **Type and class**, **Registration and flag**, **Build and origin**, **Size and dimensions**.
7. In **Type and class**, read **Vessel type** (a ring chart, "Share of fleet") and **Class** (bars, "Size band, coloured by vessel type").
8. In **Registration and flag**, read **Flag** and **Port of registry**. They show the "Top 5 by vessel count".
9. To see every value, select **Show all (N)**. Select **Show top 5** to go back.
   `[SCREENSHOT 3: Flag chart switched to Show all]`
10. In **Build and origin**, read **Country of build**, **Builder** and **Age profile**.
11. In **Size and dimensions**, read **Size** and **Dimensions**.
12. Switch **Size** between **DWT** and **GT** (it opens on **GT**). Switch **Dimensions** between **LOA**, **Beam** and **Draught** (it opens on **Draught**).
13. Hover over a bar or ring segment. The tooltip shows the label, **Vessels** and **Share** (for example "12% of 40").
   `[SCREENSHOT 4: Chart tooltip]`
14. To save a chart, open its menu at the top right of the card and choose **Export Data (CSV)** or **Export Image (PNG)**.
15. To see which vessels are behind the numbers, select **View vessels (N)** or the **Vessels** card.
16. In the **Vessels (X of Y)** panel, type in **Search name, IMO, type, class…** and use **Sort** (**Name** or **IMO**).
17. Select a vessel to see its details. Use the back arrow to return, or **Full Details** to open its vessel page.
   `[SCREENSHOT 5: Vessels side panel]`

## Expected result

The cards and charts describe the vessels that match your filters, and every chart can be exported.

## Good to know

- Bar labels show the number of vessels. The tooltip adds the share of the filtered total.
- Grey bars are labelled "unknown", or values outside your current flag or class selection. **[CONFIRM]** exactly when grey is used.
- **Total DWT** and the **Size** (DWT) and **Dimensions** charts may show "Based on X of Y vessels". The info icon explains that only some vessels have adequate data. If none do, you see "No DWT data available" (or the matching measure).
- **[CONFIRM]** how **Average age**, **Total DWT**, the size bands in **Class** and **Age profile**, and the **Share** percentages are calculated, and which units **Dimensions** uses.
- The CSV has three columns: the chart name, **Vessels** and **Percentage**. The file is named after the fleet and chart.
- There is no **MTI Score** filter on this tab.
- If you untick every value in a filter, the page shows no data. A planned **Export** button for the whole tab is switched off in the code.

## Troubleshooting

| Problem | What to do |
|---|---|
| A chart shows **No data available** | Select **Reset Filters** or refresh the page. |
| **View vessels** is greyed out | No vessels match the filters. Reset them. |
| **Show all** is greyed out | The chart has five or fewer values. |
| **Export Image (PNG)** does nothing in **Show all** view | Switch back to **Show top 5** and export again. **[CONFIRM]** |
| Numbers do not match **Overview** | Each tab has its own filters. Check both. |
