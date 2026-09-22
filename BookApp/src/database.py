import os 
import sqlite3
from model import Livro

# os.path.join concatena caminhos com o separador do sistema
# i.e. "/" no Linux e "\" no Windows
BOOKAPP__SQL__PATH = os.path.join(
    # nome do diretório em que o arquivo database.py está
    # ex. /home/aluno/Documentos/fleTprojects/BookApp/src
    os.path.dirname(os.path.abspath(__file__)),
    "sql",
    "bookapp.sql"
)

INSERT_BOOK_QUERY = '''
    INSERT INTO books (title, author, desc, price) VALUES (?, ?, ?, ?);
    '''

class Database(object):
    def __init__(self, db_path: str):
        '''db_path: caminho do arquivo sqlite (banco de dados)'''
        self.db_path = db_path
        self.__create_tables()

    def __connect(self) -> sqlite3.Connection:
        '''abre o arquivo sqlite para consulta/modificação'''
        import sqlite3
        self.conn = sqlite3.connect(self.db_path)
        self.cursor = self.conn.cursor()
        return sqlite3.connect(self.db_path) 

    def __create_tables(self):
        '''cria tabelas no banco de dados'''
        '''Abre a conexão conn com o banco sqlite'''
        '''Abre o arquivo "bookapp.sql" em "sqlf"'''
        '''Fecha "conn" e fecha "sqlf"'''
        with self.__connect() as conn:
            with open(BOOKAPP__SQL__PATH, "r", encoding = 'utf-8') as sqlf:
                sql_script = sqlf.read()
                conn.executescript(sql_script)

    def insert_book(self, book:Livro):
        '''insere livros na tabela "books" do banco de dados
            * book: objeto da classe Livro
            * conecta-se ao banco de dados
            * executa a query INSERT_BOOK_QUERY com os atributos do livro
        '''
        with self.__connect() as conn:
            conn.execute(
                INSERT_BOOK_QUERY,
                (book.titulo, book.autor, book.descricao, book.preco))

    def fetch_all(self) -> list[Livro]:
        pass
