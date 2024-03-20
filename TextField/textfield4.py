import flet as ft

def main(page: ft.Page):

    def count_characters(e):
        tf.counter_text = f'{len(tf.value)} symbols typed'
        page.update()
        
        if tf.value.isalnum():
            tf.error_text = None
        else:
            tf.error_text = "Hibás bemenet!"
        page.update()

    tf = ft.TextField(
            color = ft.colors.RED,
            label="Nums and Chars",
            hint_text="Type numbers and characters only!",
            helper_text="Enter numbers and characters!",
            counter_text="0 symbols typed",
            on_change=count_characters,
            width=300
        )
    page.add(tf,)
    page.update()

ft.app(target=main)