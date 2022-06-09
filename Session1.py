# Gruppe 3 DK 1
# 4. semester

# Imports
import time # Et module som importere tid.
from random import *


def Session():  # En funktion bliver defineret.
    import Connect_server as connection  # Database forbindelsen bliver importeret.

    # En variabel bliver defineret til at være
    session_start = time.strftime("%H:%M:%S")

    thisConn = connection.connect()  # En variabel bliver defineret til at være databaseforbindelsen
    # Denne kommando producere en markør som kan eksekvere en forspørgsel på MySQL serveren.
    # "cur" bliver sat til at være en markør på "connection" som er forbindelsen til serveren.
    cur = thisConn.cursor()

    Kunde_id = input("Hvad er dit kunde_id?")  # Et input fra brugeren.

    Sql = "SELECT * FROM Delivery3.Kundedata WHERE Kunde_id = %s;"

    print("Måling startet ", session_start)
    input("Tryk enter for at stoppe sessionen:")

    Tidstoppet = time.strftime("%H:%M:%S")
    print("Session stoppet", Tidstoppet)

    def get_sec(time_str):
        """Get Seconds from time."""
        h, m, s = time_str.split(':')
        return int(h) * 3600 + int(m) * 60 + int(s)

    start = get_sec(session_start)
    end = get_sec(Tidstoppet)

    ForbrugtTid_sec = end - start

    sql = "INSERT INTO Delivery3.Måling(Kunde_id, Tidstartet, Tidstoppet, ForbrugtTid_sec) values(%s, %s, %s, %s);"
    val = (Kunde_id, session_start, Tidstoppet, ForbrugtTid_sec)

    cur.execute(sql, val)

    #########################
    # Random tal
    Data1 = randint(1, 100)
    Data2 = randint(1, 100)
    Data3 = randint(1, 100)
    Data4 = randint(1, 100)
    Data5 = randint(1, 100)
    Data6 = randint(1, 100)
    Data7 = randint(1, 100)
    Data8 = randint(1, 100)
    Data9 = randint(1, 100)
    Data10 = randint(1, 100)

    sqldata = "INSERT INTO Delivery3.Måling_data(Kunde_id, Data1, Data2, Data3, Data4, Data5, Data6, Data7, Data8, Data9, Data10) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
    valdata = (Kunde_id, Data1, Data2, Data3, Data4, Data5, Data6, Data7, Data8, Data9, Data10)

    cur.execute(sqldata, valdata)

    # Denne kommando får eksekveringen til at træde i kraft på MySQL serveren.
    thisConn.commit()

    # Denne kommando lukker for forbindelsen.
    thisConn.close()