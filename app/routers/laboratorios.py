from fastapi import APIRouter, HTTPException, status
from app.services.laboratorio_services import LaboratorioService
from app.repositories.laboratorio_repo import LaboratorioRepository
from app.schemas.laboratorio_schema import(
    LaboratorioCriar, 
    LaboratorioAtualizar, 
    LaboratorioResposta)

from app.exceptions.custom_exceptions import (
    NomeDuplicado,
    LaboratorioNaoEncontrado)

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

@router.get('/{id}', response_model=LaboratorioResposta)
def buscar_laboratorio(id: str):
    try:
        lab = service.buscar(id)
        return LaboratorioResposta(**lab.to_dict())
    except LaboratorioNaoEncontrado as e:
        raise HTTPException(
            status_code=404,
            detail=str(e)
        )


@router.put('/{id}', response_model=LaboratorioResposta)
def atualizar_laboratorio(
    id: str,
    dados: LaboratorioAtualizar
):
    try:
        lab = service.atualizar(id, dados)
        return LaboratorioResposta(**lab.to_dict())

    except LaboratorioNaoEncontrado as e:
        raise HTTPException(
            status_code=404,
            detail=str(e)
        )

    except NomeDuplicado as e:
        raise HTTPException(
            status_code=409,
            detail=str(e)
        )