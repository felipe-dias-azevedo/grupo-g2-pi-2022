from create import create_db, drop_table_db
from generate_data import generate_data
from insert import insert_data, delete_data
from select_data import select_data

running = True

print()
print("Use Sqlite?")
print("1* - YES")
print("2* - NO")

is_sqlite = int(input("$: "))

is_sqlite = True if is_sqlite == 1 else False

while running:
    print()
    print("1* - View data only")
    print("2* - Select data from DB")
    print("3* - Insert data to DB")
    print("4* - Delete DB")
    print("5* - Drop Table DB")
    print("6* - Quit")

    inp = int(input("$: "))

    if inp == 1:
        dados = generate_data(sort=True)
        print(dados)
    elif inp == 2:
        conn = create_db()
        cursor = conn.cursor()
        dados = select_data(cursor=cursor, sqlite=is_sqlite)
        print()
        print(dados)
        print("\nDone!\n")
    elif inp == 3:
        conn = create_db(sqlite=is_sqlite)
        dados = generate_data()
        insert_data(conn, dados, sqlite=is_sqlite)
        print("\nInserted!\n")
    elif inp == 4:
        conn = create_db(sqlite=is_sqlite)
        delete_data(conn, sqlite=is_sqlite)
        print("\nDeleted!\n")
    elif inp == 5:
        conn = create_db(sqlite=is_sqlite)
        drop_table_db(sqlite=is_sqlite)
        print("\nDropped Table!\n")
    elif inp == 6:
        running = False
        print("\nBye!\n")