from progress.bar import ChargingBar as ProgressBar
from datetime import datetime
from sys import getsizeof


def get_data_ranges() -> tuple:
    return (
        range(100000, 600000, 100000),
        range(1000, 6000, 100), 
        range(100, 600, 100), 
        range(10, 60, 10), 
        range(1000000, 6000000, 1000000)
    )


def append_data(data: list) -> list:
    dados = []
    memory_accumulator = 0
    pgbar = ProgressBar('Generating...', max=sum([len(element) for element in data]))
    for range_data in data:
        for value in range_data:
            inicio = datetime.now()
            acumulador = 0
            for i in range(value, 0, -1):
                acumulador += i
            memory_accumulator += getsizeof(value)
            duracao = datetime.now() - inicio
            dados.append((value, memory_accumulator, duracao.microseconds))
            pgbar.next()
    pgbar.finish()
    return dados


def generate_data(sort: bool = False) -> list:
    dados = append_data(get_data_ranges())

    if sort:
        dados = sorted(dados, key=lambda x: x[0])

    return dados 