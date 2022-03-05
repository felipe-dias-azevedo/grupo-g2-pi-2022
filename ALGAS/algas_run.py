from progress.bar import ChargingBar as ProgressBar
from generate_data import generate_data
from db_manager import DatabaseManager
from database_options import DatabaseOptions as db_options
from database_selection import DatabaseSelection as db_types

def choose_database():
    print()
    print("Choose database type:")
    print(f"{db_types.SQLITE}* - SQLite")
    print(f"{db_types.MYSQL}* - MySQL")

    is_sqlite = int(input("$: "))

    if is_sqlite == db_types.SQLITE:
        return True
    elif is_sqlite == db_types.MYSQL:
        return False
    else:
        return choose_database()


def main():
    running = True
    db_is_sqlite = choose_database()

    db = DatabaseManager(sqlite=db_is_sqlite)

    while running:
        print()
        print(f"{db_options.VIEW_DATA}* - View data only")
        print(f"{db_options.SELECT_DATA}* - Select data from DB")
        print(f"{db_options.INSERT_DATA}* - Insert data to DB")
        print(f"{db_options.DELETE_DATA}* - Delete DB")
        print(f"{db_options.DROP_TABLE}* - Drop Table DB")
        print(f"{db_options.EXPORT_CSV}* - Export data to CSV")
        print(f"{db_options.EXPORT_JSON}* - Export data to JSON")
        print(f"{db_options.QUIT}* - Quit")

        inp = int(input("$: "))

        if inp == db_options.VIEW_DATA:
            print()
            dados = generate_data(sort=True)
            print(f"\n{dados}")
        elif inp == db_options.SELECT_DATA:
            dados = db.select()
            print(f"\n{dados}")
            print("\nDone!")
            print(f"Selected {len(dados)} Rows.\n")
        elif inp == db_options.INSERT_DATA:
            print()
            dados = generate_data()
            db.transact_begin()
            print()
            pgbar = ProgressBar('Inserting...', max=len(dados))
            for dado in dados:
                db.transact_insert(dado)
                pgbar.next()
            pgbar.finish()
            db.transact_commit()
            print("\nDone!")
            print(f"Inserted {len(dados)} Rows.\n")
        elif inp == db_options.DELETE_DATA:
            db.delete()
            print("\nDeleted!\n")
        elif inp == db_options.DROP_TABLE:
            db.drop()
            print("\nDropped Table!\n")
        elif inp == db_options.EXPORT_CSV:
            dados = db.select()
            db.export_csv(dados)
            print("\nExported Data Successfully!\n")
        elif inp == db_options.EXPORT_JSON:
            dados = db.select()
            db.export_json(dados)
            print("\nExported Data Successfully!\n")
        elif inp == db_options.QUIT:
            running = False
            print("\nBye!\n")


if __name__ == "__main__":
    main()