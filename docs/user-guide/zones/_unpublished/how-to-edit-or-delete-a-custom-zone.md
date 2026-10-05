# How to edit or delete a custom zone

UNPUBLISHED: the Delete action is commented out in the front-end code and there is no delete API call. Do not publish until Delete ships. Editing is documented in the live article "How to edit a custom zone".

## Steps (delete, once available)
1. Open **Library** > **Zones** > **Custom Zones**.
2. In the zone's row, click the three-dot icon in **Actions** and choose **Delete** **[CONFIRM: not live; label unverified in UI]**.
3. Confirm in the dialog that reads "Are you sure you want to delete this custom zone?" **[CONFIRM: browser confirm dialog in code; intended final design unknown]**.

## Good to know
- In the current code the confirmation only removes the row from the on-screen list; it does not call the server, so the zone would reappear on reload.
