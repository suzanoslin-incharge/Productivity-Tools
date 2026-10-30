# Lucidchart Integration Reference

How to get a swim-lane process map from Claude into an actual Lucidchart
diagram. There are three real paths, in order of reliability. **Do not
default to the AI text-prompt path for anything where lane placement
matters** — see the caveat in §3.

Researched 2026-09-29 (section 1 corrected 2026-10-09) from Lucid's own help center, developer docs, GitHub,
and product-team responses in their community forum. Where I couldn't fetch
a page directly (marked below), treat the detail as reasonably sourced but
worth a quick sanity check against the live page before relying on it for
something company-facing.

---

## 1. CSV import (recommended default for swim-lane accuracy)

Lucidchart has a documented **"Create a process diagram from CSV import"**
feature built specifically for this. It places shapes deterministically,
including into named swim lanes, and lays them out itself. It does not leave
placement to an AI's interpretation of a prompt.

**Corrected 2026-10-09.** The first version of this section guessed the
layout from search summaries and was wrong: it produced files that stacked
every shape in one column. The layout below is Lucid's own sample file
(`SalesProcess.csv`, from Lucid's help center) and was confirmed with a
working import and a Visio export.

**Columns (in this order):** `Id, Name, Shape Library, Page ID, Contained By,
Line Source, Line Destination, Source Arrow, Destination Arrow, Text Area 1`
and then `Text Area 2`, `Text Area 3` and so on, as many as there are lanes.
There are no color, size or position columns. Lucid sets those. Color shapes
by hand after the import.

**Rows, in this order:**

| Row | Name | Shape Library | Page ID | Contained By | Other cells |
| --- | --- | --- | --- | --- | --- |
| Page | `Page` | blank | blank | blank | `Text Area 1` = `Page 1` |
| Swim-lane container | `Swim Lane` | `Flowchart Shapes` | `1` | blank | `Text Area 1..n` = **the lane names, one per column, in lane order** |
| Each step | `Process`, `Decision` or `Terminator` | `Flowchart Shapes` | `1` | `<swim lane Id>:<lane number>` | `Text Area 1` = the step text |
| Each arrow | `Line` | blank | `1` | blank | `Line Source` = the step Id, `Line Destination` = the next step Id, `Source Arrow` = `None`, `Destination Arrow` = `Arrow`, `Text Area 1` = the arrow label (can be blank) |

**Lane placement syntax:** `Contained By` is the Id of the Swim Lane row, a
colon, then the **lane number**, counting from 1 in the order the lane names
appear in the Text Area columns. Example: `2:3` is the third lane of the swim
lane whose Id is 2. It is not the lane's name.

**Rules that avoid a broken import (learned 2026-10-08):**

- Give every shape at least one arrow in or out. A file with several
  unconnected note shapes and arrows that loop back to an earlier step failed
  to lay out (shapes piled in one spot, and Lucid's auto-arrange errored).
  Files with only one of the two problems laid out fine. Keep notes in a
  separate sheet or table, not in the diagram, and avoid loops unless needed.
- Do not leave a lane empty. Drop it, or the diagram shows an empty band.
- Keep lane names to about 10 characters or fewer ("Customer", "PayFabric",
  "Accounting"). Longer names are drawn twice in the narrow lane header: this
  happened at 25 characters ("Customer (payer and AP contact)" showed as
  "Customer (payer and AP contact)(payer and AP contact)") and again at 17
  characters ("Accounting and AR"; Suzan, 2026-10-12). Put the full name in a lane
  key (a sheet in the master), not in the lane header.
- Shape and arrow Ids must be unique and contiguous. Arrow rows come after
  all the shape rows.
- Write the file as UTF-8 with CRLF line endings. Excel's "CSV UTF-8"
  save is fine. Plain "CSV" can garble characters.
- Test with a small file first, then the full one, and check lane count, lane
  order, a few steps in their lanes, and all arrow labels.

**Import steps (from Lucid's help center, summarized):**

1. Open or create a **new, blank** document in Lucidchart.
2. Select **Import Data** at the bottom left of the document (or the
   equivalent "Import Data" action in the toolbar).
3. Upload the CSV.
4. Map/verify columns if prompted.
5. Lucid builds the diagram, placing shapes per `Contained By`.

Source: [Lucid Help Center, Create a process diagram from CSV import](https://help.lucid.co/hc/en-us/articles/15927090927508-Create-a-process-diagram-from-CSV-import).
*(This page returned a 403 to automated fetch. The sample layout above comes
from Lucid's own `SalesProcess.csv`, which was imported and laid out
correctly.)*

**What `map-swimlane-builder` should produce for this path:** one CSV in the
layout above, one row per step and one row per arrow, with a master table of
the steps (step ID, lane, step, next step, label, confirmed) kept beside it
so the diagram can be regenerated. Mark unconfirmed steps in the step text
(for example "(?)").

**Visio.** Lucid exports to .vsdx (File, Export, Visio). Visio's Data
Visualizer is decommissioned at InCharge, so it is not an option. Round
trips between Lucid and Visio lose fidelity, so keep the master table as the
source and treat each diagram as an output.

---

## 2. Lucid MCP server (real integration, needs admin approval)

Lucid publishes an official MCP server that connects an AI client — including
Claude — directly to a Lucid account. This is the actual "integration," as
opposed to a copy-paste prompt or file.

**What it can do** (per Lucid's own announcement and GitHub repo):

- Search and retrieve existing Lucid documents by natural-language query.
- Summarize a document's content and pull out action items.
- **Generate a new diagram from a prompt or from a dataset.**
- Edit, add, or delete shapes in an existing document.
- Create shareable links with specific permissions, or share by email.
- Export a document as PNG.
- Convert an image/visual Claude produces into a Lucid document.

**Setup:**

```bash
claude mcp add --transport http lucid https://mcp.lucid.app/mcp
```

Authentication is OAuth 2.0 with Dynamic Client Registration — you'll be
prompted to sign in to Lucid the first time it's used. Lucid states the
server is a pass-through: it does not retain document content, prompts, or
queries.

**Gate to know about:** this requires a **Team or Enterprise Lucid plan with
admin approval** for MCP access. It's excluded for FedRAMP accounts. This is
a company decision (IT/Lucid admin), not something to self-enable — check
with Delphine or IT before assuming it's available.

Sources: [Lucid community announcement](https://community.lucid.co/community-news-and-announcements-9/introducing-the-lucid-model-context-protocol-mcp-server-12230),
[lucidsoftware/lucid-mcp-server on GitHub](https://github.com/lucidsoftware/lucid-mcp-server).

Once this is enabled for your account, `map-swimlane-builder` should prefer
calling the MCP server directly over producing a CSV for manual import —
update this file's "preferred path" note when that happens.

---

## 3. AI text prompt (fallback only — has a known lane-fidelity problem)

Lucidchart's built-in **"Generate diagram" / Lucid AI** feature (the two-
diamonds icon on the canvas toolbar) takes a natural-language prompt and
can attach supporting files (images, PDFs, text) for context. It's genuinely
useful for a rough first draft or for non-lane diagrams (flowcharts, ERDs,
mind maps).

**The caveat that matters here:** in Lucid's own community forum, a Lucid
product-team member confirmed that **if the diagram is generated against a
standard flowchart shape library, the AI will often ignore pool/lane
instructions entirely.** Swim lanes and pools are BPMN-shape-set constructs;
a prompt that says "swimlane = Sales" without explicitly requesting the BPMN
shape library is likely to be silently dropped, producing a flat flowchart
instead of a lane diagram.

**If you use this path anyway** (quick draft, or CSV import isn't practical):

- Explicitly state "use the BPMN shape library with pools and lanes" in the
  prompt — don't just name lanes and assume Lucid will infer the shape type.
- Be specific and give full context in one prompt rather than a terse one;
  Lucid's own guidance is "natural language, but detailed" — no special
  syntax needed, but vague prompts under-perform.
- Iterate: generate, then send follow-up prompts to add detail, decision
  points, or reorganize rather than trying to get it perfect in one shot.
- Attach the SIPOC table or process notes as a file rather than retyping
  them into the prompt.

Sources: [Lucid community thread on CSV/AI lane limitations](https://community.lucid.co/product-questions-3/can-i-add-import-a-process-diagram-csv-into-lucid-ai-and-display-hidden-metadata-on-the-lucidchart-diagram-12569),
[Lucid — Generate a diagram with AI](https://help.lucid.co/hc/en-us/articles/30324063850516-Generate-a-diagram-with-AI-in-Lucidchart)
*(this help page also 403'd on direct fetch; detail above is from search
summaries)*,
[Lucid AI diagramming tips](https://lucid.co/diagram/ai-diagramming-tutorial).

---

## 4. Formatting labels for Lucid (added 2026-10-12)

Lucid can color shapes and lines from text labels in the data (conditional
formatting rules), so the data carries fixed labels instead of colors or hex
codes. This section only **adds** label columns to the master table. It does
not change step IDs, lanes, arrows, the CSV layout in section 1, or the rules
for what goes in a step.

There are two ways to get the data into Lucid, and their rules differ:

| | Used | Rules in |
| --- | --- | --- |
| **CSV import** | now (no Enterprise plan) | 4.3 |
| **XLSX live link** to a workbook on SharePoint | only if the account moves to Enterprise | 4.4 |

The master workbook (4.1) and the labels (4.2) are the same for both.

### 4.1 Master workbook (the source for both)

Two sheets, as in the cash deposit master. Suzan chose this on 2026-10-12 over
one sheet with comma-separated line labels, which misaligns when a step
branches.

| Sheet | One row per | Columns |
| --- | --- | --- |
| Steps | shape | `Step ID`, `Lane`, `Step Name`, `ShapeType`, `Status`, plus the existing columns (`Shape`, `Confirmed`) unchanged. No connection columns |
| Arrows | arrow | `Line ID`, `From`, `To`, `Label`, `LineType` |

- `Step Name` is the visible text, the same text as the existing `Step`
  column. Keep the existing step IDs (`S01`, `S02`).
- `Line ID` is a unique ID for each arrow (`L01`, `L02`), in the order the
  arrows appear. `From` and `To` are step IDs. `Label` is the arrow's text
  (Yes, No, Found, Not found); leave it blank when the arrow has no text. A
  draft that writes `S17 (Yes), S15 (No)` becomes two Arrows rows, one with
  `Label` = Yes and one with No.
- Keep the master as the source and regenerate the CSV or the linked sheet
  from it.

**Checks before handing anything over:**

1. Every step except `Start` has an arrow in, and every step except `Final`
   has an arrow out.
2. Every `From` and `To` on Arrows is a real `Step ID`, and every `Line ID` is
   unique.
3. No blank `ShapeType`, `Status` or `LineType`; no spelling, capital or
   trailing-space differences between labels.
4. Every `System Decision` and `Manual Review` has at least two arrows out, and
   at most one is `Main Flow` unless the branches are parallel.
5. Fonts are Calibri 12 point or larger, as for every file this skill makes.

### 4.2 Labels (same for CSV and XLSX)

**ShapeType** (function of the shape; one value per shape):

| Label | Use for |
| --- | --- |
| `Start` | the trigger step (no arrow comes in) |
| `Final` | an end step (no arrow goes out) |
| `System Decision` | a system or rule decides on its own, with two or more outcomes (for example "Payment successful?" in PayFabric). Each outcome has its own arrow |
| `Manual Review` | a person checks or decides, with two or more outcomes (for example "Remittance and invoice found?"). Pass moves forward; fail cannot move forward and goes another way (Exception Path or Loop Back) |
| `Manual` | every other step a person does (the default when unsure) |
| `Automated` | a step the system does with no person: a Salesforce flow, a Business Central action, PayFabric, the integration. Its shape and border differ from `Manual` in Lucid (Suzan, 2026-10-23) |

Both decision types must branch. A step worded Review, Verify or Check with a
pass path and a fail path is a `Manual Review` (or a `System Decision` if a
system does it). With no branching it is `Manual` (or `Automated`), even if it is worded as a
review (for example "Review the bank report and lockbox the day after receipt");
ask whether a fail path exists. `Start` and `Final` keep their own labels even when a system does the step, and a decision made by a system stays `System Decision`.

Suzan changed these labels on 2026-10-23: the old `Standard` became `Manual`, and `Automated` is new.

**Gray zone (Suzan, 2026-10-12):** if a person looks up or reads a system's
result and then decides, it is a `Manual Review`, even though the data comes
from a system (for example "BC sales order ID already filled in on the
opportunity?", checked by Sales Support). Use `System Decision` only when the
system or rule decides on its own with no person involved (for example
"Payment successful?" in PayFabric). The lane does not decide the label; who
makes the call does.

Notes are not
shapes; they stay in the Excel reading copy, as before. The existing `Shape`
column (`Process`, `Decision`, `Terminator`) keeps feeding the CSV import.

**Status** (so unconfirmed items show until they are confirmed; one value per
shape):

| Label | Meaning |
| --- | --- |
| `Confirmed` | a named person or source states it |
| `Unconfirmed` | we think it is correct but it still needs checking: in the draft, or something Suzan said to assume |
| `TBD` | nobody has figured it out yet; the answer depends on an open question |

Only these three values (Suzan, 2026-10-23). The old `Assumed` became
`Unconfirmed`; the reason stays in the note column (for example "Assumed (Suzan,
2026-10-08)"), not in `Status`. `TBD` stays a separate value: `Unconfirmed` is
what we think is right but need to check; `TBD` is what nobody has worked out
yet. Keep the label exact.

How Status shows in Lucid (changed by Suzan, 2026-10-29; full style set in 4.5): `Unconfirmed` changes only the fill to pastel amber and keeps the shape and border for `Manual` or `Automated`. `TBD` overrides the whole shape: coral fill and crimson border, with no Manual or Automated distinction. The data never holds a color. The labels stay in the data either way.

**LineType** (what the arrow means; one value per arrow):

| Label | Use for |
| --- | --- |
| `Main Flow` | the normal path, including the expected branch of a decision and parallel branches that both happen. Use it when unsure |
| `Exception Path` | a forward arrow into a problem path: the "No" branch, wrong account, not found, rejected, sent back |
| `Loop Back` | an arrow that returns to an earlier step (rework, retry). Use this even if it is also a problem path |

The arrow's wording stays in `Label` (for example Yes, No, Found, Not found).

### 4.3 CSV rules (used now)

A CSV import is one file, not two sheets. Everything in section 1 still
applies (layout, short lane names, every shape connected, UTF-8 with CRLF).

- Build the CSV from the master: shape rows from Steps, `Line` rows from
  Arrows, in the section 1 layout.
- Append `ShapeType` and `Status` as extra columns after the `Text Area`
  columns, filled on shape rows only. Leave `LineType` out of the CSV (it does
  not import, see the test result below) and keep it in the master.
- The CSV has no `Line ID`; Lucid numbers rows itself. Keep `Line ID` in the
  master only.
- **Tested 2026-10-12 (Suzan, test files A and B).** Both import and lay out
  correctly. In B, `ShapeType` and `Status` come in as custom data on each
  shape (Data panel, Custom Data), so shape rules can read them. They also show
  as text inside the shape; untick them under Header Fields in the Properties
  panel to hide that. `LineType` on the `Line` rows did **not** come in: a
  selected arrow shows "No attached data". So from a CSV, rules can color shapes
  by `ShapeType` and `Status`, but lines cannot be colored by `LineType` from the
  file. Style lines by hand, or add a `LineType` data field by hand to the few
  Exception Path and Loop Back lines and leave Main Flow as the default line
  style. Still to test: whether the shape rules change exactly the right shapes.

- **Lucid AI applies the rules from a table (tested 2026-10-12).** Giving Lucid's
  own AI the rules table (`Lucid-Format-Rules`, CSV or tab-separated) formatted
  the shapes and lines correctly: fills, dashed outlines, and the three line
  styles. It found the lines because the table's last column named each arrow
  ("S14 to S15 (No)"); it cannot read `LineType` from the file. So for every
  map, generate a rules table from the master: shape rules by label, and line
  rules that list each arrow as `From to To` (with its label). If the arrows
  change, regenerate the table.
- **Rule order.** When two rules set the same property on a shape, the later
  rule won (S12: `Assumed`, now `Unconfirmed`, yellow over `Start` green). Put `Status` rules after
  `ShapeType` rules so an alert status shows. A shape that matches rules for
  different properties gets both (S20: blue fill and dashed outline).
- **To confirm.** Whether the AI created live conditional formatting rules or
  one-time styles. Check the Conditional formatting panel: if rules are listed,
  they are live for shapes; if not, the styling is fixed and must be redone when
  the diagram changes.

### 4.4 XLSX rules (only if the account moves to Enterprise)

Linking an Excel file stored on SharePoint is an Enterprise feature (Suzan,
2026-10-12). Suzan will not start on that plan and may upgrade later. These
rules are for that day and are untested.

- **Two sheets, not one file.** Link the master's two sheets: choose two
  sheets in Lucid's import, point the shape settings at Steps and the line
  settings at Arrows.
- **Header row.** Put the headers in row 1 of each linked sheet. The real
  masters have title rows above the headers; a linked sheet may need them
  removed or moved.
- **No connection column.** The Steps sheet has no `Next Step ID`. Add one
  (the `To` IDs of that step's arrows, comma-separated, filled from Arrows,
  never typed by hand) only if a single-sheet import is used instead.
- **Exact names.** Use the header names in 4.1, or set the column mapping in
  Lucid once to match them. Spelling, spacing and capitals in the labels must
  match every time.
- **Not tested yet.** Whether Lucid draws arrows from the Arrows sheet of a
  linked workbook, whether a rule can format a line from a sheet column, and
  that the import asks for one sheet or two, are not verified. Test with a
  small file first: `Lucid-Link-Test_ShapeType-LineType_2026-10-12.xlsx` in
  `Lucid-Import-Tests/`.

### 4.5 Styles are set in Lucid, not in the data (decided 2026-10-29)

Suzan chose the style set below on 2026-10-29. It replaces the starting point of 2026-10-12 (decisions as diamonds, amber for both Unconfirmed and TBD, orange and purple dashed lines). The data never holds a color or a geometry; the labels in 4.2 drive all of it.

| Label | Lucid style |
| --- | --- |
| `Start` | Oval, muted green |
| `Final` | Oval, dark gray |
| `Manual`, `Manual Review` | Sharp-edged rectangle, pale blue fill, dark blue outline `#007aff` |
| `Automated`, `System Decision` | Rounded rectangle, light slate-gray fill, dark slate outline |
| Status `Unconfirmed` | Pastel amber fill; geometry and border kept |
| Status `TBD` | Coral/magenta fill, crimson outline, one shape for Manual and Automated alike (overrides the two rows above) |
| LineType `Main Flow` | Solid dark gray line |
| LineType `Exception Path`, `Loop Back` | Dashed dark gray line (the two look the same) |
| Swim-lane headers | Solid `#007aff` fill, white text; lane backgrounds transparent |

Notes:

- A decision is no longer a diamond in the finished map: `Manual Review` is a rectangle and `System Decision` a rounded rectangle. The `Shape` column in the master (`Decision`) and the CSV `Name` column still say Decision; the rules change the look in Lucid, so leave the files as they are.
- `TBD` and `Unconfirmed` rules go after the shape rules, as in 4.3, so the status wins.
- `LineType` does not import from a CSV (4.3). The line styles come from the rules table that lists each arrow as `From to To`, built from the Arrows sheet of the master. Every master needs `Line ID` and `LineType` on its Arrows sheet.
- Untested as of 2026-10-29. The blueprint prompt below came as a draft and has not been run in Lucid. It asks Lucid's AI to read `LineType` from the data, which a CSV import cannot supply, and the AI prompt path has the lane problem in section 3. Test it on a small file first.

Blueprint prompt as Suzan supplied it (a template with 3 placeholder lanes):

```text
Generate a professional horizontal swimlane diagram template with 3 lanes. Configure the diagram to look at three CSV data columns: "ShapeType", "LineType", and "Status".

Apply these exact shape geometric and formatting rules:
1. ShapeType "Start" & "Final": Use Ovals. Start is muted green, Final is dark gray.
2. ShapeType "Manual" & "Manual Review": Use sharp-edged Rectangles. Standard fill is light pale blue with a dark blue outline using corporate hex #007aff.
3. ShapeType "Automated" & "System Decision": Use Rounded Rectangles. Standard fill is light tech-slate gray with a dark slate outline.

Apply these exact line routing rules based on "LineType":
4. LineType "Main Flow": Solid, dark gray line.
5. LineType "Exception Path" & "Loop Back": Dashed, dark gray line.

Apply these "Status" conditional override rules:
6. If the data property "Status" is exactly equal to "Unconfirmed", change the shape fill color to a light pastel amber/yellow, preserving the original shape geometry and border.
7. If the data property "Status" is exactly equal to "TBD", override the shape entirely to a light coral/magenta fill with a crimson red border, removing any automated vs manual distinction.

Style the swimlane headers with a solid dark blue fill using hex code #007aff and white text; keep the lane backgrounds transparent. Place a small sequence of these placeholder shapes on the canvas to establish the template.
```

Label values the data must use, exactly (every master and Lucid CSV in Accounting-MyNotes checked on 2026-10-29): ShapeType `Start`, `Final`, `Manual`, `Manual Review`, `Automated`, `System Decision`; LineType `Main Flow`, `Exception Path`, `Loop Back`; Status `Confirmed`, `Unconfirmed`, `TBD`.

---

## Which path to use, by situation

| Situation | Use |
| --- | --- |
| Lane placement must be correct and reviewable/versioned | **CSV import (§1)** — default |
| Lucid MCP is approved for your account | **MCP server (§2)** — best, once available |
| Quick rough draft, lanes not yet final, or exploring options | **AI prompt (§3)**, with the BPMN-shape-library instruction spelled out |
| Color shapes by label from a CSV import (no Enterprise plan) | **CSV rules (§4.3)**: `ShapeType` and `Status` columns import as shape data; lines are styled by hand; shape rules still to test |
| Diagram linked to the master workbook on SharePoint (Enterprise plan only) | **XLSX rules (§4.4)**; untested and not needed until the plan changes |
