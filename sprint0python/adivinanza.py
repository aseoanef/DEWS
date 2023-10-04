from random import randint  
score = 0
def pregunta1(score):
    respuesta = input("tengo agujas y no se coser,tengo numeros y no se leer\n a.reloj \n b.escorpion \n c.calculadora \n")
    if respuesta == "a":
        print("Congrats")
        score=  score +10
        return score
    else:
        print("Dumbass")
        score =  score - 5
        return score
    
def pregunta2(score):
    respuesta = input("si tu me quieres comer me veras marron y peludo no me podras romper porque por fuera soy duro\n a.chocolate \n b.coco \n c.armadillo \n")
    if respuesta == "b":
        print("Congrats")
        score=   score + 10
        return score
    else:
        print("Dumbass") 
        score =  score - 5
        return score
    
def pregunta3(score):
    respuesta = input("pequeña como un raton cuida la casa como un leon \n a.gato \n b.pistola \n c.llave \n")
    if respuesta == "c":
        print("Congrats")
        score= score+10
        return score
    else:
        print("Dumbass")
        score = score - 5
        return score
    
preguntaA=randint(1,3)
if preguntaA==1:
    score=pregunta1(score)
elif preguntaA==2:
    score=pregunta2(score)
elif preguntaA==3:
    score=pregunta3(score)
preguntaB=preguntaA
while preguntaB==preguntaA:
    preguntaB=randint(1,3)
    if preguntaB==1 and preguntaA!=preguntaB:
        score=pregunta1(score)
        
    elif preguntaB==2 and preguntaB!=preguntaA:
        score=pregunta2(score)
        
    elif preguntaB==3 and preguntaB!=preguntaA:
        score=pregunta3(score)
        

print("your score is :"  +str(score))       
