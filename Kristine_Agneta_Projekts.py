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
    try:
        if iz == 1 :
            liet = ieiet()
            iespejas(liet)
        elif iz == 2 :
            izveidot()
        else:
            print("nederīga ievade!! ")
    except ValueError:
        print("Lūdzu ievadi tikai skaitli!")
    
def ieiet():
    c = savienojums()
    liet = input("ievadiet savu lietotājvārdu: ")
    try:
        #c.execute(f"SELECT * from LIETOTAJS WHERE Lietotajv = \"{liet} \"")
        c.execute(f"SELECT Liet_ID from LIETOTAJS WHERE Lietotajv = \"{liet}\"")
        d = c.fetchall()[0][0]
    except:
        print(f"Kļūda pieslēdzoties(lietotājs neeksistē)")
        return None
    return d
def izveidot():
    c = savienojums()
    vards = input("ievadiet savu vārdu:")
    uzvards = input ("ievadiet savu uzvārdu: ")
    lietotajv = input("ievadiet savu lietotājvārdu:  ")
    kl = input("ievadiet savu klasi: ")
    stundas = input("ievadi stundu skaitu nedēļā: ")
    try:
        if c.fetchone():
            print("Šāds lietotājvārds jau eksistē. Lūdzu, izvēlieties citu.")
            izveidot()
        c.execute(f"insert into LIETOTAJS (vards, Uzvards, Klase, Lietotajv ) values(\"{vards}\", \"{uzvards}\", {kl}, \"{lietotajv}\"  )")
        c.connection.commit()
        liet_ID = c.lastrowid
        c.execute(f"INSERT INTO STUNDAS (ned_st, liet_ID) VALUES ({stundas}, {liet_ID})")
        c.connection.commit()
        iespejas(liet_ID) 
    except ValueError:
        print("Stundu skaitam jābūt skaitlim!")
        izveidot()
    except :
        print(f"Kļūda izveidojot profilu")
def iespejas(liet):
    c = savienojums()
    print("Izvēlies darbību:")
    try:
        while True:
            print("1.Pievienot nedēļas apmeklējumu\n2. apskatīt profilu\n3. Beigt darbu")
            izvele = input("Tava izvēle: ")
            if izvele not in ["1", "2","3","4","5"]:
                print("Nederīga ievade")
                continue
            if izvele == "1":
                pievienot(liet)
            elif izvele == "2":
                apskatit(liet)
            elif izvele == "3":
                break
    except Exception as e:
        print(f"Kļūda darbībā: {e}")
def pievienot(liet):
    try:
        c = savienojums()
        stundas_kopa = int(input("Ievadi kopējo stundu skaitu nedēļā: "))
        kavetas_stundas = int(input("Ievadi kavēto stundu skaitu nedēļā: "))
        apmeklets = stundas_kopa - kavetas_stundas
        kavejums = apmeklets / stundas_kopa * 100
        q = f"UPDATE STUNDAS SET Ned_st = {stundas_kopa}, Neapm = {kavetas_stundas} WHERE liet_ID = {liet}"
        c.execute(q)
        print(f"Tavs apmeklējums šajā nedēļā ir {kavejums:.2f}%.")
        c.connection.commit()
    except ValueError:
        print("Lūdzu ievadi skaitļus!")
    except Exception as e:
        print(f"Kļūda atjauninot datus: {e}")
def apskatit(liet):
    try:
        c = savienojums()
        
        c.execute(f"SELECT * FROM LIETOTAJS WHERE Liet_ID= {liet}")
        dati = c.fetchone()
        print(dati)
    except Exception as e:
        print(f"Kļūda skatot profilu: {e}") 



if __name__ == "__main__":
    main()