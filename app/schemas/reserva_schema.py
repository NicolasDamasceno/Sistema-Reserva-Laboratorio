from pydantic import BaseModel, Field
from typing import Optional
from app.models.reserva import StatusReserva

class ReservaCriar(BaseModel):
    laboratorio_id: str
    solicitante: str = Field(..., min_length=2)
    data: str = Field(..., pattern=r'^\d{4}-\d{2}-\d{2}$')
    hora_inicio: str = Field(..., pattern=r'^\d{2}:\d{2}$')
    hora_fim: str = Field(..., pattern=r'^\d{2}:\d{2}$')

class AvaliarReserva(BaseModel):
    acao: str = Field(..., pattern='^(aprovar|rejeitar)$')
    justificativa: Optional[str] = None

class ReservaResposta(BaseModel):
    id: str
    laboratorio_id: str
    solicitante: str
    data: str
    hora_inicio: str
    hora_fim: str
    status: StatusReserva
    justificativa: Optional[str] = None
    data_cancelamento: Optional[str] = None