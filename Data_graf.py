
import matplotlib.pyplot as plt
import Connect_server as connection # Database forbindelsen bliver importeret.
def graf():
    thisConn = connection.connect()  # En variabel bliver defineret til at være databaseforbindelsen
    # Denne kommando producere en markør som kan eksekvere en forspørgsel på MySQL serveren.
    # "cur" bliver sat til at være en markør på "connection" som er forbindelsen til serveren.
    cur = thisConn.cursor()

    Kunde_id = input("Hvad er dit Kunde_id?")
    sql = (
        "SELECT Data1, Data2, Data3, Data4, Data5, Data6, Data7, Data8, Data9, Data10 FROM Delivery3.Måling_data WHERE Kunde_id = %s;")
    cur.execute(sql, (Kunde_id,))
    result = cur.fetchall

    Kunde_id = []
    Data = []

    for i in cur:
        Data.append(i)
        Kunde_id.append(i)

    # Visulizing Data using Matplotlib
    plt.scatter([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], Data)
    plt.ylabel("Måling data")
    plt.xlabel("Målingstal")
    plt.title("Flot graf")
    plt.show()
