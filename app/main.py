from fastapi import FastAPI
# from app.routers import laboratorios Próximas Tasks
from app.routers import reserva_router

app = FastAPI(
    title="Sistema de Reserva de Laboratórios",
    description="IFPI TADS — Engenharia de Software II",
    version="1.0.0",
)

# app.include_router(laboratorios.router) Próximas Tasks
app.include_router(reserva_router.router)

@app.get("/")
def root():
    return {"message": "API de Reserva de Laboratórios — acesse /docs"}