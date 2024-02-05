import flet as ft

def main(page: ft.Page):
    page.title = "Szöveg igazítás gyakorlása"
    page.theme_mode = ft.ThemeMode.DARK

    text = ft.Text(
        "Szöveg igazítás gyakorlása. Szöveg balra, középen.",
    )
    page.add(text)
    page.horizontal_alignment = ft.CrossAxisAlignment.START
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.update()

ft.app(target=main)
