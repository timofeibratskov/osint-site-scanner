import re

SOCIAL_PATTERNS = {
    "VK": r"vk\.com/[A-Za-z0-9_.]+",
    "Telegram": r"t\.me/[A-Za-z0-9_]+",
    "YouTube": r"youtube\.com/\S+",
    "GitHub": r"github\.com/[A-Za-z0-9_.-]+",
    "X/Twitter": r"twitter\.com/[A-Za-z0-9_]+"
}


def run_social(html_text: str) -> dict:
    if not html_text:
        return {"error": "Нет данных для анализа"}

    matches = {}
    for name, pattern in SOCIAL_PATTERNS.items():
        found = re.findall(pattern, html_text)
        if found:
            matches[name] = list(set(found))

    return {
        "found_count": sum(len(links) for links in matches.values()),
        "links": matches
    }
