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