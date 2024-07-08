import flet as ft
from flet_route import Params, Basket

class Vocabulary(ft.UserControl):
    def __init__(self, page):
        def back_home_button_clicked(e):
            page.go("/")

        self.back_home_button = ft.TextButton(
            content = ft.Container(
                content = ft.Column(
                    controls = [
                        ft.Text(value = f"{page.strings['vocabulary_back_home_button']}", size = 20),
                    ],
                    alignment = ft.MainAxisAlignment.CENTER,
                    spacing = 5,
                )
            ),
            on_click = back_home_button_clicked
        )

    def view(self, page: ft.Page, params: Params, basket: Basket) -> ft.View:
        return ft.View(
            controls = [
                ft.Column(
                    expand = True,
                    controls = [
                        self.back_home_button,
                    ]
                )
            ]
        )