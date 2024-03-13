import flet as ft

def main(page: ft.Page):
    page.padding = 0
    page.title = "Dolgozat"
    page.scroll = ft.ScrollMode.AUTO
    elso = ft.Row(
        [
            ft.Text(
                value = "Hello",
            ),
            ft.Text(
                value = "World",
            ),
        ],
        
        alignment = ft.MainAxisAlignment.SPACE_BETWEEN
    )

    masodik = ft.Container(
        height=200,
        width=10000,
        margin = ft.margin.all(0),
        padding=ft.padding.all(0),
        bgcolor = ft.colors.CYAN,
        alignment=ft.alignment.center,
        content = ft.Text(
            value = "A"
        )
    )

    harmadik = ft.Row(
        
        [
            ft.Container(
                margin = ft.margin.only(left = 10),
                bgcolor = ft.colors.YELLOW,
                height = 200,
                width = 200,
            ),
            ft.Container(
                margin = ft.margin.only(left = 10),
                bgcolor = ft.colors.BLUE,
                height = 200,
                width = 200,
            ),
            ft.Container(
                margin = ft.margin.only(left = 10),
                bgcolor = ft.colors.GREEN,
                height = 200,
                width = 200,
            ),
            ft.Container(
                margin = ft.margin.only(left = 10),
                bgcolor = ft.colors.BLACK,
                height = 200,
                width = 200,
            ),
            ft.Container(
                margin = ft.margin.only(left = 10),
                bgcolor = ft.colors.RED,
                height = 200,
                width = 200,
            ),
        ],
        wrap = True
    )

    page.add(elso, masodik, harmadik)
    page.update()


ft.app(target = main)
