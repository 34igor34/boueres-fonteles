from Entidades.autor import AutorProcesso
from Entidades.advogado import Advogado
from Entidades.parceiro import Parceiro
from Entidades.baseProcesso import Processo
from Entidades.desfecho_processo_adm import Desfecho, Exigencia, Cancelado, Concluido, ResultadoBeneficio
from datetime import date
from dataclasses import dataclass
from Util.value_objects import ProtocoloRequerimento, DataEntrada

@dataclass(slots=True)
class ProcessoAdministrativo(Processo):
    autor: list[AutorProcesso]
    advogado: list[Advogado]
    parceiro: Parceiro
    data_entrada:DataEntrada
    protocolo_requerimento = ProtocoloRequerimento | None
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