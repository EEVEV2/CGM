# import webbrowser
from select_rejestratorki import select_rejestratorki
from select_lekarza import select_lekarza


def main():
    while True:
        wybor = int(input("Jestem: Rejestratorką(1)/Lekarzem(2): "))
        if wybor == 1:
            select_rejestratorki()
            # webbrowser.open("select_rejestratorki.html")
        elif wybor == 2:
            select_lekarza()
            # webbrowser.open("select_lekarza.html")
        else:
            print("Nieprawidłowy wybór!")

        kontynuacja = int(input("Czy chcesz kontynuować pracę w programie? 1(Tak)/2(Nie): "))
        if kontynuacja == 2:
            break


if __name__ == "__main__":
    main()
