import flet as ft

from src.ui.client.api_client import ApiClient


class AddSiteDialog(ft.AlertDialog):

    def __init__(self, page, on_success):
        super().__init__()
        self.main_page = page
        self.on_success = on_success
        self.modal = True
        self.domain_input = ft.TextField(
            label="Domain",
            autofocus=True
        )
        self.title = ft.Text("Add domain")
        self.content = self.domain_input
        self.actions = [
            ft.TextButton(
                "Cancel",
                on_click=self.close
            ),
            ft.ElevatedButton(
                "Add",
                on_click=self.save
            )
        ]

    def show(self):
        if self not in self.main_page.overlay:
            self.main_page.overlay.append(self)
        self.open = True
        self.main_page.update()

    def close(self, e=None):
        self.open = False
        self.main_page.update()

    def save(self, e):
        try:
            ApiClient.add_site(
                self.domain_input.value
            )
            self.close()
            self.on_success()
        except Exception as ex:
            self.domain_input.error_text = str(ex)
            self.main_page.update()