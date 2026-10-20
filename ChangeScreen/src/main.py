import flet as ft

@ft.control
class Tela1(ft.Container):
    def init(self):
        self.text_tela1 = ft.Text('Tela 1')
        self.btnGo = ft.Button('Vá para Tela 2', on_click=self.on_click_btnGo)
        self.expand = True
        self.bgcolor = ft.Colors.BLUE_100
        self.col = ft.Column(
            expand=True,
            controls=[self.text_tela1, self.btnGo],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.CENTER
        )
        self.content = ft.Row(
            controls=[self.col],
        )
    def on_click_btnGo(self, e):
        self.page.navigate('/Tela2')

@ft.control
class Tela2(ft.Container):
    def init(self):
        self.text_tela1 = ft.Text('Tela 2')
        self.btnGo = ft.Button('Volte para a tela 1', on_click=self.on_click_btnGo)
        self.bgcolor = ft.Colors.RED_100
        self.expand = True
        self.col = ft.Column(
            expand=True,
            controls=[self.text_tela1, self.btnGo],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.CENTER
        )
        self.content = ft.Row(
            controls=[self.col],
        )
    def on_click_btnGo(self, e):
        self.page.navigate('/')

def main(page: ft.Page):
    page.title = 'app'
    page.padding = 0

    def route_change_listener(e=None):
        page.views.clear()
        page.views.append(
            ft.View(
                route = '/', 
                controls=[Tela1()]
            )
        )
        if page.route == '/tela2':
            page.views.append(
                ft.View(
                    route = '/tela2',
                    controls=[Tela2()]
                )
            )
        page.update()

    page.on_route_change = route_change_listener
    route_change_listener()

if __name__ == '__main__':
    ft.run(main)
