from fastapi import FastAPI

TAREFAS = [{"id": 1, "titulo": "Tarefa 1"}]

app = FastAPI()

@app.get('/tarefas')
def listar():
    return TAREFAS