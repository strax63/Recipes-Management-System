from Meni_opcije.prijava_korisnika import prijava_korisnika

def glavni_meni():

    print("*****GLAVNI MENI*****")
    print("1. Prijava korisnika")
    print("2. Izlaz iz aplikacije")
    #opcija = input("Izaberite zeljenu opciju:")

    #while opcija!="1" and opcija!="2":                  #ako ne unese 1 ili 2 a unese bilo sta drugo ponavlja unos
        #print("Greska, molimo Vas unesite broj u opsegu(1-2).")
        #opcija = input("Izaberite zeljenu opciju:")
    while True:
        try:
            opcija = int(input("Izaberite zeljenu opciju (1-2): "))
            if opcija < 0 or opcija > 3 :
                print("Greska,broj mora biti iz opsega (1-3).")
            else:
                break
        except ValueError:
            print("Greska, morate uneti broj!")
    if opcija == 1:
        prijava_korisnika()                             #ukoliko korisnik izabere opciju 1 poziva se funkcija prijava
        glavni_meni()                                   #kad korisnik izabere izlaz u funkciji prijava ponovo mu se pojavljuje glavni meni
    elif opcija == 2:
        print("Izasli ste iz aplikacije!")
        return

    
    