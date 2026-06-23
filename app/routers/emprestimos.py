from fastapi import APIRouter

from ..schemas.emprestimo import EmprestimoSchema
from ..services.emprestimo_service import emprestar_livro, devolver_livro
from ..database.emprestimos import (
    listar_emprestimos,
    listar_emprestimos_usuario,
    listar_emprestimos_livro,
)

router = APIRouter()


@router.post("/")
def criar_emprestimo(dados: EmprestimoSchema):
    return emprestar_livro(
        id_usuario=dados.usuario_id,
        id_livro=dados.livro_id,
    )


@router.put("/devolver")
def remover_emprestimo(dados: EmprestimoSchema):
    return devolver_livro(
        id_usuario=dados.usuario_id,
        id_livro=dados.livro_id,
    )


@router.get("/")
def listar_todos_emprestimos():
    return listar_emprestimos()


@router.get("/usuario/{id_usuario}")
def listar_por_usuario(id_usuario: int):
    return listar_emprestimos_usuario(id_usuario)


@router.get("/livro/{id_livro}")
def listar_por_livro(id_livro: int):
    return listar_emprestimos_livro(id_livro)