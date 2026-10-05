# How to view vessel details, save a vessel and use Ask IQ

Use the vessel page to see a vessel's particulars, switch to another vessel, save it to your Library and start an Ask IQ question.

## Before you begin
- Open a vessel from the Library (**Library** > **Vessels**) or by searching. The page is at an address ending in /analytics/vessel/ followed by the vessel ID.
- **Ask IQ** appears only if your account has access to it. **[CONFIRM: which plan includes Ask IQ]**

## Steps
1. Open the vessel. The header shows the vessel name, and below it the IMO, flag and vessel type.
   `[SCREENSHOT 1: Vessel page header with breadcrumbs, name and subtitle]`
2. Make sure the **Overview** tab is selected. The other tab is **Events**.
3. In the left-hand panel, read the top rows: **Type**, **IMO**, **MMSI**, **Flag**, **Flag since** (only when known), **Callsign** and **Status**.
   `[SCREENSHOT 2: Vessel details panel identity rows]`
4. Select a section name to expand it: **Next Port**, **Dimensions**, **Registry** or **Ownership**. Select it again to collapse.
5. In **Next Port**, read **Destination** and **ETA**.
6. In **Dimensions**, read **LOA**, **Beam**, **Draught**, **Gross tonnage**, **Deadweight**, **Displacement** and **Service speed**.
7. In **Registry**, read **Built**, **Shipbuilder**, **Country of build**, **Hull type**, **Port of registry**, **Classification**, **P&I Club** and **DOC company**.
8. In **Ownership**, read **Operator**, **Registered owner**, **Technical manager**, **Ship manager** and **Group beneficial owner**.
   `[SCREENSHOT 3: Ownership section expanded]`
9. To switch vessel, select the vessel name at the top. Use the search box (**Search vessels…**) or the **Recent** and **Library** tabs, then select a vessel.
10. To save the vessel, select the three-dot menu at the top right and choose **Add to Library**.
    `[SCREENSHOT 4: Three-dot menu showing Add to Library]`
11. To remove it, open the same menu and choose **Remove from Library**.
12. To start a question about the vessel, select **Ask IQ** next to the tabs.
    `[SCREENSHOT 5: Ask IQ button beside the Overview and Events tabs]`

## Expected result
After saving or removing, a message confirms the change, for example "[vessel name] added to bookmarks" or "removed from bookmarks". Ask IQ opens with a ready-made prompt asking for a 30-day summary of the vessel: voyage status, port calls, zone events, AIS gaps and anything notable.

## Good to know
- Empty values show a dash (-). Hover over a value to see the full text.
- Next to each ownership name is a company search icon. **[CONFIRM: what the company search shows]**
- Hide or show the left panel with the ship icon (**Hide Vessel Details** / **Show Vessel Details**) in the map toolbar.
- No notification or subscription setting is shown on the vessel page. **[CONFIRM: whether vessel alerts exist elsewhere]**
- No export button appears on the vessel page in this code. **[CONFIRM]**
- Data sources and refresh frequency for these fields are not shown. **[CONFIRM]**

## Troubleshooting
| Problem | What to do |
|---|---|
| Error page instead of the vessel | Refresh the page or return to the **Library** and reopen the vessel. |
| **Ask IQ** is missing | Your account may not include it. Contact your administrator. |
| Add or remove does not work | Wait for the menu button to finish loading, then try again. |
| A field shows - | No data is held for that field. |
