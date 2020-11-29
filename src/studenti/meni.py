""" Modul meni u okviru paketa studenti sadrži samo funkciju meni_studenta
    koja omogućava pristup funkcionalnostima prijavljenog studenta i izlazak iz menija.
    Napomena: Za ove funkcionalnosti mora biti prijavljen korisnik i to kao student.
"""

from studenti.funkcionalnosti import *

def meni_studenta(broj_indeksa):
    """ Funkcija meni_studenta omogućava prijavljenom studentu: računanje globalne
        prosečne ocene, prikaz položenih ili nepoloženih predmeta, prikaz podataka o
        profesoru koji predaje predmet i povratak na glavni meni
    """
    print("\nMeni studenta")
    print("1. Računanje globalne prosečne ocene")
    print("2. Prikaz položenih ili nepoloženih predmeta")
    print("3. Prikaz podataka o profesoru koji predaje predmet")
    print("4. Povratak na glavni meni")
    opcija = None
    while opcija not in (1, 2, 3, 4):
        try:
            opcija = int(input("Izaberite jednu od navedenih opcija (1/2/3/4): "))
        except ValueError:
            continue
    # poziv funkcije u zavisnosti od izabrane opcije
    if opcija == 1:
        globalna_prosecna_ocena(broj_indeksa)
    elif opcija == 2:
        predmeti(broj_indeksa)
    elif opcija == 3:
        prikaz_profesora()
    elif opcija == 4:
        return
    # rekurzivno pozivanje funkcije, potrebno za povratak 
    # iz ostalih funkcija kako bi ostali u meniju studenta
    meni_studenta(broj_indeksa)