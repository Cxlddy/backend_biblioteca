from pydantic import BaseModel, EmailStr


class UsuarioCadastroSchema(BaseModel):
    nome: str
    email: EmailStr
    senha: str


class UsuarioLoginSchema(BaseModel):
    email: EmailStr
    senha: str