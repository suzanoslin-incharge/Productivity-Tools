---
name: good-morning-claude
description: Start-of-day pickup for Suzan. Reads DAILY-PICKUP.md (including last night's context) and shows Where we left off, Next up and Outstanding. Use when Suzan says "good morning", "good morning Claude", "pick up", "where were we" or opens a session asking what is next.
---

# Good Morning Claude

Starts the day from `$ACCT_MYNOTES/DAILY-PICKUP.md`. Read only that file. Do not read the journal. Do not search mail, calendar, Teams, trackers or other files.

## Steps

1. Read the whole pickup file. Read "Context for Claude" for names and rules. Use it to work; do not show it.
2. Reply with only these three parts, short:
   - **Where we left off:** show the section as written: each thread with where it stands and where to restart, ending with the first thing to do. Do not shrink it to task names.
   - **Next up:** one line per item, in file order.
   - **Outstanding:** one line per item, in file order, with the count.
3. Do not list open questions, follow-up items or waiting-on lines. They live in the trackers. Mention them only if Suzan asks.
4. Do not change any file.

## Rules

- Plain English, no filler. One line per item; cut long items to their title.
- Dates are yyyy-mm-dd.
