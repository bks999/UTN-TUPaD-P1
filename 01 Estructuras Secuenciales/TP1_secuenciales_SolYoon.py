# Ejercicio 1
print("Hola Mundo!")

print("---------------------------")

# Ejercicio 2
nombre = input("Ingrese su nombre: ")
print(f"Hola {nombre}!")

print("---------------------------")

# Ejercicio 3
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su lugar de residencia: ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

print("---------------------------")

# Ejercicio 4
import math
radio = float(input("Ingrese el radio de un circulo: "))
area = round(math.pi * (radio)**2, 2)
perimetro = round(2 * math.pi * radio, 2)
print(f"Area: {area}, perimetro: {perimetro}")

print("---------------------------")

# Ejercicio 5
segundos = float(input("Ingrese una cantidad de segundos: "))
horas = round(segundos / 3600, 2)
print(f"{segundos} segundos equivalen a {horas} horas")

print("---------------------------")

# Ejercicio 6
numero = int(input("Ingrese un numero: "))
print(f"{numero} x 0 = {numero*0}")
print(f"{numero} x 1 = {numero*1}")
print(f"{numero} x 2 = {numero*2}")
print(f"{numero} x 3 = {numero*3}")
print(f"{numero} x 4 = {numero*4}")
print(f"{numero} x 5 = {numero*5}")
print(f"{numero} x 6 = {numero*6}")
print(f"{numero} x 7 = {numero*7}")
print(f"{numero} x 8 = {numero*8}")
print(f"{numero} x 9 = {numero*9}")
print(f"{numero} x 10 = {numero*10}")

print("---------------------------")

# Ejercicio 7
print("Ingrese dos numeros enteros distintos de 0")
num1 = int(input("Numero 1: "))
num2 = int(input("Numero 2: "))
print(f"Suma: {num1 + num2}")
print(f"Division: {round(num1 / num2, 2)}")
print(f"Multiplicacion: {num1 * num2}")
print(f"Resta: {num1 - num2}")

print("---------------------------")

# Ejercicio 8
altura = float(input("Ingrese su altura: "))
peso = float(input("Ingrese su peso: "))
IMC = round(peso/(altura**2), 2)
print(f"Su indice de masa corporal(IMC) es: {IMC} kg/m2")

print("---------------------------")

# Ejercicio 9
celcius = float(input("Ingrese una temperatura en grados Celcius: "))
fahrenheit = 9 / 5 * celcius + 32
print(f"{celcius} grados Celcius equivalen a {fahrenheit} grados Fahrenheit")

print("---------------------------")

# Ejercicio 10
print("Ingrese 3 numeros: ")
num1 = float(input("Num1: "))
num2 = float(input("Num2: "))
num3 = float(input("Num3: "))
promedio = round((num1 + num2 + num3) / 3,2)
print(f"El promedio de los numeros ingresados es: {promedio}")

print("---------------------------")