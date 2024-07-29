import flet as ft

# TopBar
def TopBar(bgcolor: str = None, title: str = "") -> ft.Container:
    return ft.Container(
        bgcolor = bgcolor,
        height = 40,
        content = ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            controls = [
                ft.Row(
                    controls = [
                        ft.Text(value = title, size = 20)
                    ]
                ),
            ]
        )
    )
def ButtonTopBar(bgcolor: str = None, title: str = "" , on_click1 = None,  on_click2 = None,  on_click3 = None) -> ft.Container:
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
                            icon_size=20,
                            on_click = on_click1
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
                            icon_size=20,
                            on_click = on_click2
                        ),
                        ft.IconButton(
                            icon = ft.icons.SETTINGS,
                            tooltip = "Settings",
                            icon_size=20,
                            on_click = on_click2
                        )
                    ]
                )
            ]
        )
    )

# Button
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
                    ft.Container(
                        bgcolor = ft.colors.SECONDARY_CONTAINER,
                        content = ft.Row(
                            spacing = 0,
                            controls = [
                                ft.Row(
                                    expand = True,
                                    spacing = 0,
                                    scroll = "AUTO",
                                    controls = [],
                                ),
                                ft.IconButton(
                                    icon = ft.icons.ADD_ROUNDED,
                                    tooltip = "Add tag",
                                    icon_size=20,
                                )
                            ]
                        )
                    )
                ]
            )
        ),
        on_click = on_click
    )
# InformationButton's tag (DLC)
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

# VocabularyDetail </>
def VocabularyDetail(title: str = "", subject: str = "", content: str = ""):
    return ft.Container(
        height = 40,
        content = ft.Column(
            controls = [
                ft.Row(
                    controls = [
                        ft.Text(value = title, size = 16),
                        
                    ]
                ),
                ft.Row(
                    controls = [
                        ft.Text(value = subject, size = 14)
                    ]
                ),
                ft.Row(
                    controls = [
                        ft.Text(value = content, size = 14)
                    ]
                ),
            ]
        )
    )