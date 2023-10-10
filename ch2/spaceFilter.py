print("saisire une chaine de carater")
ch = input("> ")
print(f"l'ancien chainde {ch}")
i=0
while(i<len(ch)):
    if(ch[i] == " "):
        ch = ch[:i]+ch[i+1:]
    i+=1
print(f"la nouvelle chaine {ch}")
