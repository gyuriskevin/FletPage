import flet as ft


def main(page):
    def login(e):
         page.add(textUser)
         textUser.value = f"Username: {username.value}\nPassword: {password.value}" 
         page.update()
    
    
    page.title = "Login"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    username = ft.TextField(label = "Username", width= 200)
    password = ft.TextField(label = "Password", width= 200, password=True, hint_text = "Enter a password")
    submit = ft.ElevatedButton(text = "Submit", width=150, on_click=login)
    textUser = ft.Text()
    
    
    page.add(
        ft.Container(
            width=400,
            height=220,
            bgcolor="#FFFFED",
            border_radius=20,
            border=ft.border.all(2, "#FFFF00"),
            padding=10,
            margin=10,
            content=(
                ft.Column(
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        username,
                        password,
                        submit
                    ]
                )
            )
        )
    )



ft.app(target=main)
