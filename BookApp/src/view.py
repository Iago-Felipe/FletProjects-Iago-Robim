import flet as ft
import os

from database import Database
from model import Livro

IMG_ERR_DEF = 'book_placeholder.jpeg'

class BookApp(ft.Container):
    def __init__(self):
        super().__init__()
        self.db = Database()
        self.expand = True
        self.title_txt = ft.TextField(label='Title', expand=True)
        self.author_txt = ft.TextField(label='Author', expand=True)
        self.desc_txt = ft.TextField(label='Description', expand=True)
        self.price_txt = ft.TextField(label='Price', expand=True)
        self.url_txt = ft.TextField(label='Book Cover Image (URL)', expand=True)
        self.output_col = ft.Column(
            expand=True,
            horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
            scroll=ft.ScrollMode.AUTO,
            )
        save_btn = ft.IconButton(
            icon=ft.Icons.ADD,
            on_click=self.save_book
        )

        fields_col = ft.Column(
            expand=True,
            controls=[
                self.title_txt, self.author_txt,
                self.desc_txt, self.price_txt,
                self.url_txt
            ]
        )
        input_row = ft.Row(
            controls=[fields_col, save_btn]
        )
        # content é o parâmetro de conteúdo control
        # da superclasse ft.Container. É o que vai ter
        # dentro do bookApp
        self.content = ft.Column(
            expand=True,
            controls=[
                input_row,
                self.output_col
                ]
        )
    def load_books(self):
        self.output_col.controls.clear()
        books = self.db.fetch_all()
        for book in books:
            self.new_book_entry(book)

    def new_book_entry(self, book:Livro):
        book_cover_img = ft.Image(
            src=book.cover if book.cover.strip() != '' else IMG_ERR_DEF,
            fit=ft.BoxFit.COVER,
            width=100,
            height=120,
        )
        book_info_col = ft.Column(
            controls=[
                ft.Text(book.titulo),
                ft.Text(book.autor),
                ft.Text(book.descricao)
            ]
        )
        book_price_txt = ft.Text(str(book.preco))
        container = ft.Container(
            expand=True,
            padding=16,
            content=ft.Row(
                controls=[book_info_col, book_price_txt]
            )
        )
        book_row = ft.Row(
            controls=[book_cover_img, container]
        )
        card = ft.Card(
            content=ft.Container(
                padding=16,
                content=book_row,
            )
        )
        self.output_col.controls.append(card)
        self.update()
    def clear_fields(self, e):
        self.title_txt.value = ''
        self.author_txt.value = ''
        self.desc_txt.value = ''
        self.price_txt.value = ''
        self.url_txt.value = ''
        
    def save_book(self, e):
       title = self.title_txt.value
       author = self.author_txt.value
       desc = self.desc_txt.value
       price = float(self.price_txt.value)
       cover = self.url_txt.value
       book = Livro(title, author, desc, price, cover)
       self.db.insert(book)
       self.new_book_entry(book)
       self.clear_fields(e)
