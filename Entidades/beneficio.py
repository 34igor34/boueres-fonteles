from dataclasses import dataclass
from Util.value_objects import NumeroBeneficio

@dataclass
#Padrão 000.000.000-0
class Beneficio:
    numero: NumeroBeneficio
    data_inicio: str
    data_fim: str
    tipo: str

    @classmethod
    def criar(cls, numero: str, data_inicio: str, data_fim: str, tipo: str):
        return cls(
            numero=NumeroBeneficio(numero),
            data_inicio = data_inicio,
            data_fim= data_fim,
            tipo = tipo
        )