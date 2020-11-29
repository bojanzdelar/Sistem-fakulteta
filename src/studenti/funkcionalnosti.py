""" Modul funkcionalnosti u okviru paketa studenti sadrži funkcije 
    globalna_prosecna_ocena, predmeti i prikaz_profesora koje omogućavaju
    računanje globalne prosečne ocene studenta, prikaz položenih i nepoloženih
    predmeta studenta i prikaz podataka o profesoru koji predaje predmet.
    Napomena: Za ove funkcionalnosti mora biti prijavljen korisnik i to kao student.
"""

from liste_podataka import ucitaj_listu_predmeta, ucitaj_listu_profesora, ucitaj_listu_studenata

def globalna_prosecna_ocena(broj_indeksa):
    """ Funkcija globalna_prosecna_ocena vrši računanje tako što se na osnovu svih 
        ocena prijavljenog studenta (na osnovu paramtera broj_indeksa) izračuna 
        prosečna ocena i prikaže se studentu
    """
    print("\nRačunanje globalne prosečne ocene")
    studenti = ucitaj_listu_studenata()
    for student in studenti:
        # trazimo zapis student sa odgovarajucim brojem indeksa
        if broj_indeksa == student["broj indeksa"]:
            suma = 0
            ocene = student["ocene"]
            for ocena in ocene:
                suma += ocena["ocena"]
    # ukoliko broj ocena nije jednak nuli delimo sumu ocena sa brojem
    # ocena studenata (ovako izbegavamo deljenje sa nulom)
    if len(ocene):
        print("- Globalna prosečna ocena studenta je", format(suma / len(ocene), ".2f"))
    else:
        print("- Student nema unesene ocene, te ni prosek")               

def predmeti(broj_indeksa):
    """ Funkcija predmeti prikazuje korisniku sve položene ili nepoložene predmete
        prijavljenog studenta, na osnovu parametra broj_indeksa
    """
    print("\nPrikaz položenih ili nepoloženih predmeta")
    print("1. Položeni")
    print("2. Nepoloženi")
    opcija = None
    while opcija not in (1, 2):
        try:
            opcija = int(input("Izaberite jednu od navedenih opcija (1/2): "))
        except ValueError:
            continue
    studenti = ucitaj_listu_studenata()
    for student in studenti:
        # trazimo zapis student sa odgovarajucim brojem indeksa
        if broj_indeksa == student["broj indeksa"]:
            ocene = student["ocene"]
            # prikupljanje sifara polozenih predmeta
            sifre_polozenih_predmeta = []
            for ocena in ocene:
                sifre_polozenih_predmeta.append(ocena["sifra_predmeta"])
    predmeti = ucitaj_listu_predmeta()
    # u zavisnost da li je opcija 1 ili 2 ovde ce biti polozeni ili nepolozeni predmeti
    rezultirajuci_predmeti = []
    for predmet in predmeti:
        sifra_predmeta = predmet.split(";")[0]
        # trazenje studentovih polozenih ili nepolozenih predmeta u listi 
        # predmeta u zavisnosti od vrednosti opcije
        if opcija == 1 and sifra_predmeta in sifre_polozenih_predmeta \
        or opcija == 2 and sifra_predmeta not in sifre_polozenih_predmeta:
            ime_predmeta = predmet.split(";")[1]
            # dodavanje imena (ne)polozenog predmeta u listu rezultirajucih predmeta
            rezultirajuci_predmeti.append(ime_predmeta)
    if opcija == 1:
        print("\nPrikaz položenih predmeta")
    else:
        print("\nPrikaz nepoloženih predmeta")
    if len(rezultirajuci_predmeti) == 0:
        print("- Ne postoje traženi predmeti")
    else:
        for predmet in rezultirajuci_predmeti:
            # metod strip se koristi kako bi obrisali \n karaktere sa kraja stringa
            print("- " + predmet.strip()) 

def prikaz_profesora():
    """ Funkcija prikaz_profesora korisniku prikazuje sve predmete, nakon čega on bira 
        šifru jednog predmeta, a funkcija štampa sve profesore koji predaju taj predmet
    """
    print("\nPrikaz podataka o profesoru koji predaje predmet")
    # prikaz korisniku svih predmeta 
    predmeti = ucitaj_listu_predmeta()
    for predmet in predmeti:
        sifra = predmet.split(";")[0]
        naziv = predmet.split(";")[1].strip()
        print("-", sifra, naziv)
    sifra_predmeta = input("Unesite šifru predmeta: ")
    print("\nPodaci profesora koji predaje predmet šifre", sifra_predmeta)
    studenti = ucitaj_listu_studenata()
    sifre_profesora = []
    # pretraga postojanja date sifre predmeta medju studentima i njihovim ocenima
    for student in studenti:
        ocene = student["ocene"]
        for ocena in ocene:
            # ukoliko se pronadje data sifra predmeta u niz se dodaje odgovarajuca sifra profesora
            if sifra_predmeta == ocena["sifra_predmeta"] and \
            "sifra_profesora" in ocena and ocena["sifra_profesora"] != "":
                sifre_profesora.append(ocena["sifra_profesora"])
    # ukoliko nije pronadjen nijedan profesor za datu sifru stampa se obavestenje o tome
    if sifre_profesora == []:
        print("- Nijedan profesor ne predaje taj predmet")
    else:
        profesori = ucitaj_listu_profesora()
        # stampanje profesora koji predaju predmet sa odgovarajucom sifrom
        for profesor in profesori:
            sifra_profesora = int(profesor.split(";")[0])
            if sifra_profesora in sifre_profesora:
                ime = profesor.split(";")[2]
                prezime = profesor.split(";")[3]
                email = profesor.split(";")[4]
                konsultacije = profesor.split(";")[5].strip()
                print("- Ime: " + ime + " " + prezime + ", email: " + email + ", konsultacije: " + konsultacije)