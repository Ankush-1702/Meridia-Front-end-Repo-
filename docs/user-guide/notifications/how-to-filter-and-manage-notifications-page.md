# How to filter and manage the Notifications page

Narrow the Notifications page to ports or zones, refresh it, export it, and choose how far back it looks.

## Before you begin
- Open **Notifications** in the sidebar, then click **View All**, or go to the **Notifications** page directly.
- You will see the **Notifications** tab and the **Downloads** tab at the top. Stay on **Notifications**.

## Steps
1. Choose **All**, **Ports** or **Zones** to filter the list by type.
   - **Ports** shows port arrival, departure, area arrival and area departure notifications.
   - **Zones** shows zone entry and exit notifications.
   `[SCREENSHOT 1: All, Ports and Zones tabs above the table]`
2. Read the table. Columns are **Date/Time** (shown as UTC or System, depending on your time zone setting), **Zone/Port Name** (**Zone Name** or **Port Name** on the other tabs), **Event Type**, **Vessel Name**, **Vessel IMO**, **Vessel Type** and **Risk**.
   `[SCREENSHOT 2: Notifications table with columns]`
3. Click a port, zone, vessel name or IMO to open its details page.
4. Hover over **Risk** or **Event Type** to see a tooltip.
5. Click **Refresh** to reload the list.
6. Click **Export** to download the rows shown on the current page as a CSV file. The file is named after the tab, for example "All-Notifications".
7. To change how far back notifications are shown, click the three-dot menu at the top right.
8. Under **Show Notifications**, choose one option from the list. The selected option has a tick.
   `[SCREENSHOT 3: Three-dot menu with Show Notifications options]`

## Expected result
The table reloads and shows only the notifications that match your choices.

## Good to know
- The options under **Show Notifications** are loaded for your account; the labels include **All** **[CONFIRM exact list, expected: All, last 7 days, last 24 hours]**.
- The table has no search box, no sorting, and no mark-as-read or delete options. Notifications are not marked read or unread.
- **Refresh** also clears the pop-ups and the bell panel list.
- If many notifications arrive quickly, a banner shows "N new notifications received" with a **show** button. Click **show** to reload the list.
- The table loads up to 500 notifications at a time **[CONFIRM paging behaviour beyond this]**.
- Risk values come from PurpleTRAC Auto-Screening **[CONFIRM]**. Tooltips say auto-screening is currently only available for Port Area Arrival and Zone Entry events, and not for tug and push-boat vessels.

## Troubleshooting
| Problem | What to do |
|---|---|
| The page says "Your notifications will appear here" | Configure notifications on items in your library, or change the **Show Notifications** option. |
| The newest notification is missing | Click **Refresh**. |
| Times look wrong | Check your time zone setting. The column heading shows **Date/Time (UTC)** or **Date/Time (System)**. |
