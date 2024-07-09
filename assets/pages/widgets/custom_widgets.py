import flet as ft

def TextButton(value: str, size: int, on_click = None) -> ft.TextButton:
    return ft.TextButton(
        content = ft.Container(
            content = ft.Column(
                controls = [
                    ft.Text(value = value, size = size),
                ],
                alignment = ft.MainAxisAlignment.CENTER,
            ),
        ),
        on_click = on_click
    )