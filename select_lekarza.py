from dbo import cursor
from tabulate import tabulate
import pyodbc
from nowe_badanie import nowe_badanie
from status_badania import status_badania
from opis_wizyty import opis_wizyty
from opis_badania import opis_badania


def select_lekarza():
    try:
        cursor.execute('SELECT * FROM Lekarze')
        columns = [column[0] for column in cursor.description]
        rows = cursor.fetchall()
        print("")
        print(tabulate(rows, headers=columns, tablefmt='grid'))
        print("")

        lekarz = int(input("Wybierz swoje Id: "))
        print("")

        cursor.execute('SELECT * FROM Wizyty WHERE IdLekarza = ?', lekarz)
        columns = [column[0] for column in cursor.description]
        rows = cursor.fetchall()
        print(tabulate(rows, headers=columns, tablefmt='grid'))
        print("")

        wizyta = int(input("Wybierz Id wizyty, którą chcesz zmodyfikować. Jeśli nie chcesz modyfikować żadnej, wybierz 0: "))
        print("")

        if wizyta == 0:
            pass
        elif wizyta:
            cursor.execute('SELECT * FROM Wizyty WHERE IdWizyty = ?', wizyta)
            columns = [column[0] for column in cursor.description]
            rows = cursor.fetchall()
            print(tabulate(rows, headers=columns, tablefmt='grid'))
            print("")

            czy_opis = int(input("Czy chcesz dodać lub zmienić opis wizyty? 1(Tak)/2(Nie): "))
            if czy_opis == 1:
                opis_wizyty(wizyta)
            elif czy_opis == 2:
                pass
            else:
                print("Nieprawidłowy wybór!")

            czy_nowe_badanie = int(input("Czy chcesz zlecić nowe badanie? 1(Tak)/2(Nie): "))
            if czy_nowe_badanie == 1:
                nowe_badanie(cursor, wizyta, lekarz)

                czy_status_badania = int(input("Czy chcesz zmienić status badania? 1(Tak)/2(Nie): "))
                if czy_status_badania == 1:
                    status_badania(cursor, wizyta, lekarz)
                elif czy_status_badania == 2:
                    pass
                else:
                    print("Nieprawidłowy wybór!")

                czy_opis_badania = int(input("Czy chcesz zmienić opis badania? 1(Tak)/2(Nie): "))
                if czy_opis_badania == 1:
                    opis_badania(wizyta)
                elif czy_opis_badania == 2:
                    pass
                else:
                    print("Nieprawidłowy wybór!")

            elif czy_nowe_badanie == 2:
                pass
            else:
                print("Nieprawidłowy wybór!")

        else:
            print("Nieprawidłowy wybór!")

        return lekarz

    except pyodbc.Error as err:
        print("Error: ", err)
        return None, None, None


if __name__ == "__main__":
    select_lekarza()
