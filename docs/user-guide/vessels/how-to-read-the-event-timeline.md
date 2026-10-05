# How to read the event timeline and Gantt chart

Use the **Events Timeline** list and the detailed Gantt chart on a vessel's **Overview** tab to see what a vessel did, and when, across the date range you choose.

## Before you begin
- Open a vessel page (`/analytics/vessel/:id`) and stay on the **Overview** tab. Both views sit beside and below the map.
- Both views show the same events and use the same date range. Events come from port calls, zone events, AIS gaps, STS pairings, positional discrepancies and Port State Control inspections. **[CONFIRM: exact event sources and how often they refresh]**
- Times in both views are shown in UTC.

## Steps
1. In the toolbar above the map, open the date-range button (it reads, for example, **Previous 30 days**, or **Custom range**) and choose **Previous 7 days**, **Previous 14 days**, **Previous 30 days**, **Previous 90 days** or **Custom range...**.
   `[SCREENSHOT 1: Date range menu open in the vessel toolbar]`
2. For a custom range, pick a **Start date** and an **End date**, then select **Apply**.
3. To show or hide the event list, select the list icon at the right of the toolbar (tooltip **Show Event Timeline** or **Hide Event Timeline**).
   `[SCREENSHOT 2: Events Timeline panel beside the map]`
4. In the **Events Timeline** panel, events are grouped under a date heading with a count. Select a date heading to collapse or expand that day.
5. To collapse every day at once, select the double-arrow button beside the search box (tooltip **Collapse** or **Expand**).
6. To change the order, select the arrow button at the top of the panel (tooltip **Oldest first** or **Newest first**).
7. To find an event, type in **Search events...**. It matches the event name and its type.
8. Select an event in the list to highlight it. Select it again to clear the highlight.
   `[SCREENSHOT 3: A highlighted event in the list]`
9. To open the Gantt chart, select the chart icon at the right end of the bar below the map (tooltip **Show detailed timeline**). Select it again (**Hide detailed timeline**) to close it.
   `[SCREENSHOT 4: Gantt chart open below the map]`
10. In the left-hand column, choose **Group by** **Type** or **Location** to change how the rows are organised.
11. Select a group heading (for example **PORT** or **ZONE EVENTS**) to collapse its rows. A collapsed heading shows the number of rows inside it.
12. Hover over a bar to see a pop-up with the event category, name, **Started**, **Ended** and **Duration**.
   `[SCREENSHOT 5: Hover pop-up on a Gantt bar]`
13. Select a bar to highlight it. The same event is highlighted in the **Events Timeline** list, and the reverse. Select it again to clear.
14. To make the chart taller or shorter, drag the thin bar above the replay controls (labelled **Resize Gantt panel**). With the keyboard, use the Up and Down arrow keys.

## Expected result
- The list shows one entry per event: a coloured round icon, the event type, the place or label, and the UTC time. Between entries, a grey strip shows the time gap when it is longer than one minute.
- The Gantt chart draws one row per place or event type, with time running left to right along the top.

## Good to know
- Colours (same in both views and the map **Legend**): Port Arrival and Port Departure are teal, Zone Entry and Zone Exit are dark blue, STS Pairing is purple, Discrepancy is yellow, PSC is pink and AIS Gap is red.
- A long bar is a period of time. A thin vertical mark is a single moment, or an event shorter than one minute. Wide bars show their duration (for example 6.5h or 2.0d) and, if wide enough, the place name.
- Arrival and departure events at the same place are joined into one bar, and so are zone entry and exit. An arrival with no matching departure appears as a thin mark. **[CONFIRM: how an arrival still in progress is intended to look]**
- With **Group by Type**, rows are organised as PORT AREA, PORT and BERTH, then ZONE EVENTS, AIS GAP, STS PAIRING, DISCREPANCY and PSC. With **Group by Location**, each place gets its own heading with Port Area, Port, Berth or Zone rows underneath.
- Which events appear is controlled by the checkboxes in the map **Legend** (**Events**, with **Show / Hide All**). Hidden types disappear from the list and the chart. An event type with no events in the range is greyed out.
- A dashed amber line labelled **ETA** shows the vessel's reported arrival time and destination, when it falls inside the visible range.
- When you play a replay, an orange line marks the replay position. Events that have not happened yet are faded, and the list shows **Replay active. Events will appear here as they occur.** until the first one occurs.
- There are no zoom buttons. The chart spaces days automatically for the range you choose (a short range is stretched out, a long range is compressed). Scroll sideways and up or down to move around. **[CONFIRM: whether zoom controls are planned]**
- Long place names are shortened in the left-hand column. Hover over the name to see it in full.

## Troubleshooting
| Problem | What to do |
|---|---|
| The Gantt chart area says **No events to display** | Widen the date range or turn event types back on in the **Legend**. |
| The list says **No events in selected range** | Choose a longer period, for example **Previous 90 days**. |
| The list says **No matching events** | Clear the **Search events...** box. |
| I cannot select a **Custom range** | The range cannot start more than two years ago or end in the future, and the end must not be before the start. The menu shows **Date range cannot exceed two years from current date.** |
| The **Apply** button is greyed out | Both a start and an end date are needed and must be valid. |
| An event type is greyed out in the **Legend** | There are no events of that type in the selected range. |
| The Gantt chart button is greyed or does nothing | The replay bar is disabled when the vessel has no events in the range. **[CONFIRM]** |
