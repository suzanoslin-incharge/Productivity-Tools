---
name: good-night-claude
description: End-of-day wrap-up for Suzan. Writes today's entry in JOURNAL.md, rolls DAILY-PICKUP.md forward with a "Where we left off" summary for tomorrow, flags loose ends, then commits and pushes any git changes in the productivity-tools repo. Use when Suzan says "good night", "good night Claude", "wrap up", "end of day" or "close out the day".
---

# Good Night Claude

Closes out the day so tomorrow's first session starts in the right place. Files, all in `$ACCT_MYNOTES` unless noted:

- `DAILY-PICKUP.md`: only what still needs doing, however old. It keeps no history: finished items are removed, and the record of what was done lives in `JOURNAL.md`. The startup hook shows its "## Next up" section (including everything under it, up to the next "## " heading) at the start of each session.
- `JOURNAL.md`: the daily work record, newest first. Suzan shares it with Delphine and leadership, so it is written for them.
- The `$TOOLS_PRODCTVTY` git repo: committed and pushed at the end.

Keep it fast: one short proposal, one "yes".

## Steps

1. **Carry-forward check (every night).** Read the whole pickup file before changing it, and keep the list of its items. Every item not completed stays, however old; an item leaves only when it was finished (say what shows it) or Suzan says to drop it. After the rewrite, compare the old and new lists and report "N carried, N added, N removed", naming each removed item and why. Never drop an item silently. Add only what Suzan asked to add during the day ("add X to pickup"). Do not search the calendar, Teams, mail or `meetingNotes` to build this list.
2. **Review the day.** Use this session. Read the pickup file's "Next up", "Started, not finished" and "Waiting on other people". If today had other sessions, use files in `$ACCT_MYNOTES` changed today. For meetings, chats and emails, search the calendar, Teams and mail for today with the Microsoft 365 connector (read only); use only what you find. Do not guess.
3. **Propose all of this in one short message, showing only the changes:**
   - **Journal entry for today** (format below).
   - **Pickup file:** finished items removed (no "done" sections, no history); every item not done stays, however old; new unfinished items in, most urgent first; items moved between "Started, not finished" and "Waiting on other people" as needed. Change the "Next up" heading to the next working day (yyyy-mm-dd and weekday).
   - **Where we left off:** a short summary of today's context, written as the first thing under "## Next up" as `### Where we left off` (8 to 12 lines), replacing last night's. It says: where each main thread stands, decisions made, corrections Suzan gave that must carry forward, what is waiting on whom, and the first thing to do tomorrow. Someone reading only this should be able to start work.
   - **Context for Claude:** update only if a fact, name or rule changed today.
   Use defaults, not questions. If one thing really blocks the update, ask one question and say what you will do if she does not answer.
4. **On "yes", write exactly what was shown.** Back up the pickup file and the journal to the scratchpad first. Do not write while a file is open with unsaved changes.
5. **Commit and push.** In `$TOOLS_PRODCTVTY`: run `git status`. If there are changes, stage them (the repo tracks only `skills/`, `shared-knowledge/` and `agents/`), look at the diff, then commit to `main` with a short message that says what changed and why, ending with the co-author line from the session's attribution instructions, and push. Suzan has asked for this every night, so do not ask again. Stop and tell her instead of committing if the diff contains any of: an ID or token (a long GUID, a key, a password, a client or tenant ID), a name or content copied from the knowledge base, or a `SKILL.md` with broken front matter (missing `name` or `description`). If the push fails, report the error and leave the commit in place.
6. **Loose ends (report, do not act).** One short list, only if there is something: drafts or messages not sent; tracker or article changes proposed but not approved; scratchpad backups that can be deleted; directions Suzan repeated today (offer to add them to her CLAUDE.md as rules).
7. **Say good night.** Two or three lines: what got done, the commit (if any), and the first thing for tomorrow.

## Journal entry format

Add above the previous entry, under a heading `## yyyy-mm-dd (Weekday)`:

- **Accomplished:** 3 to 7 lines. Each starts with a project tag in brackets, such as [PayFabric] or [AR reporting], so entries can be rolled up by project. Say what was done and the result; include counts where they help (articles, questions closed or opened, follow-up items).
- **Meetings and conversations:** meetings, Teams chats and emails, in time order (Pacific). Each is one bullet of one or two sentences: the meeting name, the chat or the email subject with the time; who took part (confirmed names only); the point, any decision, and the next step with its owner. Not thin, not a transcript: no quotes, no step lists, no sub-bullets. Merge several messages in one chat into one bullet. If you cannot find what was discussed, say "No notes saved" and ask Suzan once at the end; do not invent.
- **Today only.** Everything in an entry must come from today's context: what happened in this session, and what is dated today (Pacific) in the calendar, Teams, mail and files changed today. Never pull in older items, even if they sit in the pickup file or in the same thread; mention an older thread only if something new happened in it today. Search today's calendar, Teams chats and mail every night before writing, because Suzan's day is mostly outside this session. Paraphrase; do not copy messages. Name the thread so Suzan can find it later. Leave out private or sensitive content (medical, personal); name the topic only, or skip personal calendar items.
- No link section. Mention an article or file by name in the line if it helps.
- Keep an entry to about 20 lines. Detail belongs in the articles and trackers, not here.

## Rules

- Keep it simple. The pickup file only carries forward what is not done and adds what Suzan asked to add. Do not search her communication channels or other files to rebuild or extend that list, and do not show long lists back to her: show only the changes.
- Write the pickup file and journal the way Suzan would write to a colleague. Never mention Claude, AI, bots or the tools used. The skill name is not written into any file.
- Dates are yyyy-mm-dd. Plain English. Spell out an acronym the first time it appears in a file or in an entry.
- Names: use a full name only if it is confirmed in `$TOOLS_PRODCTVTY/shared-knowledge/org-glossary.md` or in the pickup file's "Names confirmed by Suzan". Otherwise keep the first name as written.
- Do not edit trackers (`OPEN_QUESTIONS.xlsx`, `FOLLOWUP_ITEMS.xlsx`) or knowledge base articles from here. List needed changes under loose ends.
- Do not delete, move or rename anything. List leftovers and leave them.
- Do not write knowledge base content or work files into the repo; the repo holds only skills, shared knowledge and agents.
- Any file this skill creates follows the 12-point minimum font rule.
