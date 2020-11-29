""" Modul liste sadrži funkcije putanja_fajla, ucitaj_listu_predmeta, ucitaj_listu_profesora, 
    ucitaj_listu_studenata, sacuvaj_listu_profesora i sacuvaj_listu_studenata koje kao rezultat 
    pozivanja: vraćaju putanju fajla; listu predmeta, profesora ili studenata; ispisuju listu 
    ili recnik koja je parametar funkcije u odgovarajuce fajlove
"""

import json, os

def putanja_fajla(ime_fajla):
    """ Funkcija putanja fajla vraća putanju do fajla koji je naveden u parametru ime_fajla
        a ukoliko je datoteka nepostojeća prazan string
    """
    try:
        trenutna_putanja = os.path.dirname(__file__)
        nova_putanja = os.path.join(trenutna_putanja, "..\\data", ime_fajla)
        return nova_putanja
    except IOError:
        return ''

def ucitaj_listu_predmeta():
    """ Funkcija ucitaj_listu_predmeta vraća listu predmeta iz datoteke predmeti.csv
        a ukoliko je datoteka nepostojeća vraća praznu listu
    """
    try:
        putanja = putanja_fajla("predmeti.csv")
        with open(putanja, "r", encoding="utf-8") as fp:
            # operator [] koristimo kako bismo preskočili prve dve linije 
            # datoteke predmeti.csv (definisanje separatora i zaglavlje)
            predmeti = fp.readlines()[2:]
        return predmeti
    except IOError:
        return []

def ucitaj_listu_profesora():
    """ Funkcija ucitaj_listu_profesora vraća listu profesora iz datoteke profesori.csv
        a ukoliko je datoteka nepostojeća vraća praznu listu
    """
    try:
        putanja = putanja_fajla("profesori.csv")
        with open(putanja, "r", encoding="utf-8") as fp:
            # operator [] koristimo kako bismo preskočili prvu liniju
            # datoteke profesori.csv (definisanje separatora)
            profesori = fp.readlines()[1:]
        return profesori
    except IOError:
        return []

def ucitaj_listu_studenata():   
    """ Funkcija ucitaj_lista_studenata vraća listu studenata iz datoteke studenti.json,
        a ukoliko je datoteka nepostojeća vraća praznu listu
    """
    try:
        putanja = putanja_fajla("studenti.json")
        with open(putanja, "r", encoding="utf-8") as fp:                      
            studenti = json.load(fp)
        return studenti
    except IOError:
        return []

def sacuvaj_listu_profesora(profesori):
    """ Funkcija sacuvaj_listu_profesora ispisuje listu profesora u datoteku profesori.csv
    """
    putanja = putanja_fajla("profesori.csv")
    with open(putanja, "w", encoding="utf-8") as fp:
        # definisanje separatora csv fajla
        fp.write("sep=;\n") 
        fp.writelines(profesori)

def sacuvaj_listu_studenata(studenti):
    """ Funkcija sacuvaj_listu_studenata ispisuje listu studenata u datoteku studenti.json
    """
    putanja = putanja_fajla("studenti.json")
    with open(putanja, "w", encoding="utf-8") as fp:
        json.dump(studenti, fp, indent=4)