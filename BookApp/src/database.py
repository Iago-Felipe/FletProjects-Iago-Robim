import os 
import sqlite3
from model import Livro

DB_PATH = os.path.join(
    os.environ['FLET_APP_STORAGE_DATA'],
    'bookapp.db'
)

# Caminho até o arquivo do banco de dados .DB
BOOKAPP_SQL_PATH = os.path.join(
    # nome do diretório em que o arquivo database.py está
    # ex. /home/aluno/Documentos/fleTprojects/BookApp/src
    os.path.dirname(os.path.abspath(__file__)),
    "sql",
    "bookapp.sql"
)

INSERT_BOOK_QUERY = '''
    INSERT INTO books (title, author, desc, price, cover) VALUES (?, ?, ?, ?, ?);
    '''
FETCH_BOOKS_QUERY = '''
    SELECT title, author, desc, price, cover FROM books;
    '''

class Database(object):
    def __init__(self):
        self.__create_tables()

    def __connect(self) -> sqlite3.Connection:
        '''abre o arquivo sqlite para consulta/modificação'''
        return sqlite3.connect(DB_PATH) 

    def __create_tables(self):
        '''cria tabelas no banco de dados'''
        '''Abre a conexão conn com o banco sqlite'''
        '''Abre o arquivo "bookapp.sql" em "sqlf"'''
        '''Fecha "conn" e fecha "sqlf"'''
        with self.__connect() as conn:
            with open(BOOKAPP_SQL_PATH, "r", encoding = 'utf-8') as sqlf:
                sql_script = sqlf.read()
                conn.executescript(sql_script)

    def insert(self, book:Livro):
        '''insere livros na tabela "books" do banco de dados
            * book: objeto da classe Livro
            * conecta-se ao banco de dados
            * executa a query INSERT_BOOK_QUERY com os atributos do livro
        '''
        with self.__connect() as conn:
            conn.execute(
                INSERT_BOOK_QUERY,
                (book.titulo, book.autor, book.descricao, book.preco, book.cover))

    def fetch_all(self) -> list[Livro]:
        '''
        fetch_all pega todos os registros de liros do banco de
        dados e retorna uma lista de objetos Book com os dados
        de cada registro
        '''
        ret = []
        with self.__connect() as conn:
            cur = conn.cursor()
            cur.execute(FETCH_BOOKS_QUERY)
            # cada valor de ROWS corresponde a uma tupla
            # contendo os valores do registro de livro
            rows = cur.fetchall()
            # para cada linha de resultados faça:
            for row in rows:
                book = Livro(
                    titulo=str(row[0]),
                    autor=str(row[1]),
                    descricao=str(row[2]),
                    preco=float(row[3]),
                    cover=str(row[4])
                )
                ret.append(book)
        return ret        
