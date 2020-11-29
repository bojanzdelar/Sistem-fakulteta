""" Modul funkcionalnosti u okviru paketa profesori sadrži funkcije 
    dodavanje_ocene, brisanje_ocene, prosecna_ocena_za_predmet,
    promena_termina_konsultacija koje omogućavaju dodavanje i brisanje ocena,
    računanej prosečne ocene za predmet i promenu termina konsultacija
    Napomena: Za ove funkcionalnosti mora biti prijavljen korisnik i to kao profesor.
"""
from liste_podataka import ucitaj_listu_predmeta, ucitaj_listu_profesora, ucitaj_listu_studenata, sacuvaj_listu_profesora, sacuvaj_listu_studenata

def dodavanje_ocene(sifra_profesora):
    """ Funkcija dodavanje_ocene najpre omogućava profesoru da pretražuje studente spram imena,
        a zatim i doda ocenu, u opsegu od 5 do 10, jednom od ponuđenih studenata (po broju indeksa)
    """
    print("\nDodavanje ocene studentu")
    ime = input("Unesite ime studenta (bez prezimena): ")
    studenti = ucitaj_listu_studenata()
    filtrirani_studenti = []
    filtrirani_brojevi_indeksa = []
    # pretrazivanje studenata sa unetim imenom
    for student in studenti:
        if ime.lower() == student["ime"].lower():
            filtrirani_studenti.append(student)
            filtrirani_brojevi_indeksa.append(student["broj indeksa"])
    # ukoliko ne postoji student sa unetim imenom program se prekida
    if not len(filtrirani_studenti): 
        print("- Nema studenata se imenom", ime)
        return
    # ukoliko postoji student sa unetim imenom stampa se njegov broj indeksa, ime i prezime
    for i in range(len(filtrirani_studenti)):
        print(str(i + 1) + ".", filtrirani_studenti[i]["broj indeksa"], \
        filtrirani_studenti[i]["ime"], filtrirani_studenti[i]["prezime"])
    broj_indeksa = None
    while broj_indeksa not in filtrirani_brojevi_indeksa:
        try:
            broj_indeksa = int(input("Unesite broj indeksa studenta: "))
        except ValueError:
            continue
    # prikaz svih predmeta sa njihovom sifrom i nazivom
    predmeti = ucitaj_listu_predmeta()
    sifre_predmeta = []
    for i in range(len(predmeti)):
        sifra = predmeti[i].split(";")[0]
        naziv = predmeti[i].split(";")[1].strip()
        sifre_predmeta.append(sifra)
        print(str(i + 1) + ".", sifra, naziv)
    # unos sifre predmeta i provera njenog postojanja u listi predmeta
    sifra_predmeta = input("Unesite šifru predmeta: ")
    if sifra_predmeta not in sifre_predmeta:
        print("- Ne postoji uneta šifra predmeta")
        return
    # unos i provera validnosti ocene
    ocena = None
    while ocena not in (5, 6, 7, 8, 9, 10):
        try:
            ocena = int(input("Unesite ocenu (5-10): "))
        except ValueError:
            continue
    for student in studenti:
        # dodavanje ucene odgovarajucem studentu
        if broj_indeksa == student["broj indeksa"]:
            nova_ocena = {"sifra_predmeta": sifra_predmeta, "sifra_profesora": sifra_profesora, "ocena": ocena}
            student["ocene"].append(nova_ocena)
            sacuvaj_listu_studenata(studenti)
            print("- Uspešno dodavanje ocene")

