import csv

def registracija_kuvara():
    with open("./data/korisnici.csv", "r", encoding="utf-8") as fp:
        citac = csv.DictReader(fp)
        podaci = list(citac)

        korisnicko_ime = input("Unesite korisnicko ime kuvara: ")
        for podatak in podaci:                                                                #prolazi kroz datoteku i proverava 
            while korisnicko_ime == podatak["korisnicko_ime"] or korisnicko_ime =="":         #da li je korisnicko ime koje je uneseno vec postoji u datoteci
                print('Error: Korisnicko ime je vec registrovano ili je pogresno uneto')      #(korisnicko ime mora biti jedinstveno) ukoliko postoji ili nije nista uneto
                korisnicko_ime=input("Unesite ponovo korisnicko ime: ")                       #ponavlja se unos
            
        email = input("Unesite email (npr. primer@gmail.com):")                               #email mora biti jedinstven isto kao i korisnicko ime
        for podatak in podaci:
            while email == podatak["email"] or email =="":
                print('Error: Email je vec registrovan ili je pogresno unet')
                email=input("Unesite ponovo email: ")
                    
        lozinka = input("Unesite lozinku:")                                                   #za sve ostalo unos se ponavlja samo ako nije nista uneseno
        while lozinka == "":
            print("Error: Morate uneti lozinku!")
            lozinka=input("Unesite lozinku: ")
        ime = input("Unesite ime kuvara:")
        while ime == "":
            print("Error: Morate uneti ime!")
            ime = input("Unesite ime:")
        prezime = input("Unesite prezime kuvara:")
        while prezime == "":
            print("Error: Morate uneti prezime!")
            prezime = input("Unesite prezime:")
        zanimanje = "kuvar"
            
           

        with open("./data/korisnici.csv", "a", encoding="utf-8") as fp:          #otvaram fajl u koji dodajem novog korisnika
            red=","
            recnik = {
                "korisnicko_ime": korisnicko_ime,
                "lozinka": lozinka,
                "ime": ime,
                "prezime": prezime,
                "email": email,
                "zanimanje": zanimanje}
            red = red.join(recnik.values())
            fp.write("\n"+ red)                                  
            print("Korisnik uspesno registrovan!")

        print("Da li zelite da dodate jos prijava? (da/ne)")                   
        opcija=input("Unesite opciju: ")
        if opcija=="da":
            registracija_kuvara()                                              
        elif opcija=="ne" or opcija !="da":
            print("Povratak na meni")
            return




        


