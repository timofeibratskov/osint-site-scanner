import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

DEFAULT_HEADERS = {
    "User-Agent": "Mozilla/5.0 (OSINT Tool)"
}

def safe_get(url, timeout=10):
    try:
        return requests.get(url, headers=DEFAULT_HEADERS, timeout=timeout, verify=False)
    except Exception:
        return None