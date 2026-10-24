---
name: good-night-claude
description: End-of-day wrap-up for Suzan. Writes today's entry in JOURNAL.md, rolls DAILY-PICKUP.md forward (where we left off, Next up, Outstanding, Context for Claude), then commits and pushes git changes in the productivity-tools repo. Use when Suzan says "good night", "good night Claude", "wrap up", "end of day" or "close out the day".
---

# Good Night Claude

Does four things, nothing else (six on Fridays):

1. Writes today's entry in `JOURNAL.md`.
2. Rolls `DAILY-PICKUP.md` forward.
3. Publishes changed production files to SharePoint (the `publish-files` skill).
4. Commits and pushes git changes in `$TOOLS_PRODCTVTY`.
5. **Fridays only:** tidies the open questions (the Tidy mode of the `kb-answer-questions` skill). Check the day with `date +%u`; 5 means Friday.
6. **Fridays only:** writes the freshness report for Suzan to review on Monday morning (section "Friday freshness report" below).

Both files are in `$ACCT_MYNOTES/TRACKERS`. No tracker or article changes (except the Friday tidy of the open questions workbook), no loose-ends report. Keep it fast: one short proposal, one "yes".

## The pickup file

Four parts, in this order:

- **Where we left off (yyyy-mm-dd):** only complex work we are in the middle of and need context to pick back up (several steps, decisions made, test results, a restart point). Never put anything finished here (a finished item goes in the journal only), and never a stand-alone task, a waiting-on item or a new ask (those go in Next up or Outstanding). The open loops of a thread we are in the middle of do belong here (see "Open loops" below). If nothing qualifies, write "Nothing in the middle." Replaced every night. One bullet per item. Each bullet says what was tried (and what happened), what is left to do, decisions and corrections that must carry forward, and exactly where to restart (the file, the step, the next action). A task name is not enough. Example: not "Finish Lucid formatting" but "Lucid CSV formatting: imported the plain file, lanes and arrows look right; still to decide colors and how Status shows. Restart by importing the labelled CSV and testing the rules table." A request or topic that came up but was never started (for example a new ask from Delphine) is not work in progress; it goes in Next up. Finish with "First thing tomorrow:". About 2 to 3 lines per item. Someone reading only this can start work. The good-morning skill shows it the next day.
- **Next up, (weekday yyyy-mm-dd):** work to do that is not in Where we left off (new asks and work not yet started), plus anything she asked to add ("add X to pickup"). Most urgent first.
- **Outstanding:** everything not finished on earlier days. It grows each day. At night, every Next up item that is not done moves here. An item leaves only when it is done (say what shows it) or Suzan says to drop it.
- **Context for Claude:** the last section, not shown at startup. Facts, names and rules Claude needs to work well. Update it every night from today's session: add new facts, names and rules, fix what changed, and remove what is no longer true. The good-morning skill reads it the next day.

**No duplicates.** A thread that is in Where we left off does not also appear in Next up or Outstanding. Where we left off carries it.

**Open loops are never to-dos.** An open loop is a loose end of a piece of work: a decision still to make, a step to confirm, a finding still to record in the notes or questions, a question to put to someone, a proposal waiting for her yes, or a file whose scope she has not settled. Examples: "decide whether the current-state files should end at Closed Won", "confirm steps S03 and S04", "rename `_KB`, waiting for yes". An open loop never goes in Outstanding or Next up. While the thinking is in progress it goes in Where we left off, as its own bullet or inside the thread's bullet, with what is decided, what is open and where to restart. Once the thinking is done and what is left is a plain action, it goes in `FOLLOWUP_ITEMS.xlsx` (propose the row in the nightly proposal; she approves it like any tracker change). Outstanding holds only stand-alone commitments with a clear next action (attend a session, write a document, review a recording, process a file).

**Sweep every night.** When you read the pickup file, check each Outstanding and Next up item against this rule. Move any open loop to Where we left off, or propose it as a follow-up row, and list it in the proposal as "moved". Never carry an open loop forward in Outstanding because it was there the day before.

**No calendar items.** Meetings, sessions and workshops are on her calendar, so they are never in Next up or Outstanding. Drop a past or upcoming event from the file; keep only a real action that came out of it, and apply the open-loop rule to that action. A recording she still needs to review for a past event is an action and stays in Outstanding until she has watched it. Good morning shows today's calendar.

**Item format.** Every Next up and Outstanding item is a bold title followed by one short sentence of context: who asked, why it matters, what is needed. No detail, no file lists, no test results. Keep the detail in the notes and files it lives in. When an item is a list of things (for example meeting notes and emails not yet processed), keep every entry of the list under it, one line each with the name and date, and carry the list forward in full. Where we left off keeps its full detail.

