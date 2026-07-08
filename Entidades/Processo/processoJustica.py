from Entidades.Partes.basePessoa import Pessoa
from Entidades.Partes.advogado import Advogado
from Entidades.Partes.parceiro import Parceiro
from Entidades.Processo.baseProcesso import Processo
from Util.enums import CodigoProcesso
from Util.value_objects import NumeroProcesso, DataDistribuicao, Jurisdicao
from dataclasses import dataclass

@dataclass
class ProcessoJustica(Processo):
        numero_processo: NumeroProcesso
        partes: list[Pessoa]
        advogado: list[Advogado]
        parceiro: Parceiro
        data_distribuicao: DataDistribuicao
        jurisdicao: Jurisdicao
        assuntos: list[CodigoProcesso]
        # Adicionar suporte a cada tipo descrito abaixo
        assunto_principal: str
        status: str
        valor_causa: str
        orgao_julgador: str
        reu: str
        audiencias: list[str]
        sentenca: str
        classe_judicial: str
