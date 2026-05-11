import flet as ft


class Sidebar(ft.Container):

    def __init__(
            self,
            on_site_select,
            on_add_click,
            on_delete_click
    ):
        super().__init__()
        self.width = 320
        self.padding = 15
        self.on_site_select = on_site_select
        self.on_add_click = on_add_click
        self.on_delete_click = on_delete_click
        self.selected_site_id = None
        self.sites_column = ft.Column(
            spacing=10,
            scroll=ft.ScrollMode.AUTO,
            expand=True
        )
        self.content = ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        ft.Text(
                            "domains",
                            size=24,
                            weight=ft.FontWeight.BOLD
                        ),
                        ft.IconButton(
                            icon=ft.Icons.ADD,
                            on_click=self.on_add_click
                        )
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                ),
                ft.Divider(),
                self.sites_column
            ],
            expand=True
        )

    def update_sites(self, sites: list):
        self.sites_column.controls.clear()
        for site in sites:
            is_selected = site["id"] == self.selected_site_id
            self.sites_column.controls.append(
                ft.Container(
                    bgcolor=(
                        ft.Colors.PRIMARY_CONTAINER
                        if is_selected
                        else ft.Colors.SURFACE_CONTAINER
                    ),
                    border_radius=10,
                    padding=12,
                    content=ft.Row(
                        controls=[
                            ft.Text(
                                site["domain"],
                                expand=True
                            ),
                            ft.IconButton(
                                icon=ft.Icons.DELETE_OUTLINE,
                                icon_color=ft.Colors.RED_400,
                                on_click=lambda e, s_id=site["id"]:
                                self.on_delete_click(s_id)
                            )
                        ]
                    ),
                    on_click=lambda e, s_id=site["id"]:
                    self.select_site(s_id)
                )
            )

    def select_site(self, site_id: int):
        self.selected_site_id = site_id
        self.on_site_select(site_id)