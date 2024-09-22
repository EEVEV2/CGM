import pyodbc


def polaczenie_z_baza():
    return pyodbc.connect(
        "Driver={ODBC Driver 17 for SQL Server};"
        "Server=LAPTOP-KTKKP8S6;"
        "Database=Szpital;"
        "Trusted_Connection=yes;"
    )


try:
    with polaczenie_z_baza() as connect:
        cursor = connect.cursor()
        cursor.execute('USE Szpital;')
        cursor.connection.commit()

except pyodbc.Error as err:
    print("Error: ", err)
