import flet as ft

# Lista de emoijis que irãao aparecer no APP
# Essa lista pode ser ampliada, o aplicativa lidará com isso
EMOJIS = ['😀', '😂', '😍', '😎', '🤔', '😢', '😡', '👍', 'cu']

# IDX CONTROLA O ÍNDICE DO EMOJI QUE ESTÁ SENDO MOSTRADO NA TELA
# Sempre estará atualizado indice com o emoji que está sendo mostrado na tela
IDX = 0

# A função recebe o objeto page que carrega todos os elementos gráficos
# Page é criado pelo flet.app() e enviado para a função main
def main(page: ft.Page):
    # Configurações da página

    # editar o titulo da janela/aba do navegador/nome do app no mobile
    page.title = 'EmojiApp'

    # Alinhamento vertical dos elementos na página
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # Alinhamento horizontal dos elementos na página
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER

    # Meus elementos (controls)

    # Elemento textual
    # Size aumenta o tamanho do texto do elemento
    input = ft.Text(value=EMOJIS[0], size=100)

    # Função que é executada ao clicar em btn
    # Função acresce o valor IDX e atualiza o valor do input com o emoji correspondente
    # A função é aninhada à main para que ela consiga acessar as variáveis 
    # O parametro "e" da função, carrega informações sobre o evento executado.
    # É possivel acessar a partir de "e" o elemento que sofreu o evento 
    def refresha_click(e):
        global IDX
        # Incremento circular:
        # Acresce IDX em 1
        # Se IDX > len(EMOJIS), então IDX = 0
        # IDX nunca passará de len(EMOJIS) 
        IDX = (IDX + 1) % len(EMOJIS)
        # altera o elemento textual para o emoji da posição IDX
        input.value = EMOJIS[IDX]


    # ELEMENTO BOTÃO COM ÍCONE DE REFRESH, QUE CHAMA A FUNÇÃO refresha_click AO SER CLICADO
    # on_click é o evento de clique do botão, que chama a função refresha_click
    # Será executada toda vez que o botão "btn" for clicado
    btn = ft.IconButton(ft.Icons.REFRESH, on_click=refresha_click)

    # Elemento de layout
    # ft.row constroi uma linha no app
    # Cada linha item inserido em "controls" será posicionado em uma coluna da linha
    # "Input" e "btn" serão posicionados lado a lado na mesma linha
    # Alignment alinha os elementos da linha no centro da página
    row = ft.Row(
        alignment=ft.MainAxisAlignment.CENTER,
        controls=[
            input,
            btn
        ]
    )

    # Adicionando os elementos à página
    # Como "row" contém "input" e "btn", ao adicionar "row" à página, os elementos serão mostrados na tela
    page.add(row)

if __name__ == "__main__":
    # ft.app dá inicio a execução do app
    # target=main envia o objeto page para a função main
    ft.run(main)