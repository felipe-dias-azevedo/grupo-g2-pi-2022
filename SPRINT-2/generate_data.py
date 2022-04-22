from sys import getsizeof
from random import randrange
from datetime import datetime


class Data:
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


def gen(count: int = 1) -> list[Data]:
    values: list[Data] = []
    for i in range(count):
        values.append(gen_one())
    return values


def gen_one() -> Data:
    inicio = datetime.now()
    d = Data()
    d.mensalidade = randrange(start=1_000, stop=10_000, step=500)
    # TODO
    d.estado = ""
    # TODO
    d.municipio = ""
    # TODO
    d.nome_curso = ""
    d.quantidade_bolsas = randrange(start=0, stop=20)
    d.nota_bolsa = randrange(start=500, stop=1_000, step=50)
    d.sexo = randrange(1, 3)
    d.raca = randrange(1, 4)
    d.deficiente = True if randrange(start=1, stop=21) % 14 == 0 else False
    d.idade = randrange(start=16, stop=50, step=2)
    d.esgoto_inexistente = gen_bool()
    d.energia_eletrica_inexistente = gen_bool()
    d.agua_inexistente = gen_bool()
    d.acesso_internet = gen_bool()
    d.faz_exame_selecao = gen_bool()
    d.especializada_deficientes = gen_bool()
    d.ensino_tecnico = gen_bool()
    d.espaco_memoria = sum([getsizeof(i) for i in d.__dict__.values()])
    d.tempo_execucao = (datetime.now() - inicio).microseconds
    return d


def gen_bool():
    return randrange(0, 2)
