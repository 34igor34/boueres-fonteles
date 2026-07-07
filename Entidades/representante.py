from Entidades.basePessoa import Pessoa
from Util.enums import TipoRepresentante
from Util.value_objects import _coagir, CPF

class RepresentanteProcesso(Pessoa):
    def __init__(self, nome, tipo, cpf, tipoRepresentante: TipoRepresentante):
        super().__init__(nome, tipo)
        self.cpf = cpf
        self.tipoRepresentante = tipoRepresentante

    @property
    def cpf(self) -> CPF:
        return self._cpf

    @cpf.setter
    def cpf(self, cpf):
        self._cpf = _coagir(cpf, CPF)

    @property
    def tipoRepresentante(self):
        return self._tipo_representante

    @tipoRepresentante.setter
    def tipoRepresentante(self, tipo):
        if isinstance(tipo, TipoRepresentante):
            self._tipo_representante = tipo
        elif isinstance(tipo, str):
            try:
                # tenta por nome da enum (MAE, PAI, ...)
                self._tipo_representante = TipoRepresentante[tipo]
            except KeyError:
                # tenta pelo valor ("mãe", "pai", ...)
                self._tipo_representante = TipoRepresentante(tipo.lower())
        else:
            raise ValueError("tipoRepresentante inválido")