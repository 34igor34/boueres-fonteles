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
    SALARIO_URBANO = "Salario"
    SALARIO_RURAL = "Salário urbano"
    LOAS = "LOAS"
    LOAS_IDOSO = "LOAS idoso"
    API_RURAL = "API rural"
    API_URBANO = "API urbano"
    PENSAO_MORTE_RURAL = "Pensão rural"
    PENSAO_MORTE_URBANO = "Pensão urbano"
    AUX_DOENCA_RURAL = "Aux. doença rural"
    AUX_DOENCA_URBANO = "Aux. doença urbano"


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