import pyodbc
from tabulate import tabulate


def status_badania(cursor, wizyta, lekarz):
    try:
        status = int(input("Wybierz nowy status badania: W trakcie(1)/Ukończone(2)/Anuluj(3): "))
        if status == 1:
            cursor.execute('UPDATE Badania SET StatusBadania = "W trakcie" WHERE IdWizyty = ?', wizyta)
            cursor.connection.commit()
            print("Zmieniono status badania na 'W trakcie'.")
            print("")
            cursor.execute('SELECT * FROM Badania WHERE LekarzZlec = ?', lekarz)
            columns = [column[0] for column in cursor.description]
            rows = cursor.fetchall()
            print(tabulate(rows, headers=columns, tablefmt='grid'))
            print("")
        elif status == 2:
            cursor.execute('UPDATE Badania SET StatusBadania = "Ukończone" WHERE IdWizyty = ?', wizyta)
            cursor.connection.commit()
            print("Zmieniono status badania na 'Ukończone'.")
            print("")
            cursor.execute('SELECT * FROM Badania WHERE LekarzZlec = ?', lekarz)
            columns = [column[0] for column in cursor.description]
            rows = cursor.fetchall()
            print(tabulate(rows, headers=columns, tablefmt='grid'))
            print("")
        elif status == 3:
            pass
        else:
            print("Nieprawidłowy wybór!")

        cursor.execute('SELECT * FROM Badania WHERE LekarzZlec = ?', lekarz)
        columns = [column[0] for column in cursor.description]
        rows = cursor.fetchall()
        print(tabulate(rows, headers=columns, tablefmt='grid'))
        print("")

    except pyodbc.Error as err:
        print("Error: ", err)
