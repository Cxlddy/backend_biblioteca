from pydantic import BaseModel


class LivroCadastroSchema(BaseModel):
    titulo: str
    autor: str
    descricao: str


class LivroBuscaSchema(BaseModel):
    titulo: str


class LivroIdSchema(BaseModel):
    id_livro: int