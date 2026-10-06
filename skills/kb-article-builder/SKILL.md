---
name: kb-article-builder
description: Take one uploaded file (.md, .txt, .docx, .xlsx, .pptx, .pdf - meeting notes, transcripts, process documents, spreadsheets, emails) and work out where it belongs in the InCharge knowledge base, what it should be called, and whether it creates a new article or updates an existing one. Proposes everything first and writes nothing until the user approves. Use when someone hands over a file and wants it filed, titled, tagged with KB metadata, or merged into the knowledge base.
---

# KB Article Builder

Input: one file. Output: a filing proposal the user approves, then the
approved writes into the knowledge base (`$KB_ROOT`). **Nothing is created,
edited, moved or renamed before the user approves.**

References (read when needed, not all at once):
- `references/metadata-standard.md`: the eight fields, rules, controlled values.
- `references/filename-standard.md`: no spaces; hyphens within a phrase, underscores between elements, ISO dates last.
- `references/InCharge_Meeting_to_Knowledge_Base_Standard.md`: the full SOP.
- In the KB: `_Taxonomy.md`, `_README.md`, `_Templates/`.

## The knowledge base

`$KB_ROOT` (falls back to `$ACCT_MYNOTES/_KB`; stop and tell the user if neither exists).

```text
01_Sources/KB-Only/Source-Name_YYYY-MM-DD/   content whose home is the KB; original kept
01_Sources/Linked/Source-Name_YYYY-MM-DD/    documents that live on SharePoint/OneDrive; metadata and link only
02_Knowledge-Articles/<Business-Function>/<Process-Area>/System_Topic.md
02_Knowledge-Articles/_Superseded-Archived/
03_Decision-Log/Decision-Log.md
_Templates/   _Taxonomy.md   _README.md
```

Articles are organized by topic or process, never by meeting: move the source's wording into the template sections (Current State, Business Rules, Open Questions, ...) without inventing content.

## Mode: KB-only or linked

Every file is handled in one of two modes. The mode is not stored as a field: it is the source folder's location, `01_Sources/KB-Only/` or `01_Sources/Linked/`.

- **KB-only.** The KB is the home of this content (emails, meeting notes, handwritten notes, anything with no other home). The original is copied into `01_Sources/KB-Only/<source folder>/` and the article is the readable version.
- **Linked.** The original lives on SharePoint or OneDrive and must stay readable there (a workbook, policy, SOP). The original is never moved, copied or edited. Its source folder goes in `01_Sources/Linked/`. The KB gets an article with the knowledge extracted from it, and the source folder records the link and dates so `kb-update-linked-docs` can refresh it later.

**How the mode is set:**
1. The user says it ("linked", "KB only"): use that.
2. The file was attached with the + button (it arrives as an attachment in the message): **KB-only**, no question.
3. Anything else (a typed or pasted path, a link, or nothing said): **ask** before proposing. Do not infer the mode from file type or location. If you cannot tell whether a file was attached or only mentioned by path, ask.

## Steps

1. **Ingest.** Read the whole file as text.
   - `.md` / `.txt`: read directly.
   - `.docx`: convert to markdown with `pandoc` or `python-docx` if installed; otherwise use the `docx` skill (or read `word/document.xml` from the zip). Keep headings, lists and tables.
   - `.xlsx`: read with `openpyxl`. Summarize per sheet (name, purpose, headers, row counts, notable values); do not dump whole sheets.
   - `.pptx`: convert with `pandoc` for text in reading order. Use `python-pptx` for tables, speaker notes and a per-slide count of pictures. A slide with several pictures and little text probably carries its meaning in a diagram: flag it, render it to an image (the `pptx` skill can help) and read the image, or ask the user. Do not treat extracted text alone as the whole slide.
   - `.pdf`: use the `pdf` skill.
   - The original file is never modified.
2. **Classify the source.** Source-Type: `Meeting`, `Email`, `Handwritten-Notes`, or `Document`. Decide the action: **new article**, **update existing article**, **reference stub**, or **skip** (not knowledge, or personal data such as bank statements). Also decide the **mode** (see above). A linked document the user does not want extracted becomes a reference stub: link, owner and a fuller-than-usual description only.
3. **Pick the category.** Read `_Taxonomy.md` only. Choose the most specific existing row. If no row fits, go to "When nothing fits" below.
4. **Check for an existing article.** Look in the category folder first, then search `02_Knowledge-Articles` by system and topic. If the file covers the same topic, the action is **update**.
   - Compare statement by statement. For each fact the new file changes (a location, owner, system, date, step order, rule), record the existing line and the new one.
   - **The new fact replaces the old one.** Do not leave both in the article.
   - If the difference is softer (a reworded or reordered description, or it is unclear which version is current), do not guess: list it as a question for the user.
