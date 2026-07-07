from Entidades.basePessoa import Pessoa
from Util.enums import TipoParte
from Util.value_objects import _coagir, OAB
class Advogado(Pessoa):
    def __init__(self, nome, tipo: TipoParte, oab):
        super().__init__(nome, tipo)
        self.oab = oab

    @property
    def oab(self) -> OAB:
        return self._oab

    @oab.setter
    def oab(self, oab):
        self._oab = _coagir(oab, OAB)