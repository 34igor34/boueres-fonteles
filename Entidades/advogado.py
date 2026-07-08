from Entidades.basePessoa import Pessoa
from Util.value_objects import OAB
from dataclasses import dataclass
from Util.enums import TipoParte

@dataclass
class Advogado(Pessoa):
    oba: OAB
    @classmethod
    def criar(cls, nome: str, tipo: TipoParte, oab: str):
        pessoa = super().criar(nome, tipo)
        
        return cls(
            nome=pessoa.nome,
            tipo=pessoa.tipo,
            oab=OAB(oab),
        )