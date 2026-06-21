from fastapi import APIRouter, HTTPException, status
from app.services.laboratorio_services import LaboratorioService
from app.repositories.laboratorio_repo import LaboratorioRepository
from app.schemas.laboratorio_schema import LaboratorioCriar, LaboratorioResposta
from app.exceptions.custom_exceptions import NomeDuplicado

router = APIRouter(prefix='/laboratorios', tags=['Laboratórios'])
service = LaboratorioService(LaboratorioRepository())

@router.post('/', response_model=LaboratorioResposta, status_code=status.HTTP_201_CREATED)
def cadastrar_laboratorio(dados: LaboratorioCriar):
    try:
        lab = service.cadastrar(dados)
        return LaboratorioResposta(**lab.to_dict())
    except NomeDuplicado as e:
        raise HTTPException(status_code=409, detail=str(e))

@router.get('/', response_model=list[LaboratorioResposta])
def listar_laboratorios():
    labs = service.listar()
    return [LaboratorioResposta(**l.to_dict()) for l in labs]