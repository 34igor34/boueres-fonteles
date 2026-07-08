from Entidades.autor import AutorProcesso
from Entidades.advogado import Advogado
from Entidades.parceiro import Parceiro
from Util.enums import TipoProcesso
from dataclasses import dataclass

@dataclass
class Processo:
        autor: list[AutorProcesso]
        advogado: list[Advogado]
        parceiro: Parceiro
        tipo: TipoProcesso