from typing import Type, TypeVar, overload
from dataclasses import dataclass
import re
T = TypeVar("T")

PADRAO_NUM_BENEFICIO = r'^\d{3}\.\d{3}\.\d{3}-\d$'

class NumeroBeneficio:
    #Padrão 000.000.000-0
    def __init__(self, valor: str):
        if valor is None or not str(valor).strip():
            raise ValueError("Numero de benefício inválido: não pode ser vazio")
        if not re.fullmatch(PADRAO_NUM_BENEFICIO, valor):
            raise ValueError("Numero de benefício inválido: valor incompátivel com padrão")

        self._valor = str(valor).strip()

    @property
    def valor(self) -> str:
        return self._valor
    
@dataclass
class Jurisdicao:
    orgao: str
    regiao: str
    secao_judiciaria: str

class DataEntradaRequerimento:
    #Formato de data esperado: DD/MM/YYYY HH:MM
    def __init__(self, valor: str):
        pass
    
    #Formato de data esperado: DD/MM/YYYY HH:MM

class DataDistribuicao:
    def __init__(self):
        pass

class Nome:
    """Nome de uma pessoa. Não pode ser vazio."""
    def __init__(self, valor: str):
        if valor is None or not str(valor).strip():
            raise ValueError("Nome inválido: não pode ser vazio")
        self._valor = str(valor).strip()

    @property
    def valor(self) -> str:
        return self._valor

    def __str__(self) -> str:
        return self._valor

    def __repr__(self) -> str:
        return f"Nome('{self._valor}')"

    def __eq__(self, other) -> bool:
        return isinstance(other, Nome) and self._valor.lower() == other._valor.lower()

    def __hash__(self) -> int:
        return hash(self._valor.lower())

class CPF:
    """CPF com validação dos dígitos verificadores (algoritmo oficial)."""

    def __init__(self, valor: str):
        digitos = re.sub(r"\D", "", valor or "")
        if len(digitos) != 11:
            raise ValueError(f"CPF inválido: '{valor}' deve conter 11 dígitos")
        if not self._digitos_validos(digitos):
            raise ValueError(f"CPF inválido: '{valor}' — dígitos verificadores incorretos")
        self._valor = digitos

    @staticmethod
    def _digitos_validos(cpf: str) -> bool:
        if cpf == cpf[0] * 11:  # ex: 111.111.111-11
            return False

        def calc_digito(parcial: str) -> int:
            soma = sum(
                int(d) * peso
                for d, peso in zip(parcial, range(len(parcial) + 1, 1, -1))
            )
            resto = soma % 11
            return 0 if resto < 2 else 11 - resto

        d1 = calc_digito(cpf[:9])
        d2 = calc_digito(cpf[:9] + str(d1))
        return cpf[-2:] == f"{d1}{d2}"

    @property
    def valor(self) -> str:
        """Apenas os 11 dígitos, sem formatação."""
        return self._valor

    def formatado(self) -> str:
        v = self._valor
        return f"{v[:3]}.{v[3:6]}.{v[6:9]}-{v[9:]}"

    def __str__(self) -> str:
        return self.formatado()

    def __repr__(self) -> str:
        return f"CPF('{self.formatado()}')"

    def __eq__(self, other) -> bool:
        return isinstance(other, CPF) and self._valor == other._valor

    def __hash__(self) -> int:
        return hash(self._valor)

class OAB:
    """Número de inscrição na OAB, no formato NNNNNN/UF."""

    _PADRAO = re.compile(r"^(\d{1,6})[/\-]?\s*([A-Za-z]{2})$")

    def __init__(self, valor: str):
        if not valor:
            raise ValueError("OAB inválida: valor não pode ser vazio")
        m = self._PADRAO.match(valor.strip())
        if not m:
            raise ValueError(f"OAB inválida: '{valor}' — formato esperado NNNNNN/UF")
        self._numero = m.group(1)
        self._uf = m.group(2).upper()

    @property
    def numero(self) -> str:
        return self._numero

    @property
    def uf(self) -> str:
        return self._uf

    def formatado(self) -> str:
        return f"{self._numero}/{self._uf}"

    def __str__(self) -> str:
        return self.formatado()

    def __repr__(self) -> str:
        return f"OAB('{self.formatado()}')"

    def __eq__(self, other) -> bool:
        return isinstance(other, OAB) and self._numero == other._numero and self._uf == other._uf

    def __hash__(self) -> int:
        return hash((self._numero, self._uf))

