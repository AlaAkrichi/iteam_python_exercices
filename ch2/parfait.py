print("saisir un nomber ")
nomber = int(input(">"))
somme = 0
print(f"en calcule la somme de {nomber} : ")
for i in range(nomber+1):
    somme=somme+i
    print(f"{somme}+",end="")
print(f"={somme}")
if(somme == nomber):
    print(f"le nomber {nomber} est parfait")
else:
    print(f"le nomber {nomber} n'est pas parfait ")
