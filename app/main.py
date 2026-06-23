from fastapi import FastAPI

from .routers import usuarios, livros, emprestimos

app = FastAPI(title="API Biblioteca")

app.include_router(usuarios.router, prefix="/usuarios", tags=["Usuários"])
app.include_router(livros.router, prefix="/livros", tags=["Livros"])
app.include_router(emprestimos.router, prefix="/emprestimos", tags=["Empréstimos"])


@app.get("/")
def home():
    return {"mensagem": "API Biblioteca funcionando"}