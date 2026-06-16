from fastapi import FastAPI

app = FastAPI(
    title="Sistema de Reserva de Laboratórios",
    description="IFPI TADS — Engenharia de Software II",
    version="1.0.0",
)


@app.get("/")
def root():
    return {"message": "API de Reserva de Laboratórios — acesse /docs"}