from Entidades.Partes.autor import AutorProcesso
from Entidades.Partes.advogado import Advogado
from Entidades.Partes.parceiro import Parceiro
from Util.enums import TipoProcesso
from dataclasses import dataclass

@dataclass
class Processo:
        autor: list[AutorProcesso]
        advogado: list[Advogado]
        parceiro: Parceiro
        tipo: TipoProcesso