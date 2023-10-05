print("saisir un nomber ")
number=int(input(">"))
print(f"le nomber {number} est ",end=" ")
if(number%3 == 0):
    print(f" divisible par 3",end=" ")
if(number%13 ==0 ):
    print(" divisible par 13",end=" ")
if(not(number%3 == 0 and number%13 == 0)):
    print("pas divisble")