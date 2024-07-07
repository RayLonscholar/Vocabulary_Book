import flet as ft
from flet_route import Params, Basket

class Home(ft.UserControl):

    # initialization
    def __init__(self, page):
        pass
    
    # display view
    def view(self, page: ft.Page, params: Params, basket: Basket) -> ft.View:
        return ft.View(
            controls = []
        )