from src.utils.webtools import safe_get
from bs4 import BeautifulSoup
import re


def run_tech(domain: str) -> dict:
    res = safe_get(f"https://{domain}")
    if not res:
        return {"error": "Не удалось загрузить HTML для анализа технологий"}

    tech = set()
    headers = res.headers

    if headers.get("Server"):
        tech.add(headers["Server"])

    if headers.get("X-Powered-By"):
        tech.add(headers["X-Powered-By"])

    soup = BeautifulSoup(res.text, "html.parser")

    if soup.find("meta", {"name": "generator", "content": re.compile("WordPress", re.I)}):
        tech.add("WordPress")

    if "wp-content" in res.text:
        tech.add("WordPress")

    return {
        "detected_technologies": sorted(list(tech)) if tech else [],
        "raw_server": headers.get("Server"),
        "powered_by": headers.get("X-Powered-By")
    }
