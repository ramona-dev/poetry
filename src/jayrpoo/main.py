from .usuario import Usuario
from .livros import Livros   
from .emprestimo import Emprestimo
from datetime import date
def main():
    usuario = Usuario("Fernanda", 1)
    livro = Livros(titulo = "Memorias postumas", autor = "Machado de Assis", codigo = 101, disponivel = True)
    emprestimo = Emprestimo(usuario = usuario, livro = livro, data_emprestimo = date.today() )

    print("Emprestimo realizado!")
    print(f"Usuario:{usuario.nome}")
    print(f"Livro:{livro.titulo}")
    print(f"Data:{emprestimo.data_emprestimo}")

if __name__ == "__main__":
    main()
