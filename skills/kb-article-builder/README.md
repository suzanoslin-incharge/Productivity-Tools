# kb-article-builder

Part of the InCharge Meeting-to-Knowledge-Base effort. Status: **the three KB skills are built and have been followed by hand on about 20 real sources (2026-10-01); not yet exercised as installed skills. Later pipeline phases not started.**

## The KB skills

| Skill | Use it to |
| --- | --- |
| `kb-article-builder` (this skill) | Turn one file into a KB article: classify it, pick the category, name it, tag it with metadata, create or update the article. Writes nothing until you approve |
| `kb-update-linked-docs` | Check every **linked** document against its original on SharePoint/OneDrive, find what changed, and propose article updates. Also re-finds files that moved |
| `kb-answer-open-questions` | Work through `$ACCT_MYNOTES/OPEN_QUESTIONS.md`: list questions by who is likely to know, and record an answer (updating the articles) |

The mapping skills (`map-sipoc-builder`, `map-swimlane-builder`) are separate.

## What kb-article-builder does

Hand it one file (`.md`, `.txt`, `.docx`, `.xlsx`, `.pptx`, `.pdf`) or an email thread and it:

- converts the file to text
- asks (unless you said, or attached the file with the + button) whether it is **KB-only** (original copied into `01_Sources/KB-Only/`) or **linked** (original stays on SharePoint/OneDrive; `01_Sources/Linked/` holds the link and dates)
- classifies it (Meeting, Email, Handwritten-Notes, Document) and decides: new article, update an existing article, reference stub, or skip
- picks the category from the KB's `_Taxonomy.md`; if nothing fits, proposes a **new row** (additive only; reads the org glossary and systems landscape only then)
- names it per the filename standard, and generates the eight-field metadata
- when it updates an article, replaces stale facts with the new ones (e.g. a new report path replaces the old one), logs the change, and archives the prior version
- for linked files: adds a row to `_Linked-Catalog.md` and puts the Finder tag `In KB` on the original
- adds the article's open questions to `OPEN_QUESTIONS.md` and its action items to `FOLLOWUP_ITEMS.md`
- presents one proposal and **writes nothing until you approve**

Files go to `$KB_ROOT` (`Accounting-MyNotes/_KB`): `01_Sources/KB-Only`,
`01_Sources/Linked`, `02_Knowledge-Articles/<Business-Function>/<Process-Area>`,
`03_Decision-Log`. This covers SOP Steps 2, 7, 8 and 10 in a first form.

## Reference files

| File | Use |
|---|---|
| `references/metadata-standard.md` | Quick metadata rules and controlled values |
| `references/filename-standard.md` | Filename rules for everything in the KB |
| `references/InCharge_Meeting_to_Knowledge_Base_Standard.md` | The complete SOP (Parts 1 and 2), verbatim. Source of truth for the later pipeline |

## Migration status

**Complete (2026-10-01).** `Procure_to_Pay`, `Upstream`, `Record-to-Report` and `Order-to-Cash` are catalogued (files starting with an underscore were excluded by design).

## What is left to do

**Near term**
- [ ] Run each KB skill as an installed skill (so far the steps were followed by hand) and adjust what does not work
- [ ] Work through `OPEN_QUESTIONS.md` with `kb-answer-open-questions`
- [ ] Add an email-intake step to `kb-article-builder` (find the thread through the Outlook connector, confirm it with you, save the text and attachments to a source folder; tagging and moving the email stays manual because the connector cannot do it)
- [x] `.docx` conversion: pandoc 3.11 installed (2026-10-01); docx skill is the fallback
- [ ] Commit and add to the plugin release

**Later pipeline (needs design)**
- [ ] Step 1: triage whether a meeting is worth processing
- [ ] Steps 3-6: extract, verify against the transcript, separate knowledge from administration
- [ ] Step 9: Decision Log updates
- [ ] Step 11: validation request to the process contact
- [ ] Step 12: cross-link, version, publish to SharePoint

## Done

- [x] `_KB` structure, templates, filename standard, `KB_ROOT`
- [x] `$ACCT_MYNOTES/OPEN_QUESTIONS.md` gathers every article's open questions in one place (2026-10-01)
- [x] `_Linked-Catalog.md` plus `In KB` Finder tag mark catalogued linked files (2026-10-01)
- [x] Taxonomy seeded (nine rows) and approved 2026-10-01; grows by approved additions only

