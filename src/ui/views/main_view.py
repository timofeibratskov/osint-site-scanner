import flet as ft

from src.ui.client.api_client import ApiClient
from src.ui.components.sidebar import Sidebar
from src.ui.dialogs.add_site_dialog import AddSiteDialog
from src.ui.views.site_details_view import SiteDetailsView


class MainView(ft.Row):

    def __init__(self, page: ft.Page):
        super().__init__()
        self.app_page = page
        self.expand = True
        self.details_view = SiteDetailsView(page)
        self.sidebar = Sidebar(
            on_site_select=self.select_site,
            on_add_click=self.open_add_dialog,
            on_delete_click=self.delete_site
        )
        self.controls = [
            self.sidebar,
            ft.VerticalDivider(width=1),
            self.details_view
        ]
        self.load_sites()

    def did_mount(self):
        self.load_sites()

    def load_sites(self):
        try:
            sites = ApiClient.get_sites()
            self.sidebar.update_sites(sites)
        except Exception as e:
            print(e)

    def select_site(self, site_id: int):
        self.details_view.load_site(site_id)
        self.sidebar.selected_site_id = site_id
        self.load_sites()

    def open_add_dialog(self, e):
        dialog = AddSiteDialog(
            self.app_page,
            self.load_sites
        )
        dialog.show()

    def delete_site(self, site_id: int):
        try:
            ApiClient.delete_site(site_id)
            self.load_sites()
            self.details_view.show_placeholder()
        except Exception as e:
            print(e)