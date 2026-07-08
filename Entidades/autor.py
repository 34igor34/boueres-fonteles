from Entidades.basePessoa import Pessoa, TipoParte
from Util.value_objects import CPF
from dataclasses import dataclass

@dataclass
class AutorProcesso(Pessoa):
    cpf = CPF

    @classmethod
    def criar(cls, nome: str, tipo: TipoParte, cpf: str ):
        pessoa = super().criar(nome, tipo)
        return cls(nome=pessoa.nome, tipo=pessoa.tipo)
