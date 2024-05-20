import random
import json
import csv
import statistics

def sifra_recepta1():                                     
    slovo1 = chr(random.randint(ord("A"), ord("Z")))     #pomocu ord pretvaramo slova u odgovarajuce brojeve prema unikodu,
    slovo2 = chr(random.randint(ord("A"), ord("Z")))     #random generisemo broj pomocu opcije random.randint,
    slovo3 = chr(random.randint(ord("A"), ord("Z")))     #na kraju random generisan broj pomocu char pretvaramo u slovo
    broj1 = str(random.randint(0, 9)) 
    broj2 = str(random.randint(0, 9))                    #random generisemo int broj i pretvaramo u string radi upisivanja 
    broj3 = str(random.randint(0, 9))
    sifra_recepta = slovo1+slovo2+slovo3+broj1+broj2+broj3
    return sifra_recepta
        
def dodavanje_recepta(email): 
    with open("./data/recepti.json", "r+", encoding= "utf-8") as fp:
        list=[]
        try:                                                                 #u slucaju da je json datoteka prazna, u toku load ucitava prazan string i izbacuje error
            svi_recepti=json.load(fp)                                       
        except json.decoder.JSONDecodeError:                                 #ako izbaci error, u datoteku ubacujem listu 
            return json.dump(list,fp,indent = 4)
        
    with open("./data/recepti.json", "r", encoding= "utf-8") as fp:
        svi_recepti=json.load(fp)
        sifra_recepta = sifra_recepta1()                                    #vrednost koju funkcija vraca stavljam u promenjivu
        for recept in svi_recepti:
            if sifra_recepta == recept["sifra_recepta"]:               #ukoliko sifra vec postoji, generisemo novu sifru
                sifra_recepta = sifra_recepta1()

    email_korisnika = email                           #email prijavljenog korisnika stavljam u promenjivu kako bi se znao autor recepta
    naziv = input("Unesite naziv recepta: ")
    kategorija = input("Unesite kategoriju recepta (nesto od: dezert, pecivo, glavno jelo, predjelo):")
    obrok = ["dezert", "pecivo", "glavno jelo", "predjelo"]
    while kategorija not in obrok:
        print("Pogresan unos, unesite nesto od navedenog: dezert, pecivo, glavno jelo, predjelo")
        kategorija = input("Unesite kategoriju recepta:")

    sastojci=[]
    sastojak = input("Unesite sastojak:")                                            #korisnik unosi sastojke
    sastojci.append(sastojak)
    nastavak = input("Da li zelite da unsete jos sastojaka? (da/ne):")
    while nastavak == "da":
        sastojak = input("Unesite sastojak:")
        sastojci.append(sastojak)
        nastavak = input("Da li zelite da unsete jos sastojaka? (da/ne):")

    koraci=[]
    korak= input("Unesite instrukcije za pravljenje jela:")                              #korisnik unosi korake
    koraci.append(korak)
    nastavak1 = input("Da li zelite da unesete jos jednu instrukciju? (da/ne):")
    while nastavak1 == "da":
        korak= input("Unesite instrukcije za pravljenje jela:")
        koraci.append(korak)
        nastavak1 = input("Da li zelite da unesete jos instrukcija? (da/ne):")
                
    recnik ={                                                                           #formira se recnik sa podacima koje je korisnik uneo
        "sifra_recepta": sifra_recepta, 
        "email_korisnika": email_korisnika,
        "naziv_recepta": naziv,
        "kategorija_recepta": kategorija,
        "sastojci": sastojci,
        "koraci": koraci
        }
    svi_recepti.append(recnik)                                                         #recnik se dodaje u datoteku kao recept
    with open("./data/recepti.json", "w", encoding="utf-8") as fp:
        json.dump(svi_recepti,fp, indent=4)
        print("\nRecept uspesno dodat!\n")
            
    print("Da li zelite da dodate jos recepata? (da/ne):")
    opcija=input("Unesite opciju: ")
    if opcija=="da":
        dodavanje_recepta(email)
    elif opcija=="ne":
        print("Povratak na meni.")
    
    

