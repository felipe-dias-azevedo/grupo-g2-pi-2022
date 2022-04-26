from typing import List, Dict
from datetime import datetime


def process_range(value, start: int, stop: int, step: int) -> int:
    values = list(range(start, stop + 1, step))
    min_val = min(values)
    max_val = max(values)
    stepper = (max_val - min_val) / len(values)
    ranger = (value - min_val) / stepper
    return values[int(ranger)]


def process_mensalidade(value: int) -> int:
    return process_range(value, start=0, stop=15_000, step=500)


def process_nome(value: str) -> str:
    # TODO: retirar acentos e corrigir acentuações
    return value


def process_nota_bolsa(value: int) -> int:
    return process_range(value, start=0, stop=1000, step=50)


def process_sexo(value: int) -> str:
    return "Masculino" if value == 0 else "Feminino"


def process_raca(value: int) -> str:
    if value == 0:
        return "Branco"
    elif value == 1:
        return "Pardo"
    elif value == 2:
        return "Preto"
    else:
        return "Outro"


def process_bool(value: bool) -> str:
    return "Sim" if value else "Não"


def process_idade(value: int) -> int:
    return process_range(value, start=14, stop=90, step=2)


def process(data: List[Dict]) -> List[Dict]:
    values: list[dict] = []
    for d in data:
        inicio = datetime.now()
        values.append({
            'mensalidade': process_mensalidade(d['mensalidade']),
            'estado': d['estado'],
            'municipio': process_nome(d['municipio']),
            'nome_curso': process_nome(d['nome_curso']),
            'quantidade_bolsas': d['quantidade_bolsas'],
            'nota_bolsa': process_nota_bolsa(d['nota_bolsa']),
            'sexo': process_sexo(d['sexo']),
            'raca': process_raca(d['raca']),
            'deficiente': process_bool(d['deficiente']),
            'idade': process_idade(d['idade']),
            'esgoto_inexistente': process_bool(d['esgoto_inexistente']),
            'energia_eletrica_inexistente': process_bool(d['energia_eletrica_inexistente']),
            'agua_inexistente': process_bool(d['agua_inexistente']),
            'acesso_internet': process_bool(d['acesso_internet']),
            'faz_exame_selecao': process_bool(d['faz_exame_selecao']),
            'especializada_deficientes': process_bool(d['especializada_deficientes']),
            'ensino_tecnico': process_bool(d['ensino_tecnico']),
            'espaco_memoria': d['espaco_memoria'],
            'tempo_execucao': (datetime.now() - inicio).microseconds + d['tempo_execucao']
        })
    return values
