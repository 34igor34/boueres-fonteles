from Entidades.Partes.autor import AutorProcesso
from Entidades.Partes.advogado import Advogado
from Entidades.Partes.parceiro import Parceiro
from Entidades.Processo.baseProcesso import Processo
from Entidades.Processo.desfecho_processo_adm import Desfecho, Exigencia, Cancelado, Concluido, ResultadoBeneficio
from datetime import date
from dataclasses import dataclass
from Util.value_objects import NumeroProtocolo, DataEntradaRequerimento

@dataclass(slots=True)
class ProcessoAdministrativo(Processo):
    data_entrada:DataEntradaRequerimento
    numero_protocolo = NumeroProtocolo | None
    desfecho: Desfecho | None # None enquanto o processo está em andamento

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