def pretraga_recepta():                                               #pretraga recepta prema nazivu i kategoriji
    with open("./data/recepti.json", "r", encoding="utf-8") as fp:
            svi_recepti=json.load(fp)
    odluka = input("Da li zelite da pretrazujete recept spram naziva ili spram kategorije? (naziv/kateogrija):")
    lista=[]
    if odluka == "naziv":                                                #ukoliko korisnik izabere naziv
                pretraga = input("Unesite naziv recepta koji trazite:")
                print("")
                promena = False
                while promena == False:
                    i = 0
                    for recept in svi_recepti:                                                #prolazi kroz datoteku
                        if pretraga == recept["naziv_recepta"]:                              #proverava da li je naziv koji je korisnik uneo isti kao neki naziv recepta iz datoteke
                                    trenutna_sifra = recept["sifra_recepta"]                                   #kad pronadje isti naziv, sifru tog recepta sacuvam u promenjivu
                                    email = recept["email_korisnika"]                                          #kao i email autora recepta
                                    with open("./data/korisnici.csv", "r", encoding="utf-8") as fp:
                                        citac = csv.DictReader(fp)
                                        podaci= list(citac)
                                        for podatak in podaci:                                       #ulazim u datoteku korisnici kako bi nasao ime i prezime
                                            if email == podatak["email"]:                            #na osnovu email-a autora trazim ime i prezime autora
                                                ime = podatak["ime"]
                                                prezime = podatak["prezime"]
                                    with open("./data/ocene.json", "r", encoding="utf-8") as fp:        #otvaram datoteku ocene kako bih proverio da li je recept ocenjen
                                        sve_ocene = json.load(fp)
                                        promena = False
                                        for recept_ocene in sve_ocene:
                                            if trenutna_sifra == recept_ocene["sifra_recepta"]:          
                                                ocena = recept_ocene["ocena"]                            #ukoliko je pronadjena ocena racuna se prosecna ocena
                                                prosecna_ocena1 = statistics.mean(ocena)
                                                promena = True
                                        if promena == False:                                             #ukoliko nije pronadjena ocena ispisuje "neocenjeno"
                                            prosecna_ocena1 = ("neocenjeno")
                                    i += 1
                                    print("{0}.{1},{2},{3},Prosecna ocena: {4}".format(i,recept["sifra_recepta"],recept["naziv_recepta"],ime+ " " +prezime, prosecna_ocena1))      
                                    sifra = recept["sifra_recepta"]
                                    lista.append(sifra)                                               #sifre od pronadjenih recepata dodajem u listu
                                       
                                    promena = True
                                    
                    if i == 0:                                                                    #ako i ostane nula znaci da nije pronadjen recept
                        print("Recept koji trazite ne postoji.")
                        opcija = input("Da li zelite da pretrazite jos recepata(da/ne):")
                        if opcija=="da":
                            pretraga_recepta()
                           
                    else:
                        return lista                            #funkcija pretraga_recepata vraca listu sa siframa pronadjenih recepata
        
    elif odluka == "kategorija":
            print("Kategorije:")
            print("1. Dezert")
            print("2. Pecivo")
            print("3. Glavno jelo")
            print("4. Predjelo")


            pretraga = input("Unesite broj ispred kategorije kako biste izabrali kategoriju koju zelite(1-4):")
            while pretraga != "1" and pretraga!= "2" and pretraga!= "3" and pretraga!= "4":
                pretraga = input("Morate uneti broj ispred ponudjene kategorije(1-4), pokusajte ponovo:")
            match pretraga:
                case "1":
                      pretraga = "dezert"
                case "2":
                      pretraga = "pecivo"
                case "3":
                      pretraga = "glavno jelo"
                case "4":
                      pretraga = "predjelo"
            print("")
            promena = False
            while promena == False:
                i = 0
                for recept in svi_recepti:
                    if pretraga == recept["kategorija_recepta"]:          #indenticno kao pretraga prema nazivu samo se trazi preko kategorije
                                trenutna_sifra = recept["sifra_recepta"]
                                email = recept["email_korisnika"]
                                with open("./data/korisnici.csv", "r", encoding="utf-8") as fp:
                                    citac = csv.DictReader(fp)
                                    podaci= list(citac)
                                    for podatak in podaci:
                                        if email == podatak["email"]:
                                            ime = podatak["ime"]
                                            prezime = podatak["prezime"]
                                with open("./data/ocene.json", "r", encoding="utf-8") as fp:
                                        sve_ocene = json.load(fp)
                                        promena = False
                                        for recept_ocene in sve_ocene:
                                            if trenutna_sifra == recept_ocene["sifra_recepta"]:
                                                ocena = recept_ocene["ocena"]
                                                prosecna_ocena1 = statistics.mean(ocena)
                                                promena = True
                                            if promena == False:
                                                prosecna_ocena1 =("neocenjeno")
                                i += 1
                                print("{0}.{1},{2},{3},Prosecna ocena: {4}".format(i,recept["sifra_recepta"],recept["naziv_recepta"],ime+ " " +prezime,prosecna_ocena1))
                                sifra = recept["sifra_recepta"]
                                lista.append(sifra)
                                              
                                promena = True
                if i == 0:
                    print("Recept koji trazite ne postoji.")
                    opcija = input("Da li zelite da pretrazite jos recepata(da/ne):")
                    if opcija=="da":
                        pretraga_recepta()
                
                else:
                    return lista

    else:
        print("Morate uneti jednu od dve ponudjene opcije (naziv/kategorija)")
        pretraga_recepta()
                


