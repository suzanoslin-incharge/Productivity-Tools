---
name: kb-update-linked-docs
description: Check every linked document in the InCharge knowledge base against its original on SharePoint or OneDrive; where a newer version exists, find what knowledge changed and propose updates to the affected articles. Use when the user asks to refresh, sync, or check linked documents, or to bring the KB up to date with its originals.
---

# Update Linked Documents

Keeps the knowledge base current for **linked** sources: documents that live
on SharePoint or OneDrive and were extracted into KB articles by
`kb-article-builder`. KB-only sources (the `01_Sources/KB-Only/` folder) are ignored.

**Read-only until the user approves.** Originals are never modified, and
nothing in the KB changes before approval.

KB layout and the article/source formats are defined in
`../kb-article-builder/SKILL.md` and the KB's `_README.md`. Use `$KB_ROOT`
(falls back to `$ACCT_MYNOTES/_KB`).

## Steps

1. **Inventory.** Read every `01_Sources/Linked/*/Source-Metadata.md`
   (the `KB-Only` folder is never checked). If the user named a source or category, limit to it.
   For each, note its link, the recorded `Original last modified`, and the
   article it produced.
2. **Check dates.** For each linked source, look up the original by its
   recorded `Item ID` using the Microsoft 365 connector and read its current
   last-modified date and address. Compare with the recorded date.
   - **Not found by ID (moved or re-created).** Search SharePoint by the
     recorded `Original file name`, narrowed by any location the user gave
     ("I moved everything to the Accounting-Internal site"). Compare the
     candidate's content with the article. Present the candidate as a
     proposed match; never adopt one without the user's confirmation. If one
     moved location is confirmed, use it as the hint for the other sources.
   - **Still not found:** mark `deleted or no access` or `could not check` and
     ask the user for the file. Never guess, and never use a local path.
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
     `Retrieved`, and, if the document moved, `Link`, `Item ID`, `Link visibility`
     and `Where the original lives`; also the article's **Source document**
     section and the document's row in `_Linked-Catalog.md` (Link and Location), and add
     a Change Log line noting the link change. Tell the user to reapply the
     `In KB` Finder tag to the moved file.
   - if the original was deleted or replaced by a different document,
     propose a Status change (`Superseded` or `Archived`) rather than editing content
7. **Report.** Counts (checked, unchanged, updated, skipped, could not
   check), which articles changed, and anything left open.

Unchanged documents are left alone: no edits to articles or sources. After a run, update `Last checked` in `$KB_ROOT/_Linked-Catalog.md` for every document checked, and `Original last modified` for those updated (that catalog edit is bookkeeping and is reported, not proposed).

**Coverage check (on request).** When the user asks what is not catalogued yet, list files in the named `Accounting-MyNotes` folder that have no `In KB` Finder tag and no row in `_Linked-Catalog.md`, ignoring names that start with `_`.
