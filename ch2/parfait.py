print("saisir un nomber ")
nomber = int(input("> "))
somme = 0
for i in range(1,nomber//2+1):
    if(nomber%i==0):
        somme = somme +i
if(somme == nomber):
    print(f"le nomber {nomber} est parfait")
else:
    print(f"le nomber {nomber} n'est pas parfait ")
