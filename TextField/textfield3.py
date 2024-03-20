import flet as ft

def main(page: ft.Page):


    def elkuld(e):
        if len(tf.value) > 0:
            nev = tf.value.split(' ')
            vezetek= ft.TextField(
                label = "Vezetéknév", 
                read_only=True,
                value = nev[0],
                width = 350,
            )
            kereszt = ft.TextField(
                label = "Keresztnév", 
                read_only=True,
                value = nev[1],
                width=350,
            )
            page.add(vezetek, kereszt)
        page.update


    tf = ft.TextField(label="Teljes név",hint_text="Add meg a teljes neved.", width = 350)
    button = ft.ElevatedButton(text="Küldés.", on_click=elkuld)
    page.add(tf, button)
    page.update()

ft.app(target=main)