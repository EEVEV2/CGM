import pyodbc
from dbo import cursor


def opis_wizyty(wizyta):
    try:
        zmiana_opis_wizyty = int(input("Wybierz, co chcesz zrobć z opisem wizyty: Dodać nowy(1)/Zmienić obecny(2)/Anuluj(3): "))
        if zmiana_opis_wizyty == 1:
            OpisWizyty = input("Wpisz nowy opis wizyty: ")
            cursor.execute('UPDATE Wizyty SET OpisWizyty = ? WHERE IdWizyty = ?', OpisWizyty, wizyta)
            cursor.connection.commit()
            print("Dodano nowy opis wizyty.")
        elif zmiana_opis_wizyty == 2:
            cursor.execute('SELECT OpisWizyty FROM Wizyty WHERE IdWizyty = ?', wizyta)
            obecny_opis_wizyty = cursor.fetchone()[0]
            print(f"Obecny opis wizyty: {obecny_opis_wizyty}")
            nowy_opis_wizyty = input("Zmień opis wizyty: ")
            if nowy_opis_wizyty:
                cursor.execute('UPDATE Wizyty SET OpisWizyty = ? WHERE IdWizyty = ?', nowy_opis_wizyty, wizyta)
                cursor.connection.commit()
                print("Zmieniono opis wizyty.")
            else:
                print("Nie zmieniono opisu wizyty.")

        elif zmiana_opis_wizyty == 3:
            pass
        else:
            print("Nieprawidłowy wybór!")

    except pyodbc.Error as err:
        print("Error: ", err)
