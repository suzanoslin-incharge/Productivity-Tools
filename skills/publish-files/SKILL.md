---
name: publish-files
description: Copy Suzan's production files (SIPOCs and similar finished work) from Accounting-MyNotes to the Accounting Internal SharePoint library under fixed, undated names, using the list in PRODUCTION_FILES.xlsx. Use when Suzan says "publish", "publish my production files" or "update SharePoint". The good-night skill runs the same steps.
---

# Publish Files

Copies the current version of each file on the list to its SharePoint folder (today always `$ACCT_AUTO`, the Automation folder in the Accounting - Internal SharePoint library, synced to this Mac). The SharePoint copy has a fixed name with no date. SharePoint version history keeps the old versions, so a new copy overwrites the old one.

Anything copied there is visible to the Accounting team, so **nothing is copied before Suzan approves the proposal.**

## The list

`$ACCT_MYNOTES/TRACKERS/PRODUCTION_FILES.xlsx` (sheet "Production files", table `ProductionFiles`). One row per file:

- **Status:** `Active`, or `Retired (kept)` (left alone in SharePoint, never copied again).
- **SharePoint file (fixed name):** the file name in that folder, no date.
- **SharePoint folder:** where the file is published, as an environment variable (such as `$ACCT_AUTO`) or a full path. Resolve it before use. It may differ by row in future.
- **Local file:** the path under `$ACCT_MYNOTES` of the current dated version.
- **Owner, Last published** (date), **Local file modified when published** (the local file's modified date and time at the last publish), and **SharePoint copy modified after last publish** (the SharePoint file's modified date and time right after the last copy).

Suzan decides which files are production. A new file goes on the list only when she says so. If `$ACCT_AUTO` is not set in the shell, use `$ACCT_INTERNAL/Automation`. A folder that does not exist is reported, never created.

## Steps

1. **Check the Excel files first.** Do not read a file as final while it is open in Excel: look for a `~$` lock file next to the local file and the list. If one exists, ask Suzan to close it.
2. **Work out what needs publishing.** For each `Active` row (skip Retired), check two things. Dates only; do not compare contents.
   - **Local changed?** There is a newer dated version of the file in the local folder, or the local file's modified date and time is later than the one in the list.
   - **SharePoint changed?** The SharePoint file's modified time is later than the one in the list, so someone else edited it since the last publish.
   Then:
   - Neither changed: up to date.
   - Local changed, SharePoint did not: needs publishing.
   - SharePoint changed, local did not: nothing to publish. Offer to copy the SharePoint version into the local folder as a new dated version (today's date), so the next edit starts from it.
   - Both changed: do not overwrite. Open both, find what the other person added (notes, answered questions, edits) and put it into the newest local version as a new dated file. Name the person if the file's properties show them. Show the merged changes in the proposal and publish the merged version.
   - A file never published, or with a missing local or SharePoint file, goes in the proposal as such.
3. **Propose in one short message:** each file that needs publishing (fixed name, which dated version), each file edited in SharePoint with what changed and what I will do, the up-to-date files in one line, and any file that is missing or open. Say that old versions stay in SharePoint version history. Suzan's plain "yes" covers it.
4. **On "yes":**
   - Copy the old SharePoint file to the scratchpad first.
   - Copy each local file to `<SharePoint folder>/<fixed name>` and check with `cmp` that the copy is identical.
   - Update the row: local path, `Last published` (today, yyyy-mm-dd), the local file's modified date and time, and the SharePoint file's new modified date and time. The list is the only place this is recorded.
5. **Reply in two lines:** what was published, and anything skipped. Remind her once, if she has not confirmed it, to check that version history is on for the library.

## Rules

- Never rename, move or delete anything in a listed SharePoint folder other than overwriting a listed file with its new version.
- Do not publish drafts or files Suzan has not put on the list.
- Names in the SharePoint folder have no dates. Dated copies stay in Accounting-MyNotes.
- Do not mention Claude, AI or the tools used in any file or in the list.
- Dates are yyyy-mm-dd.
