def run_leaks(domain: str) -> dict:
    dorks = [
        f'"{domain}" "password"',
        f'"{domain}" "credentials"',
        f'site:pastebin.com "{domain}"',
        f'site:github.com "{domain}"'
    ]

    return {
        "scan_type": "passive_osint",
        "description": "Это пассивный поиск через Google Dorks. Проверьте данные ссылки вручную в поисковой системе.",
        "google_dorks": dorks,
        "search_links": [f"https://www.google.com/search?q={dork.replace(' ', '+')}" for dork in dorks]
    }