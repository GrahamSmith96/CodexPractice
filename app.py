import json
from pathlib import Path
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
from runner import run_lead_scoring

load_dotenv()
app = Flask(__name__)

DATA_DIR = Path(__file__).resolve().parent / "data"


@app.get("/")
def index():
    leads = json.loads((DATA_DIR / "sample_leads.json").read_text(encoding="utf-8"))
    return render_template("index.html", leads=leads)


@app.post("/analyze")
def analyze():
    lead = request.json or {}
    output = run_lead_scoring(lead)
    return jsonify(output)


if __name__ == "__main__":
    app.run(debug=True)
