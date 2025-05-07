import sqlite3
import os
import unittest

# Pārbaudes DB nosaukums (testa vidē)
TEST_DB = "test_Kristine_Agneta_Projekts.db"

# Palīgfunkcija, lai izveidotu testējamu datubāzi
def setup_test_db():
    if os.path.exists(TEST_DB):
        os.remove(TEST_DB)
    conn = sqlite3.connect(TEST_DB)
    c = conn.cursor()
    c.execute('''CREATE TABLE LIETOTAJS (
        Liet_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Vards TEXT,
        Uzvards TEXT,
        Klase TEXT,
        Lietotajv TEXT UNIQUE
    )''')
    c.execute('''CREATE TABLE STUNDAS (
        Stundas_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Ned_st INTEGER,
        Neapm INTEGER,
        Liet_ID INTEGER,
        FOREIGN KEY(Liet_ID) REFERENCES LIETOTAJS(Liet_ID)
    )''')
    conn.commit()
    return conn

class TestKavejumiProgram(unittest.TestCase):

    def setUp(self):
        self.conn = setup_test_db()
        self.cursor = self.conn.cursor()

    def tearDown(self):
        self.conn.close()
        if os.path.exists(TEST_DB):
            os.remove(TEST_DB)

    def test_insert_user_and_attendance(self):
        # Ievieto lietotāju
        self.cursor.execute("INSERT INTO LIETOTAJS (Vards, Uzvards, Klase, Lietotajv) VALUES (?, ?, ?, ?)",
                            ("Anna", "Ozola", "12A", "annaozola"))
        liet_id = self.cursor.lastrowid
        self.conn.commit()

        # Ievieto stundu info
        self.cursor.execute("INSERT INTO STUNDAS (Ned_st, Neapm, Liet_ID) VALUES (?, ?, ?)",
                            (35, 5, liet_id))
        self.conn.commit()

        # Pārbauda datus
        self.cursor.execute("SELECT * FROM STUNDAS WHERE Liet_ID = ?", (liet_id,))
        dati = self.cursor.fetchone()
        self.assertIsNotNone(dati)
        self.assertEqual(dati[1], 35)  # Ned_st
        self.assertEqual(dati[2], 5)   # Neapm

    def test_update_attendance(self):
        # Ievieto lietotāju un sākotnējos datus
        self.cursor.execute("INSERT INTO LIETOTAJS (Vards, Uzvards, Klase, Lietotajv) VALUES (?, ?, ?, ?)",
                            ("Jānis", "Kalniņš", "11B", "janisk"))
        liet_id = self.cursor.lastrowid
        self.cursor.execute("INSERT INTO STUNDAS (Ned_st, Neapm, Liet_ID) VALUES (?, ?, ?)",
                            (30, 10, liet_id))
        self.conn.commit()

        # Atjaunina datus
        self.cursor.execute("UPDATE STUNDAS SET Ned_st = ?, Neapm = ? WHERE Liet_ID = ?",
                            (40, 4, liet_id))
        self.conn.commit()

        # Pārbauda atjauninājumu
        self.cursor.execute("SELECT Ned_st, Neapm FROM STUNDAS WHERE Liet_ID = ?", (liet_id,))
        ned_st, neapm = self.cursor.fetchone()
        self.assertEqual(ned_st, 40)
        self.assertEqual(neapm, 4)

if __name__ == '__main__':
    unittest.main()