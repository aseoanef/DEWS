respuesta = input("adivinanza \n a. \n b. \n c. \n")
score = 0
if respuesta == "a":
    print("Congrats")
    score= score+10
else:
    print("Dumbass")
    score = score - 5
respuesta = input("adivinanza \n a. \n b. \n c. \n")
if respuesta == "b":
    print("Congrats")
    score= score+10
else:
    print("Dumbass") 
    score = score - 5
respuesta = input("adivinanza \n a. \n b. \n c. \n")
if respuesta == "c":
    print("Congrats")
    score= score+10
else:
    print("Dumbass")
    score = score - 5
print("your score is :",score)       
