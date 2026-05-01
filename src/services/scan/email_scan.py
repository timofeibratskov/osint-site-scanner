import re

EMAIL_RE = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[A-Za-z]{2,}"


def run_emails(html_text: str) -> dict:
    if not html_text:
        return {"error": "Нет данных для поиска email"}

    emails = set(re.findall(EMAIL_RE, html_text))

    sorted_emails = sorted(list(emails))

    return {
        "found_count": len(sorted_emails),
        "emails": sorted_emails if sorted_emails else []
    }
