# 2 semester exam
# Created Juni 2021 by DK1Gruppe3

# Funktioner bliver importet fra andre Python filer.
from Session1 import Session
from Data_graf import graf


# En funktion bliver oprettet.
def menu():
    # I denne liste ses alle mulighederne som der er i menuen.
    options = ["Start måling", "Se data/graf", "Q for quit"]
    for i, option in enumerate(options): # i dette loop kører den hvert objekt i listen.
        # Enumerate tager listen og returnere listen som et optælingsobjekt.
        print("[" + str(i + 1) + "] " + option)

def main():
    loop = True
    while loop:
        menu()
        try:
            choice = int(input(""))
            if choice in range(1, 3):
                if choice == 1:
                    Session()
                if choice == 2:
                    graf()
                if choice == "Q" or "q":
                    break
            else:
                quit()

        except ValueError:
            print("Forbindelsen er afbrudt, programmet lukkes ned.")
            quit()

main()