from pydantic import BaseModel


class EmprestimoSchema(BaseModel):
    usuario_id: int
    livro_id: int