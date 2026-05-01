import httpx
from bs4 import BeautifulSoup
from src.services import scan
from fastapi import HTTPException

async def scan_site(full_url: str) -> dict:
    domain = str(full_url).replace("https://", "").replace("http://", "").split('/')[0]

    async with httpx.AsyncClient(timeout=15, follow_redirects=True) as client:
        try:
            response = await client.get(str(full_url))
            html_text = response.text
            status_code = response.status_code
        except Exception as e:
            raise HTTPException(status_code=502, detail=f"Не удалось подключиться: {str(e)}")

    soup = BeautifulSoup(html_text, "html.parser")
    title = soup.title.string if soup.title else None

    report = {
        "target": {
            "domain": domain,
            "url": str(response.url),
            "title": title,
            "status_code": status_code
        },
        "whois": scan.run_whois(domain),
        "dns": scan.run_dns(domain),
        "headers": scan.run_headers(domain),
        "technologies": scan.run_tech(domain),
        "subdomains": scan.run_subdomains(domain),
        "service_files": scan.run_service_files(domain),
        "leaks_dorks": scan.run_leaks(domain),

        "social_links": scan.run_social(html_text),
        "found_emails": scan.run_emails(html_text)
    }

    return report