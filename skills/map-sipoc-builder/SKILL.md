---
name: map-sipoc-builder
description: Build a SIPOC (Suppliers, Inputs, Process, Outputs, Customers) table for a business process, and optionally convert it into a swim-lane map. Use when someone asks for a SIPOC, wants to scope a process before detailed mapping, or asks how suppliers/customers relate to swim lanes.
---

# SIPOC Builder

A SIPOC is a one-page, five-column table (**S**uppliers, **I**nputs,
**P**rocess, **O**utputs, **C**ustomers) that scopes a process before it gets
mapped in detail. Use this skill when asked to build one, or to explain how
a SIPOC relates to a swim-lane diagram.

Read `references/sipoc-swimlane-guide.md` before writing a SIPOC — it has
the build method, a worked example, and the SIPOC → swim-lane conversion
rule in full. This file is the short version.

## When a SIPOC vs. a swim-lane map

- **SIPOC first.** High level, 5–7 process steps, no detail on who does what
  or where handoffs occur. Use it to agree scope and stakeholders.
- **Swim-lane map second.** Detailed flowchart; one lane per person/team/
  system; shows handoffs, waits, decisions, loops. Use it once the SIPOC is
  agreed, to find rework and unclear ownership.

**The link:** every Supplier and Customer in the SIPOC becomes a lane in the
swim-lane map. Don't re-derive who the lanes should be — the SIPOC already
answered it.

## Steps to build a SIPOC

1. **Name the process and its boundaries.** One trigger that starts it, one
   event that ends it.
2. **Process** — list 5–7 steps as verb + noun. If it needs more than ~7,
   it's probably two processes.
3. **Outputs** — what the process produces (documents *and* status changes).
4. **Customers** — who receives each output, including internal customers.
5. **Inputs** — what each step needs.
6. **Suppliers** — who or what provides each input. Include systems
   (e.g. an ERP, a CRM) as suppliers when they provide data, not just people.
7. **Check it with the people who do the work.** A SIPOC built without them
   is usually missing something.

This skill is general-purpose — usable for any department's process, not
just accounting/finance (the worked example in the reference guide is a
generic service-invoicing illustration, not scope). If the
person names a company-specific system, role, or term you don't recognize,
ask rather than guess. A department may maintain its own glossary in its own
tools repo (e.g. `accounting-tools`) — check there if relevant, but
don't assume it exists for every team.

## Output format

Default to a markdown table:

| Suppliers | Inputs | Process | Outputs | Customers |
|---|---|---|---|---|
| ... | ... | ... | ... | ... |

State the process name and its start/end boundary above the table. If asked
for a swim-lane conversion, follow the four conversion steps in
`references/sipoc-swimlane-guide.md` §4 and present the result as a markdown
table with one column per lane, rows in step order, and `→` marking
handoffs across lanes.

## What this skill does not do

- It does not replace a detailed swim-lane map, value-stream map, or BPMN
  diagram — offer those as a next step, don't silently produce one instead.
- It does not invent company facts. If suppliers, systems, or customers for
  a given process aren't known, ask, or mark them `TBD` rather than guessing.
