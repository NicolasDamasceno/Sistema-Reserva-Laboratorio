from fastapi import APIRouter, HTTPException, status
import json
import uuid
from datetime import date
from pathlib import Path
from app.schemas.reserva_schema import ReservaCriar, AvaliarReserva, ReservaResposta

router = APIRouter(prefix='/reservas', tags=['Reservas'])
DATA_FILE = Path('data/reservas.json')

def load_data():
    if not DATA_FILE.exists():
        return []
    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

@router.post('/', response_model=ReservaResposta, status_code=201)
def solicitar_reserva(dados: ReservaCriar):
    reservas = load_data()
    nova_reserva = {
        "id": str(uuid.uuid4()),
        "laboratorio_id": dados.laboratorio_id,
        "solicitante": dados.solicitante,
        "data": dados.data,
        "hora_inicio": dados.hora_inicio,
        "hora_fim": dados.hora_fim,
        "status": "pendente",
        "justificativa": None,
        "data_cancelamento": None
    }
    reservas.append(nova_reserva)
    save_data(reservas)
    return nova_reserva

@router.get('/', response_model=list[ReservaResposta])
def listar_reservas():
    return load_data()

@router.get('/{id}', response_model=ReservaResposta)
def buscar_reserva(id: str):
    reservas = load_data()
    for r in reservas:
        if r['id'] == id:
            return r
    raise HTTPException(status_code=404, detail="Reserva não encontrada")

@router.patch('/{id}/avaliar', response_model=ReservaResposta)
def avaliar_reserva(id: str, dados: AvaliarReserva):
    reservas = load_data()
    for r in reservas:
        if r['id'] == id:
            r['status'] = "aprovada" if dados.acao == "aprovar" else "rejeitada"
            r['justificativa'] = dados.justificativa
            save_data(reservas)
            return r
    raise HTTPException(status_code=404, detail="Reserva não encontrada")

@router.patch('/{id}/cancelar', response_model=ReservaResposta)
def cancelar_reserva(id: str, solicitante: str):
    reservas = load_data()
    for r in reservas:
        if r['id'] == id:
            if r['solicitante'].lower() != solicitante.lower():
                raise HTTPException(status_code=422, detail="Somente o solicitante pode cancelar a reserva.")
            r['status'] = "cancelada"
            r['data_cancelamento'] = str(date.today())
            save_data(reservas)
            return r
    raise HTTPException(status_code=404, detail="Reserva não encontrada")