def ocenjivanje_recepta(email):
    with open("./data/ocene.json", "r+", encoding= "utf-8") as fp:
        lista_json=[]
        try:                                                                 #u slucaju da je json datoteka prazna, u toku load ucitava prazan string i izbacuje error
            svi_recepti=json.load(fp)                                       
        except json.decoder.JSONDecodeError:                                 #ako izbaci error, u datoteku vracam listu
            return json.dump(lista_json,fp,indent = 4)
          
    sifre = pretraga_recepta()                                                   #pozivam pretragu koja mi vraca listu sa siframa, listu stavljam u promenjivu sifre
    izbor = int(input("Unesite redni broj recepta koji zelite da ocenite:")) 
    sifra = sifre[izbor-1]                                                       #[izbor-1] u listi se krece od nulte pozicije
    
    with open("./data/korisnici.csv", "r", encoding ="utf-8") as fp:
        citac = csv.DictReader(fp)
        podaci = list(citac)
        for podatak in podaci:
            if email == podatak["email"]:                                                     #trazim ime i prezime prijavljenog korisnika 
                ime = podatak["ime"]                                                          #da bi se znalo ko je uneo komentar
                prezime = podatak["prezime"]

    with open("./data/recepti.json", "r", encoding="utf-8") as fp:
        svi_recepti = json.load(fp)
        for recept in svi_recepti:
            if sifra == recept["sifra_recepta"]:                                                        #trazim email autora recepta 
                email_autora = recept["email_korisnika"]                                                #da bi iz csv korisnici pomocu email nasao korisnicko ime
                with open("./data/korisnici.csv", "r", encoding="utf-8") as fp:
                    citac = csv.DictReader(fp)
                    podaci = list(citac)
                    for podatak in podaci:
                        if email_autora == podatak["email"]:
                            korisnicko_ime = podatak["korisnicko_ime"]                                  #iz csv datoteke korisnici pomocu email autora pronalazim korisnicko ime

    with open("./data/ocene.json", "r", encoding="utf-8") as fp:
        svi_recepti_ocene = json.load(fp)
        while True:
            try:
                ocena = int(input("Unesite ocenu (0-10): "))
                if ocena >= 0 or ocena <= 10:
                    break
                else:
                    print("Ocena mora biti izmedju 0 i 10. Pokusajte opet.")
            except ValueError:
                print("Pogresan unos. Molimo unesite broj.")                          #unosi se ocena, ako korisnik unese broj veci od 10 ili ako ne unese broj ponavlja unos
                                                                                      
        opcija = input("Da li zelite da unesete komentar? (da/ne):")
        if opcija == "da":
            komentar = input("Unesite komentar:")                                      #unosi se komentar
            ceo_komentar = ("{0} {1}: {2}".format(ime,prezime, komentar))
        elif opcija == "ne":
            komentar = "nema komentara"
            ceo_komentar = ("{0} {1}: {2}".format(ime,prezime, komentar))

        lista_sifara=[]
        for recept_ocena in svi_recepti_ocene:
            lista_sifara.append(recept_ocena["sifra_recepta"]) 

            if sifra == recept_ocena["sifra_recepta"]:                                  #ako sifra recepta vec postoji u datoteci ocene dodajemo ocenu i komentar u vec postojece ocene i komentare
                recept_ocena["ocena"].append(ocena)
                if opcija == "da":
                    recept_ocena["komentari"].append(ceo_komentar)

                with open("./data/ocene.json", "w", encoding="utf-8") as fp:
                    json.dump(svi_recepti_ocene,fp,indent=4)
                    print("\nRecept uspesno ocenjen!\n")
                
                    
        if sifra not in lista_sifara:                                           #ako sifra ne postoji u datoteci ocene, dodajemo ceo ocenjen recept
            recnik ={
            "sifra_recepta": sifra,
            "korisnicko_ime": korisnicko_ime,
            "ocena": [ocena],
            "komentari": [ceo_komentar]
            }
            svi_recepti_ocene.append(recnik)
            with open("./data/ocene.json", "w", encoding="utf-8") as fp:
                json.dump(svi_recepti_ocene,fp,indent=4)
                print("\nRecept uspesno ocenjen!\n") 
        
        for recept_ocena in svi_recepti_ocene:
            if sifra == recept_ocena["sifra_recepta"]:
                brojevi = recept_ocena["ocena"]
                prosecna_ocena = statistics.mean(brojevi)
                    
                print("Prosecna ocena:{0}, Komentari:{1}".format(prosecna_ocena, recept_ocena["komentari"]))         #nakon ocenjivanja ispisujemo prosecnu ocenu i komentare
            
                         
                                                            
      