class NumeroProcesso:
    """Número Único de Processo (padrão CNJ): NNNNNNN-DD.AAAA.J.TR.OOOO"""

    _PADRAO = re.compile(r"^\d{7}-\d{2}\.\d{4}\.\d\.\d{2}\.\d{4}$")

    def __init__(self, valor: str):
        if not valor or not self._PADRAO.match(valor.strip()):
            raise ValueError(
                f"Número de processo inválido: '{valor}' — "
                "formato esperado NNNNNNN-DD.AAAA.J.TR.OOOO"
            )
        self._valor = valor.strip()

    @property
    def valor(self) -> str:
        return self._valor

    def __str__(self) -> str:
        return self._valor

    def __repr__(self) -> str:
        return f"NumeroProcesso('{self._valor}')"

    def __eq__(self, other) -> bool:
        return isinstance(other, NumeroProcesso) and self._valor == other._valor

    def __hash__(self) -> int:
        return hash(self._valor)

class NumeroProtocolo:
    """Protocolo de requerimento administrativo (ex.: INSS). Só dígitos, 9 a 15 posições."""

    _PADRAO = re.compile(r"^\d{9,15}$")

    def __init__(self, valor: str):
        digitos = re.sub(r"\D", "", valor or "")
        if not self._PADRAO.match(digitos):
            raise ValueError(f"Protocolo inválido: '{valor}' deve conter entre 9 e 15 dígitos")
        self._valor = digitos

    @property
    def valor(self) -> str:
        return self._valor

    def __str__(self) -> str:
        return self._valor

    def __repr__(self) -> str:
        return f"ProtocoloRequerimento('{self._valor}')"

    def __eq__(self, other) -> bool:
        return isinstance(other, ProtocoloRequerimento) and self._valor == other._valor

    def __hash__(self) -> int:
        return hash(self._valor)

class Contato:
    """Contato de um parceiro: e-mail ou telefone, detectado automaticamente."""

    _EMAIL = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")
    _TELEFONE = re.compile(r"^\+?\d{10,13}$")

    def __init__(self, valor: str):
        if not valor:
            raise ValueError("Contato inválido: não pode ser vazio")
        v = valor.strip()
        digitos = re.sub(r"\D", "", v)
        if self._EMAIL.match(v):
            self._tipo = "email"
            self._valor = v.lower()
        elif self._TELEFONE.match(digitos):
            self._tipo = "telefone"
            self._valor = digitos
        else:
            raise ValueError(f"Contato inválido: '{valor}' não é um e-mail nem telefone válido")

    @property
    def tipo(self) -> str:
        return self._tipo

    @property
    def valor(self) -> str:
        return self._valor

    def __str__(self) -> str:
        return self._valor

    def __repr__(self) -> str:
        return f"Contato('{self._valor}', tipo='{self._tipo}')"

    def __eq__(self, other) -> bool:
        return isinstance(other, Contato) and self._valor == other._valor

    def __hash__(self) -> int:
        return hash(self._valor)

@overload
def _coagir(valor: object, classe: Type[Contato] | Type[ProtocoloRequerimento]) -> Contato | None:
    ...

@overload
def _coagir(valor: object, classe: Type[T]) -> T:
    ...
    
def _coagir(valor, classe):
    # Verifica se o valor passado é diferente de None e adiciona uma camada de aceitação prática aos campos
    if valor is None:
        if classe is Contato:
            return None
        raise ValueError(f"{classe.__name__} inválido: não pode ser None")
    
    if isinstance(valor, classe):
        return valor
    return classe(valor)