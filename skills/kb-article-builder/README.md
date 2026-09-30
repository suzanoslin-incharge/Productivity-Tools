# kb-article-builder

Part of the InCharge Meeting-to-Knowledge-Base effort. Status: **Phase 1 built; full pipeline not started.**

## What exists today (Phase 1)

A single skill (`SKILL.md`). Hand it a text file and it returns a
knowledge-base-ready file:

- a new title based on what the content is about
- the standard eight-field metadata block (Title, Category, Document Type, Keywords, Status, Primary Process Contact, Related Teams, Short Description)
- the original content, unchanged

It writes a new file named after the new title and leaves the original alone.
Unsupported metadata values become `Needs confirmation`; nothing is guessed.
This corresponds to **Step 10** of the SOP only.

It has not yet been tested on real meeting files.

## Reference files

| File | Use |
|---|---|
| `references/metadata-standard.md` | Quick metadata rules and controlled values; used by the skill today |
| `references/InCharge_Meeting_to_Knowledge_Base_Standard.md` | The complete SOP (Parts 1 and 2), verbatim. Source of truth for the later pipeline |

## What is left to do

SOP step numbers refer to Part 1 of the full SOP.

**Near term**
- [ ] Test Phase 1 on 2–3 real meeting files and adjust the title and metadata behavior
- [ ] Decide: should it ever overwrite the original file instead of writing a new one?
- [ ] Get the real category taxonomy (until then categories are `Proposed:`)
- [ ] Commit and add to the plugin release

**Full pipeline (later; needs design and your review of the SOP)**
- [ ] Step 1: decide if a meeting is worth processing
- [ ] Step 2: build the meeting source package (dated folder, AI summary, Loop notes, transcript, links, meeting metadata)
- [ ] Steps 3–6: extract from the AI summary and Loop notes, verify against the transcript, and separate knowledge from meeting administration
- [ ] Steps 7–8: choose article type and topic, split by topic, and draft the article in the standard structure
- [ ] Step 9: create or update the Decision Log
- [ ] Step 11: validation with the process contact
- [ ] Step 12: publish, cross-link, and maintain (version, last-reviewed date, review owner)

Likely shape: a skill per bounded step, plus agents for the multi-step,
multi-file work (source package, batch processing, Decision Log updates).
Decide this after reviewing the SOP.

## Open decisions (the SOP doesn't answer these)

- Category taxonomy (Business Function > Process Area values)
- SharePoint locations for 01 Meeting Sources, 02 Knowledge Articles, 03 Decision Log
- Which system holds action items
- Where the Primary Process Contact and review owner come from
- Whether to publish to SharePoint directly (Microsoft 365 connector is available) or hand off files for manual upload
