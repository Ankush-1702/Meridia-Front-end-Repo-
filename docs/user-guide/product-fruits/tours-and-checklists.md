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

## Checklist – "Get started with Meridia"
1. Sign in to Meridia (Tour 1)
2. Choose your time zone and theme (My Profile → General) – link: `/analytics/account`
3. Decide on notification pop-ups (My Profile → Notifications)
4. Review your account details (My Profile → Personal)

## Notes
- The "Change password" form inside My Profile reuses ids `#otp`, `#newPassword`, `#confirmNewPassword`, so Tour 3's steps 3–5 also work at `/analytics/account` once the form is open.
- Theme/time zone/notification controls have no ids; use Product Fruits' point-and-click selector, or ask engineering to add `data-pf` ids. **[Suggestion]**
