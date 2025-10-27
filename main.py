'''

variable1 = 10

print(variable1)

nombre = input("Introduce tu nombre: ")
print("Tu nombre es: " + nombre)

print("Vamos a sumar dos números, para ello dime el primer número a sumar")
numero1 = int(input("Introduce tu numero: "))
numero2 = int(input("Introduce tu segundo numero: "))

print("Tu número es: " + str(numero1 + numero2))

'''

x = 1
pregunta1 = ""

def suma(numero1, numero2):
    return numero1 + numero2

def resta(numero1, numero2):
    return numero1 - numero2

def multiplicacion(numero1, numero2):
    return numero1 * numero2

def division(numero1, numero2):
    return numero1 / numero2

while x==1:


    if pregunta1 != "Si":
        numero1 = int(input("Introduce tu numero: "))

    print("Elige una operacion")
    print("Suma = 1, Resta = 2, Multiplicacion = 3, Division = 4")
    operacion = int(input("Introduce tu operacion: "))
    numero2 = int(input("Introduce tu segundo numero: "))

    if operacion == 1:
        resultado = suma(numero1, numero2)
        numero1 = resultado
        print(f'El resultado es: {resultado}')
    elif operacion == 2:
        resultado = resta(numero1, numero2)
        numero1 = resultado
        print(f'El resultado es: {resultado}')
    elif operacion == 3:
        resultado = multiplicacion(numero1, numero2)
        numero1 = resultado
        print(f'El resultado es: {resultado}')
    elif operacion == 4:
        resultado = division(numero1, numero2)
        numero1 = resultado
        print(f'El resultado es: {resultado}')
    else:
        print("Operacion no valida")
        break

    pregunta1 = (input("Quieres usar el resultado obtenido?"))
    if pregunta1 == "Si":
        numero1 = resultado

    respuesta = (input("¿Desea realizar otra operacion?"))

    if respuesta == "Si":
        x=1
    else:
        x=0