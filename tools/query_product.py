import json
from pathlib import Path
from typing import Dict, Any

DATA_DIR = Path(__file__).resolve().parent.parent / "data"


def _read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8") if path.exists() else ""


def query_product(product_of_interest: str, query: str = "") -> Dict[str, Any]:
    catalog_path = DATA_DIR / "product_catalog.json"
    catalog = json.loads(catalog_path.read_text(encoding="utf-8")) if catalog_path.exists() else {"products": []}

    target = None
    q = (product_of_interest + " " + query).lower()
    for item in catalog.get("products", []):
        hay = " ".join([
            item.get("id", ""),
            item.get("name", ""),
            item.get("description", ""),
            " ".join(item.get("capabilities", [])),
        ]).lower()
        if any(token in hay for token in q.split() if token):
            target = item
            break

    sop = _read_text(DATA_DIR / "sales_sop.md")
    forbidden = _read_text(DATA_DIR / "forbidden_claims.md")

    return {
        "source": "local_mock_assets",
        "matched_product": target,
        "sales_sop": sop,
        "forbidden_claims": forbidden,
        "tool_status": "ok"
    }