def brisanje_recepata(email):
    lista=[]
    with open("./data/recepti.json", "r", encoding="utf-8") as fp:
        svi_recepti = json.load(fp)
        i=0
        for recept in svi_recepti:                             #samo autor recepta moze da obrise recept
            if email == recept["email_korisnika"]:             #proveravam da li je email trenutno prijavljenog korisnika isti kao email autora recepta
                trenutna_sifra = recept["sifra_recepta"]
                with open("./data/ocene.json", "r", encoding="utf-8") as fp:
                    sve_ocene = json.load(fp)
                    promena = False
                    for recept_ocene in sve_ocene:
                        if trenutna_sifra == recept_ocene["sifra_recepta"]:
                            ocena = recept_ocene["ocena"]
                            prosecna_ocena1 = statistics.mean(ocena)
                            promena = True
                        if promena == False:
                            prosecna_ocena1 =("neocenjeno")
                i += 1                                                            
                print("{0}.{1},{2},Prosecna ocena: {3}".format(i,recept["sifra_recepta"],recept["naziv_recepta"],prosecna_ocena1))     #ispisujem sve recepte koje je korisnik kreirao
                lista.append(recept["sifra_recepta"])         #sifru recepta dodajem u listu
        if i == 0:
            print("Nije pronadjen ni jedan recept koji se vi kreirali.")
        elif i>0:
            promena = True
            while promena == True:
                izbor = (input("Unesite sifru recepta koji zelite da izbrisete: "))
                if izbor in lista:                                   #ukoliko je sifra koju smo uneli u listi brisemo recept iz datoteke recepti
                    for recept in svi_recepti:
                        if recept["sifra_recepta"] == izbor:
                            indeks_za_brisanje = next((i for i, d in enumerate(svi_recepti) if d['sifra_recepta'] == izbor), None)
                            if indeks_za_brisanje is not None:
                               del svi_recepti[indeks_za_brisanje]
                            with open("./data/recepti.json", "w", encoding="utf-8") as fp:
                                json.dump(svi_recepti,fp,indent=4)
                                promena = False
                                break
                    with open("./data/ocene.json", "r", encoding="utf-8") as fp:           #brisemo recept iz datoteke ocene
                        sve_ocene = json.load(fp)
                        for recepti_ocene in sve_ocene:
                            if recepti_ocene["sifra_recepta"] == izbor:
                                indeks_za_brisanje = next((i for i, d in enumerate(sve_ocene) if d['sifra_recepta'] == izbor), None)
                                if indeks_za_brisanje is not None:
                                   del sve_ocene[indeks_za_brisanje]
                                
                                with open("./data/ocene.json", "w", encoding="utf-8") as fp:        
                                    json.dump(sve_ocene,fp,indent=4)
                                    promena = False
                                    break
                        print("\nRecept uspesno izbrisan.")
                elif izbor not in lista:
                    print("sifra koju ste uneli je netacna, unesite jednu od ponudjenih")
                    
                    
            
       
            
    

                
            
            

        
                    

        
            

        

        
        


