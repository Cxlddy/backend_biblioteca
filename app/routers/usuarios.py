from fastapi import APIRouter

from ..schemas.usuario import UsuarioCadastroSchema, UsuarioLoginSchema
from ..services.auth_services import criar_user, autenticar_usuario

router = APIRouter()


@router.post("/cadastro")
def cadastro(dados: UsuarioCadastroSchema):
    return criar_user(
        nome=dados.nome,
        email=dados.email,
        senha=dados.senha,
    )


@router.post("/login")
def login(dados: UsuarioLoginSchema):
    try:
        return autenticar_usuario(
            email=dados.email,
            senha=dados.senha,
        )
    except Exception:
        import logging
        logging.exception("Error in login endpoint")
        return {"sucesso": False, "mensagem": "Erro interno no servidor"}