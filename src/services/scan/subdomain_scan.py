from src.utils.webtools import safe_get

def run_subdomains(domain: str) -> dict:
    url = f"https://crt.sh/?q=%25.{domain}&output=json"

    res = safe_get(url, timeout=20)

    if not res or res.status_code != 200:
        return {"error": "Не удалось получить данные от crt.sh или сервис недоступен"}

    try:
        data = res.json()
    except Exception:
        return {"error": "Сервис вернул некорректный JSON"}

    found = set()

    for entry in data:
        name = entry.get("name_value", "")
        for s in name.split("\n"):
            if domain in s and "*" not in s:
                found.add(s.strip())

    return {
        "count": len(found),
        "subdomains": sorted(list(found))
    }