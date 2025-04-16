import sqlite3
import datetime
def main():
    print("Programma ļauj apskatīt savus stundu kavējumus un rezultātus redzēt procentuāli.")
        #izveido savienojumu ar db un kursoru kas izpildīs vaicājumus
    izvele()
def savienojums():
    with sqlite3.connect("Kristine-Agneta_Projekts.db") as conn:
        c = conn.cursor()
        return c

def izvele ():
    iz = int(input("Izvēlaties darbību : ieiet profilā - 1, izveidot profilu - 2: "))
    if iz == 1 :
        ieiet()
    elif iz == 2 :
        izveidot()
    
def ieiet():
    c = savienojums()
    liet = input("ievadiet savu lietotājvārdu")
    c.execute(f"SELECT * from LIETOTAJS WHERE lietotajv = \"{liet} \"")
    iespejas()
def izveidot():
    c = savienojums()
    vards = input("ievadiet savu vārdu:")
    uzvards = input ("ievadiet savu uzvārdu: ")
    lietotajv = input("ievadiet savu lietotājvārdu: ")
    kl = input("ievadiet savu klasi: ")
    stundas = input("ievadi stundu skaitu nedēļā: ")
    c.execute(f"insert into LIETOTAJS (vards, Uzvards, Klase, Lietotajv ) values(\"{vards}\", \"{uzvards}\", {kl}, \"{lietotajv}\"  )")
    c.execute(f"insert into STUNDAS (ned_st) values({stundas} WHERE LIETOTAJS.Liet_ID = STUNDAS.liet_ID )")
    iespejas() 
    c.connection.commit()
def iespejas():
    c = savienojums()
    print("Izvēlies darbību:")
    while True:
        print("1.Pievienot nedēļas apmeklējumu\n2. Aprēķināt apmeklējumu procentu\n3. Aprēķināt aptuveno gada apmeklējumu\n4. Skatīt iepriekšējos datus\n5. Beigt darbu")
        izvele = input("Tava izvēle: ")
        if izvele not in ["1", "2","3","4","5"]:
            print("Nederīga ievade")
            continue
        if izvele == "1":
            pievienot(c)
        elif izvele == "2":
            procenti(c)
        elif izvele == "3":
            gads(c)
        elif izvele == "4":
            ieprieksejie(c)
        elif izvele == "5":
            break
def pievienot(c):
    c = savienojums()
    stundas_kopa = int(input("Ievadi kopējo stundu skaitu nedēļā: "))
    c.execute(f"")
    kavetas_stundas = int(input("Ievadi kavēto stundu skaitu nedēļā: "))
    apmeklets = stundas_kopa - kavetas_stundas
    kavejums = apmeklets / stundas_kopa * 100
    c.execute(f"")
    print(f"Tavs apmeklējums šajā nedēļā ir {kavejums:.2f}%.")




if __name__ == "__main__":
    main()