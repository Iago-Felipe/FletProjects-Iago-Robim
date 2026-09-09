import flet as ft

def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.DARK
    def close_dialog(e):
        page.pop_dialog()
        page.update()

    def on_click_send(e):
        valor = input_txt.value

        def text_decoration(e):
            if check_button.value == True:
                check_button.label_style=ft.TextStyle(color=ft.Colors.GREY, decoration=ft.TextDecoration.LINE_THROUGH)
            elif check_button.value == False:
                check_button.label_style=ft.TextStyle(color=None, decoration=ft.TextDecoration.NONE)
            page.update()

        def delete_task(e):
            output_col.controls.remove(task_container)
            page.update()

        if input_prio.value == 'Alta':
            cor_barra = ft.Colors.RED
        elif input_prio.value == 'Média':
            cor_barra = ft.Colors.YELLOW
        elif input_prio.value == 'Baixa':
            cor_barra = ft.Colors.GREEN
        else:
            dialog.content = ft.Text('Selecione uma prioridade!')
            page.show_dialog(dialog)
            input_txt.value = ''
            return
        page.update()

        if (input_txt.value == ''):
            dialog.content = ft.Text('O campo está vazio!')
            page.show_dialog(dialog)
            input_prio.value = None
            return
        
        check_button = ft.Checkbox(value=False, label=valor, on_change=text_decoration)
        delete_button = ft.IconButton(icon=ft.Icons.DELETE, on_click=delete_task)
        output_row = ft.Row(
                spacing=0,
                controls=[check_button, delete_button],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN
            )

        task_container = ft.Container(
            content=output_row,
            border=ft.Border.only(left=ft.BorderSide(width=5, color=cor_barra)),
            padding=ft.Padding(left=10),
            margin=ft.Margin(bottom=10),
        )

        output_col.controls.append(task_container)
        input_txt.value = ''
        input_prio.value = None
        page.update()

    # ---- Widgets
    dialog = ft.AlertDialog(
        title = ft.Text('Erro!'),
        content =ft.Text(''),
        actions = [
            ft.TextButton('Fechar', on_click=close_dialog)
        ]
    )
    input_txt = ft.TextField(
        expand=True,
        hint_text='Digite uma tarefa...'
        )
    input_prio = ft.Dropdown(
        label='Prioridade',
        options=[
            ft.dropdown.Option('Alta'),
            ft.dropdown.Option('Média'),
            ft.dropdown.Option('Baixa')
        ]
    )
    input_btn = ft.IconButton(
        icon=ft.Icons.ADD,
        on_click=on_click_send
        )

    # ----- Layout
    input_rowInterno = ft.Row(
        expand=True,
        controls=[input_txt, input_prio]
    )
    input_row = ft.Row(
        controls=[input_rowInterno, input_btn],
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
    page.title = 'ToDo List'
    page.add(main_col)

if __name__ == "__main__":
    ft.run(main)