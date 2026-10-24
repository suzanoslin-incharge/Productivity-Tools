---
name: map-swimlane-builder
description: Turn a scoped process (often a SIPOC's output) into a swim-lane diagram Lucidchart can actually render — as a CSV import file (default, reliable), an AI-generation prompt (fallback, has known limitations), or via the Lucid MCP server if connected. Use when someone asks for a swimlane/cross-functional flowchart, wants to visualize handoffs between roles/teams/systems, or asks to get a process into Lucidchart.
---

# Swim-lane Builder

Produces a swim-lane (cross-functional flowchart) diagram of a process,
targeted at Lucidchart. This skill is downstream of `map-sipoc-builder`: a
SIPOC scopes the process and names the suppliers/customers; this skill takes
that scope and produces the detailed, lane-by-lane flow.

This skill is general-purpose — usable for any department's process. If the
process involves company-specific roles or systems you don't recognize, ask
rather than guess. A department may maintain its own glossary in its own
tools repo (e.g. `accounting-tools`) — check there if relevant, but
don't assume it exists for every team.

Two references, kept separate on purpose:
- `references/swimlane-process-map.md` — the method: what a swim-lane map is,
  when to use it, how to build and validate one, pitfalls. Tool-agnostic.
- `references/lucidchart-integration.md` — the output mechanics for Lucidchart.

Read `references/lucidchart-integration.md` before producing output — it
has the exact CSV column format, the MCP setup, and a real limitation of
Lucid's AI prompt feature that changes which output format you should
default to. **Do not skip this** — the naive approach (just writing a
natural-language prompt) is the least reliable of the three options and is
known to silently drop lane instructions.

## What "background" to expect

If the person doesn't hand you a SIPOC or a clear list of who does what,
ask for or reconstruct:
1. The process name and its start/end trigger.
2. The lanes: every person, team, or system that performs a step. (If a
   SIPOC exists, its Supplier and Customer columns are the starting list —
   see `map-sipoc-builder`'s guide for that conversion rule.)
3. The ordered steps, each assigned to exactly one lane.
4. Where handoffs, decisions, waits, and loops happen — these are the
   points worth calling out explicitly, since they're usually where the
   process actually breaks down.

## What to produce

**Default: a Lucid-ready CSV** per `references/lucidchart-integration.md`
§1 — one row per step, correct `Contained By` swim-lane syntax, ready for
Import Data in Lucidchart. This is the reliable path for anything where
lane correctness matters (i.e., basically everything this skill is used
for).

**If shapes and lines should be colored by label in Lucid**, add the label
columns in `references/lucidchart-integration.md` §4: `ShapeType` (Start, Final, Manual, Automated, Manual Review, System Decision) and `Status` (Confirmed, Unconfirmed, TBD)
on the shapes, `Line ID` and `LineType` on the arrows in the master workbook.
Use the CSV rules (§4.3) now; the XLSX live-link rules (§4.4) apply only if
the account moves to Enterprise. The columns add to the master table; they do
not change step IDs, lanes, arrows or the section 1 CSV layout. Ask which
labels to use if Suzan has not said, and mark the approach as untested until
she has tried a small file.

**If the Lucid MCP server is connected** (check for an MCP tool whose name
suggests Lucid), prefer generating/editing the document directly per
§2 over handing back a file.

**Only if asked for a prompt specifically, or CSV import isn't practical**:
produce an AI-generation prompt per §3, and explicitly include the
instruction to use the BPMN shape library with pools/lanes — a prompt that
just names lanes without that instruction is likely to be rendered as a
flat flowchart, per Lucid's own documented limitation.

Always also give a markdown table sketch of the lanes and steps in the
response itself (like the worked example in `map-sipoc-builder`'s reference
guide) — it's the fastest way for a person to sanity-check the flow before
importing anything into Lucidchart.

## What this skill does not do

- It does not invent lanes, owners, or steps that weren't given or sourced.
  Mark unknowns `TBD` rather than guessing at a company process.
- It does not silently pick the AI-prompt path when CSV import is
  practical — that trades reliability for convenience.
- It does not assume the Lucid MCP server is connected or approved for the
  account — check, don't assume.

**Open questions and follow-ups (Suzan, 2026-10-20).** The swim-lane master does not keep its own sheets for them. They live in the SIPOC workbook for the same process (see `map-sipoc-builder`) and in the trackers.

**Keep the workbook lean (Suzan, 2026-10-15).** Do not add a "What changed" sheet or a "Change" column to a SIPOC or a swim-lane master. Do not track versions inside the file; a new dated file is enough. Be complete and accurate, but record only the current state.

**File names (Suzan, 2026-10-22).** Name each file with the workflow first, then the document type, then the date last, so related files sort together: `<Workflow>_SIPOC_<yyyy-mm-dd>.xlsx`, `<Workflow>_Swimlane-Master_<yyyy-mm-dd>.xlsx` and `<Workflow>_Lucid-Import_<yyyy-mm-dd>.csv`. Short hyphenated workflow names, no prefix the folder already gives. Published names on SharePoint are the same without the date. Move older versions into an `_archive` subfolder. Full rules are in `$ACCT_MYNOTES/CLAUDE.md`.

**One CSV only (Suzan, 2026-10-22).** Always produce the labeled CSV (ShapeType and Status columns, section 4.3) and no unlabeled copy. Do not put "with-labels" in the file name.
