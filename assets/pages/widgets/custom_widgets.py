import flet as ft

def TextButton(value: str = "", text_size: int = 10, on_click = None) -> ft.TextButton:
    return ft.TextButton(
        style = ft.ButtonStyle(shape = ft.RoundedRectangleBorder(radius=5)),
        content = ft.Container(
            content = ft.Column(
                controls = [
                    ft.Text(value = value, size = text_size)
                ],
                alignment = ft.MainAxisAlignment.CENTER,
            )
        ),
        on_click = on_click
    )
def InformationButton(value: str = "", value2: str = "", value_text_size: int = 10, value2_text_size: int = 10, on_click = None) -> ft.TextButton:
    return ft.TextButton(
        style = ft.ButtonStyle(shape = ft.RoundedRectangleBorder(radius=5)),
        content = ft.Container(
            content = ft.Column(
                controls = [
                    ft.Row(
                        controls = [
                            ft.Text(value = value, size = value_text_size, expand = True)
                        ]
                    ),
                    ft.Row(
                        controls = [
                            ft.Text(value = value2, size = value2_text_size, expand = True)
                        ]
                    ),
                    ft.Row(
                        spacing = 0,
                        scroll = "AUTO",
                        controls = [],
                    )
                ]
            )
        ),
        on_click = on_click
    )
def InformationButton_tag(value: str = "", text_size: int = 10, on_click = None) -> ft.TextButton:
    return ft.TextButton(
        content = ft.Container(
            content = ft.Row(
                wrap = True,
                controls = [
                    ft.Text(value = value, size = text_size)
                ]
            )
        ),
        on_click = on_click
    )
def TopBar(bgcolor: str = None, title: str = "" , on_click1 = None,  on_click2 = None,  on_click3 = None) -> ft.Container:
    return ft.Container(
        bgcolor = bgcolor,
        height = 40,
        content = ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            controls = [
                ft.Row(
                    controls = [
                        ft.IconButton(
                            icon = ft.icons.KEYBOARD_BACKSPACE,
                            tooltip = "Back",
                            icon_size=20
                        ),
                        ft.Text(value = title, size = 20)
                    ]
                ),
                # add SearchBar widget ... </>
                ft.Row(
                    spacing = 0,
                    controls = [
                        ft.IconButton(
                            icon = ft.icons.HOME,
                            tooltip = "Back home",
                            icon_size=20
                        ),
                        ft.IconButton(
                            icon = ft.icons.SETTINGS,
                            tooltip = "Settings",
                            icon_size=20
                        )
                    ]
                )
            ]
        )
    )