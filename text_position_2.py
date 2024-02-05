import flet as ft

def main(page: ft.Page):
    page.title = "Szöveg igazítás gyakorlása"
    page.bgcolor = ft.colors.YELLOW

    text = ft.Text(
        "Szöveg igazítás gyakorlása. Szöveg középen.",
    )
    page.add(text)
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.update()

ft.app(target=main)
