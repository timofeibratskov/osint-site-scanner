from src.utils.webtools import safe_get
import re


def run_service_files(domain: str) -> dict:
    report = {
        "robots": {"found": False, "disallowed_paths": []},
        "sitemap": {"found": False}
    }

    robots_res = safe_get(f"https://{domain}/robots.txt")
    if robots_res and robots_res.status_code == 200:
        report["robots"]["found"] = True
        paths = re.findall(r"Disallow: (.*)", robots_res.text)
        report["robots"]["disallowed_paths"] = [p.strip() for p in paths if p.strip()]

    sitemap_res = safe_get(f"https://{domain}/sitemap.xml")
    if sitemap_res and sitemap_res.status_code == 200:
        report["sitemap"]["found"] = True

    return report
