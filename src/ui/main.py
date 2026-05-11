import flet as ft

from src.ui.views.main_view import MainView

def main(page: ft.Page):
    page.title = "OSINT Domains"
    page.theme_mode = ft.ThemeMode.DARK

    page.window_width = 1400
    page.window_height = 900

    page.padding = 0
    page.spacing = 0

    page.add(
        MainView(page)
    )


if __name__ == "__main__":
    ft.run(main)