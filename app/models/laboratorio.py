from enum import Enum


class StatusLaboratorio(str, Enum):
    ATIVO = "ativo"
    INATIVO = "inativo"