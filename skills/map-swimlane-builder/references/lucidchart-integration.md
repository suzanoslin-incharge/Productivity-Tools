# Lucidchart Integration Reference

How to get a swim-lane process map from Claude into an actual Lucidchart
diagram. There are three real paths, in order of reliability. **Do not
default to the AI text-prompt path for anything where lane placement
matters** — see the caveat in §3.

Researched 2026-09-29 from Lucid's own help center, developer docs, GitHub,
and product-team responses in their community forum. Where I couldn't fetch
a page directly (marked below), treat the detail as reasonably sourced but
worth a quick sanity check against the live page before relying on it for
something company-facing.

---

## 1. CSV import (recommended default for swim-lane accuracy)

Lucidchart has a documented **"Create a process diagram from CSV import"**
feature built specifically for this. It places shapes deterministically —
including into named swim lanes — rather than leaving placement to an AI's
interpretation of a prompt.

**Required columns:**

| Column | Meaning |
| --- | --- |
| `ID` | A unique identifier for the row/shape. |
| `Name` | The shape's label. |
| `Shape Library` | Which Lucid shape library to draw from (must be spelled/capitalized exactly as Lucid expects). |
| `Page ID` | Which page/canvas the shape belongs to. |
| `Contained By` | What container (swim lane, pool) the shape sits inside. |
| `Text Area 1` | The visible text on the shape. |

**Swim-lane placement syntax:** the `Contained By` cell uses
`<SwimlaneShapeID>:<RowName>` — the ID of the swim-lane container shape,
a colon, then the name of the specific lane row the shape belongs in. Every
row that should land inside a lane needs this filled in correctly; a blank
or malformed value is the most common reason shapes land outside their
intended lane.

**Import steps (from Lucid's help center, summarized):**

1. Open or create the target document in Lucidchart.
2. Select **Import Data** at the bottom left of the document (or the
   equivalent "Import Data" action in the toolbar).
3. Upload the CSV.
4. Map/verify columns if prompted.
5. Lucid builds the diagram, placing shapes per `Contained By`.

Source: [Lucid Help Center — Create a process diagram from CSV import](https://help.lucid.co/hc/en-us/articles/15927090927508-Create-a-process-diagram-from-CSV-import).
*(This page returned a 403 to automated fetch when researched — the column
list and syntax above come from search-result summaries of it, not a direct
read. Confirm against the live page before treating the exact column names
as final.)*

**What `map-swimlane-builder` should produce for this path:** a CSV with one row
per process step, `Contained By` set from the lane the step's owner sits in,
plus a lane "header" row per swim-lane container if the target diagram
needs the lanes created rather than reused from a template.

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