5. **Title and filename.** Title = system or product name plus the process or topic; not a generic meeting title and not the old filename. Filename = `System_Topic.md` from that title, per the filename standard. Source folder = `Source-Name_YYYY-MM-DD`.
6. **Metadata.** Generate the eight fields in order: Title, Category, Document Type, Keywords, Status, Primary Process Contact, Related Teams, Short Description. Use only what the file supports; never guess contacts or teams. If the file already carries a metadata block, keep every value it states, standardize the format (bulleted list, exact field names, controlled values, plain hyphen in Status), and flag any value that does not match the controlled lists. Expand a first-name-only contact to a full name only when the department directory (`org-glossary.md`) has exactly one match whose role fits; otherwise keep the name as written and record it as unconfirmed. List any unclear field in the proposal with a short question and, where reasonable, a suggested value. Write `Needs confirmation` only if the user declines to answer.
7. **Check the open questions.** Read the "Open" sheet of `$ACCT_MYNOTES/OPEN_QUESTIONS.xlsx` (the `Question` and `Context` columns; leave out questions this same file just raised). Find the questions the file answers and the ones it only informs. For each, keep the passage that supports it (a short quote, with the timestamp for a transcript). Sort each into: **answers it fully**, **answers it partly** (say what is still open), **informs it** (relevant, not an answer), or **conflicts** with the question's context or with an article. Never infer an answer the file does not state, and do not match on a shared keyword alone. Work from the question text and its context, not from memory of the file. Do this even when the action is "new article" or "reference stub". Hand-off and recording are described in `../kb-answer-open-questions/SKILL.md` (sections 3 and 4).
8. **Present one proposal and wait.** See "The proposal". Do not write anything yet.
9. **On approval, write exactly what was approved** (see "Writes"). If the user edits the proposal, apply the edits and show the changed items again before writing.
10. **Reply briefly:** what was written and where, the metadata, which open questions were answered, and anything still `Needs confirmation`.

## When nothing fits

The taxonomy is additive only. Never rename, split, merge or retire an existing row. If no row is a valid match:

1. Read `$TOOLS_PRODCTVTY/shared-knowledge/org-glossary.md` (department names and lines of business, for the Business Function) and `$TOOLS_PRODCTVTY/shared-knowledge/systems-landscape.md` (exact system names, for the Process Area). Read them only now, not on normal runs.
2. Add a **new-row proposal** to the proposal: the Category text, the folder name, the glossary or landscape entries it is based on, and the files that would go under it.
3. If approved, append the row to `_Taxonomy.md` with a change-history line (marked Proposed until the user approves it as a standing row) and use it. If declined, file the article with `Category: Proposed: <category>` and flag it.

## The proposal

One message, in this order:

1. **File:** name, type, Source-Type.
2. **Mode and action:** KB-only or linked (this decides the source subfolder), and new article / update existing / reference stub / skip, and why.
3. **Where:** full path of the article, and of the source folder.
4. **Name:** the title and filename.
5. **Taxonomy:** the row used, or a new-row proposal.
6. **Changes (updates only):** a before/after list: existing statement, new statement, for each changed fact. Then the questions about softer differences.
7. **Metadata:** the eight fields.
8. **Open questions this file may answer:** one table with the ID, the question, the fit (fully, partly, informs, conflicts), the supporting passage, who said it and when, and what would change (the article statement, the Change Log line, the workbook row). Say "none found" if there are none. Partly answered and informing ones stay open; they get a short note added to the question's Context cell only if the user approves.
9. **Unsure:** every field or decision you could not settle, with a question each.

End by asking the user to approve, edit or reject.

## Writes

Only after approval:

