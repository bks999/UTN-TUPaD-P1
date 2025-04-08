# TRABAJO PRACTICO 3: Estructuras condicionales

# Actividades

# Ejercicio 1: Escribir un programa que solicite la edad del usuario. 
# Si el usuario es mayor de 18 años, deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

edadUsuario = int(input("Ingrese su edad: "))
if edadUsuario > 18:
    print("Es mayor de edad")

# Ejercicio 2: Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
# mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el mensaje “Desaprobado”.

notaUsuario = int(input("Ingrese la nota del usuario: "))
if notaUsuario >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

# Ejercico 3: Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un número par, 
# imprimir por pantalla el mensaje "Ha ingresado un número par"; en caso contrario, imprimir por pantalla "Por favor, ingrese un número par".
# Nota: investigar el uso del operador de módulo (%) en Python para evaluar si un número es par o impar.

num = int(input("Ingrese un numero par: "))
if num % 2 == 0:
    print("Ha ingresado un numero par")
else:
    print("Por favor, ingrese un numero par")

# Ejercicio 4: Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las siguientes categorías pertenece:
#   ● Niño/a: menor de 12 años.
#   ● Adolescente: mayor o igual que 12 años y menor que 18 años.
#   ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
#   ● Adulto/a: mayor o igual que 30 años.

edadUsuario1 = int(input("Ingrese su edad: "))
if edadUsuario1 < 12:
    print("Usted es un/a niño/a")
elif edadUsuario1 >= 12 and edadUsuario1 < 18:
    print("Usted es un/a adolescente")
elif edadUsuario1 >= 18 and edadUsuario1 < 30:
    print("Usted es un/a adulto/a joven")
elif edadUsuario1 >= 30:
    print("Usted es un/a adulto/a")

# Ejercicio 5: Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres (incluyendo 8 y 14).
# Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en pantalla el mensaje "Ha ingresado una contraseña correcta";
# en caso contrario, imprimir por pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres".
# Nota: investigue el uso de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal como una lista o un string

password = input("Ingrese una nueva contraseña (8-14 caracteres): ")
if len(password) >= 8 and len(password) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

# Ejercicio 6: Escribir un programa que tome la lista numeros_aleatorios, calcule su moda, 
# su mediana y su media y las compare para determinar si hay sesgo positivo, negativo o no hay sesgo.
# Imprimir el resultado por pantalla.

from statistics import mode, median, mean
import random
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
print(numeros_aleatorios)

if mean(numeros_aleatorios) > median(numeros_aleatorios) and median(numeros_aleatorios) > mode(numeros_aleatorios):
    print("Hay sesgo positivo")
elif mean(numeros_aleatorios) == median(numeros_aleatorios) == mode(numeros_aleatorios):
    print("No hay sesgo")
else:
    print("Hay sesgo negativo")

# Ejercicio 7: Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado termina con vocal,
# añadir un signo de exclamación al final e imprimir el string resultante por pantalla; en caso contrario, 
# dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla.

stringUsuario = input("Ingrese una frase o palabra: ")
ultima_letra = stringUsuario[len(stringUsuario)-1].lower()

if ultima_letra == "a" or ultima_letra == "e" or ultima_letra == "i" or ultima_letra == "o" or ultima_letra == "u":
    print(stringUsuario + "!")
else:
    print(stringUsuario)

# Ejercicio 8: Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 dependiendo de la opción que desee:
# 1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
# 2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
# 3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
# El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el usuario e imprimir el resultado por pantalla.
# Nota: investigue uso de las funciones upper(), lower() y title() de Python para convertir entre mayúsculas y minúsculas.

nombreUsuario = input("Ingrese su nombre: ")
opcion = int(input("""Elija una opcion:
        1. Nombre en MAYUSCULA
        2. Nombre en MINUSCULA
        3. Nombre con la primera letra en mayuscula
        Opcion: """))
if opcion == 1:
    print(nombreUsuario.upper())
elif opcion == 2:
    print(nombreUsuario.lower())
elif opcion == 3:
    print(nombreUsuario.title())
else:
    print("Opcion invalida")

# Ejercicio 9: Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la magnitud en una de las siguientes 
# categorías según la escala de Richter e imprima el resultado por pantalla:
    # ● Menor que 3: "Muy leve" (imperceptible).
    # ● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
    # ● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero generalmente no causa daños).
    # ● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras débiles).
    # ● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
    # ● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).

magnitud_terremoto = float(input("Ingrese la magnitud del terremoto: "))
print("Segun la escala de Richter se clasifica como: ")
if magnitud_terremoto < 3:
    print("Muy leve (imperceptible)")
elif magnitud_terremoto >= 3 and magnitud_terremoto < 4:
    print("Leve (ligeramente perceptible)")
elif magnitud_terremoto >= 4 and magnitud_terremoto < 4:
    print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif magnitud_terremoto >= 5 and magnitud_terremoto < 6:
    print("Fuerte (puede causar daños en estructuras débiles)")
elif magnitud_terremoto >= 6 and magnitud_terremoto < 7:
    print("Muy Fuerte (puede causar daños significativos)")
elif magnitud_terremoto >= 7:
    print("Extremo (puede causar graves daños a gran escala)")

# Ejercicio 10: Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
# del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
# si el usuario se encuentra en otoño, invierno, primavera o verano.

hemisferio = input("En que hemisferio se encuentra? ").upper()
mes = int(input("Que mes del año es?(1-12) "))
dia = int(input("Que dia es hoy? "))
estacion = ""

if hemisferio == "N":
    if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <=20):
        estacion = "Invierno"
    elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <=20):
        estacion = "Primavera"
    elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <=20):
        estacion = "Verano"
    else:
        estacion = "Otoño"
elif hemisferio == "S":
    if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <=20):
        estacion = "Verano"
    elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <=20):
        estacion = "Otoño"
    elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <=20):
        estacion = "Invierno"
    else:
        estacion = "Primavera"

print(f"Está en la estación de {estacion}")