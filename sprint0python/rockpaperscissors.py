from random import randint
scorem=0
scorep=0
i=0
while i < 5:
    player =int(input("1-tijeras\n2-papel\n3-piedra\n"))
    maquina = randint(1,3)
    if maquina==1:
        print("tijeras")
    elif maquina==2:
        print("papel")
    elif maquina==3:
        print("piedra")
    if player==1 and maquina==3:
        print("tu pierdes")
        scorem=scorem+1
    elif player==3 and maquina==1:
        scorep=scorep+1
        print("tu ganas")
    elif player==maquina:
        print("empate")
    elif player<maquina:
        scorep=scorep+1
        print("tu ganas")
    else :
        scorem=scorem+1
        print("tu pierdes")
    i=i+1
print("score player= "+str(scorep) +" score computer= "+str(scorem))
    