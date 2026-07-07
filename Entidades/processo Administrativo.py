class ProcessoAdministrativo(Processo):
    def __init__(
        self,
        autor: list[AutorProcesso],
        advogado: list[Advogado],
        parceiro: Parceiro,
        protocolo_requerimento,
    ):
        super().__init__(autor, advogado, parceiro, TipoProcesso.ADMINISTRATIVO)
        self.protocolo_requerimento = protocolo_requerimento

    @property
    def protocolo_requerimento(self) -> ProtocoloRequerimento:
        return self._protocolo_requerimento

    @protocolo_requerimento.setter
    def protocolo_requerimento(self, protocolo_requerimento):
        self._protocolo_requerimento = _coagir(protocolo_requerimento, ProtocoloRequerimento)