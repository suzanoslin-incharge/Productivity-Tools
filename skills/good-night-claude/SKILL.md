---
name: good-night-claude
description: End-of-day wrap-up for Suzan. Writes today's entry in JOURNAL.md, rolls DAILY-PICKUP.md forward (where we left off, Next up, Outstanding, Context for Claude), then commits and pushes git changes in the productivity-tools repo. Use when Suzan says "good night", "good night Claude", "wrap up", "end of day" or "close out the day".
---

# Good Night Claude

Does three things, nothing else:

1. Writes today's entry in `JOURNAL.md`.
2. Rolls `DAILY-PICKUP.md` forward.
3. Commits and pushes git changes in `$TOOLS_PRODCTVTY`.

Both files are in `$ACCT_MYNOTES`. No tracker or article changes, no loose-ends report. Keep it fast: one short proposal, one "yes".

## The pickup file

Four parts, in this order:

- **Where we left off (yyyy-mm-dd):** a summary of today's chat context, replaced every night. One bullet per thread Suzan was in the middle of. Each bullet says: where it stands, what was just done, decisions and corrections that must carry forward, what is waiting on whom, and exactly where to restart (the file, the step, the next action). A task name is not enough. Example: not "Finish Lucid formatting" but "Lucid CSV formatting: imported the plain file, lanes and arrows look right; still to decide colors and how Status shows. Restart by importing the labelled CSV and testing the rules table." Finish with "First thing tomorrow:". About 2 to 3 lines per thread, 10 to 20 lines in all. Someone reading only this can start work. The good-morning skill shows it the next day.
- **Next up, (weekday yyyy-mm-dd):** what Suzan was in the middle of today, plus anything she asked to add ("add X to pickup"). Most urgent first.
- **Outstanding:** everything not finished on earlier days. It grows each day. At night, every Next up item that is not done moves here. An item leaves only when it is done (say what shows it) or Suzan says to drop it.
- **Context for Claude:** the last section, not shown at startup. Facts, names and rules Claude needs to work well. Update it every night from today's session: add new facts, names and rules, fix what changed, and remove what is no longer true. The good-morning skill reads it the next day.

Do not put open questions, follow-up items or waiting-on lines in the file. They live in the trackers. Add one only if Suzan asked.

## Steps

1. **Read first.** Read the whole pickup file and list its items before changing anything.
2. **Review the day.** Use this session. If there were other sessions, use files in `$ACCT_MYNOTES` changed today. For the journal's meetings, search today's calendar, Teams and mail with the Microsoft 365 connector (read only); use only what you find. Do not guess. Do not use this search to add pickup items.
3. **Propose in one short message, showing only the changes:**
   - The journal entry for today (format below).
   - The new "Where we left off".
   - Pickup changes: finished items removed; unfinished Next up items moved to Outstanding; new Next up items; the Next up heading set to the next working day.
   - Context for Claude: the lines that change.
   - The count: "N carried, N added, N removed", naming each removed item and why. Never drop an item silently.
   Use defaults, not questions. If one thing really blocks the update, ask one question and say what you will do if she does not answer.
4. **On "yes", write exactly what was shown.** Back up the pickup file and the journal to the scratchpad first. Do not write while a file is open with unsaved changes.
5. **Commit and push.** In `$TOOLS_PRODCTVTY`: run `git status`. If there are changes, stage them (the repo tracks only `skills/`, `shared-knowledge/` and `agents/`), look at the diff, then commit to `main` with a short message that says what changed and why, ending with the co-author line from the session's attribution instructions, and push. Do not ask again. Stop and tell Suzan instead of committing if the diff contains any of: an ID or token (a long GUID, a key, a password, a client or tenant ID), a name or content copied from the knowledge base, or a `SKILL.md` with broken front matter (missing `name` or `description`). If the push fails, report the error and leave the commit in place.
6. **Say good night.** Two lines: what got done (and the commit, if any), and the first thing for tomorrow.

## Journal entry format

Add above the previous entry, under a heading `## yyyy-mm-dd (Weekday)`. Suzan shares the journal with Delphine and leadership, so write it for them.

- **Accomplished:** 3 to 7 lines. Each starts with a project tag in brackets, such as [PayFabric] or [AR reporting], so entries can be rolled up by project. Say what was done and the result; include counts where they help.
- **Meetings and conversations:** meetings, Teams chats and emails, in time order (Pacific). Each is one bullet of one or two sentences: the meeting name, the chat or the email subject with the time; who took part (confirmed names only); the point, any decision, and the next step with its owner. No quotes, no step lists, no sub-bullets. Merge several messages in one chat into one bullet. If you cannot find what was discussed, say "No notes saved" and ask Suzan once at the end; do not invent.
- **Today only.** Everything in the entry comes from today: this session, and what is dated today (Pacific) in the calendar, Teams, mail and files changed today. Never pull in older items. Paraphrase; do not copy messages. Name the thread so Suzan can find it later. Leave out private or sensitive content; name the topic only, or skip personal calendar items.
- No link section. Mention an article or file by name if it helps.
- About 20 lines. Detail belongs in the articles and trackers.

## Rules

- Write both files the way Suzan would write to a colleague. Never mention Claude, AI, bots or the tools used. The skill name is not written into any file.
- Dates are yyyy-mm-dd. Plain English. Spell out an acronym the first time it appears in a file or entry.
- Names: use a full name only if it is confirmed in `$TOOLS_PRODCTVTY/shared-knowledge/org-glossary.md` or in the pickup file's "Names confirmed by Suzan". Otherwise keep the first name as written.
- Do not edit trackers or knowledge base articles. Do not delete, move or rename anything.
- Any file this skill creates follows the 12-point minimum font rule.
