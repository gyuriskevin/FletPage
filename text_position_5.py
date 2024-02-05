import flet as ft

def main(page: ft.Page):
    page.title = "Szöveg igazítás gyakorlása"
    page.theme_mode = ft.ThemeMode.DARK

    text = ft.Text(
        "Szöveg igazízás gyakorlása Szöveg alapértelmezett és padding."
    )
    page.add(text)
    page.padding = ft.padding.only(top = 100, left = 150)
    page.update()

ft.app(target=main)
