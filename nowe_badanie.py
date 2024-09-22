from datetime import date
import pyodbc
from tabulate import tabulate


def nowe_badanie(cursor, wizyta, lekarz):
    try:
        print("Wypełnij ankietę, aby dodać nowe badanie:")
        IdUslugi = int(input("Podaj Id usługi: "))
        IdWizyty = wizyta
        StatusBadania = "Nowe zlecenie"
        LekarzZlec = lekarz
        DataWykonania = input("Wybierz datę wykonania (YYYY-MM-DD): ")
        DataZlecenia = date.today().strftime("%Y-%m-%d")
        OpisBadania = input("Dodaj opis badania: ")

        cursor.execute(
            'INSERT INTO Badania (IdUslugi, IdWizyty, StatusBadania, LekarzZlec, DataWykonania, DataZlecenia, OpisBadania) VALUES (?, ?, ?, ?, ?, ?)',
            (IdUslugi, IdWizyty, StatusBadania, LekarzZlec, DataWykonania, DataZlecenia, OpisBadania)
        )
        cursor.connection.commit()
        print("Dodano nowe badanie.")
        print("")

        cursor.execute('SELECT * FROM Badania WHERE LekarzZlec = ?', lekarz)
        columns = [column[0] for column in cursor.description]
        rows = cursor.fetchall()
        print(tabulate(rows, headers=columns, tablefmt='grid'))
        print("")

    except pyodbc.Error as err:
        print("Error: ", err)
