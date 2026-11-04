# Lucid style definitions

Template name: Finalized Template Rules. The same rules, in importable form, are in `Lucid-Style-Rules_2026-11-03.js`.

## Labels the data must use (exact spelling)

| Field | Values |
| --- | --- |
| ShapeType | Start, Final, Manual, Manual Review, Automated, System Decision, Storage |
| LineType | Main Flow, Exception Path, Loop Back |
| Status | Confirmed, Unconfirmed, TBD |

## Status meaning

| Status | Meaning |
| --- | --- |
| Confirmed | Checked with the people who do the work. |
| Unconfirmed | We think it is right but need to check. |
| TBD | Nobody has worked it out yet. The answer depends on an open question. |

## Shapes (text #17324d unless noted; every border is 3 px)

| ShapeType | Fill | Border | Stroke |
| --- | --- | --- | --- |
| Start | #9bb89d | #4c535d | solid |
| Final (also called Termination) | #4c535d, text #ffffff | #4c535d | solid |
| Manual, Manual Review | #d6e9ff | #005fcc | solid |
| Automated, System Decision | #cdcddb | #553f6a | solid |
| Storage (drive, SharePoint, inbox, database) | #ffffff | #3a414a | solid |

A decision is not drawn as a diamond. Manual Review looks like Manual, and System Decision looks like Automated.

## Status (applied after the shape rules, so the status wins)

| Status | Fill | Border | Stroke |
| --- | --- | --- | --- |
| Unconfirmed | #feeb89 | keeps the ShapeType border color | keeps the ShapeType width (3 px solid) |
| TBD (one look for Manual and Automated alike) | #f6b6a6 | #b83280 | 3 px dashed |
| Confirmed | no change | no change | no change |

## Connectors (all #4c535d, 3 px)

| LineType | Line |
| --- | --- |
| Main Flow | solid |
| Exception Path | dashed |
| Loop Back | dashed (looks the same as Exception Path) |

## Swim lanes

- Header fill #007aff, header text #ffffff, border #3a414a 1 px.
- Lane body fills alternate: lane 1 #fdf5f5, lane 2 #f5fbf7, lane 3 #f5f9fd. Repeat the pattern after lane 3.
- Lane names in ALL CAPS, about 10 characters or fewer.

## Text in the diagram

Font Inter, size 10, color #17324d. (The 12 point minimum applies to documents and workbooks, not to text inside a Lucid diagram.)

## Theme roles

Canvas #ffffff, font Inter. Default = Storage, primary = Manual, secondary = Automated, accent = amber (fill #feeb89, border #005fcc, 3 px solid), highlight = TBD, success = Start, error = Final. Default line: elbow shape, #4c535d, 3 px solid, no outline on the text.

## Key (legend) and checks

The key is editable, built from representative shapes, and keeps the exact labels and styles. The template checks text contrast, text overflow, overlapping blocks, a disconnected line end, a line through a block, an inefficient connector, and editable output.
