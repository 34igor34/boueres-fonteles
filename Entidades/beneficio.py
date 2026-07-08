from dataclasses import dataclass
from Util.value_objects import NumeroBeneficio, Nome

@dataclass
class Beneficio:
    numero: NumeroBeneficio
    beneficiario: Nome
    data_inicio: str
    data_fim: str
    tipo: str

    @classmethod
    def criar(cls, numero: str, beneficiario:str, data_inicio: str, data_fim: str, tipo: str):
        return cls(numero=NumeroBeneficio(numero),beneficiario=Nome(beneficiario),data_inicio = data_inicio,
            data_fim= data_fim,tipo = tipo)