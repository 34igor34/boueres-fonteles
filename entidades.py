from enum import Enum
class TipoParte(Enum):
    ADVOGADO = "advogado"
    AUTOR = "autor"
    REPRESENTANTE = "representante"
    PARCEIRO = "parceiro"

class TipoRepresentante(Enum):
    MAE = "mãe"
    PAI = "pai"
    TUTOR = "tutor"
    TUTORA = "tutora"
    GUARDIAO = "guardião"
    GUARDIA = "guardiã"

class TipoProcesso(Enum):
    ADMINISTRATIVO = "administrativo"
    JUSTICA = "justiça"

class TipoRequerimento(Enum):
    SALARIO_URBANO = "salario"
    SALARIO_RURAL = "salário urbano"
    LOAS = "loas"
    LOAS_IDOSO = "loas idoso"
    API_RURAL = "api rural"
    API_URBANO = "api urbano"
    PENSAO_MORTE_RURAL = "pensão rural"
    PENSAO_MORTE_URBANO = "pensão urbano"
    AUX_DOENCA_RURAL = "aux doença rural"
    AUX_DOENCA_URBANO = "aux doença urbano"

class CodigoProcesso(Enum):
    AUX_DOENCA_RURAL = "6101"
    AUX_DOENCA_URBANO = "14809"
    SALARIO_URBANO = "14828"  
    SALARIO_RURAL = "6103"  
    LOAS = "11946"
    LOAS_IDOSO = "11947"
    API_RURAL = "6098"
    API_URBANO = "6097"
    API_HIBRIDA = "12399"
    PENSAO_MORTE = "6104"

class Pessoa:
    def __init__(self, nome: str, tipo: TipoParte):
        self._nome = nome
        self._tipo = tipo

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        if nome is None:
            raise ValueError("Passe um nome válido")
        self._nome = nome

    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, tipo):
        self._tipo = tipo

class Advogado(Pessoa):
    def __init__(self, nome: str, tipo: TipoParte, oab: str):
        super().__init__(nome, tipo)
        self._oab = oab

    @property
    def oab(self) -> str:
        return self._oab

    @oab.setter
    def oab(self, oab: str):
        self._oab = oab

class AutorProcesso(Pessoa):
    def __init__(self, nome, tipo, cpf):
        super().__init__(nome, tipo)
        self._cpf = cpf

    @property
    def cpf(self):
        return self._cpf

    @cpf.setter
    def cpf(self, cpf):
        self._cpf = cpf

class RepresentanteProcesso(Pessoa):
    def __init__(self, nome, tipo, cpf, tipoRepresentante: TipoRepresentante):
        super().__init__(nome, tipo)
        self._cpf = cpf
        self._tipo_representante = tipoRepresentante

    @property
    def cpf(self):
        return self._cpf

    @cpf.setter
    def cpf(self, cpf):
        self._cpf = cpf

    @property
    def tipoRepresentante(self):
        return self._tipo_representante

    @tipoRepresentante.setter
    def tipoRepresentante(self, tipo):
        if isinstance(tipo, TipoRepresentante):
            self._tipo_representante = tipo
        elif isinstance(tipo, str):
            try:
                # tenta por nome da enum (MAE, PAI, ...)
                self._tipo_representante = TipoRepresentante[tipo]
            except KeyError:
                # tenta pelo valor ("mae", "pai", ...")
                self._tipo_representante = TipoRepresentante(tipo.lower())
        else:
            raise ValueError("tipoRepresentante inválido")

class Parceiro(Pessoa):
    def __init__(self, nome, tipo, contato = None):
        super().__init__(nome, tipo)
        self._contato = contato

    @property
    def contato(self):
        return self._contato

    @contato.setter
    def contato(self, contato):
        self._contato = contato

class Processo:
    def __init__(self, autor: list[AutorProcesso], advogado: list[Advogado], parceiro: Parceiro, tipo: TipoProcesso):
        self._autor = autor
        self._advogado = advogado
        self._parceiro = parceiro
        self._tipo = tipo

    @property
    def autor(self) -> list[AutorProcesso]:
        return self._autor

    @autor.setter
    def autor(self, autor):
        self._autor = autor

    @property
    def advogado(self) -> list[Advogado]:
        return self._advogado

    @advogado.setter
    def advogado(self, advogado):
        self._advogado = advogado

    @property
    def parceiro(self) -> Parceiro:
        return self._parceiro

    @parceiro.setter
    def parceiro(self, parceiro):
        self._parceiro = parceiro

    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, tipo):
        self._tipo = tipo

class ProcessoAdministrativo(Processo):
    def __init__(self, autor: list[AutorProcesso], advogado: list[Advogado], parceiro: Parceiro, protocolo_requerimento: str):
        super().__init__(autor, advogado, parceiro, TipoProcesso.ADMINISTRATIVO)
        self._protocolo_requerimento = protocolo_requerimento

    @property
    def protocolo_requerimento(self):
        return self._protocolo_requerimento

    @protocolo_requerimento.setter
    def protocolo_requerimento(self, protocolo_requerimento):
        self._protocolo_requerimento = protocolo_requerimento

class ProcessoJustica(Processo):
    def __init__(self, autor: list[AutorProcesso], advogado: list[Advogado], parceiro: Parceiro, numero_processo: str, codigos: list[CodigoProcesso]):
        super().__init__(autor, advogado, parceiro, TipoProcesso.JUSTICA)
        self._numero_processo = numero_processo
        self._codigos = codigos

    @property
    def numero_processo(self):
        return self._numero_processo

    @numero_processo.setter
    def numero_processo(self, numero_processo):
        self._numero_processo = numero_processo

    @property
    def codigo(self):
        return self._codigos

    @codigo.setter
    def codigo(self, codigo):
        self._codigos = codigo