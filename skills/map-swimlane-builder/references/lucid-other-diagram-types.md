# Lucid: other diagram types and what builds them

Added 2026-11-09. The swim-lane CSV import is in `lucidchart-integration.md` and is the only path tested so far. This file lists what Lucid can build from data for other diagram types, and which one to pick for a piece of work.

**Status of every claim below: from Gemini, untested.** The summary table was pasted by Suzan Oslin on 2026-11-09. Claude cannot test Lucid. When Suzan tries one, change its status to Confirmed or Does not work, with the date and what she saw, the same way the swim-lane CSV notes are kept. Leave Lucid's AI features and the Lucid MCP server out of anything for Delphine, Jack or Niko.

## What Lucid builds from data

| Diagram type | Best input | Lucid feature | Status |
| --- | --- | --- | --- |
| Swim-lane or flowchart | CSV | File > Import > Process Diagram | Tested, see `lucidchart-integration.md` |
| System context or data-flow diagram (DFD) | CSV | File > Import > Process Diagram, using line source and line destination | Tested, works (Suzan Oslin, 2026-11-09) |
| Sequence diagram | Text markup (PlantUML style) | UML Sequence library > Use Markup | Tested, works, including the alt block (Suzan Oslin, 2026-11-09) |
| Org chart | CSV, Excel, Google Sheets or HR data | Create from Data > Org Chart | Untested |
| Database schema (entity-relationship diagram, ERD) | Result file of Lucid's metadata query (a CSV) | Import Data > Entity Relationship > SQL Server | Tested, works (Suzan Oslin, 2026-11-09), see the section below |
| Mind map | TXT with tab indents | Import > Mind Map | Untested |
| Cloud setup (AWS, Azure, GCP) | Live environment data | Lucidscale (separate add-on) | Not relevant; reads live environments, not files |

Data linking is not diagram building. Lucid can link a CSV to a diagram you drew by hand and show values on the shapes, but it does not draw the shapes.

## Which diagram for which question (integration work)

| Question | Diagram | Why |
| --- | --- | --- |
| Which job or system carries what between Salesforce, Business Central (BC) and PayFabric? Which arrows are unchanged, replaced or new? | System context diagram, 2024 and now | One box for each system or job, arrows labeled with what moves |
| Which Salesforce field maps to which BC field? | Data-flow map | The guide's field tables, one arrow for each field |
| How often does each job run? | Timeline strip for each job | Shows 15, 10 and 5 minute runs and why a sync can miss a change made just before a run. Not a Lucid import; a table or a hand-drawn strip. |
| What happens in what order between people and systems (Make Order against Closed Won, a cancelled quote)? | Sequence diagram | Time runs down the page, which a swim-lane does not show |
| Who does each step of one process? | Swim-lane | The existing path |

Do not use a swim-lane for the whole architecture. The lane rule says a system lane holds only steps the system runs without a person, so a swim-lane suits the people-and-system steps of one process and not the system-to-system picture.

## Notes for a first test of the system context diagram

- **Same import, different file.** The Process Diagram import is the one already used for swim-lanes. A context diagram has no swim-lane container, so the file would be the Page row, one row for each system or job, and `Line` rows.
- **Columns may differ from what Gemini listed.** Gemini names Id, Name, Line Source, Line Destination and Text Area. The tested swim-lane file also has Shape Library, Page ID, Contained By, Source Arrow and Destination Arrow. Start from the tested layout and drop only the container row and `Contained By`, then check the result.
- **Styling.** The swim-lane CSV carries no color, size, position or line type columns. Expect to set colors and line styles by hand, and to use the `Status` label (Confirmed, Unconfirmed, TBD) the same way, if it imports.
- **Shapes.** The import uses standard flowchart shapes. Circles for processes and open-ended data stores would need a manual shape swap.
- **Every shape connected** and short names, as in section 1 of `lucidchart-integration.md`.

## Diagrams from one workbook (changed 2026-11-09)

Status: all three files import and work in Lucid (Suzan Oslin, 2026-11-09). A re-import into an existing ERD keeps the layout. Not yet checked: whether hand-set line colors survive a re-import.

The ERD, the sequence diagram and the system context are all made from the same workbook, so they can be compared. Do not write a separate set of data for each diagram, and do not write a SQL script: Lucid's SQL Server import wants the result of a metadata query, and a CSV in that shape is enough.

1. **The workbook** (for the SF to BC work: `Integration-Documentation/SF-to-BC-Integration_Field-Map_<date>.xlsx`) has one sheet for each purpose: Field map (one row per field, grouped by object, with direction, trigger, job, owner and status), ERD (tables, columns, keys, links), Sequence (numbered steps), Nodes and Arrows (system context). Change the data in the workbook first, then regenerate. When a fact changes, update every sheet it touches.
2. **Run** `python3 integration-diagrams-from-workbook.py <workbook> <yyyy-mm-dd>` (in this folder). It writes three files next to the workbook: `<Topic>_ERD_<date>.csv`, `<Topic>_Sequence_<date>.txt` and `<Topic>_System-Context_<date>.csv`. Give Suzan the files, not the script.
3. **ERD in Lucid:** Import Data > Entity Relationship > SQL Server, skip the query, upload the CSV. Re-importing a changed file over the same diagram keeps the layout. Never run Lucid's query on Business Central or any live database.
4. **Column names show direction:** a column that receives data from the other system ends in `_SF_to_BC` or `_BC_to_SF`, named for the system that writes it. No suffix where the direction is not known. A column holding the other system's ID is a foreign key, so Lucid draws a line.
5. **Line colors do not import.** Set them by hand (red for SF to BC, blue for BC to SF). Not yet checked whether hand-set colors survive a re-import.
6. **Sequence in Lucid:** UML Sequence library > Use markup, paste the text. One diagram covers the 2024 original and now, in sections A to D, numbered so steps can be discussed. Participant names are single words.
7. **Keep out of the diagrams:** BC customizations that are not Salesforce fields (Print 1099, general journal import, the purchase quote job, permission sets). They stay in the Field map only.
8. **Name the owner of each piece** (Adil's integration code, Priya's Salesforce code, the Integrato job) and mark what is unconfirmed.
