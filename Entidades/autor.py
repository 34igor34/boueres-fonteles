from Entidades.basePessoa import Pessoa
from Util.value_objects import _coagir, CPF
class AutorProcesso(Pessoa):
    def __init__(self, nome, tipo, cpf):
        super().__init__(nome, tipo)
        self.cpf = cpf

    @property
    def cpf(self) -> CPF:
        return self._cpf

    @cpf.setter
    def cpf(self, cpf):
        self._cpf = _coagir(cpf, CPF)