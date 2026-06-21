from app.repositories.laboratorio_repo import LaboratorioRepository
from app.models.laboratorio import Laboratorio
from app.schemas.laboratorio_schema import LaboratorioCriar
from app.exceptions.custom_exceptions import NomeDuplicado

class LaboratorioService:

    def __init__(self, repo: LaboratorioRepository):
        self.repo = repo

    def cadastrar(self, dados: LaboratorioCriar) -> Laboratorio:
        if self.repo.buscar_por_nome(dados.nome):
            raise NomeDuplicado(f'Laboratório com nome "{dados.nome}" já existe.')
        lab = Laboratorio(id='', nome=dados.nome, capacidade=dados.capacidade)
        return self.repo.salvar(lab)

    def listar(self) -> list[Laboratorio]:
        return self.repo.listar()