import dns.resolver


def run_dns(domain: str) -> dict:
    results = {}
    record_types = ("A", "MX", "NS", "TXT")

    for rtype in record_types:
        try:
            answers = dns.resolver.resolve(domain, rtype)
            results[rtype] = [str(r) for r in answers]
        except Exception:
            results[rtype] = []

    return {
        "domain": domain,
        "records": results
    }