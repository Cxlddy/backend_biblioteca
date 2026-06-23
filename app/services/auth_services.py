import hashlib

from ..database.usuarios import criar_usuario, fazer_login as buscar_usuario_por_email


def criar_user(nome: str, email: str, senha: str):
    senha_hash = hashlib.sha256(senha.encode()).hexdigest()

    return criar_usuario(
        nome=nome,
        email=email,
        senha=senha_hash,
    )


def autenticar_usuario(email: str, senha: str):
    try:
        usuario = buscar_usuario_por_email(email)

        if usuario is None:
            return {
                "sucesso": False,
                "mensagem": "Usuário não encontrado",
            }

        senha_hash = hashlib.sha256(senha.encode()).hexdigest()

        # Normalize stored password (handle bytes)
        senha_db = None
        if isinstance(usuario, dict):
            senha_db = usuario.get("senha")
        else:
            senha_db = None

        if isinstance(senha_db, (bytes, bytearray)):
            try:
                senha_db = senha_db.decode()
            except Exception:
                senha_db = str(senha_db)

        if senha_db is None:
            return {"sucesso": False, "mensagem": "Credenciais inválidas"}

        if senha_hash != senha_db:
            return {"sucesso": False, "mensagem": "Senha incorreta"}

        usuario_out = {
            "id": usuario.get("id") if isinstance(usuario, dict) else None,
            "nome": usuario.get("nome") if isinstance(usuario, dict) else None,
            "email": usuario.get("email") if isinstance(usuario, dict) else None,
        }

        return {"sucesso": True, "mensagem": "Login realizado com sucesso", "usuario": usuario_out}
    except Exception:
        import logging
        logging.exception("Error in autenticar_usuario")
        return {"sucesso": False, "mensagem": "Erro interno no servidor"}