__serial = 1
def _autoincrement() -> int:
    global __serial
    valor = __serial
    __serial += 1
    return valor

class Pessoa:
    def __init__(self, nome: str, idade: int, email: str):
        self.id = _autoincrement()
        self.nome = nome
        self.idade = idade
        self.email = email