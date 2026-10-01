---
name: update-linked-documents
description: Check every linked document in the InCharge knowledge base against its original on SharePoint or OneDrive; where a newer version exists, find what knowledge changed and propose updates to the affected articles. Use when the user asks to refresh, sync, or check linked documents, or to bring the KB up to date with its originals.
---

# Update Linked Documents

Keeps the knowledge base current for **linked** sources: documents that live
on SharePoint or OneDrive and were extracted into KB articles by
`kb-article-builder`. KB-only sources (emails, meeting notes) are ignored.

**Read-only until the user approves.** Originals are never modified, and
nothing in the KB changes before approval.

KB layout and the article/source formats are defined in
`../kb-article-builder/SKILL.md` and the KB's `_README.md`. Use `$KB_ROOT`
(falls back to `$ACCT_MYNOTES/_KB`).

## Steps

1. **Inventory.** Read every `01_Sources/*/Source-Metadata.md`. Keep those
   with `Mode: Linked`. If the user named a source or category, limit to it.
   For each, note its link, the recorded `Original last modified`, and the
   article it produced.
2. **Check dates.** For each linked source, get the original's current
   last-modified date from its link using the Microsoft 365 connector
   (SharePoint search or read). Compare with the recorded date. If the
   connector cannot reach the link, mark it `could not check` and ask the user
   for the file. Never guess, and never use a local path (none is stored).
3. **Report, then ask.** Show one table: source, article, recorded date,
   current date, status (`unchanged`, `changed`, `moved`, `deleted or no
   access`, `could not check`). Ask which changed documents to process
   (default: all `changed`). Nothing is written yet.
4. **Find the new knowledge.** For each chosen document, fetch the current
   content to the scratchpad (not into the KB) and convert it with the
   kb-article-builder ingest rules (pandoc for `.docx`, `openpyxl` for
   `.xlsx`, the pdf skill for `.pdf`). Compare it with the existing article
   statement by statement:
   - **Changed facts** (a location, owner, system, date, step order, rule):
     existing line and new line. The new fact replaces the old one.
   - **New knowledge** not yet in the article.
   - **Removed content:** things the article states that the new version no
     longer supports. Flag them; do not delete without approval.
   - **Softer differences** (reworded, reordered, unclear which is current):
     list as questions, do not guess.
   - **Moved:** if only the location changed, the update is the link.
5. **Propose, one document at a time.** Use the "update" proposal format from
   kb-article-builder: article path, new last-modified date, the before/after
   list, the new knowledge, the removals, the questions, and any metadata that
   would change (Keywords, Short Description). Wait for approve, edit or reject.
6. **On approval, write exactly what was approved:**
   - copy the current article to `02_Knowledge-Articles/_Superseded-Archived/<filename>_<today>.md`
   - edit the article: replace approved facts, add approved new knowledge, set
     `Last updated`, add a Change Log line naming the change and the new
     document date
   - update the source's `Source-Metadata.md`: `Original last modified`,
     `Retrieved`, and `Link` if the document moved
   - if the original was deleted or replaced by a different document,
     propose a Status change (`Superseded` or `Archived`) rather than editing content
7. **Report.** Counts (checked, unchanged, updated, skipped, could not
   check), which articles changed, and anything left open.

Unchanged documents are left alone: no edits, no date updates.
