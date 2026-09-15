import flet as ft
from model import Pessoa

def main(page: ft.Page):
    def close_dialog(e):
        page.pop_dialog()
        page.update()

    def add_person(e):
        nome = name_text.value
        idade = age_text.value
        email = email_text.value

        if nome == "" or idade == "" or email == "":
            dialog.content = ft.Text("Todos os campos devem ser preenchidos!")
            page.show_dialog(dialog)
            return

        try:
            idade_int = int(idade)
        except ValueError:
            dialog.content = ft.Text("Idade deve ser um número inteiro!")
            page.show_dialog(dialog)
            return

        pessoa = Pessoa(nome, idade_int, email)
        output_col.controls.append(ft.Text(f"Nome: {pessoa.nome}, Idade: {pessoa.idade}, Email: {pessoa.email}"))
        
        name_text.value = ""
        age_text.value = ""
        email_text.value = ""
        page.update()

    # Widgets
    dialog = ft.AlertDialog(
        title = ft.Text('Erro!'),
        content =ft.Text(''),
        actions = [
            ft.TextButton('Fechar', on_click=close_dialog)
        ]
    )
    name_text = ft.TextField(hint_text="Nome")
    age_text = ft.TextField(hint_text="Idade")
    email_text = ft.TextField(hint_text="Email")
    add_button = ft.IconButton(icon=ft.Icons.ADD, on_click=add_person)

    # Layout
    name_row = ft.Row(
        controls=[name_text]
    )
    age_row = ft.Row(
        controls=[age_text, add_button]
    )
    email_row = ft.Row(
        controls=[email_text]
    )
    input_col = ft.Column(
        controls=[name_row, age_row, email_row],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )
    output_col = ft.Column(
        spacing=0,
        controls=[]
    )
    main_col = ft.Column(
        controls=[output_col, input_col],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        alignment=ft.MainAxisAlignment.CENTER
    )

    page.title = "People App"
    page.add(main_col)

if __name__ == "__main__":
    ft.run(main)