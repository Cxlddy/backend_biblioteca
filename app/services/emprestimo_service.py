from ..database.usuarios import busca_u_id

from ..database.livros import (
    busca_l_id,
    marcar_livro_disponivel,
    marcar_livro_indisponivel,
    incrementar_emprestimos
)

from ..database.emprestimos import (
    criar_emprestimo,
    buscar_emprestimo_ativo,
    finalizar_emprestimo
)

def emprestar_livro(id_usuario: int, id_livro: int):
    
    usuario = busca_u_id(id_usuario)

    if usuario is None:
        return {
            'sucesso' : False,
            'mensagem' : "Usuário não encontrado"
        }
    
    livro = busca_l_id(id_livro)

    if livro is None:
        return {
            'sucesso': False,
            'mensagem' : "Livro não encontrado"
        }
    
    if not livro.get("disponivel"):
        return {
            'sucesso' : False,
            'mensagem' : "Livro indisponível"
        }
    
    try:
        criar_emprestimo(id_usuario=id_usuario, id_livro=id_livro)

        marcar_livro_indisponivel(id_livro)
        incrementar_emprestimos(id_livro)

        return {
            'sucesso' : True,
            'mensagem' : "Empréstimo criado com sucesso"
        }
    
    except Exception as e:
        return {
            'sucesso' : False,
            'mensagem' : str(e)
        }
def devolver_livro(id_usuario: int, id_livro: int):

    emprestimo = buscar_emprestimo_ativo(
        id_usuario=id_usuario,
        id_livro=id_livro
    )

    if emprestimo is None:
        return {
            "sucesso": False,
            "mensagem": "Nenhum empréstimo ativo encontrado"
        }


    try:

        finalizar_emprestimo(
            emprestimo["id"]
        )

        marcar_livro_disponivel(
            id_livro
        )

        return {
            "sucesso": True,
            "mensagem": "Livro devolvido com sucesso"
        }

    except Exception as e:

        return {
            "sucesso": False,
            "mensagem": str(e)
        }