import flet as ft
from flet_route import Params, Basket

class Home(ft.UserControl):

    # initialization
    def __init__(self, page):
        def vocabulary_button_clicked(e):
            page.go("/vocabulary")

        self.vocabulary_button = ft.TextButton(
            content = ft.Container(
                content = ft.Column(
                    controls = [
                        ft.Text(value = f"{page.strings['home_vocabulary_button']}", size = 20),
                    ],
                    alignment = ft.MainAxisAlignment.CENTER,
                    spacing = 5,
                )
            ),
            on_click = vocabulary_button_clicked
        )
        self.add_vocabulary_button = ft.TextButton(
            content = ft.Container(
                content = ft.Column(
                    controls = [
                        ft.Text(value = f"{page.strings['home_add_vocabulary_button']}", size = 20),
                    ],
                    alignment = ft.MainAxisAlignment.CENTER,
                    spacing = 5,
                )
            )
        )
        self.settings_button = ft.TextButton(
            content = ft.Container(
                content = ft.Column(
                    controls = [
                        ft.Text(value = f"{page.strings['home_settings_button']}", size = 20),
                    ],
                    alignment = ft.MainAxisAlignment.CENTER,
                    spacing = 5,
                )
            )
        )
    
    # display view
    def view(self, page: ft.Page, params: Params, basket: Basket) -> ft.View:
        return ft.View(
            controls = [
                ft.Column(
                    expand = True,
                    controls = [
                        self.vocabulary_button,
                        self.add_vocabulary_button,
                        self.settings_button,
                    ],
                )
            ]
        )