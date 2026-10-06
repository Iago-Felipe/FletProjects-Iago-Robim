class Livro:
    def __init__(self, titulo: str, autor: str, 
                 descricao: str, preco: float,
                 cover: str = ''):
        self.titulo = titulo
        self.autor = autor
        self.descricao = descricao
        self.preco = preco
        self.cover = cover
    def __repr__(self) -> str:
        return f'Book({self.titulo}, {self.autor})'