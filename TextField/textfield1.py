import flet as ft

def main(page: ft.Page):


    def elkuld(e):
        if len(tf.value) > 0:
            t1.value = f"Szia {tf.value}!"
            page.update()

    tf = ft.TextField(label="Név",hint_text="Add meg a neved.", width = 250)
    button = ft.ElevatedButton(text="Küldés.", on_click=elkuld)
    t1 = ft.Text();
    page.add(tf, button, t1)
    page.update()

ft.app(target=main)
