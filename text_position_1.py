import flet as ft

def main(page: ft.Page):
    page.title = "Szöveg igazítás gyakorlása"
    page.theme_mode = ft.ThemeMode.DARK

    text = ft.Text(
        "Szöveg igazítás gyakorlása. Szöveg alul, középen.",
    )
    page.add(text)
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.END
    page.update()

ft.app(target=main)
