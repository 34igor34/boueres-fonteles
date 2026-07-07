from __future__ import annotations

from abc import ABC
from dataclasses import dataclass
from datetime import date, datetime
from Entidades.processoAdministrativo import ProcessoAdministrativo
from Entidades.baseProcesso import Processo
# Resultado do benefício — só existe quando o processo é CONCLUÍDO

class ResultadoBeneficio(ABC):
    ...


@dataclass(frozen=True, slots=True)
class Concedido(ResultadoBeneficio):
    ...

@dataclass(frozen=True, slots=True)
class Indeferido(ResultadoBeneficio):
    motivo: str

    def __post_init__(self) -> None:
        if not self.motivo.strip():
            raise ValueError("Motivo do indeferimento não pode ser vazio.")


# Desfechos possíveis de um ProcessoAdministrativo
class Desfecho(ABC):
   #Classe base para os desfechos possíveis do processo
   ...


@dataclass(frozen=True, slots=True)
class Concluido(Desfecho):
    numero_beneficio: str
    resultado: ResultadoBeneficio


@dataclass(frozen=True, slots=True)
class Cancelado(Desfecho):
    data: date
    motivo: str

    def __post_init__(self) -> None:
        if not self.motivo.strip():
            raise ValueError("Motivo do cancelamento não pode ser vazio.")


@dataclass(frozen=True, slots=True)
class Exigencia(Desfecho):
    documentos: list  # list[Documento] — sua classe de validação existente
    prazo: date

    def __post_init__(self) -> None:
        if not self.documentos:
            raise ValueError("Exigência deve conter ao menos um documento.")

# Exemplo com match/case
def descrever_desfecho(desfecho: Desfecho | None) -> str:
    match desfecho:
        case None:
            return "Processo em andamento."
        case Concluido(numero_beneficio=nb, resultado=Concedido()):
            return f"Concedido. Benefício nº {nb}."
        case Concluido(numero_beneficio=nb, resultado=Indeferido(motivo=m)):
            return f"Indeferido (benefício nº {nb}). Motivo: {m}."
        case Cancelado(data=d, motivo=m):
            return f"Cancelado em {d}. Motivo: {m}."
        case Exigencia(documentos=docs, prazo=p):
            return f"Exigência aberta: {len(docs)} documento(s), prazo até {p}."
        case _:
            raise ValueError("Desfecho desconhecido.")