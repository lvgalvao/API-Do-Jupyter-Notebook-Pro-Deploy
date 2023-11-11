from fastapi import FastAPI  # Importa a classe FastAPI do framework FastAPI.
from .router import router  # Importa o objeto 'router' do módulo 'router' local.

app = FastAPI()  # Cria uma instância do aplicativo FastAPI.
# 'app' é a instância central do seu aplicativo web.

app.include_router(router)  # Anexa o roteador 'router' ao aplicativo FastAPI.
# Isso registra todas as rotas e operações definidas em 'router' no aplicativo.
