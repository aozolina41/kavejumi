import sqlite3
import datetime
def main():
    print("Programma ļauj apskatīt savus stundu kavējumus un rezultātus redzēt procentuāli.")
    #izveido savienojumu ar db un kursoru kas izpildīs vaicājumus
    with _sqlite3.connect("Kristine-Agneta_Projekts.db") as conn:
        c = conn.cursor()
        izvele(c)
def izvele(c):
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
    try:
        stundas_kopa = int(input("Ievadi kopējo stundu skaitu nedēļā: "))
        kavetas_stundas = int(input("Ievadi kavēto stundu skaitu nedēļā: "))
        kavejums = aprekini(stundas_kopa, kavetas_stundas)
        if lietotajs not in data:
            data[lietotajs] = []
        data[lietotajs].append(kavejums)
        save_data(lietotajs, data)
        print(f"Tavs apmeklējums šajā nedēļā ir {kavejums:.2f}%.")
    except ValueError:
        print("Nederīga ievade")