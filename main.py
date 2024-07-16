import flet as ft
from flet_route import Routing, path
import ctypes
import json
from assets.pages.home import Home
from assets.pages.vocabulary import Vocabulary


def main(page: ft.Page) -> ft.Page:

    # load data files
    page.data_file = "./assets/data/local.json"
    page.strings_file = "./assets/value/strings.json"
    with open(page.data_file, encoding="utf-8") as f:
        read_file = f.read()
        page.data_file_content = json.loads(read_file)
    with open(page.strings_file, encoding="utf-8") as f:
        read_file = f.read()
        page.strings_file_content = json.loads(read_file)
        page.strings = page.strings_file_content['zh-tw']

    # window settings
    page.window_width = 600
    page.window_height = 600
    page.title = page.strings['window_title']
    # main theme
    theme = ft.Theme()
    theme.page_transitions.windows = ft.PageTransitionTheme.NONE # disable animation transition
    page.theme = theme
    page.theme_mode = "DARK"
    page.update()

    # main routes
    routes = [
        path(
            url = "/",
            clear = True,
            view = Home(page).view,
        ),
        path(
            url = "/vocabulary",
            clear = True,
            view = Vocabulary(page).view,
        ),
    ]
    Routing(
        page = page,
        app_routes = routes,
    )
    print(page.route)
    page.go(page.route)
    page.update()

ft.app(target = main, assets_dir = "assets")