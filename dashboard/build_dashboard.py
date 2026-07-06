"""Build the standalone Armenia powerlifting dashboard.

Reads output/armenia_workload_report.csv and output/armenia_totalkg_forecast.csv
(produced by ../armenia_powerlifting_analysis.ipynb), embeds them as JSON into
dashboard_template.html, and writes the result to armenia_dashboard.html.

Run after the notebook (or whenever output/*.csv changes):
    venv/Scripts/python.exe dashboard/build_dashboard.py
"""
import json
import math
from pathlib import Path

import pandas as pd

DASHBOARD_DIR = Path(__file__).parent
PROJECT_ROOT = DASHBOARD_DIR.parent
OUTPUT_DIR = PROJECT_ROOT / "output"

TEMPLATE_PATH = DASHBOARD_DIR / "dashboard_template.html"
OUT_PATH = DASHBOARD_DIR / "armenia_dashboard.html"
PLACEHOLDER = "/*__DATA_JSON__*/"


def clean_records(df: pd.DataFrame) -> list[dict]:
    """Convert a DataFrame to JSON-safe records (NaN -> null; JSON has no NaN)."""
    records = df.to_dict(orient="records")
    for record in records:
        for key, value in record.items():
            if isinstance(value, float) and math.isnan(value):
                record[key] = None
    return records


def build() -> None:
    workload = pd.read_csv(OUTPUT_DIR / "armenia_workload_report.csv")
    forecast = pd.read_csv(OUTPUT_DIR / "armenia_totalkg_forecast.csv")

    payload = {
        "workload": clean_records(workload),
        "forecast": clean_records(forecast),
    }
    data_json = json.dumps(payload, separators=(",", ":"), allow_nan=False)

    template = TEMPLATE_PATH.read_text(encoding="utf-8")
    if PLACEHOLDER not in template:
        raise RuntimeError(f"Template is missing the {PLACEHOLDER} placeholder")

    final_html = template.replace(PLACEHOLDER, data_json)
    OUT_PATH.write_text(final_html, encoding="utf-8")
    print(f"Wrote {OUT_PATH} ({len(final_html):,} bytes)")


if __name__ == "__main__":
    build()
