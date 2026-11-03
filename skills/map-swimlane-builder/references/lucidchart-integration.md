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
| `Storage` | any place where data or files are kept: a shared drive folder, SharePoint, a mailbox such as the AR inbox, or a database such as Business Central or Salesforce records (Suzan, 2026-11-02). One shape for all of them; the text says which. Not a step and not a lane. Show it only where work is saved to it or read from it |

Both decision types must branch. A step worded Review, Verify or Check with a
pass path and a fail path is a `Manual Review` (or a `System Decision` if a
system does it). With no branching it is `Manual` (or `Automated`), even if it is worded as a
review (for example "Review the bank report and lockbox the day after receipt");
ask whether a fail path exists. `Start` and `Final` keep their own labels even when a system does the step, and a decision made by a system stays `System Decision`.

**Storage shape (Suzan, 2026-11-02).** Drives, SharePoint, inboxes and databases are places, not actors, so they never get a lane unless the system itself runs steps (see the lane rule in SKILL.md). All of them are one `Storage` shape for simplicity; the text names the place (for example "Daily Statements folder", "AR inbox", "BC"). Place the shape in the lane of the person or job that writes to it, join it with arrows (save, read), and give it at least one arrow in and one out. In the CSV use `Process` for `Name` (as for decisions) and let the ShapeType label drive the look in Lucid. The Storage style is in section 4.5 (revised 2026-11-02); the CSV does not carry it. Untested in a CSV import.

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

How Status shows in Lucid (changed by Suzan, 2026-10-29; full style set in 4.5): `Unconfirmed` changes only the fill to amber (`#feeb89`) and keeps the shape and border for `Manual` or `Automated`. `TBD` overrides the whole shape: coral fill (`#f6b6a6`) and a dashed border (`#b83280`), with no Manual or Automated distinction. The data never holds a color. The labels stay in the data either way.

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
  style. Tried again on 2026-11-02 with a `LineType` column on the `Line` rows of a real map: it did not work either (Suzan Oslin), so leave `LineType` out of the CSV. Still to test: whether the shape rules change exactly the right shapes.

- **Lucid AI applies the rules from a table (tested 2026-10-12).** Giving Lucid's
  own AI the rules table (`Lucid-Format-Rules`, CSV or tab-separated) formatted
  the shapes and lines correctly: fills, dashed outlines, and the three line
  styles. It found the lines because the table's last column named each arrow
  ("S14 to S15 (No)"); it cannot read `LineType` from the file. Since 2026-11-02 a rules
  table is not needed for each map: Suzan's Lucid template applies the styles
  from the labels, so only the label values in the data matter. Section 4.5 and
  `shared-knowledge/Lucid_Style_Definitions.pdf` are the written record of the
  styles (Suzan Oslin, 2026-11-02). Build a rules table only if she asks.
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

### 4.5 Styles are set in Lucid, not in the data (revised values, 2026-11-02)

The authority is the revised template rules Suzan gave on 2026-11-02, saved in `lucid-style-rules_2026-11-02.js` in this folder. They replace the values in `shared-knowledge/Lucid_Style_Definitions.pdf` (2026-10-29) wherever the two differ. Suzan's Lucid template applies them from the labels in 4.2. The data never holds a color or a geometry, and the CSV does not need them. Use the exact hex values and stroke names; make no substitutions.

**Shapes** (text `#17324d` unless noted; every border is 3 px)

| ShapeType | Fill | Border | Stroke |
| --- | --- | --- | --- |
| `Start` | `#9bb89d` | `#4c535d` | solid |
| `Final` (also called Termination) | `#4c535d` (text `#ffffff`) | `#4c535d` | solid |
| `Manual`, `Manual Review` | `#d6e9ff` | `#005fcc` | solid |
| `Automated`, `System Decision` | `#cdcddb` | `#553f6a` | solid |
| `Storage` (drive, SharePoint, inbox or database) | `#ffffff` | `#3a414a` | solid |

**Status** (applied after the shape rules, so the status wins)

