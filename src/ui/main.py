import flet as ft
import httpx

API_BASE_URL = "http://127.0.0.1:8000"

def main(page: ft.Page):
    page.title = "OSINT Domains List"
    page.theme_mode = ft.ThemeMode.DARK
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.horizontal_alignment = ft.CrossAxisAlignment.START
    page.padding = 20

    domains_column = ft.Column(spacing=10)
    url_input = ft.TextField(label="Введите домен (example.com)", on_submit=lambda _: send_scan_request())

    # --- ФУНКЦИЯ УДАЛЕНИЯ ---
    def delete_domain(domain_id):
        try:
            with httpx.Client() as client:
                # Отправляем запрос на удаление по ID
                # Убедись, что путь в FastAPI такой: DELETE /sites/{id}
                response = client.delete(f"{API_BASE_URL}/sites/{domain_id}")
                if response.status_code == 200 or response.status_code == 204:
                    load_domains() # Перерисовываем список
                else:
                    print(f"Ошибка удаления: {response.status_code}")
        except Exception as ex:
            print(f"Ошибка связи при удалении: {ex}")

    def send_scan_request(e=None):
        if not url_input.value:
            return
        try:
            with httpx.Client() as client:
                response = client.post(f"{API_BASE_URL}/sites/", json={"url": url_input.value})
                if response.status_code == 200:
                    add_dialog.open = False
                    url_input.value = ""
                    load_domains()
                else:
                    url_input.error_text = f"Ошибка: {response.status_code}"
                    page.update()
        except Exception as ex:
            url_input.error_text = "Нет связи с сервером"
            page.update()

    def close_dialog(e):
        add_dialog.open = False
        page.update()

    add_dialog = ft.AlertDialog(
        title=ft.Text("Добавить новый скан"),
        content=url_input,
        actions=[
            ft.TextButton("Отмена", on_click=close_dialog),
            ft.Button("Сканировать", on_click=send_scan_request),
        ],
    )

    def open_dialog(e):
        page.dialog = add_dialog
        add_dialog.open = True
        page.update()

    def load_domains():
        try:
            with httpx.Client() as client:
                response = client.get(f"{API_BASE_URL}/sites/")
                if response.status_code == 200:
                    sites = response.json()
                    domains_column.controls.clear()

                    for site in sites:
                        # Извлекаем ID и URL из ответа API
                        d_id = site.get("id")
                        d_url = site.get("url", "Без названия")

                        # Создаем строку: Текст + Кнопка удаления
                        row = ft.Row(
                            controls=[
                                ft.IconButton(
                                    icon=ft.Icons.DELETE_OUTLINE,
                                    icon_color="red",
                                    icon_size=18,
                                    # Используем замыкание, чтобы передать ID
                                    on_click=lambda _, id=d_id: delete_domain(id)
                                ),
                                ft.Text(d_url, size=16),
                            ],
                            alignment=ft.MainAxisAlignment.START
                        )
                        domains_column.controls.append(row)
                else:
                    domains_column.controls.append(ft.Text(f"Ошибка сервера: {response.status_code}", color="red"))
        except Exception as e:
            domains_column.controls.append(ft.Text(f"Ошибка связи: {e}", color="red"))
        page.update()

    page.overlay.append(add_dialog)

    page.add(
        ft.Row([
            ft.Row([
                ft.Container(
                    content=ft.IconButton(
                        icon=ft.Icons.ADD,
                        icon_color="white",
                        on_click=open_dialog
                    ),
                    border=ft.Border.all(1, "white"),
                    border_radius=25,
                ),
                ft.Text("OSINT SCANNER", size=20, weight="bold"),
            ], spacing=15),
            ft.IconButton(
                icon=ft.Icons.REFRESH,
                on_click=lambda _: load_domains()
            )
        ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
        ft.Divider(),
        domains_column
    )

    load_domains()

if __name__ == "__main__":
    ft.run(main)