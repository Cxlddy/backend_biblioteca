from fastapi import APIRouter

from ..schemas.livro import LivroCadastroSchema
from ..database.livros import add_livro, busca_l_titulo, busca_l_id, excluir_livro

router = APIRouter()


@router.post("/")
def criar_livro(dados: LivroCadastroSchema):
    return add_livro(
        titulo=dados.titulo,
        autor=dados.autor,
        descricao=dados.descricao,
    )


@router.get("/")
def buscar_livro(titulo: str = ""):
    return busca_l_titulo(titulo)


@router.get("/{id_livro}")
def buscar_id_livro(id_livro: int):
    return busca_l_id(id_livro)


@router.delete("/{id_livro}")
def remover_livro(id_livro: int):
    return excluir_livro(id_livro)