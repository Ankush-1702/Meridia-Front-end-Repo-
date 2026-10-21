# How to view inbound vessels

See which vessels are heading to a port, with their reported arrival time, using the port **Overview** and **Events** tabs.

## Before you begin
- Open a port page (`/analytics/port/:id`).
- A vessel is matched to the port through the destination it declares on AIS, together with its ETA. Only vessels whose destination was updated in the last 60 days and that have not yet arrived are included.
- Inbound vessels are available to accounts with the Meridia feature enabled.

## Steps
1. On the **Overview** tab, find the **Vessels Inbound** card (shown with the time frame, for example **Vessels Inbound (next 24h)**) and select it to expand it.
   `[SCREENSHOT 1: Vessels Inbound card on the port Overview]`
2. Under **Within next**, choose **24h**, **7d**, **30d** or **All**. Your choice is remembered.
3. Read the list. Each vessel shows its name, vessel type, IMO and **ETA** in UTC. The header shows the number of vessels, for example "12 Vessels".
4. Select a vessel in the list to open its vessel page.
5. To see all columns, select **View all Events**. This opens the **Events** tab on **Inbound Vessels**.
   `[SCREENSHOT 2: Events tab, Inbound Vessels selected]`
6. Under **Within next**, choose **24h**, **7d**, **30d** or **All**.
7. Type in **Search...** to narrow the rows.
8. Select a column heading to sort.
9. Select a row to open the vessel's page.
10. On the **Overview** map, select an inbound vessel marker to see a popup, then click the vessel for more details.
   `[SCREENSHOT 3: Inbound vessel popup on the map]`

## Expected result
The table lists inbound vessels, with the number of rows shown above the table, for example "Showing most recent 25 events". Each row has an **Inbound** badge in the **Event** column.

## Good to know
- Default columns:


| Column | Meaning |
|---|---|
| **Event** | Always **Inbound** for this view. |
| **ETA (UTC)** or **ETA (System)** | The arrival time the vessel reports. Follows your time-zone setting. A dash (-) means none reported. |
| **Vessel** | Vessel name with its flag. |
| **IMO** | Vessel IMO number. |
| **Type** | Vessel type. |
| **Flag** | Flag country. |

- Further fields available for this view: **Reported Destination**, **MMSI**, **Call Sign**, **Latitude**, **Longitude**, **Course (°)**, **Speed (kts)**, **Heading (°)**, **Draught (m)**, **Navigational Status (status)**, and **Last Updated (UTC)** or **Last Updated (System)**. Position values come from the vessel's latest position report.
- The table shows at most 500 vessels. Use **Export** for the rest.
- In the map popup the labels are **Name**, **IMO**, **Vessel Type**, **Flag**, **Reported Dest**, **Reported ETA**, **Timestamp** and **Speed/Course**.
- **Export** on this view offers **24h**, **7d**, **30d** or **All** (no custom range). The file appears under **Notifications** then **Downloads**; the file is a CSV and export times are in UTC.
- **Navigational Status (status)** shows the status as received from the vessel.
- Data refreshes every 5 minutes. **Updated ... ago** shows its age; select **Refresh** to reload.

## Troubleshooting
| Problem | What to do |
|---|---|
| **No inbound vessels** or **No data available** | Choose a longer **Within next** period such as **All**, or clear **Search...**. |
| **ETA** is a dash | The vessel has not reported an arrival time. |
| A vessel is missing | Its destination may be older than 60 days or already marked arrived. |
| The list will not load | Select **Refresh** or try again later. |
