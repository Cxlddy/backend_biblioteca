from .connection import banco


def criar_cursor():
    return banco.cursor(dictionary=True)


def buscar_emprestimo_ativo(id_usuario: int, id_livro: int):
    c = criar_cursor()
    try:
        query = """
            SELECT *
            FROM emprestimos
            WHERE usuario_id = %s
            AND livro_id = %s
            AND data_devolucao IS NULL
        """

        c.execute(query, (id_usuario, id_livro))

        resultado = c.fetchone()

        return resultado
    except Exception:
        import logging
        logging.exception("Error in buscar_emprestimo_ativo")
        return None
    finally:
        try:
            c.close()
        except Exception:
            pass


def criar_emprestimo(id_usuario: int, id_livro: int):
    c = criar_cursor()
    try:
        query = """
            INSERT INTO emprestimos (
                usuario_id,
                livro_id,
                data_emprestimo
            )
            VALUES (
                %s,
                %s,
                NOW()
            )
        """

        c.execute(query, (id_usuario, id_livro))

        banco.commit()

    except Exception:
        banco.rollback()
        import logging
        logging.exception("Error in criar_emprestimo")
        raise
    finally:
        try:
            c.close()
        except Exception:
            pass


def finalizar_emprestimo(id_emprestimo: int):
    c = criar_cursor()
    try:
        query = """
            UPDATE emprestimos
            SET data_devolucao = NOW()
            WHERE id = %s
        """

        c.execute(query, (id_emprestimo,))

        banco.commit()

    except Exception:
        banco.rollback()
        import logging
        logging.exception("Error in finalizar_emprestimo")
        raise
    finally:
        try:
            c.close()
        except Exception:
            pass


def listar_emprestimos():
    c = criar_cursor()

    c.execute("SELECT * FROM emprestimos")

    resultado = c.fetchall()

    c.close()

    return resultado


def listar_emprestimos_usuario(id_usuario: int):
    c = criar_cursor()

    query = """
        SELECT *
        FROM emprestimos
        WHERE usuario_id = %s
    """

    c.execute(query, (id_usuario,))

    resultado = c.fetchall()

    c.close()

    return resultado


def listar_emprestimos_livro(id_livro: int):
    c = criar_cursor()

    query = """
        SELECT *
        FROM emprestimos
        WHERE livro_id = %s
    """

    c.execute(query, (id_livro,))

    resultado = c.fetchall()

    c.close()

    return resultado