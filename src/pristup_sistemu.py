""" Modul pristup_sistemu sadrži funkcije prijava_na_sistem i registracija
    koje omogućavaju korisniku da pristupi profesorskom ili studentskom meniju
"""

from liste_podataka import ucitaj_listu_profesora, ucitaj_listu_studenata, sacuvaj_listu_profesora, sacuvaj_listu_studenata
from profesori.meni import meni_profesora
from studenti.meni import meni_studenta

def prijava_na_sistem():
    """ Funkcija prijava_na_sistem podrazumeva unos šifre profesora ili broja indeksa, 
        kao korisničkog imena, i unos lozinke
    """
    print("\nPrijava na sistem")
    korisnicko_ime = None
    while True:
        try:
            korisnicko_ime = int(input("Unesite korisničko ime (ceo broj) - šifra profesora ili broj indeksa: "))
            break
        except ValueError:
            continue
    lozinka = input("Unesite lozinku: ")
    # provera postojanja datog korisnickog imena i lozinke u bazi profesora
    profesori = ucitaj_listu_profesora()
    for profesor in profesori:
        prof_korisnicko_ime = int(profesor.split(";")[0])
        prof_lozinka = profesor.split(";")[1]
        if korisnicko_ime == prof_korisnicko_ime and lozinka == prof_lozinka:
            print("- Uspešno prijavljivanje profesora")
            meni_profesora(korisnicko_ime)
            return
    # provera postojanja datog korisnickog imena i slozinke u bazi studenata
    studenti = ucitaj_listu_studenata()
    for student in studenti:                                        
        if korisnicko_ime == student["broj indeksa"] and lozinka == str(student["lozinka"]): 
            print("- Uspešno prijavljivanje studenta")
            meni_studenta(korisnicko_ime)
            return       
    print("- Neuspešno prijavljivanje")
 

def registracija():
    """ Funkcija registracija zahteva podatke koji opisuju profesora ili studenta,
        u zavisnosti od izbora korisnika
    """
    print("\nRegistracija")
    print("1. Profesor")
    print("2. Student")
    opcija = None
    while opcija not in (1, 2):
        try:
            opcija = int(input("Koga zelite da registrujete (1/2)? "))
        except ValueError:
            continue
    # pokusaj registrovanja profesora 
    if opcija == 1:
        print("\nRegistracija profesora")
        while True:
            try:
                korisnicko_ime = int(input("Unesite korisnicko ime (ceo broj) - šifra profesora: "))
                break
            except ValueError:
                continue
        profesori = ucitaj_listu_profesora()
        # provera postojanja datog korisnickog imena (sifre profesora) u bazi profesora
        for profesor in profesori:
            prof_korisnicko_ime = int(profesor.split(";")[0])
            if korisnicko_ime == prof_korisnicko_ime:
                print("- Korisnicko ime (sifra profesora) je zauzeta")
                return
        # ukoliko funkcija nije prekinuta (korisnicko ime nije zauzeto)
        # traze se preostali podaci, i novi_profesor se dodaje u bazu
        lozinka = input("Unesite lozinku: ")
        ime = input("Unesite ime: ")
        prezime = input("Unesite prezime: ")
        email = input("Unesite email adresu: ")
        konsultacije = input("Unesite termin konsultacija (dan, vreme): ")
        novi_profesor = str(korisnicko_ime) + ";" + lozinka + ";" + ime + ";" + prezime + ";" + email + ";" + konsultacije + "\n"
        profesori.append(novi_profesor)
        sacuvaj_listu_profesora(profesori)
        print("- Uspešna registracija profesora")
    # pokusaj registrovanja studenta
    elif opcija == 2:
        print("\nRegistracija studenta")
        while True:
            try:
                korisnicko_ime = int(input("Unesite korisnicko ime (ceo broj) - broj indeksa: "))
                break
            except ValueError:
                continue
        studenti = ucitaj_listu_studenata()
        # provera postojanja datog korisnickog imena (broj indeksa) u bazi studenata
        for student in studenti:
            stud_korisnicko_ime = student["broj indeksa"]
            if korisnicko_ime == stud_korisnicko_ime:
                print("- Korisnicko ime (broj indeksa) je zauzet")
                return 
        # ukoliko funkcija nije prekinuta (korisnicko ime nije zauzeto)
        # traze se preostali podaci, i novi_student se dodaje u bazu 
        lozinka = input("Unesite lozinku: ")
        ime = input("Unesite ime: ")
        prezime = input("Unesite prezime: ")
        email = input("Unesite email adresu: ")
        novi_student = {"broj indeksa": korisnicko_ime, "lozinka": lozinka, "ime": ime, "prezime": prezime, "email": email, "ocene": []}
        studenti.append(novi_student)
        sacuvaj_listu_studenata(studenti)
        print("- Uspešna registracija studenta")