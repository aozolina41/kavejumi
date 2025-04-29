import sqlite3

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
        liet = ieiet()
        iespejas(liet)
    elif iz == 2 :
        izveidot()
    
def ieiet():
    c = savienojums()
    liet = input("ievadiet savu lietotājvārdu: ")
    #c.execute(f"SELECT * from LIETOTAJS WHERE Lietotajv = \"{liet} \"")
    c.execute(f"SELECT Liet_ID from LIETOTAJS WHERE Lietotajv = \"{liet}\"")
    d = c.fetchall()[0][0]
    print(d)
    return d
def izveidot():
    c = savienojums()
    vards = input("ievadiet savu vārdu:")
    uzvards = input ("ievadiet savu uzvārdu: ")
    lietotajv = input("ievadiet savu lietotājvārdu:  ")
    kl = input("ievadiet savu klasi: ")
    stundas = input("ievadi stundu skaitu nedēļā: ")
    if c.fetchone():
        print("Šāds lietotājvārds jau eksistē. Lūdzu, izvēlieties citu.")
        izveidot()
    c.execute(f"insert into LIETOTAJS (vards, Uzvards, Klase, Lietotajv ) values(\"{vards}\", \"{uzvards}\", {kl}, \"{lietotajv}\"  )")
    c.connection.commit()
    liet_ID = c.lastrowid
    c.execute(f"INSERT INTO STUNDAS (ned_st, liet_ID) VALUES ({stundas}, {liet_ID})")
    c.connection.commit()
    iespejas(liet_ID) 
def iespejas(liet):
    c = savienojums()
    print("Izvēlies darbību:")
    while True:
        print("1.Pievienot nedēļas apmeklējumu\n2. Aprēķināt apmeklējumu procentu\n3. Aprēķināt aptuveno gada apmeklējumu\n4. apskatīt profilu\n5. Beigt darbu")
        izvele = input("Tava izvēle: ")
        if izvele not in ["1", "2","3","4","5"]:
            print("Nederīga ievade")
            continue
        if izvele == "1":
            pievienot(c)
        elif izvele == "2":
            procenti()
        elif izvele == "3":
            gads()
        elif izvele == "4":
            apskatit(liet)
        elif izvele == "5":
            break
def pievienot(liet):
    c = savienojums()
    stundas_kopa = int(input("Ievadi kopējo stundu skaitu nedēļā: "))

    kavetas_stundas = int(input("Ievadi kavēto stundu skaitu nedēļā: "))

    apmeklets = stundas_kopa - kavetas_stundas
    kavejums = apmeklets / stundas_kopa * 100
    c.execute("UPDATE STUNDAS SET ned_st = ?, neapm = ? WHERE liet_ID = {}")
    print(f"Tavs apmeklējums šajā nedēļā ir {kavejums:.2f}%.")
    c.connection.commit()
#def procenti():
def apskatit(liet):
    c = savienojums()
    
    c.execute(f"SELECT * FROM LIETOTAJS WHERE Liet_ID= {liet}")
    dati = c.fetchone()
    print(dati)



if __name__ == "__main__":
    main()