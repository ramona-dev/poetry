from datetime import date

class Emprestimo:
    def __init__(self, usuario, livro, data_emprestimo=None, ativo=True):
        self.usuario = usuario
        self.livro = livro
        if data_emprestimo is None:
            data_emprestimo = date.today()
        self.data_emprestimo = data_emprestimo
        self.ativo = ativo