Do not put open questions, follow-up items or waiting-on lines in the file. They live in the trackers. Add one only if Suzan asked.

## Steps

1. **Read first.** Read the whole pickup file and list its items before changing anything.
2. **Review the day.** Use this session. If there were other sessions, use files in `$ACCT_MYNOTES` changed today. For the journal's meetings, search today's calendar, Teams and mail with the Microsoft 365 connector (read only); use only what you find. Do not guess. Do not use this search to add pickup items.
3. **Propose in one short message, showing only the changes:**
   - The journal entry for today (format below).
   - The new "Where we left off".
   - Pickup changes: open loops moved out of Next up and Outstanding (see "Open loops are never to-dos"); finished items removed; unfinished Next up items moved to Outstanding; new Next up items; the Next up heading set to the next working day.
   - Context for Claude: the lines that change.
   - Production files to publish: run steps 1 to 3 of the `publish-files` skill and show its short list here (nothing if no file changed). Suzan can say "skip publishing tonight".
   - **Fridays only, tidy the questions:** run steps 1 and 2 of Tidy (section 6 of `kb-answer-questions`) read-only and show the short table here: duplicates to merge, questions that could be closed by looking at a file, bundled questions, and empty Context cells. Say "nothing to tidy" if there are none. Suzan can say "skip the tidy tonight".
   - **Fridays only, freshness report:** one line saying a report will be written to `$ACCT_MYNOTES/_Productivity/Freshness-Report_yyyy-mm-dd.md` and that a Monday "Next up" item will point to it. Do not show the report itself tonight. Suzan can say "skip the freshness report".
   - The count: "N carried, N added, N removed", naming each removed item and why. Never drop an item silently.
   Use defaults, not questions. If one thing really blocks the update, ask one question and say what you will do if she does not answer.
4. **On "yes", write exactly what was shown.** Run step 4 of `publish-files` for the files listed. On Fridays also re-sort the Open sheet by batch and write only the tidy items she approved (close the workbook check first: if it is open in Excel, ask her to close it). Back up the pickup file and the journal to the scratchpad first. Do not write while a file is open with unsaved changes.
5. **Fridays only: write the freshness report** (read-only; see below), then add this item at the top of Monday's Next up in the new pickup file: **Review the Friday freshness report** with one sentence: what it covers and the file name. Skip both if she said to skip it.
6. **Commit and push.** In `$TOOLS_PRODCTVTY`: run `git status`. If there are changes, stage them (the repo tracks only `skills/`, `shared-knowledge/` and `agents/`), look at the diff, then commit to `main` with a short message that says what changed and why, ending with the co-author line from the session's attribution instructions, and push. Do not ask again. Stop and tell Suzan instead of committing if the diff contains any of: an ID or token (a long GUID, a key, a password, a client or tenant ID), a name or content copied from the knowledge base, or a `SKILL.md` with broken front matter (missing `name` or `description`). If the push fails, report the error and leave the commit in place.
7. **Say good night.** Two lines: what got done (and the commit, if any), and the first thing for tomorrow.

## Friday freshness report

Read-only. It changes nothing in the knowledge base or the trackers. Suzan reads it on Monday morning, not on Friday night. Write it to `$ACCT_MYNOTES/_Productivity/Freshness-Report_yyyy-mm-dd.md` (the Friday's date), as a short plain-English markdown file with three sections. Under each section, say "Nothing to report" if it is empty. Write it as Suzan would to a colleague; never mention Claude, AI or the tools used. Dates are yyyy-mm-dd.

1. **Articles not updated in 6 weeks.** Read the `Last updated` line of every article in `$KB_ROOT/02_Knowledge-Articles` (skip `_Superseded-Archived`). List the ones more than 42 days old: title, last updated date, days since, and the article's status. Oldest first.
2. **Open questions with no movement in 30 days.** The Open sheet has no "last touched" column, so use the `Raised` date: list questions raised more than 30 days ago that are still open, grouped by `Batch`, with the ID, the question and who may know. Say that "no movement" means still open since it was raised.
3. **Linked documents not refreshed.** Run steps 1 and 2 of `kb-update-linked-docs` (inventory and date check, read-only, Microsoft 365 connector). List each linked source whose original is newer than the recorded date, or that could not be checked: source, article, recorded date, current date, status. Do not run the update.

End the file with one line: how many items in each section, so the Monday reminder can say it. Do not add a "what changed" section or version notes.

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
- Do not edit trackers or knowledge base articles (the Friday report is a new file in `_Productivity`, nothing else changes). Do not delete, move or rename anything.
- Any file this skill creates follows the 12-point minimum font rule.
