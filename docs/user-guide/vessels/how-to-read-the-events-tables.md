# How to read the events tables

Use this guide to understand each column in the **Events** tab of a vessel page, event type by event type.

## Before you begin
- Open a vessel page, select the **Events** tab and use **Event Type** to choose the events you want (see "How to view and filter vessel events").
- The **Events** tab uses one combined table. The first nine columns (under the **Overview** heading) are shown by default. The others are hidden until you add them in the **Columns** panel.
- A dash (-) means the value is not available for that event type.
- The **TimeStamp**, **Reported ETA**, **Inspection Date**, **Release Date**, **STS Ended**, **Gap Stopped**, **Gap Resumed** and **Stopped Timestamp** headers end in **(UTC)** or **(System)**, following your time-zone setting.

## Steps
1. Select the **Events** tab.
2. Open **Event Type** and tick the event type you want to read.
   `[SCREENSHOT 1: Event Type dropdown with one type selected]`
3. Find the matching section below to see which columns carry information for that type.
4. Open the **Columns** panel to show the extra columns listed in each section.
   `[SCREENSHOT 2: Columns panel with grouped columns]`

## Columns shown for every event type
| Column | Meaning |
|---|---|
| TimeStamp | When the event happened (for a span, when it started). |
| Event | A coloured label with the event type, for example Arrival or AIS Gap. Hover to see the full name. |
| Vessel, IMO, MMSI, Call Sign, Flag, Type | Hidden by default. The vessel's identity, repeated on each row. |

### Port events
Event types: **Area Arrival**, **Arrival**, **Departure**, **Area Departure**.

| Column | Meaning |
|---|---|
| Location | Name of the port or port area. |
| Country | Country of the port, with its flag. |
| UN/LOCODE | The port's UN/LOCODE. |
| Zone Type | The kind of area the event relates to. **[CONFIRM: values shown]** |
| Speed | Vessel speed at the event, in knots (kn). |
| Course | Direction of travel over the ground, in degrees. |
| Duration (hours) | Not filled in for port events (shows -). |
| Heading | Hidden. Direction the bow points, in degrees. |
| Draught | Hidden. Depth of the vessel in the water, in metres. |
| Navigational Status (Status) | Hidden. The status the vessel reported, such as at anchor. **[CONFIRM: wording]** |
| Reported Destination | Hidden. Destination typed in by the crew. |
| Reported ETA | Hidden. Arrival time reported by the vessel. |

Row click: opens the port page.

### Zone events
Event types: **Zone Entry**, **Zone Exit**.

| Column | Meaning |
|---|---|
| Location | Name of the zone entered or left. |
| Country | Country the zone is in, with its flag. |
| UN/LOCODE | Always blank (-) for zone events. |
| Zone Type | The type of zone. |
| Speed, Course | Speed (kn) and course (degrees) at the event. |
| Heading, Draught, Navigational Status (Status), Reported Destination, Reported ETA | Hidden. Same meaning as for port events. |

Row click: opens the zone page.

### STS (ship-to-ship) pairings
Event type: **STS Pairing**. A pairing is a period when this vessel was close to another vessel, which may indicate a ship-to-ship transfer. **[CONFIRM: definition used by the data provider]**

| Column | Meaning |
|---|---|
| TimeStamp | When the pairing started. |
| Duration (hours) | How long the pairing lasted. |
| STS Type | Hidden. The category of pairing. **[CONFIRM: possible values]** |
| Paired Vessel | Hidden. Name of the other vessel. |
| Paired IMO | Hidden. IMO number of the other vessel. |
| STS Ended (UTC/System) | Hidden. When the pairing ended. |
| Location, Country, UN/LOCODE, Zone Type | Not filled in for STS pairings (-). |

### AIS gaps
Event type: **AIS Gap**. A period when the vessel's AIS transmissions stopped and then resumed.

| Column | Meaning |
|---|---|
| TimeStamp | When the vessel stopped transmitting. |
| Speed | Speed (kn) in the last report before the gap. |
| Course | Course (degrees) in the last report before the gap. |
| Duration (hours) | Length of the gap. |
| Gap Stopped (UTC/System) | Hidden. When the signal stopped. |
| Gap Resumed (UTC/System) | Hidden. When the signal came back. |
| Draught Change | Hidden. Difference in reported draught across the gap, in metres. Can hint at loading or unloading. **[CONFIRM: sign convention]** |
| Navigational Status (Status), Navigational Status (Code) | Hidden. Status reported when the signal stopped. |

### Positional discrepancies
Event type: **Positional Discrepancy**. A period when the vessel's reported position disagreed with other evidence of where it was. **[CONFIRM: how discrepancies are detected]**

| Column | Meaning |
|---|---|
| TimeStamp | When the discrepancy started. |
| Duration (hours) | How long it lasted. |
| Has Ended | Hidden. Yes if it is over, No if still ongoing. |
| Started Latitude, Started Longitude | Hidden. Position when it began, in degrees. |
| Stopped Timestamp (UTC/System) | Hidden. When it ended. |
| Stopped Latitude, Stopped Longitude | Hidden. Position when it ended. |

The kind of discrepancy (shown on the timeline) is not a column in this table.

### Port State Control
Event type: **Port State Control**. An inspection of the vessel by a port authority.

| Column | Meaning |
|---|---|
| TimeStamp | The inspection date. |
| Location | The port where the inspection took place. |
| Country | The port's country, with its flag. |
| Authority | Hidden. The inspecting authority. |
| Inspection Type | Hidden. The kind of inspection. |
| Inspection Date (UTC/System) | Hidden. Same date as **TimeStamp**. |
| Detained | Hidden. Yes or No. |
| Days Detained | Hidden. Number of days held. |
| No. Defects | Hidden. Number of defects found. |
| Release Date (UTC/System) | Hidden. When the vessel was released. |

## Expected result
You can tell, for each event type, which columns to read and which to ignore.

## Good to know
- The code also contains separate, longer column sets for each event type. They include **Port Name**, **Sub Type**, **Zone Name**, **Started At**, **Stopped At**, **Stopped Reporting At**, **Resumed Reporting At**, **Gap Duration (hours)**, **Expanded Inspection**, **Follow up Inspection** and similar. They are not used in the vessel **Events** tab. **[CONFIRM: whether they appear anywhere else]**
- **Speed**, **Course**, **Heading** and **Draught** can show 0 when the data source gave no value. **[CONFIRM]**
- Export files include all available columns and use UTC times. **[CONFIRM: export column list]**

## Troubleshooting
| Problem | What to do |
|---|---|
| A column is empty (-) | That column does not apply to this event type. |
| I cannot see **Paired Vessel** or **Authority** | Open the **Columns** panel and tick it. |
| Times look different from the Overview tab | The table follows your time-zone setting. The timeline shows UTC. |
| Columns are in a mess | Select **Reset columns**. |
