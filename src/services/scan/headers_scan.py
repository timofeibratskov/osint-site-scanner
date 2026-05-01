from src.utils.webtools import safe_get


def run_headers(domain: str) -> dict:
    url = f"https://{domain}"
    res = safe_get(url)

    if not res:
        return {"error": "Не удалось получить заголовки для данного домена"}

    headers = res.headers

    return {
        "analysis_info": {
            "final_url": str(res.url),
            "status_code": res.status_code
        },
        "server_info": {
            "server": headers.get("Server"),
            "x_powered_by": headers.get("X-Powered-By")
        },
        "security_headers": {
            "content_security_policy": headers.get("Content-Security-Policy", "Missing"),
            "x_frame_options": headers.get("X-Frame-Options", "Missing"),
            "strict_transport_security": headers.get("Strict-Transport-Security", "Missing"),
            "x_content_type_options": headers.get("X-Content-Type-Options", "Missing"),
            "referrer_policy": headers.get("Referrer-Policy", "Missing")
        }
    }
