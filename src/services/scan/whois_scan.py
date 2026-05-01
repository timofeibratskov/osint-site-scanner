import whois


def run_whois(domain):
    try:
        data = whois.whois(domain)
        if not data:
            return {"error": "WHOIS не найден или скрыт"}
        return {
            "domain": data.domain_name,
            "registrar": data.registrar,
            "creation_date": str(data.creation_date),
            "emails": data.emails
        }
    except Exception as e:
        return {"error": str(e)}
