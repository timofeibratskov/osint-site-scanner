import flet as ft

from src.ui.components.section_card import SectionCard
from src.ui.components.key_value_list import KeyValueList


class ScanCard(ft.Card):

    def __init__(self, scan_data: dict):
        super().__init__()

        raw = scan_data.get("raw_data") or {}
        ai_response = scan_data.get("ai_response")

        self.content = ft.Container(
            padding=15,
            content=ft.Column(
                controls=[

                    ft.ExpansionTile(
                        title=ft.Text(
                            f"Скан от {scan_data['timestamp'][:19]}"
                        ),
                        subtitle=ft.Text(
                            raw.get("target", {}).get("domain", "")
                        ),
                        controls=[

                            SectionCard(
                                "AI Report",
                                ft.Text(
                                    ai_response if ai_response else "empty",
                                    selectable=True
                                )
                            ),

                            self.build_target_section(raw),
                            self.build_dns_section(raw),
                            self.build_headers_section(raw),
                            self.build_technologies_section(raw),
                            self.build_whois_section(raw),
                        ]
                    )
                ]
            )
        )

    def build_target_section(self, raw):
        return SectionCard("Target", KeyValueList(raw.get("target", {})))

    def build_dns_section(self, raw):
        return SectionCard("DNS", KeyValueList(raw.get("dns", {}).get("records", {})))

    def build_headers_section(self, raw):
        return SectionCard("Headers", KeyValueList(raw.get("headers", {})))

    def build_technologies_section(self, raw):
        return SectionCard("Technologies", KeyValueList(raw.get("technologies", {})))

    def build_whois_section(self, raw):
        return SectionCard("WHOIS", KeyValueList(raw.get("whois", {})))