## Moving everything to SharePoint

Today the KB (`_KB`) and the linked originals both sit in Suzan Oslin's
personal OneDrive, so links to the originals open only for her. This section
records what to do, and what must change, when everything moves to SharePoint.
There are two separate moves. Do them in this order.

### Before either move: decide

- [ ] The shared site and library for the **originals** (for example the Accounting-Internal site)
- [ ] The site and library for the **KB**
- [ ] **One library with the three folders** (`01_Sources`, `02_Knowledge-Articles`, `03_Decision-Log`) is recommended. If the SOP's three libraries are used instead, every relative link between them breaks and must be rewritten as a URL.
- [ ] Who gets edit rights (KB owners) and who gets read access (everyone)
- [ ] Whether `FOLLOWUP_ITEMS.md` (now in `Accounting-MyNotes`, outside `_KB`) stays personal or moves to the shared site

### Move 1: the linked originals (do first; links must be right before publishing)

Why first: the personal OneDrive can be removed when the contractor account
ends, which would break every link.

1. Move the originals into the shared site (SharePoint "Move to", or move them in the synced folder). Keep their file names. Moving to a different site gives each file a **new item ID**, so the old IDs stop working.
2. Run `kb-update-linked-docs` and tell it where the files went ("I moved everything to the Accounting-Internal site"). It finds each file by name, shows you the match, and after you confirm updates the new link, item ID and link visibility.
3. What has to be updated for each moved original. The skill does the first three; check them:
   - `01_Sources/Linked/<source>/Source-Metadata.md`: **Link**, **Item ID**, **Link visibility** (now "Site members" or similar, no longer "Owner only"), **Where the original lives**, **Owner** (a real owner, not the OneDrive account)
   - the article's **Source document** section (the link and the line "opens for the owner only")
   - `_Linked-Catalog.md`: **Link**, **Location**, **Original last modified**, **Last checked**
   - the Finder tag `In KB`: it lives on the local copy, so reapply it to the new synced location (the `xattr` command is in `SKILL.md`)
   - a Change Log line in each article noting the link change (this is not a content update)
4. Check: open each link from a second account that is not the file's owner.

Currently catalogued (6): the five Procure_to_Pay originals and
`Order-to-Cash_Assessment-Executive-Summary.pptx` (item IDs pending for the
training document and the deck).

### Move 2: the KB itself

1. Copy the whole `_KB` tree to the library **intact**: same folder names, same structure, no renames. All relative links keep working because they are relative. File names already have no spaces, which keeps SharePoint URLs clean.
2. Sync the library locally, then point the tools at it:
   - set `KB_ROOT` in `~/.zshrc` to the synced folder
   - update the fallback `$ACCT_MYNOTES/_KB` named in `SKILL.md` and in `_KB/_README.md` (it will no longer be the home)
   - update the README's mentions of staging in `_KB/_README.md` ("Staging area ... until the site is chosen")
3. Run a relative-link check over every `.md` file in the new location and confirm nothing is broken.
4. Retire the old copy (rename it `_KB-OLD` or archive it) once the new one is verified, so there are not two live copies.
5. Apply the same `In KB` Finder-tag convention going forward; nothing else about the skills changes.

What does **not** need to change: the filename standard, templates, taxonomy,
article content, and the glossary and landscape (they live in the
productivity-tools repo, not in the KB).

### After both moves

- **Cross-link from the original back to the KB.** Now possible, since an article has a real shared URL. Add a document property or a visible line in each original ("Catalogued in KB: <article URL>"). This edits the file and changes its modified date, so record the new date in `Source-Metadata.md` and `_Linked-Catalog.md` right after, so the update checker does not count it as a change.
- **Other documents** that refer to an article should link to its SharePoint URL, not a relative path.
- **SharePoint metadata columns.** The eight metadata fields live in each article's body today. To filter and search by them in SharePoint, add them as library columns and fill them from the article metadata. Copilot reads the article text either way.
- **Permissions and review.** Confirm the review owner and who may change Status (open items in `_KB/_README.md`).

## Open decisions (the SOP doesn't answer these)

- Category taxonomy: seeded and approved; new rows are added case by case
- SharePoint locations for 01 Meeting Sources, 02 Knowledge Articles, 03 Decision Log
- Which system holds action items
- Where the Primary Process Contact and review owner come from
- Whether to publish to SharePoint directly (Microsoft 365 connector is available) or hand off files for manual upload
