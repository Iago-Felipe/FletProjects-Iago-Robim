import flet as ft
from view import BookApp

def main(page: ft.Page):
    page.title = "BookApp"
    book_app = BookApp()
    # SafeArea permite criar um padding em volta do conteúdo
    # para evitar que o conteúdo interseccione com detalhes
    # de tela de um determinado sistema operacional (ex. Android)
    # No caso do Android, este aplicativo evitou que o campo "title"
    # ficasse sobreposto pela barra de notificações
    page.add(ft.SafeArea(
        expand=True,
        content=book_app
    ))
    book_app.load_books()

if __name__ == "__main__":
    ft.run(main)