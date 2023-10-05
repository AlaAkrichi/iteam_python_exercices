counter = 1
max= 0 
while True :
    print("saisier une nomber")
    number = int(input(">"))
    if(number > max ):
        max = number
    counter+=1
    if(counter>3):
        break
print(f"le nomber maximal {max}")