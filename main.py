import flet as ft
from flet_route import Routing, path
import ctypes
import json
from assets.pages.home import Home

def main(page: ft.Page) -> ft.Page:

    # load data files
    data_file = "./assets/data/cache.json"
    strings_file = "./assets/value/strings.json"
    with open(data_file, encoding="utf-8") as f:
        read_file = f.read()
        data_file_content = json.loads(read_file)
    with open(strings_file, encoding="utf-8") as f:
        read_file = f.read()
        strings_file_content = json.loads(read_file)

    # window settings
    page.window_width = 600
    page.window_height = 600
    page.title = strings_file_content["zh-tw"]["page_title"]
    # main theme
    theme = ft.Theme()
    theme.page_transitions.windows = ft.PageTransitionTheme.NONE # disable animation transition
    page.theme = theme
    page.theme_mode = "Dark"
    page.update()

    # main routes
    routes = [
        path(
            url = "/",
            clear = True,
            view = Home(page).view,
        ),
    ]
    Routing(
        page = page,
        app_routes = routes,
    )
    page.go(page.route)
    page.update()

ft.app(target = main, assets_dir = "assets")