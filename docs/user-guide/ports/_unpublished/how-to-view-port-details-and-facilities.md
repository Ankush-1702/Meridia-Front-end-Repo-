# How to view port details and facilities

Review a port's reference details (harbour, dimensions, pilotage, services and facilities) in the port Details view.

## Before you begin

- **[CONFIRM]** The **Details** tab is switched off in the current front-end build: it is not in the tab bar on the port page. Publish this article only when the tab is enabled.
- When enabled, the data comes from World Port Index (WPI) records. **[CONFIRM]** the data source, edition and update date.

## Steps

1. Open a port page. See "How to open and read a port page".
2. Select the **Details** tab.
   `[SCREENSHOT 1: Details tab with category cards]`
3. If WPI data exists for the port, read the cards. Each card is a category with rows of field names and values.
4. If no WPI data exists, you instead see a single table with **Name**, **Type**, **Sub Type**, **Country**, **UNLOCODE**, **WPI Number** and **Sub Division**.
   `[SCREENSHOT 2: Details tab without WPI data]`
5. Select **Export** (top right) to download the details. The file is named "Port-Details".
   `[SCREENSHOT 3: Export button]`
6. Read the categories in this order:
   - **Basic Port Information**: WPI Number, Main Port Name, Region Number, Region Name, Country Code, Country Name, Alternate Port Name, UN/LOCODE
   - **Geographic Information**: Latitude, Longitude, Latitude (Decimal), Longitude (Decimal)
   - **Harbor Characteristics**: Harbor Size, Harbor Type, Harbor Use, Shelter Afforded
   - **Entrance Restrictions**: Tide, Heavy Swell, Ice, Other
   - **Physical Dimensions**: Overhead Limits, Entrance Width (m), Channel Depth (m), Anchorage Depth (m), Cargo Pier Depth (m), Oil Terminal Depth (m), Liquified Natural Gas Terminal Depth (m), Tidal Range (m)
   - **Vessel Limitations**: Maximum and Offshore Maximum Vessel Length (m), Beam (m) and Draft (m)
   - **Port Operations**: Good Holding Ground, Turning Area, Underkeel Clearance Management System, Port Security, Estimated Time of Arrival Message, Traffic Separation Scheme, Vessel Traffic Service
   - **Entry Requirements**: First Port of Entry, US Representative
   - **Pilotage Services**: Compulsory, Available, Local Assistance, Advisable
   - **Tug Services**: Salvage, Assistance
   - **Quarantine**: Pratique, Sanitation, Other
   - **Communications**: Telephone, Telefax, Radio, Radiotelephone, Airport, Rail, Search and Rescue
7. Continue with the remaining categories:
   - **Facilities - Moorings**: Wharves, Anchorage, Dangerous Cargo Anchorage, Med Mooring, Beach Mooring, Ice Mooring, RoRo
   - **Facilities - Cargo Types**: Solid Bulk, Liquid Bulk, Container, Breakbulk, Oil Terminal, LNG Terminal, Other
   - **Port Services**: Medical Facilities, Garbage Disposal, Chemical Holding Tank Disposal, Degaussing, Dirty Ballast Disposal
   - **Cranes**: Fixed, Mobile, Floating, Container
   - **Lifting Capacity**: 100+ Tons, 50-100 Tons, 25-49 Tons, 0-24 Tons
   - **Services**: Longshoremen, Electricity, Steam, Navigation Equipment, Electrical Repair, Ice Breaking, Diving
   - **Supplies**: Provisions, Potable Water, Fuel Oil, Diesel Oil, Aviation Fuel, Deck, Engine
   - **Repair Facilities**: Repairs, Dry Dock, Railway
   - **Navigation and Publications**: Sailing Direction or Publication, Standard Nautical Chart, NAVAREA, Digital Nautical Chart, S-57 and S-101 Electronic Navigational Chart, World Water Body, IHO S-130 Sea Area
   - **System Fields**: Global ID

## Expected result

You see the port's reference data grouped into category cards.

## Good to know

- Yes/No fields show **Yes**, **No** or **Unknown**. A missing value shows "Not Available".
- Harbour codes are shown in words: size (**Large**, **Medium**, **Small**, **Very Small**), type (for example **Coastal (Natural)**, **River (Basin)**, **Open Roadstead**), use (**Cargo**, **Fishing**, **Military**, **Ferry**, **Unknown**) and shelter (**Excellent** to **None**).
- Repairs show **Major**, **Moderate**, **Limited**, **Emergency Only** or **None**. Dry Dock and Railway show **Small**, **Medium** or **Large**. Underkeel Clearance Management System shows **Static**, **Dynamic**, **None** or **Unknown**.
- Only categories and fields with data from the port record are listed. **[CONFIRM]** whether empty categories are hidden.
- **[CONFIRM]** the units shown for dimensions, and the meaning of Facilities fields (only labels are in the code).
- **[CONFIRM]** the Export file layout. It writes one header row and one value row of the WPI fields.
- **[CONFIRM]** the label "Harbor" (US spelling) is as shown in the app.

## Troubleshooting

| Problem | What to do |
|---|---|
| You see only a short table of seven rows | No WPI data is held for this port. |
| **Export** is missing | **Export** appears only when WPI data exists. |
| A field shows "Not Available" | No value is recorded for that field. |
