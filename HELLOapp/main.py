import flet as ft
# flet run main.py --> no terminal
# flet run --web main.py --> no navegador

def main(page: ft.Page):
    # muda o título da janela na web e do app no mobile
    page.title = 'HelloApp'
    # alinha os elementos inseridos a partir do centro da página
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER
    # cria um componente visual de texto
    text = ft.Text(
        value='Hello World!',
        text_align=ft.TextAlign.CENTER,
        width=1
    )
    # método add adiciona elementos (controls) dentro da página
    # para ser mostrado na tela
    page.add(text)

if __name__ == '__main__':
    # ft app cria o objeto: page = Page()
    # o objeto page é enviado ppara a função target (main)
    # para ser preenchido
    ft.app(target=main)