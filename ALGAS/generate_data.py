from sys import getsizeof
from datetime import datetime

def generate_data(sort: bool = False):
    dados = []

    def append_data(data: list):
        memory_accumulator = 0
        for d in data:
            for val in d:
                dt_inicio = datetime.now()
                acumulador= 0
                for i in range(val, 0, -1):
                    acumulador += i 
                    #memory_accumulator += getsizeof(i)
                memory_accumulator += getsizeof(val)
                dados.append((val, memory_accumulator, (datetime.now() - dt_inicio).total_seconds()))

    append_data(
        (range(0, 100000, 100),)
    )

    if sort:
        dados = sorted(dados, key=lambda x: x[0])

    return dados 