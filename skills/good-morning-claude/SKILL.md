---
name: good-morning-claude
description: Start-of-day pickup for Suzan. Reads DAILY-PICKUP.md (including last night's context) and shows Where we left off, Next up and Outstanding. Use when Suzan says "good morning", "good morning Claude", "pick up", "where were we" or opens a session asking what is next.
---

# Good Morning Claude

Starts the day from `$ACCT_MYNOTES/TRACKERS/DAILY-PICKUP.md`. Read only that file. Do not read the journal. Do not search mail, calendar, Teams, trackers or other files.

## Steps

1. Read the whole pickup file. Read "Context for Claude" for names and rules. Use it to work; do not show it.
2. Reply with only these three parts, short:
   - **Where we left off:** show the section as written: each thread with where it stands and where to restart, ending with the first thing to do. Do not shrink it to task names.
   - **Next up:** each item in file order: the title, then one short sentence of context (who asked, why it matters, what is needed). No detail.
   - **Outstanding:** each item in file order, with the count: the title, then one short sentence of context. When an item has a list under it (for example the KB meeting notes and emails not yet processed), show each entry of that list on its own short line (name and date), so Suzan can see which ones. Never cut a list down to its title.
   Layout to match every time: the three headings in this order, with Outstanding showing the count; Where we left off in full, one bullet per thread, ending with "First thing tomorrow"; Next up and Outstanding as a bold title plus one short sentence; lists under an Outstanding item shown entry by entry. Nothing appears in two sections.
3. Do not list open questions, follow-up items or waiting-on lines. They live in the trackers. Mention them only if Suzan asks.
4. Do not change any file.

## Rules

- Where we left off is only for complex work in the middle that needs context to pick back up. Never show a finished item there or under Next up (skip anything marked done, `[x]`), and never repeat in Where we left off something that is also in Next up or Outstanding. If the section has nothing, say "Nothing in the middle."
- Plain English, no filler. Cut long items to a title plus one short sentence, except Where we left off (show in full) and any list under an Outstanding item (show every entry).
- Dates are yyyy-mm-dd.
