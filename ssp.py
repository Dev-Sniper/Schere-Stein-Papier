import random
stats = input("Sollen die Statistiken dieses Spiels in die All-time Statistik einfließen oder nicht (J/N)?")
if stats.lower() == "j":
    f = open("ssp.txt", "a")
    f.close()
    f = open("ssp.txt", "r")
    if f.readline() == "":
        f.close()
        f = open("ssp.txt", "a")
        f.write("0")
        f.write("\n")
        f.write("0")
    f.close()
    f = open("ssp.txt", "r")
    counter_player = int(f.readline())
    counter_pc = int(f.readline())
    f.close()
else:
    counter_player = 0
    counter_pc = 0

def GameLoop(counter_pc, counter_player):
    while True:
        user = input("Stein (R), Papier(P) oder Schere (S)?\n")
        if user.lower() == "r":
            user = "Stein"
        elif user.lower() == "p":
            user = "Papier"
        elif user.lower() == "s":
            user = "Schere"
        else:
            print("Ungültige Eingabe")
            GameLoop(counter_pc, counter_player)
        actions = ["Stein", "Papier", "Schere"]
        pc = random.choice(actions)
        print(f"""\nDeine Wahl = {user}, Wahl des Computers: {pc}""")

        if user == pc:
            print("Unentschieden!")

        elif user == "Stein":
            if pc == "Papier":
                print("Der Computer gewinnt!")
                counter_pc += 1
            else:
                print("Du gewinnst!")
                counter_player += 1

        elif user == "Papier":
            if pc == "Schere":
                print("Der Computer gewinnt!")
                counter_pc += 1
            else:
                print("Du gewinnst!")
                counter_player += 1

        elif user == "Schere":
            if pc == "Stein":
                print("Der Computer gewinnt!")
                counter_pc += 1
            else:
                print("Du gewinnst.")
                counter_player += 1

        print(f"""Spielstand\nSpieler: {counter_player}\nComputer: {counter_pc}\n""")
        continueGame = input("Erneut spielen (J/N):\n")

        if continueGame.lower() != "j" or continueGame.lower() == "n":
            if stats.lower() == "j":
                f = open("ssp.txt", "w")
                f.write(str(counter_player))
                f.write("\n")
                f.write(str(counter_pc))
                f.close()
            break

GameLoop(counter_pc, counter_player)