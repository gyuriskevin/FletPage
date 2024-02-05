import flet as ft

def main(page: ft.Page):
    page.title = "Szöveg igazítás gyakorlása"
    page.bgcolor = ft.colors.TEAL
    page.color = ft.colors.GREY_100

    text = ft.Text(
        "Szöveg igazítás gyakorlása. Szöveg jobbra fent.",
    )
    page.add(text)
    page.horizontal_alignment = ft.CrossAxisAlignment.END
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.update()

ft.app(target=main)
