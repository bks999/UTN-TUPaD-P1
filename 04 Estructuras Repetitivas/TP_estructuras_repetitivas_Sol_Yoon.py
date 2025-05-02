# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

for num in range(0,101):
    print(num)

# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de dígitos que contiene.

num1 = input("Ingrese un numero: ")
digitos=len(num1)
print(f"El numero ingresado tiene {digitos} digitos")

# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
# dados por el usuario, excluyendo esos dos valores.

print("Ingrese dos numeros")
a = int(input("Numero a: "))
b = int(input("Numero b: "))
suma=0
for i in range(a,b):
    suma+=i
print(f"La suma de los numeros comprendidos entre a y b son: {suma}")

# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0.

print("Ingrese numeros enteros para sumar en secuencia. Ingrese 0 para terminar")
num_entero=int(input())
suma_enteros=0
while num_entero!=0:
    suma_enteros+=num_entero
    num_entero=int(input())
print(f"La suma de los numeros ingresados es: {suma_enteros}")

# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

import random
num_aleatorio=random.randint(0,9)
contador=1
numero_adivinado=int(input("Adivina el numero: "))
while numero_adivinado!=num_aleatorio:
    contador+=1
    numero_adivinado=int(input())
print(f"Adivinaste en {contador} intentos!")

# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos entre 0 y 100, en orden decreciente.

for i in range(100,-1,-1):
    if i % 2 == 0:
        print(i)

# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un número entero positivo indicado por el usuario.

print("Ingrese dos numeros positivos")
num_x=int(input("Primer numero: "))
num_y=int(input("Segundo numero: "))
sumatoria=0
if num_x > 0 < num_y:
    for z in range(num_x,num_y+1):
        sumatoria+=z
    print(f"La suma de los numeros comprendidos entre los numeros ingresados es: {sumatoria}")
else:
    print("No se ha ingresado valores positivos")

# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
# menor, pero debe estar preparado para procesar 100 números con un solo cambio).

print("Ingrese 100 numeros enteros")
positivos=0
negativos=0
pares=0
impares=0
for i in range(0,100):
    num=int(input(f"{i+1}. "))
    if num%2==0:
        pares+=1
    else:
        impares+=1
    if num>=0:
        positivos+=1
    else:
        negativos+=1
print(f"""Conteo:
      Pares: {pares}
      Impares: {impares}
      Positivos: {positivos}
      Negativos: {negativos}""")

# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
# poder procesar 100 números cambiando solo un valor).

suma=0
num_final=100
print("Ingrese 100 numeros enteros")
for i in range(0,num_final):
    num=int(input(f"{i+1}. "))
    suma+=num
media=suma/num_final
print(f"La media de los valores ingresados es: {media}")

# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

num=input("Ingrese un numero: ")
invertido=""
for digito in num:
    invertido = digito + invertido
print(f"{num} invertido es: {invertido}")