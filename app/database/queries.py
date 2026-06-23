from .connection import banco


def criar_cursor():
    return banco.cursor(dictionary=True)


# ==========================
# LISTAGENS
# ==========================

def ver_livros():
    c = criar_cursor()

    c.execute("SELECT * FROM livros")

    r = c.fetchall()

    c.close()

    return r


def ver_usuarios():
    c = criar_cursor()

    c.execute("SELECT * FROM usuarios")

    r = c.fetchall()

    c.close()

    return r


def ver_emprestimos():
    c = criar_cursor()

    c.execute("SELECT * FROM emprestimos")

    r = c.fetchall()

    c.close()

    return r


def ver_emprestimo_u(id_usuario: int):
    c = criar_cursor()

    query = """
        SELECT *
        FROM emprestimos
        WHERE usuario_id = %s
    """

    c.execute(query, (id_usuario,))

    r = c.fetchall()

    c.close()

    return r


def ver_emprestimo_l(id_livro: int):
    c = criar_cursor()

    query = """
        SELECT *
        FROM emprestimos
        WHERE livro_id = %s
    """

    c.execute(query, (id_livro,))

    r = c.fetchall()

    c.close()

    return r