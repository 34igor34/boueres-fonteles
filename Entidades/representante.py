from Entidades.basePessoa import Pessoa
from Util.enums import TipoRepresentante, TipoParte
from Util.value_objects import CPF
from dataclasses import dataclass

@dataclass
class RepresentanteProcesso(Pessoa):
    cpf = CPF
    tipoRepresentante: TipoRepresentante

    @classmethod
    def criar(
        cls, nome: str, tipo: TipoParte, tipo_representante: str, cpf:str):
            pessoa = super().criar(nome, tipo)

            return cls(nome=pessoa.nome, tipo=pessoa.tipo, _cpf=CPF(cpf), tipo_representante=TipoRepresentante(tipo_representante),)