| Status | Fill | Border | Stroke |
| --- | --- | --- | --- |
| `Unconfirmed` | `#feeb89` | keeps the ShapeType border color | keeps the ShapeType width (3 px solid) |
| `TBD` (one shape for Manual and Automated alike) | `#f6b6a6` | `#b83280` | 3 px dashed |
| `Confirmed` | no change | no change | no change |

**Connectors** (all `#4c535d`, 3 px)

| LineType | Line |
| --- | --- |
| `Main Flow` | solid |
| `Exception Path` | dashed |
| `Loop Back` | dashed (looks the same as Exception Path) |

Exception Path and Loop Back lines stay at 3 px dashed (Suzan Oslin, 2026-11-02). The "Exception Path / Loop Back" shape entry in the rules file originally said 4 px; it is corrected to 3 px.

**Swim lanes:** header fill `#007aff`, header text `#ffffff`, border `#3a414a` 1 px. Lane body fills alternate in a fixed order: lane 1 `#fdf5f5`, lane 2 `#f5fbf7`, lane 3 `#f5f9fd`. The rules list three body fills; repeat the pattern past lane 3.

**Text in the diagram:** font Inter, size 10, color `#17324d`. This is the Lucid template setting. The 12 point minimum and Calibri rule apply to the files this skill makes (workbooks, documents, PDFs), not to text inside a Lucid diagram.

**Theme (template name "Finalized Template Rules"):** canvas `#ffffff`, font Inter. Roles: default = Storage, primary = Manual, secondary = Automated, accent = amber (fill `#feeb89`, border `#005fcc`, 3 px solid; the rules point at an Unconfirmed shape entry that does not exist, so this fallback applies), highlight = TBD, success = Start, error = Final. Default line: elbow shape, `#4c535d`, 3 px solid, no outline on the line label, label text in the text style above.

**Key (legend):** editable; built from representative shapes; keeps the exact labels and exact styles.

**Checks the template runs:** text contrast, text overflow, blocks overlapping, a disconnected line end, a line through a block, an inefficient connector, and editable output.

**How the rules map:** `ShapeType` picks the exact shape entry above, `LineType` picks the exact connector entry, and `Status: Unconfirmed` overlays the amber fill while keeping the ShapeType border.

Notes:

- A decision is not a diamond in the finished map: `Manual Review` is shaped like `Manual` and `System Decision` like `Automated`. The `Shape` column in the master (`Decision`) and the CSV `Name` column still say Decision; the template changes the look in Lucid, so leave the files as they are.
- `Storage` shapes use `Process` as the CSV `Name`; the label drives the look (see 4.2).
- `LineType` does not import from a CSV (4.3). Line styles come from Suzan's Lucid template. A per-map rules table is not needed (Suzan Oslin, 2026-11-02); this section and the saved rules file are the record. Every master needs `Line ID` and `LineType` on its Arrows sheet.
- Export must stay editable. Check the exported rendering before sending.
- Label values the data must use, exactly: ShapeType `Start`, `Final`, `Manual`, `Manual Review`, `Automated`, `System Decision`, `Storage`; LineType `Main Flow`, `Exception Path`, `Loop Back`; Status `Confirmed`, `Unconfirmed`, `TBD`.

---

## Which path to use, by situation

| Situation | Use |
| --- | --- |
| Lane placement must be correct and reviewable/versioned | **CSV import (§1)** — default |
| Lucid MCP is approved for your account | **MCP server (§2)** — best, once available |
| Quick rough draft, lanes not yet final, or exploring options | **AI prompt (§3)**, with the BPMN-shape-library instruction spelled out |
| Color shapes by label from a CSV import (no Enterprise plan) | **CSV rules (§4.3)**: `ShapeType` and `Status` columns import as shape data; lines are styled by hand; shape rules still to test |
| Diagram linked to the master workbook on SharePoint (Enterprise plan only) | **XLSX rules (§4.4)**; untested and not needed until the plan changes |
