""" Modul meni u okviru paketa profesori sadrži samo funkciju meni_profesora
    koja omogućava pristup funkcionalnostima prijavljenog profesora i izlazak iz menija.
    Napomena: Za ove funkcionalnosti mora biti prijavljen korisnik i to kao profesor.
"""

from profesori.funkcionalnosti import *

def meni_profesora(sifra_profesora):
    """ Funkcija meni_profesora omogućava prijavljenom profesoru: dodavanje i brisanje
        ocene studentu, računanje prosečne ocene za predmet, promenu termina 
        konsultacija i povratak na glavni meni
    """
    print("\nMeni profesora")
    print("1. Dodavanje ocene studentu")
    print("2. Brisanje ocene studentu")
    print("3. Računanje prosečne ocene za predmet")
    print("4. Promena termina konsultacija")
    print("5. Povratak na glavni meni")
    opcija = None
    while opcija not in (1, 2, 3, 4, 5):
        try:
            opcija = int(input("Izaberite jednu od navedenih opcija (1/2/3/4/5): "))
        except ValueError:
            continue
    # poziv funkcije u zavisnosti od izabrane opcije
    if opcija == 1:
        dodavanje_ocene(sifra_profesora)
    elif opcija == 2:
        brisanje_ocene(sifra_profesora)
    elif opcija == 3:
        prosecna_ocena_za_predmet(sifra_profesora)
    elif opcija == 4:
        promena_termina_konsultacija(sifra_profesora)
    elif opcija == 5:
        return
    # rekurzivno pozivanje funkcije, potrebno za povratak 
    # iz ostalih funkcija kako bi ostali u meniju profesora
    meni_profesora(sifra_profesora)