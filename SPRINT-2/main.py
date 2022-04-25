from database_manager import DatabaseManager
from generate_data import gen
from enum import Enum


class Options(int, Enum):
    VIEW_DATA, SELECT_DATA, INSERT_DATA, DELETE_DATA, QUIT = range(1, 6)


def main():
    running = True

    db = DatabaseManager("44.204.224.207", "root", "123mysql@", "grupodois")

    while running:
        print()
        print(f"{Options.VIEW_DATA}* - View data only")
        print(f"{Options.SELECT_DATA}* - Select data from DB")
        print(f"{Options.INSERT_DATA}* - Insert data to DB")
        print(f"{Options.DELETE_DATA}* - Delete DB")
        print(f"{Options.QUIT}* - Quit")

        inp = int(input("$: "))

        if inp == Options.VIEW_DATA:
            dados = gen(1)
            print()
            print(dados[0])
        elif inp == Options.SELECT_DATA:
            dados = db.select()
            print()
            print(dados)
            print("\nDone!")
            print(f"Selected {len(dados)} Rows.\n")
        elif inp == Options.INSERT_DATA:
            dados = gen(1000)
            db.insert(dados)
            print()
            print("\nDone!")
            print(f"Inserted {len(dados)} Rows.\n")
        elif inp == Options.DELETE_DATA:
            db.delete()
            print("\nDropped Table!\n")
        elif inp == Options.QUIT:
            running = False
            print("\nBye!\n")


if __name__ == "__main__":
    main()
