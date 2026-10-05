# Product Fruits – in-app tour / checklist versions

Use these when building a **Tour** or **Checklist** (not a KB article) in Product Fruits.
CSS selectors come from the front-end code (element `id`s), so they are stable. Tours on `/login` and `/reset-password` run for signed-out users – make sure the Product Fruits snippet is loaded on those public pages **[CONFIRM]**.

## Tour 1 – How to log in (URL: `/login`)
| # | Selector | Title | Text |
|---|---|---|---|
| 1 | `#email` | Enter your email | Type the email address registered with your Meridia account. |
| 2 | `#password` | Enter your password | Type your password. |
| 3 | `#keepLoggedIn` | Stay signed in? | Tick this on your own device. Leave it unticked on shared computers. |
| 4 | `button[type="submit"]` | Sign in | Click **Sign in**. If your account uses two-step verification, you'll be asked for a code next. |
| 5 | `a[href="/reset-password"]` | Forgot your password? | Click here to reset it. |

## Tour 2 – Verification code (MFA) (shown after Sign in; URL `/login`)
| # | Selector | Title | Text |
|---|---|---|---|
| 1 | `#otp` | Enter the code | Type the 6-digit code from your email. It's valid for 10 minutes. |
| 2 | `button[type="submit"]` | Sign in | Click **Sign in** to finish. |

## Tour 3 – Reset your password (URL: `/reset-password`)
Step 1 screen:
| # | Selector | Title | Text |
|---|---|---|---|
| 1 | `#email` | Your email | Enter your registered email address. |
| 2 | `button[type="submit"]` | Continue | Click **Continue** – we'll email you a 6-digit code. |

Step 2 screen (after Continue; trigger on element appearing):
| # | Selector | Title | Text |
|---|---|---|---|
| 3 | `#otp` | Enter the code | Type the code from your email (valid 10 minutes). |
| 4 | `#newPassword` | Choose a new password | At least 8 characters with a number, a special character, an uppercase and a lowercase letter. |
| 5 | `#confirmNewPassword` | Confirm it | Re-type the same password. |
| 6 | `button[type="submit"]` | Continue | Click **Continue**, then sign in with your new password. |

## Tour 4 – Add your first item to the Library (URL: `/analytics/library`)
No stable ids exist on these controls; use Product Fruits' point-and-click selector (or ask engineering for `data-pf` ids).
| # | Element | Title | Text |
|---|---|---|---|
| 1 | **Add** button (header, top right) | Add items | Click **Add**, then choose **Vessel**, **Port** or **Zone** under *Find and add*. |
| 2 | Search box (in the window, `input[placeholder^="Search"]`) | Search | Type at least 3 characters. Use the dropdown on the left to search by IMO, MMSI, UN/LOCODE, etc. |
| 3 | **Filters** button | Narrow results | Filter by flag, country, type and more. |
| 4 | **Add to Library** button | Save it | Click **Add to Library**. The item now appears on your Library page. |

## Tour 5 – Explore a vessel (URL: `/analytics/vessel/*`)
Use Product Fruits' point-and-click selector (these controls have no stable ids).
| # | Element | Title | Text |
|---|---|---|---|
| 1 | Page header (vessel name) | Vessel page | See the vessel's name, flag, IMO and type. |
| 2 | **Overview** / **Events** tabs | Two views | Overview shows the map and timeline; Events lists port, zone and other events. |
| 3 | Vessel details panel | Details | Expand a section such as Dimensions, Registry or Ownership. |
| 4 | Map toolbar date range | Choose a period | Pick Previous 7/14/30/90 days or a Custom range. |
| 5 | Replay bar | Replay | Press play to replay the vessel's movements. |
| 6 | Three-dot menu (header) | Save it | Add the vessel to your Library. |

## Tour 6 – Explore a port (URL: `/analytics/port/*`)
Use Product Fruits' point-and-click selector (no stable ids).
| # | Element | Title | Text |
|---|---|---|---|
| 1 | Page header (port name) | Port page | See the port's name and country. |
| 2 | Tabs: **Overview**, **Congestion and Utilisation**, **Berths**, **Events** | Four views | Switch between live traffic, congestion charts, berths and port events. |
| 3 | Overview map | Live traffic | See vessels in and heading to the port. |
| 4 | Time range / date picker | Choose a period | Pick a preset or a custom range. |
| 5 | **Events** → Inbound Vessels | Who's coming | See vessels heading to this port. |
| 6 | Three-dot menu (header) | Save it | Add the port to your Library. |


## Tour 7 – Create a custom zone (URL: `/analytics/custom-zones/new`)
Use Product Fruits' point-and-click selector (no stable ids).
| # | Element | Title | Text |
|---|---|---|---|
| 1 | Form: name & description | Name your zone | Give the zone a name and a description (5–150 characters). |
| 2 | **Polygon** / **Circle** tabs | Choose a shape | Pick the shape you want to draw. |
| 3 | Map drawing tools | Draw it | Draw the zone on the map, or upload a GeoJSON/WKT file. |
| 4 | Save button | Save | Save the zone. New zones can take up to 24 hours to show data. **[CONFIRM]** |

## Tour 8 – Create your first fleet (URL: `/analytics/fleet/new`)
Use Product Fruits' point-and-click selector (no stable ids). Only for accounts with fleet management.
| # | Element | Title | Text |
|---|---|---|---|
| 1 | Fleet name field | Name your fleet | Give the fleet a clear name. |
| 2 | Add vessels card | Add vessels | Search for vessels by name or IMO, or upload a list of IMOs (use **Download template**). |
| 3 | Preview | Check it | Review the vessels that will be in the fleet. |
| 4 | Save button | Save | Save the fleet. It then appears on the **Fleets** tab in your Library. |

## Checklist – "Get started with Meridia"
1. Sign in to Meridia (Tour 1)
1b. Add your first vessel, port or zone to the Library (Tour 4)
2. Choose your time zone and theme (My Profile → General) – link: `/analytics/account`
3. Decide on notification pop-ups (My Profile → Notifications)
4. Review your account details (My Profile → Personal)

## Notes
- The "Change password" form inside My Profile reuses ids `#otp`, `#newPassword`, `#confirmNewPassword`, so Tour 3's steps 3–5 also work at `/analytics/account` once the form is open.
- Theme/time zone/notification controls have no ids; use Product Fruits' point-and-click selector, or ask engineering to add `data-pf` ids. **[Suggestion]**
