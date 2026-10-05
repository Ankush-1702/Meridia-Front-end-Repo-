# How to upload a zone shape file or GeoJSON

Create or fill in a custom zone by loading a GeoJSON or WKT file instead of drawing.

## Before you begin
- Prepare a file ending in `.geojson`, `.json`, `.wkt` or `.txt`. Shapefiles and KML are not supported.
- Only the first shape in the file is used.

## Steps
1. Open the **New Zone** page (**Library** > **Add** > **Custom zone**).
2. Scroll to the box below the **or** divider that reads **Click to upload or drag and drop** with **GeoJSON, WKT**.
   `[SCREENSHOT 1: Upload box under the or divider]`
3. Click the box and choose your file, or drag the file onto it.
4. Wait for the green message, for example "Polygon with 5 points loaded" or "Circle loaded successfully".
   `[SCREENSHOT 2: Loaded file pill, green message and shape on the map]`
5. Check the **Name**, which is filled in from the file name. Change it if you like.
6. Click **Create Zone**.

## Expected result
The shape appears on the map and the map zooms to it. The type switches to **Polygon** or **Circle** to match the file. The file name appears in place of the upload box.

## Good to know
- While a file is loaded, the type tabs, drawing button and coordinate fields are locked.
- To start over, click the **✕** next to the file name (tooltip **Remove file and clear data**). This clears the shape and name.
- Circles can come from a GeoJSON point with a radius, or from WKT `POINT` or `CIRCLE`. If no radius is given, 1000 m is used **[CONFIRM: confirm this default is intended]**.
- The same size limits apply as when drawing (3 to 100 points, circle radius 100 m to 1,000 km).
- Maximum file size **[CONFIRM]**.

## Troubleshooting
| Problem | What to do |
|---|---|
| "Please upload a GeoJSON or WKT file" | Use a `.geojson`, `.json`, `.wkt` or `.txt` file. |
| "Unable to parse file. Please check the format." | Check the file holds a valid polygon, point or circle. |
| "Error processing file: …" | The file is not valid; fix and retry. |
| "Error reading file" | Try selecting the file again. |
| "Zone type must be Polygon" (or Circle) | When editing a zone, the file shape must match the zone's type. |
