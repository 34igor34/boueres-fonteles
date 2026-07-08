from Util.enums import TipoParte
from Util.value_objects import Nome
from dataclasses import dataclass

@dataclass(frozen=True)
class Pessoa:
    nome: Nome
    tipo_parte: TipoParte
    
    @classmethod
    def criar(cls, nome: str, tipo_parte: TipoParte):
        return cls(
            nome=Nome(nome),
            tipo_parte=tipo_parte
        )