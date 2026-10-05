# How to create a fleet

Create a named group of vessels so you can monitor them together.

> Available only if fleet management is enabled for your account. If you don't have it, you won't see the **Fleets** tab or the **Fleet** option.

## Before you begin
- You need the IMO numbers or names of the vessels you want to add.
- A fleet needs a name (at least 3 characters) and at least one vessel.
- A fleet can hold up to 1,000 vessels. **[CONFIRM]** whether this limit differs by plan; the screen refers to "your" limit.

## Steps
1. In the Library, click **Add**, then under **Create new** click **Fleet**.
   `[SCREENSHOT 1: Add menu with Fleet under Create new]`
2. On the **New Fleet** page, type a name in **Name** (up to 100 characters).
3. Optional: type a note in **Description (optional)** (up to 200 characters).
   `[SCREENSHOT 2: Details card with Name and Description]`
4. In **Add Vessels**, stay on the **Search** tab and type a vessel name or IMO number in **Search vessel name or IMO...**. **[CONFIRM]** Search starts after you type at least 3 characters.
5. Click a vessel in the results to add it. Vessels already added show a tick and can't be clicked again.
   `[SCREENSHOT 3: Search results with an added vessel ticked]`
6. To add many vessels at once, click the **Bulk Import** tab.
7. Either paste IMO numbers into **Paste IMO numbers** (comma or space separated) and click **Add**, or upload a file in **Upload CSV** and click **Upload**.
   `[SCREENSHOT 4: Bulk Import tab with paste and upload options]`
8. Check the **Vessels** panel on the right. It lists every vessel added and a count such as 12 / 1,000.
   `[SCREENSHOT 5: Vessels preview panel with count]`
9. Click **Save Changes**.

## Expected result
A "Fleet "name" created successfully" message appears and the new fleet opens.

## Good to know
- **Upload a CSV:** click **Download template** for the format. The file must be a .csv with one IMO per row. Drag and drop works too; click the X next to the file name to remove it. You can use paste or upload, not both at once.
- **IMOs that can't be added:** a yellow panel shows "N IMOs couldn't be added" with counts of "not found" and "invalid format". Click it to see each IMO and the reason, and use the X or **Dismiss all** to clear them. The reasons come from the system. **[CONFIRM]**
- **Remove vessels:** click the X beside a vessel in the **Vessels** panel, or open the panel's vessel actions menu and click **Clear fleet** to remove all of them.
- **Near the limit:** the count turns yellow at 90% of the limit and red above it, with a message "Remove N vessel(s) to save".
- **Leaving without saving:** click **Cancel**. If you've entered anything, **Discard changes?** asks you to confirm with **Discard changes**, or click **Keep editing**.
- Fleets you create here are static: they contain exactly the vessels you add.

## Troubleshooting
| Problem | What to do |
|---|---|
| **Save Changes** is greyed out | Read the message beside it and fix that item. |
| "Add a name and at least one vessel" | Enter a name and add a vessel. |
| "Add a name" / "Name is required" | Type a fleet name. |
| "Name must be at least 3 characters" | Use a longer name. |
| "A fleet with this name already exists" | Choose a name not used by another of your fleets (capitals are ignored). |
| "Add at least one vessel" | Add a vessel by search or bulk import. |
| "Remove N vessels to save — limit is 1000" | Remove vessels in the **Vessels** panel. |
| "No results found for ..." | Check the spelling or try the IMO number. |
| "N IMOs couldn't be added" | Open the panel, correct the IMOs and add them again. |
