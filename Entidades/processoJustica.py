from Entidades.autor import AutorProcesso
from Entidades.advogado import Advogado
from Entidades.parceiro import Parceiro
from Entidades.baseProcesso import Processo
from Util.enums import TipoProcesso, CodigoProcesso
from Util.value_objects import _coagir, NumeroProcesso, DataAjuizamento

class ProcessoJustica(Processo):
    def __init__(
        self,
        autor: list[AutorProcesso],
        advogado: list[Advogado],
        parceiro: Parceiro,
        numero_processo: NumeroProcesso,
        data_ajuizamento: DataAjuizamento,
        codigos: list[CodigoProcesso],
    ):
        super().__init__(autor, advogado, parceiro, TipoProcesso.JUSTICA)
        self._numero_processo = numero_processo
        self._codigos = codigos
        self._data_ajuizamento = data_ajuizamento
    
    @property
    def data_ajuizamento(self) -> DataAjuizamento:
        return self._data_ajuizamento
    
    @data_ajuizamento.setter
    def data_ajuizamento(self, data: DataAjuizamento):
        self._data_ajuizamento = data

    @property
    def numero_processo(self) -> NumeroProcesso:
        return self._numero_processo

    @numero_processo.setter
    def numero_processo(self, numero_processo):
        self._numero_processo = _coagir(numero_processo, NumeroProcesso)

    @property
    def codigo(self):
        return self._codigos

    @codigo.setter
    def codigo(self, codigo):
        self._codigos = codigo