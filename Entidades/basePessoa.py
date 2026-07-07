from Util.enums import TipoParte
from Util.value_objects import _coagir, Nome
class Pessoa:
    def __init__(self, nome, tipo: TipoParte):
        self.nome = nome
        self._tipo = tipo

    @property
    def nome(self) -> Nome:
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = _coagir(nome, Nome)

    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, tipo):
        self._tipo = tipo