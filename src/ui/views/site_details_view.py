import flet as ft

from src.ui.client.api_client import ApiClient
from src.ui.components.scan_card import ScanCard


class SiteDetailsView(ft.Container):

    def __init__(self, page: ft.Page):
        super().__init__()
        self.app_page = page
        self.expand = True
        self.padding = 20
        self.content_column = ft.Column(
            spacing=20,
            scroll=ft.ScrollMode.AUTO,
            expand=True
        )
        self.content = self.content_column
        self.show_placeholder()

    def show_placeholder(self):
        self.content_column.controls.clear()
        self.content_column.controls.append(
            ft.Container(
                expand=True,
                alignment=ft.Alignment.CENTER,
                content=ft.Text(
                    "choose a domain",
                    size=22,
                    color=ft.Colors.GREY_500
                )
            )
        )

    def load_site(self, site_id: int):
        self.show_loading()
        try:
            site = ApiClient.get_site_details(site_id)
            self.render_site(site)
        except Exception as e:
            self.show_error(str(e))

    def show_loading(self):
        self.content_column.controls.clear()
        self.content_column.controls.append(
            ft.ProgressRing()
        )

    def show_error(self, message: str):
        self.content_column.controls.clear()
        self.content_column.controls.append(
            ft.Text(
                value=message,
                color=ft.Colors.RED
            )
        )

    def render_site(self, site: dict):
        self.content_column.controls.clear()
        self.content_column.controls.append(
            ft.Row(
                controls=[

                    ft.Text(
                        site["domain"],
                        size=34,
                        weight=ft.FontWeight.BOLD
                    ),
                    ft.ElevatedButton(
                        content=ft.Row(
                            controls=[
                                ft.Icon(ft.Icons.PLAY_ARROW),
                                ft.Text("run scan")
                            ],
                            spacing=5
                        ),
                        on_click=lambda e: self.start_scan(site["id"])
                    )
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN
            )
        )
        self.content_column.controls.append(
            ft.Divider()
        )
        scans = site.get("scans", [])
        if not scans:
            self.content_column.controls.append(
                ft.Text(
                    "empty",
                    color=ft.Colors.GREY_500
                )
            )
        else:
            for scan in reversed(scans):
                self.content_column.controls.append(
                    ScanCard(scan)
                )

    def start_scan(self, site_id: int):
        try:
            ApiClient.start_scan(site_id)
            self.page.snack_bar = ft.SnackBar(
                content=ft.Text("scan is running")
            )
            self.page.snack_bar.open = True
            self.page.update()
        except Exception as e:
            self.show_error(str(e))
