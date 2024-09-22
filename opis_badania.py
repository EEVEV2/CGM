import pyodbc
from dbo import cursor


def opis_badania(wizyta):
    try:
        zmiana_opis_badania = int(input("Wybierz, co chcesz zrobć z opisem badania: Dodać nowy(1)/Zmienić obecny(2)/Anuluj(3): "))
        if zmiana_opis_badania == 1:
            OpisBadania = input("Wpisz nowy opis badania: ")
            cursor.execute('UPDATE Badania SET OpisBadania = ? WHERE IdWizyty = ?', OpisBadania, wizyta)
            cursor.connection.commit()
            print("Dodano nowy opis badania.")
        elif zmiana_opis_badania == 2:
            cursor.execute('SELECT OpisBadania FROM Badania WHERE IdWizyty = ?', wizyta)
            obecny_opis_badania = cursor.fetchone()[0]
            print(f"Obecny opis badania: {obecny_opis_badania}")
            nowy_opis_badania = input("Zmień opis badania: ")
            if nowy_opis_badania:
                cursor.execute('UPDATE Wizyty SET OpisWizyty = ? WHERE IdWizyty = ?', nowy_opis_badania, wizyta)
                cursor.connection.commit()
                print("Zmieniono opis badania.")
            else:
                print("Nie zmieniono opisu wizyty.")

        elif zmiana_opis_badania == 3:
            pass
        else:
            print("Nieprawidłowy wybór!")

    except pyodbc.Error as err:
        print("Error: ", err)
