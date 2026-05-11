import httpx
from bs4 import BeautifulSoup
from fastapi import HTTPException

from src.db.database import SessionLocal
from src.db.models import Site, Scan
from src.services import scan
from src.services.ai_service import ask_gemini


def scan_site(site_id: int):
    with SessionLocal() as db:
        db_site = db.query(Site).filter(Site.id == site_id).first()
        if not db_site:
            print(f"Сайт {site_id} не найден")
            return

        domain = db_site.domain

    full_url = f"http://{domain}"
    domain = str(full_url).replace("https://", "").replace("http://", "").split('/')[0]

    with httpx.Client(timeout=15, follow_redirects=True) as client:
        try:
            response = client.get(str(full_url))
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
    print("create report successfully")

    ai_prompt = f"""
    Ты эксперт по кибербезопасности. Проанализируй данные OSINT сканирования для домена: {report['target']['domain']}
    
    ДАННЫЕ:
    1. Заголовки: {report['headers']['security_headers']}
    2. Технологии: {report['technologies']}
    3. Сервисные файлы: {report['service_files']}
    4. Утечки/Dorks: {report['leaks_dorks']}

    ЗАДАЧА:
    Напиши отчет в свободном текстовом стиле по пунктам:
    1. Описание сайта.
    2. Проблемы и уязвимости.
    3. Советы и рекомендации.
    4. Оценка защищенности (от 1 до 10).
    
    Отвечай СТРОГО текстом, без использования JSON и фигурных скобок.
    """
    ai_response = ask_gemini(ai_prompt)

    if ai_response is not None :
        print("ai response created successfully")
        ai_response.replace("```json", "").replace("```", "").strip()

    try:
        new_scan = Scan(
            site_id=site_id,
            raw_data=report,
            ai_report=ai_response
        )
        db.add(new_scan)
        db.commit()
        print(f"Скан для {domain} успешно сохранен!")
    except Exception as e:
        db.rollback()
        print(f"Ошибка сохранения в базу: {e}")
