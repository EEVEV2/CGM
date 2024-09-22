USE Szpital;

CREATE TABLE Pacjenci (
    IdPacjenta INT IDENTITY(1,1) PRIMARY KEY,
    ImiePacjenta VARCHAR(20) NOT NULL,
    NazwiskoPacjenta VARCHAR(55) NOT NULL,
	  Pesel VARCHAR(11) UNIQUE NOT NULL,
    DataUrodzenia DATE NOT NULL,
    Adres VARCHAR(255) UNIQUE NOT NULL,
    Telefon VARCHAR(9) UNIQUE NOT NULL,
    EmailPacjenta VARCHAR(100) UNIQUE NOT NULL
);

CREATE TABLE Lekarze (
    IdLekarza INT IDENTITY(1,1) PRIMARY KEY,
    ImieLekarza VARCHAR(20) NOT NULL,
    NazwiskoLekarza VARCHAR(55) NOT NULL,
    Specjalizacja VARCHAR(100) NOT NULL,
    EmailLekarza VARCHAR(100) UNIQUE NOT NULL
);

CREATE TABLE Wizyty (
    IdWizyty INT IDENTITY(1,1) PRIMARY KEY,
    IdPacjenta INT NOT NULL,
    IdLekarza INT NOT NULL,
    DataWizyty DATETIME NOT NULL,
    OpisWizyty VARCHAR(255),
    FOREIGN KEY (IdPacjenta) REFERENCES Pacjenci(IdPacjenta),
    FOREIGN KEY (IdLekarza) REFERENCES Lekarze(IdLekarza)
);

INSERT INTO Pacjenci (ImiePacjenta, NazwiskoPacjenta, Pesel, DataUrodzenia, Adres, Telefon, EmailPacjenta)
VALUES ('Piotr', '£uszcz', '78031842137', '1978-03-18', 'Jelenia Góra', '197842000', 'leci.magik@example.com');

INSERT INTO Lekarze (ImieLekarza, NazwiskoLekarza, Specjalizacja, EmailLekarza)
VALUES ('Karol', 'Wojty³a', 'Dzieci', 'jan.pawel2@watykan.com');

CREATE TABLE Uslugi (
	IdUslugi INT IDENTITY(1,1) PRIMARY KEY,
	Kod VARCHAR(5) NOT NULL,
	NazwaUslugi VARCHAR(255) NOT NULL
);

CREATE TABLE Badania (
	IdBadania INT IDENTITY(1,1) PRIMARY KEY,
	IdUslugi INT NOT NULL,
	IdWizyty INT NOT NULL,
	StatusBadania VARCHAR(255) NOT NULL,
	LekarzZlec INT NOT NULL,
	DataWykonania DATETIME,
	DataZlecenia DATETIME NOT NULL,
	OpisBadania VARCHAR(500) NOT NULL,
	FOREIGN KEY (IdUslugi) REFERENCES Uslugi(IdUslugi),
	FOREIGN KEY (IdWizyty) REFERENCES Wizyty(IdWizyty),
	FOREIGN KEY (LekarzZlec) REFERENCES Lekarze(IdLekarza)
);

INSERT INTO Uslugi (Kod, NazwaUslugi)
VALUES ('LBTM', 'Lobotomia')

SELECT * FROM Pacjenci
SELECT * FROM Lekarze
SELECT * FROM Wizyty
SELECT * FROM Uslugi
SELECT * FROM Badania