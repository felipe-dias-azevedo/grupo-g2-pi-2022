from database_manager import DatabaseManager
from process_data import process
from generate_data import gen
from enum import Enum


class Options(int, Enum):
    VIEW_DATA_RAW, VIEW_DATA_PROCESSED, SELECT_DATA_RAW, SELECT_DATA_PROCESSED, INSERT_DATA_RAW, INSERT_DATA_PROCESSED, DELETE_DATA_RAW, DELETE_DATA_PROCESSED, QUIT = range(1, 10)


def main():
    running = True

    db = DatabaseManager("3.232.74.193", "root", "123mysql@", "grupodois")

    while running:
        print()
        print(f"[{Options.VIEW_DATA_RAW}] - View raw data only")
        print(f"[{Options.VIEW_DATA_PROCESSED}] - View processed data only")
        print(f"[{Options.SELECT_DATA_RAW}] - Select raw data from DB")
        print(f"[{Options.SELECT_DATA_PROCESSED}] - Select processed data from DB")
        print(f"[{Options.INSERT_DATA_RAW}] - Insert raw data to DB")
        print(f"[{Options.INSERT_DATA_PROCESSED}] - Insert processed data to DB")
        print(f"[{Options.DELETE_DATA_RAW}] - Delete raw DB")
        print(f"[{Options.DELETE_DATA_PROCESSED}] - Delete processed DB")
        print(f"[{Options.QUIT}] - Quit")

        inp = int(input("$: "))

        if inp == Options.VIEW_DATA_RAW:
            dados = gen(1)
            print()
            print(dados[0])
        if inp == Options.VIEW_DATA_PROCESSED:
            dados = gen(1)
            dados_processados = process(dados)
            print()
            print(dados_processados[0])
        elif inp == Options.SELECT_DATA_RAW:
            dados = db.select(raw=True)
            print()
            print(dados)
            print("\nDone!")
            print(f"Selected {len(dados)} Rows.\n")
        elif inp == Options.SELECT_DATA_PROCESSED:
            dados = db.select(raw=False)
            print()
            print(dados)
            print("\nDone!")
            print(f"Selected {len(dados)} Rows.\n")
        elif inp == Options.INSERT_DATA_RAW:
            dados = gen(1000)
            db.insert(dados, raw=True)
            print()
            print("\nDone!")
            print(f"Inserted {len(dados)} Rows.\n")
        elif inp == Options.INSERT_DATA_PROCESSED:
            dados = db.select(raw=True)
            dados_processados = process(dados)
            db.insert(dados_processados, raw=False)
            print()
            print("\nDone!")
            print(f"Inserted {len(dados)} Rows.\n")
        elif inp == Options.DELETE_DATA_RAW:
            db.delete(raw=True)
            print("\nDropped Table!\n")
        elif inp == Options.DELETE_DATA_PROCESSED:
            db.delete(raw=False)
            print("\nDropped Table!\n")
        elif inp == Options.QUIT:
            running = False
            print("\nBye!\n")


if __name__ == "__main__":
    main()
