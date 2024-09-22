import pyodbc


def dodaj_pacjenta(cursor):
    try:
        print("Wypełnij ankietę, aby dodać nowego pacjenta:")
        ImiePacjenta = input("Podaj imię: ")
        NazwiskoPacjenta = input("Podaj nazwisko: ")
        Pesel = input("Podaj pesel: ")
        DataUrodzenia = input("Podaj datę urodzenia (YYYY-MM-DD): ")
        Adres = input("Podaj adres: ")
        Telefon = int(input("Podaj numer telefonu: "))
        EmailPacjenta = input("Podaj adres email: ")

        cursor.execute(
            'INSERT INTO Pacjenci (ImiePacjenta, NazwiskoPacjenta, Pesel, DataUrodzenia, Adres, Telefon, EmailPacjenta) VALUES (?, ?, ?, ?, ?, ?, ?)',
            (ImiePacjenta, NazwiskoPacjenta, Pesel, DataUrodzenia, Adres, Telefon, EmailPacjenta)
        )
        cursor.connection.commit()
        print("Dodano nowego pacjenta.")

        cursor.execute('SELECT IdPacjenta FROM Pacjenci WHERE Pesel = ?', Pesel)
        pacjent = cursor.fetchone()
        return pacjent.IdPacjenta

    except pyodbc.Error as err:
        print("Error: ", err)
