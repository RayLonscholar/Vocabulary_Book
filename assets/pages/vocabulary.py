import flet as ft
from flet_route import Params, Basket
import assets.pages.widgets.custom_widgets as custom_widgets

class Vocabulary(ft.UserControl):
    def __init__(self, page):

    # top bar
        def back_button_clicked(e):
            pass
        def back_home_button_clicked(e):
            page.go("/")
        def settings_button_clicked(e):
            pass
        self.vocabulary_page_top_bar = custom_widgets.TopBar(ft.colors.SECONDARY_CONTAINER, "ABC")

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
        def vocabulary_button_clicked(e):
            print("vocabulary_button_clicked")
        def vocabulary_button_tag_clicked(e):
            print("vocabulary_button_tag_clicked")
        def create_vocabulary_button():
            self.vocabulary_button_list.controls = []
            for memory in page.data_file_content['data']:
                vocabulary_content = page.data_file_content['data'][f'{memory}']
                if "test1" in vocabulary_content['tag']:
                    InformationButton = custom_widgets.InformationButton(
                        f"{memory}",
                        f"主旨：{vocabulary_content['subject']}",
                        18,
                        15,
                        vocabulary_button_clicked
                    )
                    if vocabulary_content['tag']:
                        for memory in vocabulary_content['tag']:
                            InformationButton.content.content.controls[2].controls.append(
                                custom_widgets.InformationButton_tag(f"{memory}", 13, vocabulary_button_tag_clicked)
                            )
                    self.vocabulary_button_list.controls.append(
                        InformationButton
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
                        self.vocabulary_page_top_bar,
                        self.tag_button_list,
                        self.vocabulary_button_list,
                    ]
                )
            ]
        )