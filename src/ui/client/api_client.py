import httpx

API_BASE_URL = "http://127.0.0.1:8000"


class ApiClient:

    @staticmethod
    def get_sites():
        response = httpx.get(f"{API_BASE_URL}/sites/")
        response.raise_for_status()
        return response.json()

    @staticmethod
    def get_site_details(site_id: int):
        response = httpx.get(f"{API_BASE_URL}/sites/{site_id}")
        response.raise_for_status()
        return response.json()

    @staticmethod
    def add_site(domain: str):
        response = httpx.post(
            f"{API_BASE_URL}/sites/",
            json={"domain": domain}
        )

        response.raise_for_status()
        return response.json()

    @staticmethod
    def delete_site(site_id: int):
        response = httpx.delete(f"{API_BASE_URL}/sites/{site_id}")
        response.raise_for_status()

    @staticmethod
    def start_scan(site_id: int):
        response = httpx.post(f"{API_BASE_URL}/sites/{site_id}/scan")
        response.raise_for_status()
        return response.json()