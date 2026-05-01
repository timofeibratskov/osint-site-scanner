from pydantic import BaseModel, HttpUrl
from typing import List, Dict, Optional, Any


class SiteCreate(BaseModel):
    url: str


class SiteResponse(BaseModel):
    id: int
    url: str


class ScanRequest(BaseModel):
    url: HttpUrl


class TargetInfo(BaseModel):
    domain: str
    url: str
    title: Optional[str]
    status_code: int


class DnsReport(BaseModel):
    domain: str
    records: Dict[str, List[str]]


class SocialReport(BaseModel):
    found_count: int
    links: Dict[str, List[str]]


class SecurityHeaders(BaseModel):
    content_security_policy: str
    x_frame_options: str
    strict_transport_security: str
    x_content_type_options: str
    referrer_policy: str


class HeadersReport(BaseModel):
    analysis_info: Dict[str, Any]
    server_info: Dict[str, Optional[str]]
    security_headers: SecurityHeaders

class AiSecurityAnalysis(BaseModel):
    summary: str
    vulnerabilities: List[str]
    recommendations: List[str]
    risk_score: int

class ScanResponse(BaseModel):
    target: TargetInfo
    whois: Dict
    dns: DnsReport
    headers: HeadersReport
    technologies: Dict
    subdomains: Dict
    service_files: Dict
    leaks_dorks: Dict
    social_links: SocialReport
    found_emails: Dict
    ai_analysis: Optional[AiSecurityAnalysis] = None

    class Config:
        from_attributes = True
