import flet as ft
from flet_route import Params, Basket
import assets.pages.widgets.custom_widgets as custom_widgets

class Home(ft.UserControl):

    # initialization
    def __init__(self, page):

    # top bar
        self.home_page_top_bar = custom_widgets.TopBar(ft.colors.SECONDARY_CONTAINER, f"{page.strings['home_title']}")
    
    # open vocabulary page
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
    # open add new vocabulary of page
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
    # open setting page
        def settings_button_clicked(e):
            page.go("/settings")
        self.settings_button = ft.TextButton(
            content = ft.Container(
                content = ft.Column(
                    controls = [
                        ft.Text(value = f"{page.strings['home_settings_button']}", size = 20),
                    ],
                    alignment = ft.MainAxisAlignment.CENTER,
                    spacing = 5,
                )
            ),
            on_click = settings_button_clicked
        )
    
    # display view
    def view(self, page: ft.Page, params: Params, basket: Basket) -> ft.View:
        return ft.View(
            controls = [
                ft.Column(
                    expand = True,
                    controls = [
                        self.home_page_top_bar,
                        self.vocabulary_button,
                        self.add_vocabulary_button,
                        self.settings_button,
                    ],
                )
            ]
        )