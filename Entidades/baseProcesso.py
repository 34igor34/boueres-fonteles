from Entidades.autor import AutorProcesso
from Entidades.advogado import Advogado
from Entidades.parceiro import Parceiro
from Util.enums import TipoProcesso
class Processo:
    def __init__(
        self,
        autor: list[AutorProcesso],
        advogado: list[Advogado],
        parceiro: Parceiro,
        tipo: TipoProcesso
    ):
        self._autor = autor
        self._advogado = advogado
        self._parceiro = parceiro
        self._tipo = tipo

    @property
    def autor(self) -> list[AutorProcesso]:
        return self._autor

    @autor.setter
    def autor(self, autor):
        self._autor = autor

    @property
    def advogado(self) -> list[Advogado]:
        return self._advogado

    @advogado.setter
    def advogado(self, advogado):
        self._advogado = advogado

    @property
    def parceiro(self) -> Parceiro:
        return self._parceiro

    @parceiro.setter
    def parceiro(self, parceiro):
        self._parceiro = parceiro

    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, tipo):
        self._tipo = tipo