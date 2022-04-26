from sys import getsizeof
from random import randrange, choices
from datetime import datetime
from typing import Dict, List


class Data(object):
    mensalidade: float
    estado: str
    municipio: str
    nome_curso: str
    quantidade_bolsas: int  # média entre integrais e parciais (ampla + cota)
    nota_bolsa: float  # média entre integrais e parciais (ampla + cota)
    # corelacionando com base do pda-prouni
    # pela fk estado, fk municipio (upper case e >95% str igual) e nome curso (>80% str igual)
    sexo: int  # (m=0, f=1)
    raca: int  # (branca=0, parda=1, preta=2)
    deficiente: bool
    idade: int  # timestamp de data de nascimento
    # corelacionando com base do educacao basica (inep)
    # pela fk estado[SG_UF], fk municipio[NO_MUNICIPIO] (upper case e >95% str igual)
    esgoto_inexistente: bool  # IN_ESGOTO_INEXISTENTE
    energia_eletrica_inexistente: bool  # IN_ENERGIA_INEXISTENTE
    agua_inexistente: bool  # IN_AGUA_INEXISTENTE
    acesso_internet: bool  # IN_INTERNET
    faz_exame_selecao: bool  # IN_EXAME_SELECAO
    especializada_deficientes: bool  # IN_ESP
    ensino_tecnico: bool  # IN_PROF_TEC
    # correlacionando performance de geração (ou obtenção do dado) pelo algoritmo
    espaco_memoria: int  # getsizeof de cada elemento
    tempo_execucao: int  # micro segundos


def gen(count: int = 1) -> List[Dict]:
    values: list[dict] = []
    for i in range(count):
        values.append(gen_one())
    return values


def gen_one() -> dict:
    # MOCK
    estados = ["SP", "RJ", "MG"]
    municipios = ["São Paulo", "Rio de Janeiro", "Belo Horizonte"]
    cursos = ["Medicina", "Ciência da Computação", "Direito", "Sociologia"]

    inicio = datetime.now()
    d = Data()
    d.mensalidade = randrange(start=1_000, stop=10_000)

    cidade_estado = choices([0, 1, 2], [0.45, 0.31, 0.24])[0]
    d.estado = estados[cidade_estado]
    d.municipio = municipios[cidade_estado]
    curso = choices([0, 1, 2, 3], [0.35, 0.2, 0.3, 0.15])[0]
    d.nome_curso = cursos[curso]

    d.quantidade_bolsas = randrange(start=1, stop=20)
    d.nota_bolsa = randrange(start=500, stop=1_000)
    d.sexo = choices([0, 1], [0.48, 0.52])[0]
    d.raca = choices([0, 1, 2, 3], [0.43, 0.47, 0.09, 0.01])[0]
    d.deficiente = gen_bool(0.95)
    d.idade = randrange(start=16, stop=50)
    d.esgoto_inexistente = gen_bool(0.8)
    d.energia_eletrica_inexistente = gen_bool(0.95)
    d.agua_inexistente = gen_bool(0.9)
    d.acesso_internet = gen_bool(0.33)
    d.faz_exame_selecao = gen_bool(0.8)
    d.especializada_deficientes = gen_bool(0.98)
    d.ensino_tecnico = gen_bool(0.75)
    d.espaco_memoria = sum([getsizeof(i) for i in vars(d).values()])
    d.tempo_execucao = (datetime.now() - inicio).microseconds
    return vars(d)


def gen_bool(probability: float) -> bool:
    prob = round(probability, 2)
    val = choices([0, 1], [prob, 1 - prob])[0]
    return False if val == 0 else True
