from dbo import cursor
from tabulate import tabulate
from dodaj_pacjenta import dodaj_pacjenta
import pyodbc
from wstaw_wizyte import wstaw_wizyte


def select_rejestratorki():
    try:
        cursor.execute('SELECT IdPacjenta, ImiePacjenta, NazwiskoPacjenta, Pesel FROM Pacjenci')
        columns = [column[0] for column in cursor.description]
        rows = cursor.fetchall()
        print("")
        print(tabulate(rows, headers=columns, tablefmt='grid'))
        print("")

        pacjent = int(input("Wybierz Id pacjenta do wizyty. Jeśli chcesz dodać nowego pacjenta, wybierz 0: "))
        if pacjent == 0:
            pacjent = dodaj_pacjenta(cursor)
        print("")

        cursor.execute('SELECT * FROM Lekarze')
        columns = [column[0] for column in cursor.description]
        rows = cursor.fetchall()
        print("")
        print(tabulate(rows, headers=columns, tablefmt='grid'))
        lekarz = int(input("Wybierz Id lekarza do wizyty: "))
        print("")

        data = input("Wybierz datę wizyty (YYYY-MM-DD): ")
        print("")

        wstaw_wizyte(pacjent, lekarz, data)

    except pyodbc.Error as err:
        print("Error: ", err)
        return None, None, None


if __name__ == "__main__":
    select_rejestratorki()
