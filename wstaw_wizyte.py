import pyodbc
from dbo import cursor


def wstaw_wizyte(pacjent, lekarz, data):
    try:
        cursor.execute(
            'INSERT INTO Wizyty (IdPacjenta, IdLekarza, DataWizyty) VALUES (?, ?, ?)',
            (pacjent, lekarz, data)
        )
        print(f"Dodano wizytę dla pacjenta {pacjent} do lekarza {lekarz} dnia {data}.")

    except pyodbc.Error as err:
        print("Error: ", err)

    if __name__ == "__main__":
        wstaw_wizyte(pacjent, lekarz, data)
