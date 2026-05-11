import flet as ft


class KeyValueList(ft.Column):

    def __init__(self, data: dict):
        super().__init__(spacing=8)

        for key, value in data.items():

            if isinstance(value, list):
                value = ", ".join(map(str, value))
            elif isinstance(value, dict):
                value = str(value)

            self.controls.append(
                ft.Row(
                    vertical_alignment=ft.CrossAxisAlignment.START,
                    controls=[

                        ft.Container(
                            width=200,
                            content=ft.Text(
                                key,
                                weight=ft.FontWeight.BOLD
                            )
                        ),

                        ft.Container(
                            expand=True,
                            content=ft.Text(
                                str(value),
                                selectable=True,
                                no_wrap=False,
                                overflow=ft.TextOverflow.VISIBLE
                            )
                        )
                    ]
                )
            )