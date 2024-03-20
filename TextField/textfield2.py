import flet as ft

def main(page: ft.Page):


    def elkuld(e):
        if len(tf.value) > 0:
            szam = int(tf.value)
            if szam % 2 == 0:
                t1.value = f"A megadott szám ({szam}) páros!"
            else:
                t1.value = f"A megadott szám ({szam}) páratlan!"
            page.update()

    tf = ft.TextField(label="Szám",hint_text="Adj meg egy számot.", width = 250)
    button = ft.ElevatedButton(text="Küldés.", on_click=elkuld)
    t1 = ft.Text();
    page.add(tf, button, t1)
    page.update()

ft.app(target=main)