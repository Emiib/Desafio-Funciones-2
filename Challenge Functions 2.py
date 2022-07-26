#1)
# Realiza una función llamada area_rectangulo() 
# que devuelva el área del rectángulo a partir de una base y una altura. 
# Calcula el área de un rectángulo de 15 de base y 10 de altura

def area_rectangulo(base, height):
    area =(base * height)
    return f"The area of the rectangle is {area}"
print(area_rectangulo(15,10))

#2)
# Realiza una función llamada area_circulo() 
# que devuelva el área de un círculo a partir de un radio. 
# Calcula el área de un círculo de 5 de radio

import math
from re import X
def area_circulo(radio):
    area_cir = (math.pi * (radio**2))
    return f"The area of the circle is {area_cir}"

print(area_circulo(5))


#3)
# Realiza una función llamada relacion()
# que a partir de dos números cumpla lo siguiente: 
# 1----- Si el primer número es mayor que el segundo, debe devolver 1.
# 2----- Si el primer número es menor que el segundo, debe devolver -1.
# 3----- Si ambos números son iguales, debe devolver un 0.
# Comprueba la relación entre los números: '5 y 10', '10 y 5' y '5 y 5'

def relacion(num_1, num_2):
    if num_1 == num_2:
        return "0 --> because they are equals"
    elif num_1 < num_2:
        return f"-1, since {num_1} is less than {num_2}"
    elif num_1 > num_2:
        return f"1, since {num_1} is bigger than {num_2}"

print(relacion(5,10))

#4)
# Realiza una función llamada intermedio()
# que a partir de dos números, devuelva su punto intermedio:
# Comprueba el punto intermedio entre -12 y 24

def intermedio(a, b):
    inter = ((a + b)/2)
    return f"The middle number is {inter}"
print(intermedio(-12, 24))

#5)
# Realizá una función llamada recortar() que reciba tres parámetros.
# El primero es el número a recortar, 
# el segundo es el límite inferior y 
# el tercero el límite superior. 
# La función tendrá que cumplir lo siguiente:
# Devolver el límite inferior si el número es menor que éste
# Devolver el límite superior si el número es mayor que éste.
# Devolver el número sin cambios si no se supera ningún límite.
# Comprueba el resultado de recortar 15 entre los límites 0 y 10

def recortar(num, num_inf, num_sup):
    if num < num_inf:
        return f"The input number is lower than {num_inf}"
    elif num > num_sup:
        return f"The input number is higher than {num_sup}"
    elif num > num_inf and num < num_sup:
        return f"The input number is between {num_inf} and {num_sup}"
print(recortar(15,0,10))


#6) Realiza una función separar()
# que tome una lista de números enteros y devuelva dos listas ordenadas.
# La primera con los números pares, y la segunda con los números impares:

lista = [6,5,2,1,7]
def separar(lista):
    lista = sorted(lista)
    pares = []
    impares = []
    for n in lista:
        if n%2 == 0:
            pares.append(n)
        else:
            impares.append(n)
    return pares, impares
pares, impares = separar(lista)
print(pares)
print(impares)
