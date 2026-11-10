"""Make the three Lucid files for an integration from one workbook.

Usage: python3 integration-diagrams-from-workbook.py <workbook.xlsx> <yyyy-mm-dd> [output folder]

The workbook holds the data once. Sheets read: ERD, Sequence, Nodes, Arrows
(the Field map sheet is the master list the other sheets were built from).
Writes, next to the workbook (or in the output folder):
  SF-to-BC-Integration_ERD_<date>.csv            Lucid: Import Data > Entity Relationship > SQL Server, upload the result file
  SF-to-BC-Integration_Sequence_<date>.txt       Lucid: UML Sequence library > Use markup, paste
  SF-to-BC-Integration_System-Context_<date>.csv Lucid: File > Import > Process Diagram
"""
import csv, os, sys
import openpyxl

wbpath, date = sys.argv[1], sys.argv[2]
out = sys.argv[3] if len(sys.argv) > 3 else os.path.dirname(os.path.abspath(wbpath))
wb = openpyxl.load_workbook(wbpath, data_only=True)

def rows(name):
    ws = wb[name]
    it = ws.iter_rows(values_only=True)
    head = next(it)
    return [dict(zip(head, r)) for r in it if any(v not in (None, "") for v in r)]

# ---- ERD: the 12 columns Lucid's SQL Server metadata query returns
erd = rows("ERD")
res, pos = [], {}
for r in erd:
    t = r["Table"]; pos[t] = pos.get(t, 0) + 1
    typ = r["Type"] or "varchar"
    ln = ("20" if r["Column"] in ("No", "Code", "Document_No", "Item_No", "Customer_No") else "255") if typ == "varchar" else ""
    key = r["Key"] or ""
    cons = []
    if "PK" in key: cons.append(("PRIMARY KEY", "", "", ""))
    if "FK" in key: cons.append(("FOREIGN KEY", "dbo", r["Refers to table"], r["Refers to column"]))
    if not cons: cons = [("", "", "", "")]
    for ct, s, rt, rc in cons:
        res.append(["sqlserver", "IntegrationERD", "dbo", t, r["Column"], pos[t], typ, ln, ct, s, rt, rc])
with open(f"{out}/SF-to-BC-Integration_ERD_{date}.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["dbms","TABLE_CATALOG","TABLE_SCHEMA","TABLE_NAME","COLUMN_NAME","ORDINAL_POSITION","DATA_TYPE","CHARACTER_MAXIMUM_LENGTH","CONSTRAINT_TYPE","TABLE_SCHEMA","TABLE_NAME","COLUMN_NAME"])
    w.writerows(res)

# ---- Sequence: plain participant names, numbered messages, consecutive rows with the same Frame become one alt block
seq = rows("Sequence")
parts = []
for r in seq:
    for p in (r["From"], r["To"]):
        if p not in parts: parts.append(p)
ORDER = ["Renewals", "SalesOps", "Accounting", "Customer", "Salesforce", "PriyaCode", "Integrato", "AdilCode", "BC", "PayFabric"]
parts = [p for p in ORDER if p in parts] + [p for p in parts if p not in ORDER]
lines = [f"participant {p}" for p in parts]
frame = None
for r in seq:
    fr = r["Frame (shown as alt)"] or None
    if frame and fr != frame: lines.append("end"); frame = None
    if fr and not frame: lines.append(f"alt {fr}"); frame = fr
    arrow = "-->" if r["Arrow"] == "dashed" else "->"
    lines.append(f'{r["From"]}{arrow}{r["To"]}: {r["Step"]} {r["Message"]}')
if frame: lines.append("end")
open(f"{out}/SF-to-BC-Integration_Sequence_{date}.txt", "w", encoding="utf-8").write("\n".join(lines) + "\n")

# ---- System context: tested Process Diagram layout without the swim-lane container
nodes, arrows = rows("Nodes"), rows("Arrows")
idx, csvrows, n = {}, [["1","Page","","","","","","","","Page 1","",""]], 2
for nd in nodes:
    person = nd["Type"] == "Person or team"
    idx[nd["Name"]] = n
    csvrows.append([str(n), "Terminator" if person else "Process", "Flowchart Shapes", "1","","","","","", nd["Name"], "Manual" if person else "Automated", "Confirmed"]); n += 1
for a in arrows:
    csvrows.append([str(n), "Line", "", "1", "", str(idx[a["From"]]), str(idx[a["To"]]), "None", "Arrow", f'{a["Status"].upper()}: {a["Label on the line"]}', "", ""]); n += 1
with open(f"{out}/SF-to-BC-Integration_System-Context_{date}.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f, lineterminator="\r\n")
    w.writerow(["Id","Name","Shape Library","Page ID","Contained By","Line Source","Line Destination","Source Arrow","Destination Arrow","Text Area 1","ShapeType","Status"])
    w.writerows(csvrows)
print("wrote ERD", len(res), "rows; sequence", len(seq), "steps; context", len(nodes), "shapes and", len(arrows), "lines")
