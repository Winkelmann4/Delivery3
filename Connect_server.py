# 2 semester exam
# Created Juni 2021 by DK1Gruppe3

import mysql.connector # Importere et module som gør det muligt at oprette forbindelse til en MySQL server.

def connect(): # En funktion bliver oprettet.
    # Nedenfor er connection princippet forklaret. Disse oplysninger kan findes i MySQL Workbench.
    # host= hostnavn på den serveren du skal connecte til.
    # database= navnet på databasen du skal oprette forbindelse til.
    # user= er brugernavnet til databasen.
    # password= skal kun udfyldes hvis der skal bruges en adgangskode til at oprette forbindelse til databasen.
    # Denne kommando danner en connection til SQL serveren.
    connection = mysql.connector.connect(host='localhost', # Her skrives hostnavnet, typisk "localhost"
                                         database='Delivery3', # Hvilken database som der arbejdes i, skal ikke ændres
                                         user='root', # Her skrives usernavnet, typisk "root"
                                         password='pass') # Her skrives passwordet til MySQL serveren, hvis der er oprettet et.
    return connection
