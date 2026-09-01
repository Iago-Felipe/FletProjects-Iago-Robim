import flet as ft

def main(page: ft.Page):
    # ----- Event Listeners
    def close_dialog(e):
        page.pop_dialog()
        page.update()

    def on_click_send(e):
        value = input_txt.value
        try:
            int_value = int(value)
            output_txt = ft.Text(value='')
            if (int_value % 2) == 0:
                output_txt.value += (f'{int_value} é par')
            else:
                output_txt.value += (f'{int_value} é ímpar')
            output_col.controls.append(output_txt)
        except ValueError:
            if (value.strip() == ''):
                dialog.content = ft.Text('O campo está vazio!')
            else:
                dialog.content = ft.Text(f'"{value}" não é um número inteiro')
            page.show_dialog(dialog)
        input_txt.value = ''
        page.update()

    # ----- Widgets
    dialog = ft.AlertDialog(
        title = ft.Text('Erro!'),
        content =ft.Text(''),
        actions = [
            ft.TextButton('Fechar', on_click=close_dialog)
        ]
    )
    input_txt = ft.TextField(
        expand=True,
        hint_text='Digite um número inteiro...'
        )
    input_btn = ft.IconButton(
        icon=ft.Icons.SEND,
        on_click=on_click_send
        )

    # ----- Layout
    input_row = ft.Row(
        controls=[input_txt, input_btn]
    )
    output_col = ft.Column(
        expand=True,
        horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
        scroll=ft.ScrollMode.AUTO,
        spacing=0,
        controls=[]
    )
    main_col = ft.Column(
        expand=True,
        controls=[input_row, output_col]
    )

    # ----- Página
    page.title = 'ParOuImparApp'
    page.add(main_col)

if __name__ == "__main__":
    ft.run(main)
