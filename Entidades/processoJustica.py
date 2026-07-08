from Entidades.autor import AutorProcesso
from Entidades.advogado import Advogado
from Entidades.parceiro import Parceiro
from Entidades.baseProcesso import Processo
from Util.enums import TipoProcesso, CodigoProcesso
from Util.value_objects import NumeroProcesso, DataAjuizamento
from dataclasses import dataclass

@dataclass
class ProcessoJustica(Processo):
        autor: list[AutorProcesso]
        advogado: list[Advogado]
        parceiro: Parceiro
        numero_processo: NumeroProcesso
        data_ajuizamento: DataAjuizamento
        codigos: list[CodigoProcesso]