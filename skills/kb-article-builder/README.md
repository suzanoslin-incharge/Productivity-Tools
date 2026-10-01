# kb-article-builder

Part of the InCharge Meeting-to-Knowledge-Base effort. Status: **intake skill rewritten (2026-10-01); untested on real files. Later pipeline phases not started.**

## What exists today

A single skill (`SKILL.md`). Hand it one file (`.md`, `.txt`, `.docx`,
`.xlsx`, `.pdf`) and it:

- converts the file to text
- classifies it (Meeting, Email, Handwritten-Notes, Document) and decides: new article, update an existing article, reference stub, or skip
- picks the category from the KB's `_Taxonomy.md`; if nothing fits, proposes a **new row** (additive only; reads the org glossary and systems landscape only then)
- names it per the filename standard, and generates the eight-field metadata
- when it updates an article, replaces stale facts with the new ones (e.g. a new report path replaces the old one), logs the change, and archives the prior version
- presents one proposal and **writes nothing until you approve**

Files go to `$KB_ROOT` (`Accounting-MyNotes/_KB`): `01_Sources`,
`02_Knowledge-Articles/<Business-Function>/<Process-Area>`, `03_Decision-Log`.
This covers SOP Steps 2, 7, 8 and 10 in a first form.

## Reference files

| File | Use |
|---|---|
| `references/metadata-standard.md` | Quick metadata rules and controlled values |
| `references/filename-standard.md` | Filename rules for everything in the KB |
| `references/InCharge_Meeting_to_Knowledge_Base_Standard.md` | The complete SOP (Parts 1 and 2), verbatim. Source of truth for the later pipeline |

## What is left to do

**Near term**
- [ ] Test on 2-3 real files (one `.docx`, one `.xlsx`, one update that overrides an existing fact) and adjust
- [x] `.docx` conversion: pandoc 3.11 installed (2026-10-01); docx skill is the fallback
- [ ] Migrate the existing Accounting-MyNotes files into `_KB` (inventory table, approve, then move)
- [ ] Commit and add to the plugin release

**Later pipeline (needs design)**
- [ ] Step 1: triage whether a meeting is worth processing
- [ ] Steps 3-6: extract, verify against the transcript, separate knowledge from administration
- [ ] Step 9: Decision Log updates
- [ ] Step 11: validation request to the process contact
- [ ] Step 12: cross-link, version, publish to SharePoint

## Done

- [x] `_KB` structure, templates, filename standard, `KB_ROOT`
- [x] Taxonomy seeded (nine rows) and approved 2026-10-01; grows by approved additions only

## Open decisions (the SOP doesn't answer these)

- Category taxonomy: seeded and approved; new rows are added case by case
- SharePoint locations for 01 Meeting Sources, 02 Knowledge Articles, 03 Decision Log
- Which system holds action items
- Where the Primary Process Contact and review owner come from
- Whether to publish to SharePoint directly (Microsoft 365 connector is available) or hand off files for manual upload
