import flet as ft

def main(page: ft.Page):
    
    def open_page(e):
        page.launch_url("https://szerelmes-versek.info/a-szemed.vers")

    def open_page2(e):
        page.launch_url("https://szerelmes-versek.info/te-meg-en.vers")
    
    page.bgcolor ="#98393A"
    page.scroll = ft.ScrollMode.AUTO
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    page.title = "Versek"

    elsoKont = ft.Container(
        height=400,
        width=500,
        margin = ft.margin.all(10),
        bgcolor= "#f4e7bd",
        content=ft.Column(
            [
                ft.Text(value="A szemed",
                        italic=True,
                        size=30,
                        color = "#555555",
                        weight = ft.FontWeight.BOLD,
                        text_align=ft.TextAlign.CENTER,
                        ),
                ft.Row(
                    [
                        ft.Icon(name=ft.icons.CALENDAR_MONTH,color="#98393A"),
                        ft.Text("2023.02.20", italic = True, color = "#8a8a8a"),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                ft.Text(value = "Nagy, mély szemed \n"
                        "reámragyog sötéten\n"
                        "S lelkemben halkan fuvoláz a vágy.\n"
                        "Mint ifú pásztor künn a messzi réten\n"
                        "Subáján fekve méláz fényes égén\n"
                        "S kezemben búsan sírdogál a nád.\n", italic = True, color = "#98393A", weight=ft.FontWeight.BOLD,
                        
                        text_align = ft.TextAlign.CENTER),
                ft.Row(
                    [
                        ft.Text(
                            spans = [
                                ft.TextSpan(
                                    text = "vers folytatása >>>",
                                    on_click=open_page,
                                )
                            ]
                            ),
                    ],
                    alignment=ft.MainAxisAlignment.END,
                ),
                ft.Row(
                    [
                        ft.Icon(name=ft.icons.FOLDER, color="#98393A"),
                        ft.Text("Vágyakozás", italic=True, color = "#8a8a8a"),
                        ft.Icon(name=ft.icons.ACCOUNT_CIRCLE, color="#98393A"),
                        ft.Text("József Attila", italic=True, color = "#8a8a8a"),
                        ft.Text("Szerelmes verse", italic=True, color = "#8a8a8a"),
                        ft.Icon(name = ft.icons.COMMENT, color="#98393A"),
                        ft.Text("Szólj hozzá", italic=True, color = "#8a8a8a"),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
            ],
            horizontal_alignment = ft.CrossAxisAlignment.CENTER
        ),
    )
    
    masodikKont = ft.Container(
        height=400,
        width=500,
        
        margin = ft.margin.all(10),
        bgcolor= "#f4e7bd",
        content=ft.Column(
            [
                ft.Text(value="Te meg Én",
                        italic=True,
                        size=30,
                        color = "#555555",
                        weight = ft.FontWeight.BOLD,
                        text_align=ft.TextAlign.CENTER,
                        ),
                ft.Row(
                    [
                        ft.Icon(name=ft.icons.CALENDAR_MONTH, color="#98393A"),
                        ft.Text("2023.02.20", italic=True, color = "#8a8a8a"),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                ft.Text(value = "Szemed Kutat! Enyémben \n"
                        "keresi a reményt.\n"
                        "Érzem szíved gyors dobogását,\n"
                        "látom arcodon, fellobbanni\n"
                        "a nyughatatlan fényt!\n", italic = True, color = "#98393A", weight=ft.FontWeight.BOLD,
                        text_align = ft.TextAlign.CENTER),
                ft.Row(
                    [
                        ft.Text(
                            spans = [
                                ft.TextSpan(
                                    text = "vers folytatása >>>",
                                    on_click=open_page2,
                                )
                            ]
                            ),
                    ],
                    alignment=ft.MainAxisAlignment.END,
                ),
                ft.Row(
                    [
                        ft.Icon(name=ft.icons.FOLDER, color="#98393A"),
                        ft.Text("Vágyakozás", italic=True, color = "#8a8a8a"),
                        ft.Icon(name=ft.icons.ACCOUNT_CIRCLE, color="#98393A"),
                        ft.Text("Tamás István", italic=True, color = "#8a8a8a"),
                        ft.Text("Szerelmes verse", italic=True, color = "#8a8a8a"),
                        ft.Icon(name = ft.icons.COMMENT, color="#98393A"),
                        ft.Text("Szólj hozzá", italic=True, color = "#8a8a8a"),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
            ],
            horizontal_alignment = ft.CrossAxisAlignment.CENTER
        ),
    )
    

    page.add(elsoKont,masodikKont)
    page.update()
    
ft.app(target=main)