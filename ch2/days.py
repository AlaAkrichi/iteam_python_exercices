print("saisir un numero de jour ")
numJour = int(input("> "))
match numJour:
    case 1:
        print("lundi")
    case 2:
        print("mardi")
    case 3:
        print("mercredi")
    case 4:
        print("jeudi")
    case 5:
        print("vendredi")
    case 6:
        print("samedi")
    case 7:
        print("dimanche")
    case _:
        print("invalide")
    