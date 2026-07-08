from Entidades.Partes.basePessoa import Pessoa
from Util.value_objects import Contato
from dataclasses import dataclass

@dataclass
class Parceiro(Pessoa):
    contato: Contato | None