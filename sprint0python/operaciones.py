result = 0
def suma(operator1,operator2):
    result=int(operator1) +int(operator2)
    return result
def resta(operator1,operator2):
    result=int(operator1)-int(operator2)
    return result
def multiplicacion(operator1,operator2):
    result=int(operator1)*int(operator2)
    return result
def division(operator1,operator2):
    if operator2=="0":
        print("operator 2 cant be 0")
    else:
        result =int(operator1)/int(operator2)
        return result
#convertirlo en funciones ,crear calculadora py,crear piedra papel tijera, modificar adivinanza     

