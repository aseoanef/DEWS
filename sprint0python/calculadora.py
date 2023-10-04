from operaciones import suma,resta,multiplicacion,division
repeat="s"
while repeat=="s":
    select = input("1-suma\n2-resta\n3-multiplicacion\n4-division\n")
    operator1 = input("operator 1: ")
    operator2 = input("operator 2: ")
    if select=="1":
        print(suma(operator1=operator1,operator2=operator2))
    elif select=="2":
        print(resta(operator1=operator1,operator2=operator2))
    elif select=="3":
        print(multiplicacion(operator1=operator1,operator2=operator2))
    elif select=="4":
        print(division(operator1=operator1,operator2=operator2))
    repeat=input("repetir? s/n  ")

    