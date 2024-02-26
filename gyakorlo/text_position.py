import flet as ft

def main(page: ft.Page):
    elso = ft.Row(
        [
            ft.Text(
                value = "Jobbra",
            )
        ],
        alignment=ft.MainAxisAlignment.END,
    )

    masodik = ft.Row(
        [
            ft.Text(
                value = "Középre",
            )
        ],
        alignment=ft.MainAxisAlignment.CENTER,
    )

    harmadik = ft.Row(
        [
            ft.Text(
                value = "Balra",
            )
        ],
        alignment=ft.MainAxisAlignment.START,
    )


    page.add(elso, masodik, harmadik)
    page.update()
if __name__ == '__main__':
    ft.app(target=main)

