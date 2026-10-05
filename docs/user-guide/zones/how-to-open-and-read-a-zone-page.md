# How to open and read a zone page

Open a zone in Meridia to see the vessels currently in it, its traffic analytics and its entry and exit events.

## Before you begin

- The zone must be in your **Library** or findable through **Search**.
- Features such as **Ask IQ** and PurpleTRAC Auto-Screening in notifications depend on your access. See Good to know.

## Steps

1. Open **Library** from the main navigation.
2. Select the **Zones** tab.
   `[SCREENSHOT 1: Library page with the Zones tab selected]`
3. Select the zone you want. **[CONFIRM]** how a zone is located on this tab (search box, list rows) because that screen is outside this page's code. You can also use **Search** and pick a zone from the results.
4. The zone page opens (its address ends with the zone's ID).
   `[SCREENSHOT 2: Zone page showing the header, tabs and Overview]`
5. Check the header. It shows the zone name and a subtitle made of the zone type, sub type and country, separated by commas. A country flag is shown when one is available; otherwise a zone icon is shown.
6. Use the breadcrumbs **Library** > **Zones** above the name to go back to your Library.
7. Select a tab: **Overview**, **Traffic** or **Events**.
   `[SCREENSHOT 3: The three zone tabs]`
8. On **Overview**, read the vessel count, the **Traffic (Previous 30 days)** panel, the map and the charts. See "How to view live zone traffic on the map".
9. On **Traffic**, review the zone's analytics over a time range you choose. See "How to read zone traffic charts".
10. On **Events**, review the individual **Entries** and **Exits**. See "How to read the zone events table".
11. To add the zone to your Library, open the three-dot menu in the header and select **Add to Library**.
12. To remove it, open the same menu and select **Remove from Library**. If you have notifications configured, a **Remove from Library?** confirmation appears.
   `[SCREENSHOT 4: Three-dot menu showing Add to Library]`
13. To set up alerts, select **Manage Notifications** in the header and switch on **Enable Live Notifications**.
   `[SCREENSHOT 5: Manage Notifications panel]`

## Expected result

You see the zone's name, type and country, and can move between its Overview, Traffic and Events tabs.

## Good to know

- A confirmation message ("added to bookmarks" or "removed from bookmarks") appears after you add or remove the zone.
- In **Manage Notifications**, you can choose **Entries** and **Exits**. Enabling notifications also adds the zone to your Library; the panel says so when the zone is not yet in your Library.
- Under **Entries**, **PurpleTRAC Auto-Screening** and the **SEVERITY** options (**Critical**, **Warning**, **OK**, **Unscored**) appear. If PurpleTRAC Auto-Screening is not enabled for you, it shows a lock and the tooltip says to contact your account manager.
- Switch on **Email Notifications** to choose **Timing** (**Immediately** or **Scheduled**). For **Scheduled**, set **Emails per day** (**1**, **2**, **3**, **4**, **Hourly**) and **Send at**. A note warns that **Immediately** on large zones and ports may trigger a large amount of emails.
- **Ask IQ** appears next to the tabs only if your account is entitled to it. Selecting it opens Ask IQ with a prompt about this zone.
- The header has no date range picker for zones. Time ranges are set on the **Traffic** tab.
- Newly created custom zones show a banner: "Traffic analytics will be available 24 hours after zone creation. Data is processed daily." It appears on **Overview** and **Traffic** and disappears after that period. **[CONFIRM]** the processing schedule and what happens if the zone was created in a test environment.
- A **Details** tab (name, type, sub type, country, UNLOCODE, WPI number, sub division) exists in the code but is not shown in the tab bar, so it is not available.
- **[CONFIRM]** There is no zone switcher on the page. To change zone, use **Search** or **Library**.

## Troubleshooting

| Problem | What to do |
|---|---|
| A loading placeholder stays on screen | Wait a moment, then reload the page. |
| An error page appears instead of the zone | Check the zone ID in the address, then try again. **[CONFIRM]** exact error text. |
| You cannot find the zone | Use **Search**, or check the **Zones** tab in **Library**. |
| The traffic panels are empty on a new custom zone | Wait for the banner period to pass and refresh. |
