import logging
from .connection import banco


def criar_cursor():
    return banco.cursor(dictionary=True)

# ==========================
# USUÁRIOS
# ==========================

def criar_usuario(nome: str, email: str, senha: str):
    c = criar_cursor()

    try:
        query = """
            INSERT INTO usuarios (
                nome,
                email,
                senha
            )
            VALUES (%s, %s, %s)
        """

        valores = (nome, email, senha)

        c.execute(query, valores)

        banco.commit()

        return {
            "sucesso": True,
            "mensagem": "Usuário criado com sucesso"
        }

    except Exception as e:
        banco.rollback()

        return {
            "sucesso": False,
            "mensagem": str(e)
        }

    finally:
        c.close()


def fazer_login(email: str):
    c = criar_cursor()
    try:
        query = """
            SELECT *
            FROM usuarios
            WHERE email = %s
        """

        c.execute(query, (email,))

        user = c.fetchone()

        if user is None:
            return None

        # Normalize keys to lowercase so callers can rely on 'id', 'nome', 'email'
        normalized = {k.lower(): v for k, v in user.items()}
        return normalized
    except Exception as e:
        logging.exception("Error in fazer_login")
        return None
    finally:
        try:
            c.close()
        except Exception:
            pass


# =========================
# BUSCAS
# =========================

def busca_u_nome(nome: str):
    if not nome.strip():
        return []

    c = criar_cursor()
    try:
        palavras = nome.strip().split()

        query = """
            SELECT * FROM usuarios WHERE
        """

        condicoes = []

        for palavra in palavras:
            condicoes.append("nome LIKE %s")

        query += " OR ".join(condicoes)

        valores = []

        for palavra in palavras:
            valores.append(f"%{palavra}%")

        c.execute(query, valores)

        r = c.fetchall()

        return r
    except Exception:
        logging.exception("Error in busca_u_nome")
        return []
    finally:
        try:
            c.close()
        except Exception:
            pass


def busca_u_id(id_usuario: int):
    c = criar_cursor()
    try:
        query = """
            SELECT * FROM usuarios
            WHERE id = %s
        """

        c.execute(query, (id_usuario,))

        r = c.fetchone()

        if r is None:
            return None

        normalized = {k.lower(): v for k, v in r.items()}
        return normalized
    except Exception:
        logging.exception("Error in busca_u_id")
        return None
    finally:
        try:
            c.close()
        except Exception:
            pass