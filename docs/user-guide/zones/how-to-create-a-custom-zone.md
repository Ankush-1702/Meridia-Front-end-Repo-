# How to create a custom zone

Define your own area of interest, as a polygon or a circle, and save it so you can analyse traffic in it.

## Before you begin
- Your account needs access to custom zones **[CONFIRM: entitlement wording]**.
- A polygon needs 3 to 100 points. A circle needs a centre and a radius of 100 m to 1,000 km.

## Steps
1. Open the creation page: on the **Library** page click **Add**, then under **Create new** choose **Custom zone**. (Or on **Custom Zones** click **New Custom Zone**.) The **New Zone** page opens.
   `[SCREENSHOT 1: New Zone page - form on the left, map on the right]`
2. Type a **Name** (required).
3. Optionally type a **Description**.
4. Next to **Type**, choose the **Polygon** or **Circle** tab.
5. Click the pencil button to the right of the tabs to turn drawing on or off (tooltip **Enable Drawing** / **Disable Drawing**). It is on by default.
6. To draw a **Polygon**, click on the map to add points. Right-click a point to remove it. Press **Escape** to finish drawing.
   `[SCREENSHOT 2: Polygon being drawn with points listed in the form]`
7. To draw a **Circle**, click on the map and drag to set the radius. Right-click the circle to edit it. Press **Escape** to stop editing.
8. Fine-tune the shape in the form if needed:
   - Polygon: edit each point's latitude and longitude, click the **+** icon to add a point, click **✕** to delete one, or click **Remove All**.
   - Circle: edit **Centre Lat**, **Centre Long** and **Radius (m)**.
   `[SCREENSHOT 3: Circle fields in the form]`
9. Click **Create Zone**. A message confirms `Custom zone "<name>" created successfully!` and you return to the **Custom Zones** list.

## Expected result
The new zone appears in the **Custom Zones** list and in your Library. Traffic analytics for it appear 24 hours after creation; data is processed daily.

## Good to know
- You can also load a shape from a file. See "How to upload a zone shape file or GeoJSON".
- **Create Zone** stays disabled until the form is valid and has at least 3 polygon points, or a radius above 0 for a circle.
- Use the map style control (top right) and zoom control (bottom right) to find your location. The map shows coordinates as you move.
- **Cancel** discards your work and returns you to the previous page.
- Switching between **Polygon** and **Circle** remembers what you drew for each type, but only the most recent shape is kept **[CONFIRM]**.

## Troubleshooting
| Problem | What to do |
|---|---|
| "Name is required" | Enter a name. |
| "Zone name must be between 1 and 100 characters" | Shorten the name. |
| "Description must be between 5 and 150 characters" | Make the description 5 to 150 characters, or leave it empty. |
| "Points (min 3)" shown in red | Add at least 3 points. |
| "Latitude is required" / "Longitude is required" | Fill in every coordinate. |
| "-90 to 90" / "-180 to 180" (polygon) or "Latitude -90 to 90" / "Longitude -180 to 180" (circle) | Enter a valid coordinate. |
| "Radius is required", "Min 100 meters", "Max 1000km" | Enter a radius from 100 to 1,000,000 metres. |
| "Polygon must have at least 3 vertices" / "Polygon cannot have more than 100 vertices" | Use 3 to 100 points. |
| "Minimum distance between vertices must be at least 50m (found …m)" | Move points further apart. |
| "Polygon area must be at least 31416 m² (found … m²)" | Make the area bigger. |
| "Polygon area cannot exceed 10M km² (found … km²)" | Make the area smaller. |
| "Please fix the validation errors before submitting" | Check the red "Validation Errors:" box in the form and correct each item. |
| Other save error | Try again; if it persists contact support **[CONFIRM: server-side limits such as maximum number of zones]**. |
