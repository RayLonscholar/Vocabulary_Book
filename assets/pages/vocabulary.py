import flet as ft
from flet_route import Params, Basket
import assets.pages.widgets.custom_widgets as custom_widgets

class Vocabulary(ft.UserControl):
    def __init__(self, page):

    # top bar
        def back_process(level1: bool, level2: bool, level3: bool):
            for memory in self.kind_of_vocabulary:
                memory.visible = level1
            for memory in self.choose_vocabulary:
                memory.visible = level2
            for memory in self.display_detail:
                memory.visible = level3
        def back_button_clicked(e):
            if self.tag_button_list.visible == True:
                page.go("/")
            if self.vocabulary_button_list.visible == True:
                back_process(True, False, False)
            if self.detail.visible == True:
                back_process(False, True, False)
            page.update()

        def back_home_button_clicked(e):
            page.go("/")
        def settings_button_clicked(e):
            pass
        self.vocabulary_page_top_bar = custom_widgets.ButtonTopBar(ft.colors.SECONDARY_CONTAINER, "ABC", back_button_clicked, back_home_button_clicked, settings_button_clicked)

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
        # choose vocabulary
        def vocabulary_button_clicked(e):
            self.selected_vocabulary = e.control.content.content.controls[0].controls[0].value # selected vocabulary
            print("vocabulary_button_clicked")
            create_detail(
                f'{self.selected_vocabulary}',
                page.data_file_content['data'][f'{self.selected_vocabulary}']['subject'],
                page.data_file_content['data'][f'{self.selected_vocabulary}']['content']
            )
            for memory in self.choose_vocabulary:
                memory.visible = False
            for memory in self.display_detail:
                memory.visible = True
            page.update()
            
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
                            InformationButton.content.content.controls[2].content.controls[0].controls.append(
                                custom_widgets.InformationButton_tag(f"{memory}", 13, vocabulary_button_tag_clicked)
                            )
                    self.vocabulary_button_list.controls.append(
                        InformationButton
                    )
            self.vocabulary_button_list.visible = True
            page.update()
        self.vocabulary_button_list = ft.Column(
            controls = []
        )
        # all widgets in this layout
        self.choose_vocabulary = [
            self.vocabulary_button_list
        ]
    # level 3
        # display detail
        def create_detail(title: str, subject: str, content: str):
            self.detail.controls = []
            self.detail.controls.append(
                custom_widgets.VocabularyDetail(title, subject, content)
            )
            page.update()
        self.detail = ft.Column(
            controls = []
        )
        self.display_detail = [
            self.detail
        ]
        

    def view(self, page: ft.Page, params: Params, basket: Basket) -> ft.View:
        return ft.View(
            controls = [
                ft.Column(
                    expand = True,
                    controls = [
                        self.vocabulary_page_top_bar,
                        self.tag_button_list,
                        self.vocabulary_button_list,
                        self.detail,
                    ]
                )
            ]
        )