def brisanje_ocene(sifra_profesora):
    """ Funkcija brisanje_ocene najpre pretražuje profesoru studente spram imena,
        prikazuje sve ocene studenta naspram broja indeksa i omogućava brisanje prikazanih ocena
    """
    print("\nBrisanje ocene studentu")
    ime = input("Unesite ime studenta (bez prezimena): ")
    studenti = ucitaj_listu_studenata()
    filtrirani_studenti = []
    filtrirani_brojevi_indeksa = []
    # pretrazivanje studenata sa unetim imenom
    for student in studenti:
        if ime.lower() == student["ime"].lower():
            filtrirani_studenti.append(student)
            filtrirani_brojevi_indeksa.append(student["broj indeksa"])
    # ukoliko ne postoji student sa unetim imenom program se prekida
    if not len(filtrirani_studenti): 
        print("- Nema studenata se imenom", ime)
        return
    # ukoliko postoji student sa unetim imenom stampa se njegov broj indeksa, ime i prezime
    for i in range(len(filtrirani_studenti)):
        print(str(i + 1) + ".", filtrirani_studenti[i]["broj indeksa"], \
        filtrirani_studenti[i]["ime"], filtrirani_studenti[i]["prezime"])
    # uneti broj indeksa mora odgovara unetom imenu
    broj_indeksa = None
    while broj_indeksa not in filtrirani_brojevi_indeksa:
        try:
            broj_indeksa = int(input("Unesite broj indeksa studenta: "))
        except ValueError:
            continue
    # brojac predstavlja broj ocena prijavljenog profesora
    brojac = 0
    for student in studenti:
        # trazenje izabranog studenta
        if broj_indeksa == student["broj indeksa"]:
            ocene = student["ocene"]
            # stampanje profesorovih ocena ukoliko postoje, prekid programa ako ih nema
            for ocena in ocene:
                if sifra_profesora == ocena["sifra_profesora"]:
                    brojac += 1
                    print(str(brojac) + ".", ocena["sifra_predmeta"], ocena["ocena"])
            if brojac == 0:
                print("- Prijavljeni profesor nema nijednu ocenu za odabranog studenta")
                return
            # odabir ocene koja se brise 
            redni_broj = None
            while redni_broj not in range(1, brojac + 1):
                try:
                    redni_broj = int(input("Unesite redni broj ocene koju želite da obrišete(1/.../n): "))
                except ValueError:
                    continue
            # brojace se resetuje, i povecava dok se ne izjednaci sa rednim brojem odabrane ocene
            brojac = 0
            # trazenje i brisanje izabrane ocene
            for i in range(len(ocene)):
                if sifra_profesora == ocene[i]["sifra_profesora"]:
                    if redni_broj == brojac + 1:
                        student["ocene"].pop(i)
                        sacuvaj_listu_studenata(studenti)
                        print("- Uspešno brisanje ocene")
                        return
                    else:
                        brojac += 1

def prosecna_ocena_za_predmet(sifra_profesora):
    """ Funkcija prosecna_ocena_za_predmet prijavljenom profesoru najpre prikazuje sve 
        predmete sa šifrom i nazivom, a zatim profesor bira redni broj predmeta za 
        koji želi da se izračuna prosečna ocena
    """
    print("\nRačunanje prosečne ocene za predmet")
    predmeti = ucitaj_listu_predmeta()
    # prikazivanje svih predmeta sa sifrom i nazivom
    for i in range(len(predmeti)):
        sifra = predmeti[i].split(";")[0]
        naziv = predmeti[i].split(";")[1].strip()
        print(str(i + 1) + ".", sifra, naziv)
    redni_broj = None
    while redni_broj not in range(1, len(predmeti) + 1):
        try:
            redni_broj = int(input("Unesite redni broj predmeta (1/.../n): "))
        except ValueError:
            continue
    sifra_predmeta = predmeti[redni_broj - 1].split(";")[0]
    suma = 0 
    broj_ocena = 0
    studenti = ucitaj_listu_studenata()
    # pretrazivanje unete sifre predmeta medju svima ocenama svih studenta
    # i njihovo sabiranje ukoliko se pronadju
    for student in studenti:
        ocene = student["ocene"]
        for ocena in ocene:
            if sifra_predmeta == ocena["sifra_predmeta"] and sifra_profesora == ocena["sifra_profesora"]:
                suma += ocena["ocena"]
                broj_ocena += 1
    # ukoliko je broj ocena različit od 0
    if broj_ocena:
        print("- Prosečna ocena za predmet šifre", sifra_predmeta, "je", format(suma / broj_ocena, ".2f"))
    else:
        print("- Ne postoji nijedna ocena prijavljenog profesora za dati predmet")

def promena_termina_konsultacija(sifra_profesora):
    """ Funkcija promena_termina_konsultacija prijavljenom profesoru, na osnovu njegove
        šifre, prikazuje trenutni termin konsultacija i nudi mogućnost promene istog.
        Ukoliko se unese prazan string, zadržava se stari termin konsultacija
    """
    print("\nPromena termina konsultacija")
    profesori = ucitaj_listu_profesora()
    # trazimo profesora ciji sifra odgovora parametru funkcije (sifra_profesora)
    for i in range(len(profesori)):
        # sifra profesora koji je trenutno izabran iz niza profesori
        trenutna_sifra = int(profesori[i].split(";")[0])
        if sifra_profesora == trenutna_sifra:
            termin_konsultacija = profesori[i].split(";")[5].strip()
            print("Trenutni termin konsultacija je:", termin_konsultacija)
            termin_konsultacija = input("Unesite novi termin konsultacija: ")
            # ukoliko novi termin konsultacija nije prazan string promenu čuvamo u datoteku
            if termin_konsultacija.strip() != "":
                profesori[i] = profesori[i].split(";")
                profesori[i][5] = termin_konsultacija + "\n"
                profesori[i] = ";".join(profesori[i])
                sacuvaj_listu_profesora(profesori)
                print("- Uspešna promena termina konsultacija")
            else:
                print("- Zadržan je stari termin konsultacija")
            return