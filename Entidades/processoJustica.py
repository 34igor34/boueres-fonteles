class ProcessoJustica(Processo):
    def __init__(
        self,
        autor: list[AutorProcesso],
        advogado: list[Advogado],
        parceiro: Parceiro,
        numero_processo,
        codigos: list[CodigoProcesso],
    ):
        super().__init__(autor, advogado, parceiro, TipoProcesso.JUSTICA)
        self.numero_processo = numero_processo
        self._codigos = codigos

    @property
    def numero_processo(self) -> NumeroProcesso:
        return self._numero_processo

    @numero_processo.setter
    def numero_processo(self, numero_processo):
        self._numero_processo = _coagir(numero_processo, NumeroProcesso)

    @property
    def codigo(self):
        return self._codigos

    @codigo.setter
    def codigo(self, codigo):
        self._codigos = codigo