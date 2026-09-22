import flet as ft
import os
from model import Livro

def main(page: ft.Page):
    db_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "bookapp.db")
    def close_dialog(e):
        page.pop_dialog()
        page.update()

    def add_person(e):
        titulo = title_text.value
        autor = author_text.value
        descricao = description_text.value
        preco = price_text.value

        if titulo == "" or autor == "" or descricao == "" or preco == "":
            dialog.content = ft.Text("Todos os campos devem ser preenchidos!")
            page.show_dialog(dialog)
            return

        try:
            preco_float = float(preco)
        except ValueError:
            dialog.content = ft.Text("Preço deve ser um número!")
            page.show_dialog(dialog)
            return

        livro = Livro(titulo, autor, descricao, preco_float)
        output_col.controls.append(ft.Text(f"Título: {livro.titulo}"))#, Autor: {livro.autor}, Descrição: {livro.descricao}, Preço: {livro.preco}"))

        title_text.value = ""
        author_text.value = ""
        description_text.value = ""
        price_text.value = ""
        page.update()

    # Widgets
    dialog = ft.AlertDialog(
        title = ft.Text('Erro!'),
        content =ft.Text(''),
        actions = [
            ft.TextButton('Fechar', on_click=close_dialog)
        ]
    )
    title_text = ft.TextField(hint_text="Título", expand=True)
    author_text = ft.TextField(hint_text="Autor", expand=True)
    description_text = ft.TextField(hint_text="Descrição", expand=True)
    price_text = ft.TextField(hint_text="Preço", expand=True)
    add_button = ft.IconButton(icon=ft.Icons.ADD, on_click=add_person)

    # Layout
    input_col = ft.Column(
        expand=True,
        controls=[title_text, author_text, description_text, price_text],
    )
    input_row= ft.Row(
        controls=[input_col, add_button],
    )
    output_col = ft.Column(
        expand=True,
        controls=[title_text.value, author_text.value, description_text.value],
    )
    output_row = ft.Row(
        spacing=0,
        controls=[output_col, price_text.value]
    )
    main_col = ft.Column(
        expand=True,
        controls=[input_row, output_row],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )

    page.title = "Book App"
    page.add(main_col)

if __name__ == "__main__":
    ft.run(main)