import flet as ft
from flet_route import Params, Basket
import assets.pages.widgets.custom_widgets as custom_widgets

class Settings(ft.UserControl):
    def __init__(self, page):

    # top bar
        self.settings_page_top_bar = custom_widgets.ButtonTopBar(ft.colors.SECONDARY_CONTAINER, "Settings")
    
    # theme settings
        def theme_switch_clicked(e):
            if e.control.label == "Dark":
                page.theme_mode = "LIGHT"
                e.control.label = "Light"
            elif e.control.label == "Light":
                page.theme_mode = "DARK"
                e.control.label = "Dark"
            page.update()
        self.theme_switch = ft.Switch(
            label = "Dark",
            on_change = theme_switch_clicked
        )

    # volume settings
        self.test = ft.Audio(
                src = f"https://translate.google.com/translate_tts?ie=UTF-8&client=tw-ob&tl=en&q=Can you hear me now? 1 2 3",
                autoplay=False,
                volume=1,
                balance=0,
            )
        def volume_slider_change(e):
            print(e.control.value / 100)
            self.test.volume = e.control.value / 100
        def test_sound_clicked(e):
            self.test.update()
            self.test.play()

        self.volume_settings = custom_widgets.VolumeSettings(volume_slider_change, test_sound_clicked)


    def view(self, page: ft.Page, params: Params, basket: Basket) -> ft.View:
        return ft.View(
            controls = [
                ft.Column(
                    expand = True,
                    controls = [
                        self.settings_page_top_bar,
                        self.theme_switch,
                        self.test,
                        self.volume_settings,
                    ],
                )
            ]
        )
        