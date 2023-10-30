#CREACIÓN DE VARIABLES
entero = 25
flotante = 10.25
cadena = "Buenas Tardes"
booleano = True

#CONCATENAR
concatenacion = cadena + str(entero) + str(flotante) + str(booleano)

#LÍMITE DE LOS NÚMEROS EN PYTHON
#Los números enteros en python no tienen límite, es decir, no hay restricción en la cantidad de dígitos que puede tener un número entero.
#Los números flotantes en python si tiene límite en la cantidad de dígitos que puede almacenar despues de la coma ",".
#El número flotante máximo que python puede convertir a entero es "1.8*10**307" o "1.77777777777*10**308"

#SUMA DE N NÚMEROS PARES
#suma = 2+4+6+...+2n
n = entero
suma = 0
contador = 2

while(suma <= 2*n):
    suma = suma + contador
    contador = contador + 2

#IMPRIMIR
print(entero)
print(flotante)
print(cadena)
print(booleano)
print(concatenacion)
print(f"la suma de los {entero} primeros números pares es: {suma}")