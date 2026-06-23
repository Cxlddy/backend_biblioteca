import logging
from .connection import banco


def criar_cursor():
    return banco.cursor(dictionary=True)

# ==========================
# LIVROS
# ==========================

def add_livro(titulo: str, autor: str, descricao: str):
    c = criar_cursor()

    try:
        query = """
            INSERT INTO livros (
                titulo,
                autor,
                descricao
            )
            VALUES (%s, %s, %s)
        """

        valores = (titulo, autor, descricao)

        c.execute(query, valores)

        banco.commit()

        return {
            "sucesso": True,
            "mensagem": "Livro adicionado com sucesso"
        }

    except Exception as e:
        banco.rollback()

        return {
            "sucesso": False,
            "mensagem": str(e)
        }

    finally:
        c.close()


def excluir_livro(id_livro: int):
    c = criar_cursor()

    try:
        query = """
            DELETE FROM livros
            WHERE id = %s
        """

        c.execute(query, (id_livro,))

        banco.commit()

        return {
            "sucesso": True,
            "mensagem": "Livro removido com sucesso"
        }

    except Exception as e:
        banco.rollback()

        return {
            "sucesso": False,
            "mensagem": str(e)
        }

    finally:
        c.close()


# ==========================
# BUSCAS
# ==========================

def busca_l_titulo(titulo: str):
    if not titulo.strip():
        return []

    c = criar_cursor()
    try:
        palavras = titulo.split()

        query = """
            SELECT * FROM livros WHERE
        """

        condicoes = []

        for palavra in palavras:
            condicoes.append("titulo LIKE %s")

        query += " OR ".join(condicoes)

        valores = []

        for palavra in palavras:
            valores.append(f"%{palavra}%")

        c.execute(query, valores)

        r = c.fetchall()

        return r
    except Exception:
        logging.exception("Error in busca_l_titulo")
        return []
    finally:
        try:
            c.close()
        except Exception:
            pass


def busca_l_id(id_livro: int):
    c = criar_cursor()
    try:
        query = """
            SELECT * FROM livros
            WHERE id = %s
        """

        c.execute(query, (id_livro,))

        r = c.fetchone()

        return r
    except Exception:
        logging.exception("Error in busca_l_id")
        return None
    finally:
        try:
            c.close()
        except Exception:
            pass


def marcar_livro_indisponivel(id_livro: int):
    c = criar_cursor()

    try:
        query = """
            UPDATE livros
            SET disponivel = FALSE
            WHERE id = %s
        """

        c.execute(query, (id_livro,))

        banco.commit()

        return True

    except Exception:
        banco.rollback()
        return False

    finally:
        c.close()


def marcar_livro_disponivel(id_livro: int):
    c = criar_cursor()

    try:
        query = """
            UPDATE livros
            SET disponivel = TRUE
            WHERE id = %s
        """

        c.execute(query, (id_livro,))

        banco.commit()

        return True

    except Exception:
        banco.rollback()
        return False

    finally:
        c.close()


def incrementar_emprestimos(id_livro: int):
    c = criar_cursor()

    try:
        query = """
            UPDATE livros
            SET total_emprestimos = total_emprestimos + 1
            WHERE id = %s
        """

        c.execute(query, (id_livro,))

        banco.commit()

        return True

    except Exception:
        banco.rollback()
        return False

    finally:
        c.close()