# All open [CONFIRM] items – one list

Total: **161** (152 in published articles + 9 in held articles). Order = knowledge-base user-journey order. Each line: what is unconfirmed, then the article it is in. Write your answer after the item or in the CSV (`CONFIRM-ITEMS.csv`).

Owner key – PM = product · BE = backend/data · FE = front-end dev · SUP = support · QA = check in running app (see CONFIRM-LIST.md for the grouped view on branch confirm-list).

1. **How to log in to Meridia** (Getting started) — A red message appears at the top after clicking Sign in — The email or password was not accepted. Re-enter them carefully (check Caps Lock). The message text comes from the server [CONFIRM exact wording].
2. **How to log in with a verification code (MFA)** (Getting started) — On the Verify your identity screen, check your email for a 6-digit code. [CONFIRM: delivery is email per the screen text "Enter the code sent to your email"]
3. **How to view your profile and account details** (Your account) — These details are read-only. To change your name, email or role, contact your Meridia account administrator or support. [CONFIRM: admin/support process]
4. **How to add a vessel, port or zone to your Library** (Library) — To remove an item, open the same search, find it, and click Added to Library again. [CONFIRM: other ways to remove]
5. **How to open and read a vessel page** (Vessels) — Select the Vessels tab. [CONFIRM] how a vessel is found or selected from this tab (search box, list rows) because that screen is outside this page's code.
6. **How to open and read a vessel page** (Vessels) — Next Port shows Destination and ETA. [CONFIRM] the source and freshness of this data.
7. **How to open and read a vessel page** (Vessels) — PurpleTRAC screening and MTI score show an "Unlock" message with "Available on request." if your account or user is not entitled to them. Hover over it and select More about PurpleTRAC or More about MTI for details and contact information. [CONFIRM: the app shows a hover card with these links, not a Contact us box]
8. **How to open and read a vessel page** (Vessels) — The header shows a refresh control. [CONFIRM] its label; it reloads the date range used for the map.
9. **How to open and read a vessel page** (Vessels) — An error page appears instead of the vessel — Check the IMO number in the address, then try again. [CONFIRM] exact error text.
10. **How to switch between vessels** (Vessels) — The Library tab shows up to 20 vessels you have added to your Library. [CONFIRM] whether vessels beyond 20 are expected to be listed.
11. **How to view vessel details, save a vessel and use Ask IQ** (Vessels) — Next to each ownership name is a company search icon. [CONFIRM: what the company search shows]
12. **How to view vessel details, save a vessel and use Ask IQ** (Vessels) — No notification or subscription setting is shown on the vessel page. [CONFIRM: whether vessel alerts exist elsewhere]
13. **How to view vessel details, save a vessel and use Ask IQ** (Vessels) — No export button appears on the vessel page in this code. [CONFIRM]
14. **How to view vessel details, save a vessel and use Ask IQ** (Vessels) — Data sources and refresh frequency for these fields are not shown. [CONFIRM]
15. **How to view a vessel's track on the map** (Vessels) — The toolbar shows the vessel's next port and ETA when available. [CONFIRM] data source.
16. **How to view a vessel's track on the map** (Vessels) — No track appears — Try a longer period. [CONFIRM] how vessels with no positions are shown.
17. **How to replay a vessel's movements** (Vessels) — Dragging the slider pauses playback. [CONFIRM] whether the replay restarts from the dragged point.
18. **How to read the event timeline and Gantt chart** (Vessels) — Both views show the same events and use the same date range. Events come from port calls, zone events, AIS gaps, STS pairings, positional discrepancies and Port State Control inspections. [CONFIRM: exact event sources and how often they refresh]
19. **How to read the event timeline and Gantt chart** (Vessels) — Arrival and departure events at the same place are joined into one bar, and so are zone entry and exit. An arrival with no matching departure appears as a thin mark. [CONFIRM: how an arrival still in progress is intended to look]
20. **How to read the event timeline and Gantt chart** (Vessels) — There are no zoom buttons. The chart spaces days automatically for the range you choose (a short range is stretched out, a long range is compressed). Scroll sideways and up or down to move around. [CONFIRM: whether zoom controls are planned]
21. **How to read the event timeline and Gantt chart** (Vessels) — The Gantt chart button is greyed or does nothing — The replay bar is disabled when the vessel has no events in the range. [CONFIRM]
22. **How to view and filter vessel events** (Vessels) — To see more columns, open the Columns panel on the side of the table and tick the columns you want. [CONFIRM: where the Columns tab appears on screen]
23. **How to view and filter vessel events** (Vessels) — Clicking a Zone Entry or Zone Exit row opens that zone's page. Clicking a port event row opens that port's page. Other event types do nothing when clicked. [CONFIRM: that Area Arrival and Area Departure rows open the port page]
24. **How to view and filter vessel events** (Vessels) — In Export, you choose Event type and Date range (Today, Yesterday, Last 7 Days, Last 30 Days, Last 90 Days or a custom range) and select Request export. When the file is ready it appears in Notifications or Downloads. [CONFIRM: file format and whether the export covers other columns]
25. **How to view and filter vessel events** (Vessels) — A type seems missing — Each type is fetched separately. If one request fails, only that type is left out. Select Refresh. [CONFIRM: no error message is shown for a failed type]
26. **How to read the events tables** (Vessels) — Zone Type — The kind of area the event relates to. [CONFIRM: values shown]
27. **How to read the events tables** (Vessels) — Navigational Status (Status) — Hidden. The status the vessel reported, such as at anchor. [CONFIRM: wording]
28. **How to read the events tables** (Vessels) — Event type: STS Pairing. A pairing is a period when this vessel was close to another vessel, which may indicate a ship-to-ship transfer. [CONFIRM: definition used by the data provider]
29. **How to read the events tables** (Vessels) — STS Type — Hidden. The category of pairing. [CONFIRM: possible values]
30. **How to read the events tables** (Vessels) — Draught Change — Hidden. Difference in reported draught across the gap, in metres. Can hint at loading or unloading. [CONFIRM: sign convention]
31. **How to read the events tables** (Vessels) — Event type: Positional Discrepancy. A period when the vessel's reported position disagreed with other evidence of where it was. [CONFIRM: how discrepancies are detected]
32. **How to read the events tables** (Vessels) — The code also contains separate, longer column sets for each event type. They include Port Name, Sub Type, Zone Name, Started At, Stopped At, Stopped Reporting At, Resumed Reporting At, Gap Duration (hours), Expanded Inspection, Follow up Inspection and similar. They are not used in the vessel Events tab. [CONFIRM: whether they appear anywhere else]
33. **How to read the events tables** (Vessels) — Speed, Course, Heading and Draught can show 0 when the data source gave no value. [CONFIRM]
34. **How to read the events tables** (Vessels) — Export files include all available columns and use UTC times. [CONFIRM: export column list]
35. **How to understand the MTI score for a vessel** (Vessels) — The gauge colours run red, orange, yellow, light green and green from low to high. The screen shows no named risk bands or thresholds. [CONFIRM: any official score bands or what counts as a good or poor score]
36. **How to understand the MTI score for a vessel** (Vessels) — How the score is calculated, and how often it is refreshed, is not shown on screen. [CONFIRM]
37. **How to understand the MTI score for a vessel** (Vessels) — The breakdown and ranking comparison are not shown in the app. The box says they are Available on request – select More about MTI to learn more and find contact details [CONFIRM: the app shows a hover card with a More about MTI link, not a Contact us box].
38. **How to run PurpleTRAC screening on a vessel** (Vessels) — The Overall row shows one badge: Ok (green), Warning (amber), Critical (red) or Unscored (grey). [CONFIRM: exact meaning of each result and what triggers Warning or Critical]
39. **How to run PurpleTRAC screening on a vessel** (Vessels) — The screening runs again each time you expand the section for a vessel that has no screening currently running. [CONFIRM: whether each run is saved or counted against a screening allowance]
40. **How to run PurpleTRAC screening on a vessel** (Vessels) — The code behind the screen says results are kept if you navigate away. [CONFIRM: how long results are retained and where to find them later]
41. **How to run PurpleTRAC screening on a vessel** (Vessels) — A box named Get the full breakdown says you can see every check behind the result (sanctions, PSC history, ship movement and more). It is marked Available on request – select More about PurpleTRAC to learn more and find contact details [CONFIRM: the app shows a hover card with a More about PurpleTRAC link, not a Contact us box].
42. **How to run PurpleTRAC screening on a vessel** (Vessels) — Result is Unscored — The screen gives no reason. [CONFIRM]
43. **How to search for company details from a vessel page** (Vessels) — If you closed the window while a search was running, the result is saved and the eye icon appears when it completes. [CONFIRM: whether the window then opens automatically or only the icon changes]
44. **How to search for company details from a vessel page** (Vessels) — [CONFIRM: whether this feature is limited to certain accounts or subscriptions. Nothing in the page limits it.]
45. **How to open and read a port page** (Ports) — Select the port you want. [CONFIRM] how a port is located on this tab (search box, list rows, add button) because that screen is outside this page's code. You can also use Search in the main navigation and pick a port from the results.
46. **How to open and read a port page** (Ports) — On Congestion and Utilisation, review the port's congestion analytics. [CONFIRM] the content of this tab, which is covered in a separate article.
47. **How to open and read a port page** (Ports) — Auto-Screen Vessels and the SEVERITY options (Critical, OK, Warning, Unscored) in notifications need PurpleTRAC Auto-Screening. If it is not enabled for you, the tooltip says to contact your account manager. [CONFIRM] exact email behaviour.
48. **How to open and read a port page** (Ports) — [CONFIRM] There is no port switcher on the page. To change port, use Search, Library, or select a vessel's port link elsewhere in the app.
49. **How to open and read a port page** (Ports) — An error page appears instead of the port — Check the port ID in the address, then try again. [CONFIRM] exact error text.
50. **How to view live port traffic on the map** (Ports) — [CONFIRM] how "in port" and "inbound" are defined, and the data sources and freshness of ATA and ETA.
51. **How to view live port traffic on the map** (Ports) — [CONFIRM] how the Performance figures and the arrival and departure counts are calculated.
52. **How to view live port traffic on the map** (Ports) — [CONFIRM] map marker interactions (hover or click) as they depend on shared map code.
53. **How to view live port traffic on the map** (Ports) — The map is blank or shows a missing-token notice — Contact support. [CONFIRM] wording and cause.
54. **How to view live port traffic on the map** (Ports) — The vessel count differs from the markers on the map — The "No mappable vessels" message means some vessels have no usable position. [CONFIRM]
55. **How to read port congestion and utilisation** (Ports) — The tab is only shown to accounts that have the Meridia feature. Locked sections lead to Contact us details. [CONFIRM: exact entitlement behaviour for this tab]
56. **How to read port congestion and utilisation** (Ports) — Preset periods end yesterday (UTC). [CONFIRM: the time basis of the charts]
57. **How to read port congestion and utilisation** (Ports) — How arrivals, unique arrivals, dwell time and congestion are calculated is not described in the app. [CONFIRM: definitions of Arrivals, Unique Arrivals per Day and Dwell time at berth]
58. **How to view inbound vessels** (Ports) — Inbound vessels are based on the destination vessels report. Only vessels whose destination was updated in the last 60 days and that have not yet arrived are included. [CONFIRM: how a vessel is matched to the port and the meaning of "reported"]
59. **How to view inbound vessels** (Ports) — Access depends on your account's features. Locked content leads to Contact us details. [CONFIRM: whether inbound vessels is a premium feature]
60. **How to view inbound vessels** (Ports) — Select a column heading to sort. Open the side panel to show or hide columns. [CONFIRM: side panel label]
61. **How to view inbound vessels** (Ports) — Export on this view offers 24h, 7d, 30d or All (no custom range). The file appears under Notifications then Downloads; export times are in UTC. [CONFIRM: file format and whether time frame windows match the table]
62. **How to view inbound vessels** (Ports) — Navigational Status (status) may show a number rather than a text description. [CONFIRM: status code meanings]
63. **How to view inbound vessels** (Ports) — A vessel is missing — Its destination may be older than 60 days or already marked arrived. [CONFIRM]
64. **How to read the port events table** (Ports) — To show more columns, use the side panel of the table and tick the columns you want. [CONFIRM: side panel label]
65. **How to read the port events table** (Ports) — Event types: Area Arrival and Area Departure relate to the port area, Arrival and Departure to the port, and Berth Arrival and Berth Departure to a berth. [CONFIRM: exact definitions and how area differs from port]
66. **How to read the port events table** (Ports) — In Export you choose Event type and Date range (Today, Yesterday, Last 7 Days, Last 30 Days, Last 90 Days or Custom), then select Request export. When ready it appears under Notifications then Downloads. A note says berth events are not included, so export those separately. [CONFIRM: berth export route and file format]
67. **How to read the port events table** (Ports) — Some events are missing — Berth and port events load separately. Select Refresh if one set is missing. [CONFIRM: no error message is shown]
68. **How to view berths in a port** (Ports) — Berth information is part of a premium section. It is visible only to entitled accounts. If you do not see the Berths tab, contact your Meridia administrator or use Contact us. [CONFIRM: exact entitlement and what non-entitled users see]
69. **How to view berths in a port** (Ports) — To clear your filters, select Reset Filters. It is greyed out when no filter is applied. [CONFIRM: whether Reset Filters restores all options or clears them]
70. **How to view berths in a port** (Ports) — Length — Berth length. [CONFIRM: unit, shown as metres in the data]
71. **How to view berths in a port** (Ports) — Max LOA — Maximum vessel length overall the berth takes. [CONFIRM: unit]
72. **How to view berths in a port** (Ports) — Max DWT — Maximum deadweight the berth takes. [CONFIRM: unit]
73. **How to view berths in a port** (Ports) — Depth (LW) — Depth at low water. [CONFIRM: unit]
74. **How to view berths in a port** (Ports) — Min dwell, Avg dwell, Median dwell, Max dwell — Minimum, average, median and maximum dwell time for the selected period. [CONFIRM: unit (hours?) and how dwell time is calculated]
75. **How to view berths in a port** (Ports) — Expand All is greyed out — It is disabled when no filter is applied. [CONFIRM: this looks like unintended behaviour]
76. **How to view berth details and dwell time** (Ports) — This section is premium and visible only to entitled accounts. [CONFIRM: entitlement behaviour]
77. **How to view berth details and dwell time** (Ports) — Read the Dwell time at berth chart on the right. Its subtitle says, for example, "Daily avg and median dwell time". [CONFIRM: Daily or Weekly is chosen by the system, not by you]
78. **How to view berth details and dwell time** (Ports) — The Top vessels by dwell time table has the columns Vessel, Type, Visits, Total Dwell and Avg Dwell, with the note "ranked by total time at berth". Select a row to open that vessel's page. [CONFIRM: when this table appears instead of the occupancy timeline; the choice comes from the data, not from a control]
79. **How to view berth details and dwell time** (Ports) — How dwell time is calculated and its unit in the box and table are [CONFIRM].
80. **How to view berth details and dwell time** (Ports) — The berth name reads "Unkown Berth" — The name could not be loaded. Go Back and reopen the berth. [CONFIRM: spelling in the product is "Unkown"]
81. **How to view vessel occupancy at a berth** (Ports) — This is part of a premium section visible only to entitled accounts. [CONFIRM: entitlement behaviour]
82. **How to view vessel occupancy at a berth** (Ports) — Whether you see the timeline or the Top vessels by dwell time table depends on the data returned for the berth and period. There is no switch. [CONFIRM: rule]
83. **How to view vessel occupancy at a berth** (Ports) — Times in tooltips are shown in UTC. [CONFIRM]
84. **How to view vessel occupancy at a berth** (Ports) — Gaps are shown in orange and vessels in red-orange. [CONFIRM: how gaps are defined, and that the timeline fills uncovered time as gaps]
85. **How to view vessel occupancy at a berth** (Ports) — Duration in the vessel tooltip is shown as a plain number. [CONFIRM: unit, likely hours]
86. **How to view vessel occupancy at a berth** (Ports) — The file is a CSV with one row per berth. Its columns are Terminal Name, Berth, Type, Vessel types, Handling, Length, Max LOA, Max DWT, Depth (LW), Min dwell, Avg dwell, Median dwell and Max dwell. [CONFIRM: the file is built by the server, so its columns may differ from the on-screen table]
87. **How to view vessel occupancy at a berth** (Ports) — Berth arrival and departure events appear in the port's Events tab as Berth Arrivals and Berth Departures. [CONFIRM: columns shown there; the berth-specific column set (TimeStamp, Berth Name, Event, Vessel, IMO, Type, Flag, optional Call Sign, Course, MMSI, Draught, Heading, Latitude, Longitude, Reported Destination, Reported ETA, Speed) was not found in use on any screen]
88. **How to view vessel occupancy at a berth** (Ports) — I see a table instead of a timeline — The page shows Top vessels by dwell time for this berth and period. [CONFIRM]
89. **How to open and read a zone page** (Zones) — Select the zone you want. [CONFIRM] how a zone is located on this tab (search box, list rows) because that screen is outside this page's code. You can also use Search and pick a zone from the results.
90. **How to open and read a zone page** (Zones) — Newly created custom zones show a banner: "Traffic analytics will be available 24 hours after zone creation. Data is processed daily." It appears on Overview and Traffic and disappears after that period. [CONFIRM] the processing schedule and what happens if the zone was created in a test environment.
91. **How to open and read a zone page** (Zones) — [CONFIRM] There is no zone switcher on the page. To change zone, use Search or Library.
92. **How to open and read a zone page** (Zones) — An error page appears instead of the zone — Check the zone ID in the address, then try again. [CONFIRM] exact error text.
93. **How to view live zone traffic on the map** (Zones) — Select a vessel marker to see a popup with name, IMO, vessel type, flag, reported destination and ETA, timestamp and speed/course. The popup says "Click vessel for more details". [CONFIRM] which fields appear for each marker.
94. **How to view live zone traffic on the map** (Zones) — The map shows custom zones from their saved shape, and other zones from the zone boundary. [CONFIRM] how boundaries are sourced.
95. **How to view live zone traffic on the map** (Zones) — [CONFIRM] What counts as "in the zone" and how often positions update, since this depends on backend data.
96. **How to view live zone traffic on the map** (Zones) — The map is blank — [CONFIRM] A message appears if the map service is not configured; contact your account manager.
97. **How to read zone traffic charts** (Zones) — For Custom, enter a Start date and End date and apply. [CONFIRM] the exact apply button label, which is outside this page's code. The date picker accepts dates within the last two years.
98. **How to read zone traffic charts** (Zones) — Visits — Number of visits [CONFIRM] how a visit is counted
99. **How to read zone traffic charts** (Zones) — [CONFIRM] How entries, exits and unique entries per day are calculated, whether the end date is included, and the data cut-off (the presets end yesterday).
100. **How to read zone traffic charts** (Zones) — [CONFIRM] What the Vessel Class values mean for each type.
101. **How to read the zone events table** (Zones) — Wait for "Export queued", then select Done. [CONFIRM] where the finished file is delivered or downloaded.
102. **How to read the zone events table** (Zones) — Columns hidden by default (shown through the table's column controls; [CONFIRM] how to reveal them):
103. **How to read the zone events table** (Zones) — Empty values show "-". [CONFIRM] units for course, heading, speed and draught, and how an event is detected.
104. **How to read the zone events table** (Zones) — The table is empty after an error — Select Refresh. [CONFIRM] whether an error message is shown.
105. **How to view and manage your custom zones** (Custom zones) — The table lists your custom zones, 20 per page [CONFIRM: pagination controls and whether the list is capped]. While you search, the count reads for example 3 results for "gulf".
106. **How to view and manage your custom zones** (Custom zones) — The Type column shows the zone's shape (for example Polygon or Circle) [CONFIRM: exact wording shown].
107. **How to create a custom zone** (Custom zones) — Your account needs access to custom zones [CONFIRM: entitlement wording].
108. **How to create a custom zone** (Custom zones) — Switching between Polygon and Circle remembers what you drew for each type, but only the most recent shape is kept [CONFIRM].
109. **How to create a custom zone** (Custom zones) — Other save error — Try again; if it persists contact support [CONFIRM: server-side limits such as maximum number of zones].
110. **How to upload a zone shape file or GeoJSON** (Custom zones) — Circles can come from a GeoJSON point with a radius, or from WKT POINT or CIRCLE. If no radius is given, 1000 m is used [CONFIRM: confirm this default is intended].
111. **How to upload a zone shape file or GeoJSON** (Custom zones) — Maximum file size [CONFIRM].
112. **How to edit a custom zone** (Custom zones) — Deleting a zone is not available in the screen [CONFIRM].
113. **How to create a fleet** (Fleets) — In Add Vessels, stay on the Search tab and type a vessel name or IMO number in Search vessel name or IMO.... [CONFIRM] Search starts after you type at least 3 characters.
114. **How to create a fleet** (Fleets) — IMOs that can't be added: a yellow panel shows "N IMOs couldn't be added" with counts of "not found" and "invalid format". Click it to see each IMO and the reason, and use the X or Dismiss all to clear them. The reasons come from the system. [CONFIRM]
115. **How to open and read a fleet page** (Fleets) — The table view in Overview shows the columns Vessel, IMO, MMSI, Type, Class, Flag, Nav Status, MTI Score (only if you have it), Next Port, Last Reported, Speed and Course. You can sort by any column and search with Search vessels.... [CONFIRM] how each value is sourced.
116. **How to open and read a fleet page** (Fleets) — Above the table, "Showing X of Y vessels" tells you how many vessels match, plus the number of filters applied. Its menu offers Export Data (CSV). [CONFIRM] exact CSV contents and file name (see report note).
117. **How to open and read a fleet page** (Fleets) — Locked scores in the vessel panel (see "How to view your fleet on the map") show a lock with an Unlock prompt. [CONFIRM] the "Contact us" details shown on click, because the code shows an "Available on request." hover card with a More about ... link.
118. **How to open and read a fleet page** (Fleets) — No Fleets tab in Library — Fleet management is not enabled for you. Ask your account manager. [CONFIRM]
119. **How to open and read a fleet page** (Fleets) — An error page appears instead of the fleet — Check you opened a fleet you can access, then try again. [CONFIRM] exact error text.
120. **How to view your fleet on the map** (Fleets) — PurpleTRAC screening and MTI score need the matching access. Without it you see a lock with Unlock. Hover to read what it offers. [CONFIRM] the "Contact us" step that opens on click: in the code this is an "Available on request." card with a More about PurpleTRAC or More about MTI link.
121. **How to view your fleet on the map** (Fleets) — Marker colours come from the vessel type. Types without a set colour use a default. [CONFIRM] the full colour list.
122. **How to view your fleet on the map** (Fleets) — The map is blank or shows a notice about a missing token — The map service is not configured. Contact support. [CONFIRM]
123. **How to read fleet composition** (Fleets) — Grey bars are labelled "unknown", or values outside your current flag or class selection. [CONFIRM] exactly when grey is used.
124. **How to read fleet composition** (Fleets) — [CONFIRM] how Average age, Total DWT, the size bands in Class and Age profile, and the Share percentages are calculated, and which units Dimensions uses.
125. **How to read fleet composition** (Fleets) — Export Image (PNG) does nothing in Show all view — Switch back to Show top 5 and export again. [CONFIRM]
126. **How to view fleet events** (Fleets) — Open the column panel on the side of the table to add or hide columns. [CONFIRM] where it appears on screen.
127. **How to view fleet events** (Fleets) — Location Type — Kind of location. [CONFIRM] values.
128. **How to view fleet events** (Fleets) — [CONFIRM] the exact definitions of AIS Gap, STS Pairing, Positional Discrepancy and Area Arrival/Departure events.
129. **How to view fleet events** (Fleets) — There are no notification settings on the fleet page. [CONFIRM] whether fleet alerts exist elsewhere.
130. **How to edit or delete a fleet** (Fleets) — Editing a fleet can't be done from the list view's rows; use the cards. [CONFIRM] whether list view offers fleet actions.
131. **How to edit or delete a fleet** (Fleets) — No Edit or Delete option — Your account may not have fleet management; contact your administrator. [CONFIRM]
132. **How to open and read your notifications** (Notifications) — Removing an item with the x only removes it from the panel list. It does not delete it from the Notifications page [CONFIRM].
133. **How to filter and manage the Notifications page** (Notifications) — The options under Show Notifications are loaded for your account; the labels include All [CONFIRM exact list, expected: All, last 7 days, last 24 hours].
134. **How to filter and manage the Notifications page** (Notifications) — The table loads up to 500 notifications at a time [CONFIRM paging behaviour beyond this].
135. **How to filter and manage the Notifications page** (Notifications) — Risk values come from PurpleTRAC Auto-Screening [CONFIRM]. Tooltips say auto-screening is currently only available for Port Area Arrival and Zone Entry events, and not for tug and push-boat vessels.
136. **How to turn notifications on for a port or zone** (Notifications) — Turning Enable Live Notifications on switches on all events for that item [CONFIRM defaults]. Turning it off switches off all events and email.
137. **How to turn notifications on for a port or zone** (Notifications) — Which accounts see the lock vs. the toggle depends on account permissions [CONFIRM].
138. **How to download your exports** (Notifications) — Request an export from a port, zone, vessel or fleet page first [CONFIRM where export is requested].
139. **How to download your exports** (Notifications) — The panel only lists exports requested recently in this browser. The page lists recent exports [CONFIRM how many].
140. **How to start a chat with Meridia IQ** (Meridia IQ) — Meridia IQ appears only for users whose account has access to it. If you do not see Meridia IQ in the left sidebar, ask your administrator. [CONFIRM: wording for how access is granted]
141. **How to start a chat with Meridia IQ** (Meridia IQ) — What Meridia IQ can and cannot answer, and which data it uses. [CONFIRM]
142. **How to start a chat with Meridia IQ** (Meridia IQ) — The example questions mention vessels by IMO number, ports and zones such as the Strait of Hormuz. [CONFIRM: whether these examples are guaranteed to return results]
143. **How to start a chat with Meridia IQ** (Meridia IQ) — A message starting "Error:" appears instead of an answer — Try asking again. [CONFIRM: recommended action]
144. **How to read Meridia IQ answers, maps and score tables** (Meridia IQ) — Score cells are green, amber or red. Colour thresholds seen in the app: 3.5 and above is green, 2.0 and above is amber, below 2.0 is red. [CONFIRM: meaning of the scores and colours]
145. **How to read Meridia IQ answers, maps and score tables** (Meridia IQ) — Meaning of each event type and marker colour. [CONFIRM]
146. **How to read Meridia IQ answers, maps and score tables** (Meridia IQ) — Accuracy of answers. [CONFIRM] The app itself advises: "We recommend verifying key information."
147. **How to read Meridia IQ answers, maps and score tables** (Meridia IQ) — Map is blank — Collapse and expand it again, or refresh the page. [CONFIRM]
148. **How to read Meridia IQ answers, maps and score tables** (Meridia IQ) — Answer shows "No response text" — Ask the question again. [CONFIRM]
149. **How to ask Meridia IQ about a vessel, port or zone** (Meridia IQ) — Quality and coverage of these summaries. [CONFIRM]
150. **How to manage your Meridia IQ chat history** (Meridia IQ) — Each chat has its own web address ending in the chat's ID. You can bookmark it to return to the chat later. [CONFIRM: whether others can open a shared link]
151. **How to manage your Meridia IQ chat history** (Meridia IQ) — The list loads the 20 most recent chats. [CONFIRM: how to reach older chats]
152. **How to manage your Meridia IQ chat history** (Meridia IQ) — How long chats are kept. [CONFIRM]
153. **How to add vessels to a fleet with filters** ((held article)) — Filters named Vessel Flag, Vessel Type, Vessel Class and MTI Score (MTI shown only if the account has it). [CONFIRM] Options come from the fleet's own vessels.
154. **How to view port details and facilities** ((held article)) — [CONFIRM] The Details tab is switched off in the current front-end build: it is not in the tab bar on the port page. Publish this article only when the tab is enabled.
155. **How to view port details and facilities** ((held article)) — When enabled, the data comes from World Port Index (WPI) records. [CONFIRM] the data source, edition and update date.
156. **How to view port details and facilities** ((held article)) — Only categories and fields with data from the port record are listed. [CONFIRM] whether empty categories are hidden.
157. **How to view port details and facilities** ((held article)) — [CONFIRM] the units shown for dimensions, and the meaning of Facilities fields (only labels are in the code).
158. **How to view port details and facilities** ((held article)) — [CONFIRM] the Export file layout. It writes one header row and one value row of the WPI fields.
159. **How to view port details and facilities** ((held article)) — [CONFIRM] the label "Harbor" (US spelling) is as shown in the app.
160. **How to edit or delete a custom zone** ((held article)) — In the zone's row, click the three-dot icon in Actions and choose Delete [CONFIRM: not live; label unverified in UI].
161. **How to edit or delete a custom zone** ((held article)) — Confirm in the dialog that reads "Are you sure you want to delete this custom zone?" [CONFIRM: browser confirm dialog in code; intended final design unknown].