- **Source folder, KB-only.** Create `01_Sources/KB-Only/Source-Name_YYYY-MM-DD/` with `Source-Metadata.md` (from the template) and the original file, unchanged, renamed to the filename standard (e.g. `Meeting-Notes_YYYY-MM-DD.docx`). A meeting recording is moved into the folder with the notes, not copied.
- **Source folder, linked.** Create `01_Sources/Linked/Source-Name_YYYY-MM-DD/` with `Source-Metadata.md` only: the SharePoint or OneDrive link, owner, original file name, the connector's item ID, who the link opens for (owner only, people in InCharge, or site members), the original's last-modified date, and the date retrieved. No copy of the file and never a local path. Get the link from the user, or look it up with the Microsoft 365 connector. The article ends with a **Source document** section repeating the link and dates and stating that the original is the record: if the two disagree, the original governs.
- **Mark a linked file as catalogued.** For every linked source: (1) add a row to `$KB_ROOT/_Linked-Catalog.md` (original file, a link to it (the SharePoint or OneDrive address, even if it opens only for the owner for now), location, article links, source folder link, catalogued date, original last modified, last checked); (2) put the Finder tag `In KB` on the local copy of the original, which changes neither its contents nor its modified date: `xattr -wx com.apple.metadata:_kMDItemUserTags "$(python3 -c "import plistlib;print(plistlib.dumps(['In KB'],fmt=plistlib.FMT_BINARY).hex())")" "<file>"`. The tag is local to this Mac. Do not edit the original itself; an in-file pointer waits until the KB is published somewhere others can open. If a linked source gains another article later, add it to the same catalog row.
- **Answered questions.** Record only the matches the user approved, following `../kb-answer-open-questions/SKILL.md` section 4: put the answer in the right section of the affected article (labeled as answered by the named person on the date, and not in the original document, for linked articles), remove it from that article's Open Questions section, set `Last updated`, add a Change Log line that names the question ID, who said it and the source, move the workbook row from "Open" to "Answered" (`Done` = `Yes`, `Answered by`, the answer), and archive the previous version of an article before replacing a statement. A new fact from this file that contradicts an existing article is a normal "Changes" item (step 4), not a question answer.
- **Open questions.** Add every open question from the article's Open Questions section as a new row below the last one in `$ACCT_MYNOTES/OPEN_QUESTIONS.xlsx` (sheet "Open", Excel table `OpenQuestions`), with `openpyxl` or the `xlsx` skill, extending the table range to include it. Columns: `Done` (leave blank; `Yes` when answered), `ID` (the next free `Q###`, across both sheets), `Question` (stands alone, see below), `Context` (see below), who may know (a suggested person from the article or the department directory; leave empty if unclear), `Related notes` (the article title, plain text), `Link` (a clickable local file link to the article, `file:///Users/suzanoslin/Library/CloudStorage/OneDrive-InChargeService/Accounting-MyNotes/` plus the article's path with spaces encoded; SharePoint links are for after migration, see the README), raised (the date, as a real date, `yyyy-mm-dd`), answer (blank). Keep the existing formatting and never rewrite or reorder other rows. Write every question so it stands alone, in the article's Open Questions section and in the workbook: name the system or process, say what the source states and what is unknown, one or two sentences ending with a question mark, never relying on the surrounding text ("The note says 'lots to be worked out'" is not a question). Put the background in the `Context` column (the workbook only; plain text, 2 to 4 sentences): what my notes say today, where the gap or conflict is, and where it came from (the meeting and date, or an email), and why it matters only when that is supported. Wording: write like a colleague talking to a colleague, in plain everyday words, for people who have not read Suzan's notes (the workbook is shared and is copied into process documents such as a SIPOC). Never write "the article", "the KB", "the source" or "per"; say "my notes" for Suzan's write-up and "the meeting notes" (or name the meeting) for a meeting. Emails can be named normally ("in Priya's email of 2026-09-29"). Do not end a Context with a stock phrase such as "From the 2026-10-05 session" and do not use the label "Why it matters:"; say it in a sentence ("This matters because ..."). Spell out an acronym the first time it appears in each cell. Do not invent context; if you cannot tell what the question refers to, ask the user while building the proposal. Skip bullets that only say a name is a first name or unconfirmed. When a question is answered later, use the `kb-answer-open-questions` skill. Include the additions in the proposal like any other write.
- **Action items.** Meeting administration (follow-ups, scheduling, tasks) does not go in the article. Append each action item to `$ACCT_MYNOTES/FOLLOWUP_ITEMS.xlsx` (sheet "Follow-up items", Excel table `FollowUps`) as a new row below the last one, with `openpyxl` or the `xlsx` skill, and extend the table range to include it. Columns: `Done` (leave blank; `Yes` when finished), action item, owner, date made (the meeting date, as a real date, `yyyy-mm-dd`), meeting title. Keep the existing formatting and never rewrite or reorder other rows. Include them in the proposal for approval like any other write.
- **New article.** Create it from `_Templates/Article-Template.md` in the category folder: title, metadata list, then the content organized under the template sections. Do not invent content; sections with nothing in the source say so or are omitted. Set `Last updated` and add the first Change Log line.
- **Update.** First copy the current article to `_Superseded-Archived/<filename>_<today>.md`. Then edit the article: replace each approved stale statement, update `Last updated`, add a Change Log line naming the change and the source, and fix metadata that changed (for example Keywords or Short Description).
- **Reference stub.** From `_Templates/Reference-Stub-Template.md`: Document Type `Reference`, the link (a SharePoint or OneDrive sharing link, never a local path), owner, retrieved date, and a fuller-than-usual Short Description. No copy of the document.
- **Links.** Relative links both ways (the source folder's subfolder, `KB-Only` or `Linked`, is part of the path): the article's Sources section to the source folder, and the source's metadata back to the article.
- **Decision Log.** Only if the source clearly records a decision (not a recommendation or action item), and only as an approved item in the proposal.

## Output layout

```markdown
# <new title>

- **Title:** ...
- **Category:** ...
- **Document Type:** ...
- **Keywords:** ...
- **Status:** ...
- **Primary Process Contact:** ...
- **Related Teams:** ...
- **Short Description:** ...

**Last updated:** YYYY-MM-DD

## Purpose
...
```

The metadata is a plain bulleted list directly under the title, not `---`
front matter, so it renders the same in any KB or markdown viewer.

Status for unvalidated process-discovery content: `Draft - Process Discovery`.
