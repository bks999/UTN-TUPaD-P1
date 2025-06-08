import math
import time

def imprimir_hola_mundo():
    print("Hola Mundo!")

def saludar_usuario(nombre):
    print(f"Hola {nombre}!")

def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

def calcular_area_circulo(radio):
    return radio * radio * math.pi

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

def segundos_a_horas(segundos):
    return segundos/3600

def tabla_multiplicar(numero):
    for i in range(1,11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b!=0 else "No se puede dividir por cero"
    return (suma, resta, multiplicacion, division)

def calcular_imc(peso, altura):
    return peso/(altura**2)
    
def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def calcular_promedio(a,b,c):
    return (a+b+c)/3

# Programa principal

# Ejercicio 1
imprimir_hola_mundo()
time.sleep(2)

# Ejercicio 2
saludar_usuario(input("Como te llamas? "))
time.sleep(2)

# Ejercicio 3
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = int(input("Ingrese su edad: "))
residencia = input("Ingrese su residencia: ")
informacion_personal(nombre,apellido,edad,residencia)
time.sleep(2)

# Ejercicio 4
radio=float(input("Ingrese el radio del circulo: "))
area_circulo = calcular_area_circulo(radio)
perimetro_circulo = calcular_perimetro_circulo(radio)
print(f"Area del circulo: {area_circulo}, Perimetro del circulo: {perimetro_circulo}")
time.sleep(2)

# Ejercicio 5
segundos=int(input("Ingrese un valor en segundos: "))
print(f"{segundos} equivalen a {segundos_a_horas(segundos)} horas")
time.sleep(2)

# Ejercicio 6
numero_para_multiplicar = int(input("Ingrese un numero para ver su tabla de multiplicar: "))
tabla_multiplicar(numero_para_multiplicar)
time.sleep(2)

# Ejercicio 7
a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))

resultado_operaciones = operaciones_basicas(a,b)

print("Resultados de las operaciones: ")
print(f"Suma: {resultado_operaciones[0]}")
print(f"Resta: {resultado_operaciones[1]}")
print(f"Multiplicación: {resultado_operaciones[2]}")
print(f"División: {resultado_operaciones[3]}")

time.sleep(2)

# Ejercicio 8
peso = float(input("Ingrese su peso(kg): "))
altura = float(input("Ingrese su altura(m): "))
print(f"Su IMC es {calcular_imc(peso,altura)}")
time.sleep(2)

# Ejercicio 9
celsius=float(input("Ingrese un valor de grados Celcius"))
print(f"Equivalen a {celsius_a_fahrenheit(celsius)} grados Fahrenheit")
time.sleep(2)

# Ejercicio 10
a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))
c = float(input("Ingrese el tercer número: "))
print(f"El promedio de los numeros ingresados es: {calcular_promedio(a,b,c)}")