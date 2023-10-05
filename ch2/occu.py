print("saisire une chaine de caractere")
ch = input("> ")
print("saisire un caractere a chercher")
c = input("> ")
nb_occ = 0
for i in ch:
    if(i==c):
        nb_occ=nb_occ+1
print(f"le caractere {c} occure {nb_occ} dans la chaine \n '++{ch}++' ")