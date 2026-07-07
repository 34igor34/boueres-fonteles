from Entidades.autor import AutorProcesso
from Entidades.advogado import Advogado
from Entidades.parceiro import Parceiro
from Entidades.baseProcesso import Processo
from Entidades.desfecho_processo_adm import Desfecho, Exigencia, Cancelado, Concluido, ResultadoBeneficio
from datetime import date
from dataclasses import dataclass
from Util.enums import TipoProcesso
from Util.value_objects import ProtocoloRequerimento, DataEntrada, _coagir

@dataclass(slots=True)
class ProcessoAdministrativo(Processo):
    #protocolo_requerimento recebe None para dar suporte ao modelo atual
    def __init__(
        self,
        autor: list[AutorProcesso],
        advogado: list[Advogado],
        parceiro: Parceiro,
        data_entrada:DataEntrada,
        protocolo_requerimento = None,
        desfecho: Desfecho | None = None  # None enquanto o processo está em andamento
    ):
        super().__init__(autor, advogado, parceiro, TipoProcesso.ADMINISTRATIVO)
        self.protocolo_requerimento = protocolo_requerimento
        self.data_entrada = data_entrada

    @property
    def data_entrada(self) -> DataEntrada:
        return self.data_entrada
    
    @data_entrada.setter
    def data_entrada(self, data: DataEntrada):
        self.data_entrada = data

    @property
    def protocolo_requerimento(self) -> ProtocoloRequerimento:
        return self._protocolo_requerimento

    @protocolo_requerimento.setter
    def protocolo_requerimento(self, protocolo_requerimento):
        self._protocolo_requerimento = _coagir(protocolo_requerimento, ProtocoloRequerimento)
    
    def concluir(self, numero_beneficio: str, resultado: ResultadoBeneficio) -> None:
        self.desfecho = Concluido(numero_beneficio, resultado)
    
    def cancelar(self, data: date, motivo: str) -> None:
        self.desfecho = Cancelado(data, motivo)
    
    def abrir_exigencia(self, documentos: list, prazo: date) -> None:
        self.desfecho = Exigencia(documentos, prazo)
    
    def cancelar_por_exigencia_nao_cumprida(self, hoje: date) -> None:
        #Chamar numa rotina agendada quando o prazo de uma exigência expirar sem cumprimento."""
        if isinstance(self.desfecho, Exigencia) and hoje > self.desfecho.prazo:
            self.desfecho = Cancelado(data=hoje, motivo="Exigência não cumprida no prazo.",)