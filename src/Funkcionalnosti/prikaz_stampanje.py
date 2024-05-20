import json
import statistics
from Funkcionalnosti.recepti import pretraga_recepta

def prikaz_recepta():
        odluka = input("Ako zelite da prikazete recepte unosom sifre unesite (sifra),ako birate pretragu recepta unesite (pretraga). (sifra/pretraga):")
        while odluka !="sifra" and odluka !="pretraga":
            print("Greska, unesite ponovo.")
            odluka = input("Ako zelite da prikazete recepte unosom sifre unesite (sifra),ako birate pretragu recepta unesite (pretraga). (sifra/pretraga):")
        if odluka == "sifra":                                        #ukoliko korisnik zeli da prikaze recepte preko sifre
            uslov = True       
            while uslov == True:
                with open("./data/recepti.json", "r", encoding="utf-8")as fp:
                    svi_recepti = json.load(fp)
                    print("Postojece sifre:")                        
                    for recept in svi_recepti:
                        print(recept["sifra_recepta"],":", recept["naziv_recepta"])           #ispisujemo sve postojece sifre i nazive recepta    
                sifra = input("Unesite sifru:")                                               #korisnik unosi neku od ponudjenih sifara
                with open("./data/ocene.json", "r", encoding="utf-8")as fp:
                    sve_ocene = json.load(fp)
                    promena = False
                    for recept_ocene in sve_ocene:
                        if sifra == recept_ocene["sifra_recepta"]:
                            ocena = recept_ocene["ocena"]                                  #ukoliko je pronadjena racuna se prosecna ocena
                            prosecna_ocena = statistics.mean(ocena)
                            promena = True
                    if promena == False:
                        prosecna_ocena =("neocenjeno")
                    promena = False
                    for recept_ocene in sve_ocene:
                        if sifra == recept_ocene["sifra_recepta"]:
                            komentar = recept_ocene["komentari"]
                            promena = True
                    if promena == False:
                        komentar = ("neocenjeno")
                    
                
                    for recept in svi_recepti:
                        if sifra == recept["sifra_recepta"]:
                            print("{0}, Autor recepta: {1}, Naziv recepta: {2}, Kategorija recepta: {3}, Sastojci: {4}, Koraci: {5}, Komentari: {6}, Prosecna ocena: {7}".format(recept["sifra_recepta"],\
                                                            recept["email_korisnika"],\
                                                            recept["naziv_recepta"],\
                                                            recept["kategorija_recepta"],\
                                                            recept["sastojci"],\
                                                            recept["koraci"],komentar,prosecna_ocena))         #ispisujem sve podatke za taj recept
                            uslov = False
                            break
                    if uslov == True:
                        print("Ne postoji recept sa unetom sifrom, pokusajte opet.")


        elif odluka == "pretraga":                #prikaz preko pretrage
           sifre = pretraga_recepta()             #pozivam pretragu recepta, nakon sto mi ispise recepte ispisuje ih ponovo sa svim podacima
           
           with open("./data/recepti.json", "r", encoding="utf-8")as fp:
                    svi_recepti = json.load(fp)
                    for recept in svi_recepti:
                        if recept["sifra_recepta"] in sifre:            #ako nadje sifru koja je u listi sifre koju vraca funkcija pretraga, ispisuje sve podatke za taj recept
                            sifra = recept["sifra_recepta"]
                            with open("./data/ocene.json", "r", encoding="utf-8")as fp:
                                sve_ocene = json.load(fp)
                                promena = False
                                for recept_ocene in sve_ocene:
                                    if sifra == recept_ocene["sifra_recepta"]:
                                        ocena = recept_ocene["ocena"]               #ukoliko je pronadjena racuna se prosecna ocena
                                        prosecna_ocena = statistics.mean(ocena)
                                        promena = True
                                if promena == False:
                                    prosecna_ocena = ("neocenjeno")

                                promena = False
                                for recept_ocene in sve_ocene:
                                    if sifra == recept_ocene["sifra_recepta"]:
                                        komentar = recept_ocene["komentari"]               #trazi komentare
                                        promena = True
                                if promena == False:
                                    komentar = ("nema komentara")
                                    
                            print("{0}, Autor recepta: {1}, Naziv recepta: {2}, Kategorija recepta: {3}, Sastojci: {4}, Koraci: {5}, Komentari: {6}, Prosecna ocena: {7}".format(recept["sifra_recepta"],\
                                                            recept["email_korisnika"],\
                                                            recept["naziv_recepta"],\
                                                            recept["kategorija_recepta"],\
                                                            recept["sastojci"],\
                                                            recept["koraci"],komentar,prosecna_ocena))           #ispisuje se recept sa svim podacima



