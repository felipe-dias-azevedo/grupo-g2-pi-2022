from datetime import datetime
from sys import getsizeof

def generate_data(sort: bool = False):
    dados = []

    def append_data(data: list):
        memory_accumulator = 0
        for d in data:
            for val in d:
                memory_accumulator += getsizeof(val)
                dados.append((val, memory_accumulator, datetime.now()))

    append_data(
        (range(100000, 600000, 100000), 
        range(1000, 6000, 100), 
        range(100, 600, 100), 
        range(10, 60, 10), 
        range(1000000, 6000000, 1000000))
    )

    if sort:
        dados = sorted(dados, key=lambda x: x[0])
    
    return dados