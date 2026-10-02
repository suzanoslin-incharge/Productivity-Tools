# Metadata standard (from InCharge Meeting-to-KB Standard, Part 2)

Fields, exactly in this order:
Title, Category, Document Type, Keywords, Status, Primary Process Contact,
Related Teams, Short Description.

| Field | Rule | Fallback |
|---|---|---|
| Title | System/product name + process or topic. Not a generic meeting title. | Needs confirmation |
| Category | `Business Function > Process Area`. Most specific valid. | `Proposed: [category]` |
| Document Type | Match content, not file format. Controlled list below. | Reference / Needs confirmation |
| Keywords | Comma-separated; supported systems, processes, products, teams, acronyms, common search terms. Concise, no duplicates. | Core supported terms only |
| Status | Controlled list below. `Draft - Process Discovery` only for unvalidated process-discovery content. | Needs confirmation |
| Primary Process Contact | Only an explicitly named owner/SME/confirmed contact. | Needs confirmation |
| Related Teams | Only teams explicitly involved, affected, responsible, consulted, or referenced. Don't infer teams that "would normally" participate. | Needs confirmation |
| Short Description | 1–3 factual sentences: scope, major systems/processes, boundaries, deferred topics. | Concise factual summary |

**Document Type:** Process Discovery Meeting Notes; Current State Process
Documentation; Future State Design; Standard Operating Procedure; How-To
Guide; Product Knowledge; Decision Record; Reference; Training Material;
Policy.
(`Policy` was added 2026-10-01. The verbatim SOP copy in
`InCharge_Meeting_to_Knowledge_Base_Standard.md` still shows the older list.)

**Status:** Draft - Process Discovery; Draft - Under Review; Validated;
Approved; Published; Superseded; Archived; Needs confirmation.

## Example

Title: Business Central Inbound Receiving and Warehouse Put-Away Process
Category: Operations > Warehouse and Inventory Management
Document Type: Process Discovery Meeting Notes
Keywords: Business Central, inbound receiving, warehouse receipts, partial shipments, inventory, non-inventory, warehouse put-away, bin management, JotForm, shipping and receiving, logistics
Status: Draft - Process Discovery
Primary Process Contact: Leeana
Related Teams: Warehouse, Shipping and Receiving, Logistics, Inventory, Accounting
Short Description: Current-state meeting notes on inbound delivery intake through JotForm, inventory and non-inventory receipt posting in Business Central, partial shipment handling, warehouse put-away and bin practices, process ownership, and opportunities to streamline receiving. Purchase-order creation was deferred to a follow-up session.
