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
        info_text = ft.Text(f"{pessoa.nome}, {pessoa.idade} anos")
        bold_text = ft.Text(f"{pessoa.email}", weight=ft.FontWeight.BOLD)

        card_pessoa = ft.Container(
            content=ft.Column(
                controls=[info_text, bold_text],
            ),
            bgcolor=ft.Colors.GREY_500,
            padding=10,
            border_radius=10,   
            width=Width,
            margin=ft.Margin.only(bottom=15)
        )
        output_list.controls.append(card_pessoa)
        
        name_text.value = ""
        age_text.value = ""
        email_text.value = ""

        output_col.visible = True
        page.update()

    # Widgets
    dialog = ft.AlertDialog(
        title = ft.Text('Erro!'),
        content =ft.Text(''),
        actions = [
            ft.TextButton('Fechar', on_click=close_dialog)
        ]
    )
    Width = 280
    name_text = ft.TextField(hint_text="Nome", width=Width)
    age_text = ft.TextField(hint_text="Idade", width=Width)
    email_text = ft.TextField(hint_text="Email", width=Width)
    add_button = ft.IconButton(icon=ft.Icons.ADD, on_click=add_person)

    # Layout
    age_button = ft.Row(
        controls=[age_text, add_button],
        alignment=ft.MainAxisAlignment.CENTER,
    )
    output_list = ft.Column(horizontal_alignment=ft.CrossAxisAlignment.START, tight=True)
    
    output_col = ft.Container(
        content=output_list,    
        margin=ft.Margin.only(bottom=15),
        visible=False
    )
    input_col = ft.Column(
        controls=[
            name_text, 
            age_button, 
            email_text,
            ft.Container(height=10), 
            output_col
        ],
        horizontal_alignment=ft.CrossAxisAlignment.START
    )
    input_row = ft.Row(
        controls=[input_col],
        alignment=ft.MainAxisAlignment.CENTER,
    )
    main_col = ft.Column(
        controls=[input_row],
        scroll=ft.ScrollMode.AUTO,
        expand=True,
    )

    page.title = "People App"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.add(main_col)

if __name__ == "__main__":
    ft.run(main)