def stampanje_recepta():
    uslov = True       
    while uslov == True:
        recepti =[]
        with open("./data/recepti.json", "r", encoding="utf-8")as fp:
            svi_recepti = json.load(fp)
            print("Postojece sifre:")
            for recept in svi_recepti:
                print(recept["sifra_recepta"],":", recept["naziv_recepta"])                #ispisujem korisniku sve sifre sa nazivima, kako bi izabrao jednu

        sifra = input("Unesite sifru recepta koji zelite da istampate:")
        with open("./data/ocene.json", "r", encoding="utf-8")as fp:           #otvaram datoteku radi pretrage: da li izabrani recept ima ocenu i komentare
            sve_ocene = json.load(fp)
            promena = False
            for recept_ocene in sve_ocene:
                if sifra == recept_ocene["sifra_recepta"]:
                    ocena = recept_ocene["ocena"]               #ukoliko je pronadjena racuna se prosecna ocena
                    prosecna_ocena = statistics.mean(ocena)
                    promena = True
            if promena == False:
                prosecna_ocena = ("neocenjeno")

            promena = False
            for recept_ocene in sve_ocene:
                if sifra == recept_ocene["sifra_recepta"]:
                    komentar = recept_ocene["komentari"]               #trazi komentar
                    promena = True
            if promena == False:
                komentar = ("nema komentara")

            
            for recept in svi_recepti:
                if sifra == recept["sifra_recepta"]:
                    autor_recepta = recept["email_korisnika"]
                    naziv_recepta = recept["naziv_recepta"]
                    kategorija_recepta = recept["kategorija_recepta"]
                    sastojci = recept["sastojci"]
                    koraci = recept["koraci"] 
                    recnik={                                         #formiramo recnik sa receptom 
                        "sifra":sifra,
                        "autor_recepta": autor_recepta,
                        "naziv_recepta": naziv_recepta,
                        "kategorija_recepta":kategorija_recepta,
                        "sastojci":sastojci,
                        "koraci":koraci,
                        "komentari":komentar,
                        "prosecna_ocena":prosecna_ocena
                        }
                    recepti.append(recnik)                           #recnike dodajem u listu     
                        
                    ime_fajla = f"{sifra} - {naziv_recepta}.txt"
                    with open("./data/{}".format(ime_fajla), 'w',encoding="UTF-8") as fajl:                 #recept zapisujem u txt datoteku
                        for red in recepti:                                             
                            fajl.write(f"Sifra: {red['sifra']}\n")
                            fajl.write(f"Autor recepta: {red['autor_recepta']}\n")
                            fajl.write(f"Naziv recepta: {red['naziv_recepta']}\n")
                            fajl.write(f"Kategorija recepta: {red['kategorija_recepta']}\n")
                            fajl.write(f"Sastojci: {red['sastojci']}\n")
                            fajl.write(f"Koraci: {red['koraci']}\n")
                            fajl.write(f"Komentari: {red['komentari']}\n")
                            fajl.write(f"Prosecna ocena: {red['prosecna_ocena']}\n")
                    print("Recept uspesno istampan!")
                    uslov = False
                    break

            if uslov == True:
                print("Ne postoji recept sa unetom sifrom, pokusajte opet.")

            
           