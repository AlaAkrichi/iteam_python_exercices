print("saisire une chaine de carater")
ch = input("> ")
noSpace =""
for c in ch:
    if(c !=" "):
        noSpace=noSpace+""+c
print(f"l'ancien chainde {ch}")
print(f"la nouvelle chaine {noSpace}")