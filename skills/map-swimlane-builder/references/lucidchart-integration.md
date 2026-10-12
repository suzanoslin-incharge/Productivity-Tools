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
- Keep lane names short, under about 25 characters. Longer names are drawn
  twice in the narrow lane header, for example "Customer (payer and AP
  contact)(payer and AP contact)". Put the detail in a table, not the name.
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

## Which path to use, by situation

| Situation | Use |
| --- | --- |
| Lane placement must be correct and reviewable/versioned | **CSV import (§1)** — default |
| Lucid MCP is approved for your account | **MCP server (§2)** — best, once available |
| Quick rough draft, lanes not yet final, or exploring options | **AI prompt (§3)**, with the BPMN-shape-library instruction spelled out |
