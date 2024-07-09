import flet as ft
from flet_route import Params, Basket
import assets.pages.widgets.custom_widgets as custom_widgets

class Vocabulary(ft.UserControl):
    def __init__(self, page):

    # top bar
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

    # kind of vocabulary
        # tag list
        def tag_button_clicked(e):
            for memory in self.kind_of_vocabulary:
                memory.visible = False
            create_vocabulary_button()
            page.update()
            
        def create_tag_button():
            self.tag_button_list.controls = []
            for memory in page.data_file_content['tag']:
                self.tag_button_list.controls.append(
                    custom_widgets.TextButton(f"{memory}", 18, tag_button_clicked)
                )
            page.update()
        self.tag_button_list = ft.Column(
            controls = []
        )
        # all widgets in this layout
        self.kind_of_vocabulary = [
            self.tag_button_list
        ]
        create_tag_button()

    # level 2
        # vocabulary in tag
        def create_vocabulary_button():
            self.vocabulary_button_list.controls = []
            for memory in page.data_file_content['data']:
                if "test1" in page.data_file_content['data'][f'{memory}']['tag']:
                    self.vocabulary_button_list.controls.append(
                        custom_widgets.TextButton(f"{memory}", 18)
                    )
            page.update()
        self.vocabulary_button_list = ft.Column(
            controls = []
        )

    def view(self, page: ft.Page, params: Params, basket: Basket) -> ft.View:
        return ft.View(
            controls = [
                ft.Column(
                    expand = True,
                    controls = [
                        self.back_home_button,
                        self.tag_button_list,
                        self.vocabulary_button_list,
                    ]
                )
            ]
        )