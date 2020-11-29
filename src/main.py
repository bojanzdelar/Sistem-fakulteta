""" Main, glavni modul aplikacije sadrži samo funkciju glavni_meni
	koja omogućava pristup sistemu ili izlazak iz aplikacije
"""

from pristup_sistemu import prijava_na_sistem, registracija

def glavni_meni():
    """ Funkcija glavni_meni nudi izbor sledećih funkcionalnosti: 
        prijavu na sistem, registraciju i izlazak iz aplikacije
    """
    print("\nGlavni meni")
    print("1. Prijava na sistem")
    print("2. Registracija")
    print("3. Izlazak iz aplikacije")
    opcija = None
    while opcija not in (1, 2, 3):
        try:
            opcija = int(input("Izaberite jednu od navedenih opcija (1/2/3): "))
        except ValueError:
            continue
    # poziv funkcije u zavisnosti od izabrane opcije
    if opcija == 1:
        prijava_na_sistem()
    elif opcija == 2:
        registracija()
    elif opcija == 3:
        return
    # rekurzivno pozivanje funkcije, potrebno pri povratku
    # iz ostalih funkcija kako se program ne bi zavrsio
    glavni_meni()

if __name__ == "__main__":
    print("Aplikaciju napravio Bojan Zdelar, 2019270983")
    glavni_meni()