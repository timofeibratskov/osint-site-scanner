import flet as ft


class SectionCard(ft.Container):

    def __init__(self, title: str, content):
        super().__init__()

        self.border_radius = 12
        self.padding = 20
        self.bgcolor = ft.Colors.SURFACE_CONTAINER

        self.content = ft.Column(
            controls=[
                ft.Text(
                    value=title,
                    size=18,
                    weight=ft.FontWeight.BOLD
                ),
                ft.Divider(),
                content
            ],
            spacing=10
        )
