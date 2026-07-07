from Entidades.basePessoa import Pessoa
from Util.value_objects import Contato
from Util.value_objects import _coagir

class Parceiro(Pessoa):
    def __init__(self, nome, tipo, contato=None):
        super().__init__(nome, tipo)
        self.contato = contato

    @property
    def contato(self) -> Contato | None:
        return self._contato

    @contato.setter
    def contato(self, contato):
        self._contato = _coagir(contato, Contato)