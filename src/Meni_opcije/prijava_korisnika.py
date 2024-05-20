import csv
from Meni_opcije.registracija_kuvara import registracija_kuvara
from Funkcionalnosti.recepti import dodavanje_recepta, pretraga_recepta, ocenjivanje_recepta, brisanje_recepata
from Funkcionalnosti.prikaz_stampanje import prikaz_recepta
from Funkcionalnosti.prikaz_stampanje import stampanje_recepta

def prijava_korisnika():
    with open("./data/korisnici.csv", "r", encoding="utf-8") as fp:
        citac = csv.DictReader(fp)
        podaci = list(citac)
        
        email = input("Unesite email:")
        lozinka = input("Unesite lozinku:")

        while email =="" or lozinka =="":                   #ukoliko ostavi prazno email ili lozinku ponavlja se unos
            print("Greska, pokusajte ponovo:")
            email = input("Unesite email:")
            lozinka = input("Unesite lozinku:")

        prijava = False
        while prijava == False:
            for podatak in podaci:
                if podatak["email"] == email and podatak["lozinka"] == lozinka:              #for petljom ide kroz datoteku korisnici i proverava
                    print("\nUspesna prijava!")                                              #da li se unesen email i lozinka poklapaju 
                    print(f"Dobrodosao {podatak['ime']}. ({podatak['zanimanje']})\n")        
                    opcije(email,lozinka)                                                    #ako se poklapaju poziva se funkcija opcije
                    prijava = True                                                           #izlazi se iz while petlje
            if prijava == False:                                                             #ako ne pronadje ide opet kroz petlju i trazi ponovni unos
                print("Uneli ste pogresan email ili lozinku, pokusajte ponovo:")
                email = input("Unesite email:")
                lozinka = input("Unesite lozinku:")

            
        
def opcije(email,lozinka):
    with open("./data/korisnici.csv", "r", encoding="utf-8") as fp:
        citac = csv.DictReader(fp)
        podaci = list(citac)

        for podatak in podaci:
            if podatak["email"] == email and podatak["lozinka"] == lozinka and podatak["zanimanje"] == "administrator":  #proverava da li je prijavljeni korisnik
                print("*****Meni*****")                                                                                  #administrator ili kuvar i u zavisnosti od toga
                print("1.Registracija kuvara")                                                                           #nudi mu odgovarajuci meni
                print("2.Pretraga recepta")
                print("3.Prikaz recepta")
                print("4.Stampanje recepta")
                print("5.Odjavi se")
                opcija = input("Izaberite zeljenu opciju:")                                                         

                while opcija!="1" and opcija!="2" and opcija!="3" and opcija!="4" and opcija !="5":
                    print("Greska, molimo Vas unesite broj u opsegu(1-4).")
                    opcija = input("Izaberite zeljenu opciju:")
                
                if opcija == "1":                                                    
                    registracija_kuvara()                                             #na osnovu korisnikovog izbora poziva se odgovarajuca funkcija
                    opcije(email,lozinka)                                             #nakon zavrsetka funkcije vraca se na meni 
                elif opcija == "2":
                    pretraga_recepta()
                    opcije(email,lozinka)
                elif opcija == "3":
                    prikaz_recepta()
                    opcije(email,lozinka)
                elif opcija == "4":
                    stampanje_recepta()
                    opcije(email,lozinka)
                elif opcija == "5":
                    print("Odjavljeni ste.\n")
                    return
        
        for podatak in podaci:
            if podatak["email"] == email and podatak["lozinka"] == lozinka and podatak["zanimanje"] == "kuvar":
                print("\n*****Meni*****")
                print("1.Dodavanje recepta")
                print("2.Pretraga recepta")
                print("3.Ocenjivanje recepta")
                print("4.Brisanje recepta")
                print("5.Prikaz recepta")
                print("6.Stampanje recepta")
                print("7.Odjavi se")
                opcija = input("Izaberite zeljenu opciju:")

                while opcija!="1" and opcija!="2" and opcija!="3" and opcija!="4" and opcija!="5" and opcija!="6" and opcija!="7":
                    print("Greska, molimo Vas unesite broj u opsegu(1-7).")
                    opcija = int(input("Izaberite zeljenu opciju:"))
                
                if opcija == "1":   
                    dodavanje_recepta(email)                                    #u nekim funkcijama prosledjujem email prijavljenog korisnika
                    opcije(email,lozinka)                                       #ukoliko mi treba neki podatak npr. ko je dodao recept
                elif opcija == "2":
                    pretraga_recepta()
                    opcije(email,lozinka)
                elif opcija == "3":
                    ocenjivanje_recepta(email)
                    opcije(email,lozinka)
                elif opcija == "4":
                    brisanje_recepata(email)
                    opcije(email,lozinka)
                elif opcija == "5":
                    prikaz_recepta()
                    opcije(email,lozinka)
                elif opcija == "6":
                    stampanje_recepta()
                    opcije(email,lozinka)
                elif opcija == "7":
                    print("Odjavljeni ste.\n")
                    return
            
