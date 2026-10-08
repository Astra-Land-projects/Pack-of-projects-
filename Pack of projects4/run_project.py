import csv, subprocess, sys
from pathlib import Path
root=Path(__file__).parent
with open(root/"manifest.csv",encoding="utf-8") as f: rows=list(csv.DictReader(f))
q=sys.argv[1:]
if not q:
    print("Usage: python run_project.py <project_id>"); raise SystemExit(1)
i=int(q[0]); row=next(r for r in rows if int(r["id"])==i)
folder=root/"projects"/f"{i:03d}-"+__import__("re").sub(r"[^a-z0-9]+","-",row["name"].lower()).strip("-")
print("Launching",row["name"],"on",row["port"])
subprocess.run([sys.executable,str(folder/"app.py")])
