# 1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa
# función para calcular y mostrar en pantalla el factorial de todos los números enteros
# entre 1 y el número que indique el usuario

def factorial(num):
    f=1
    for i in range(1,num+1):
        f *= i
    return f

def factorial_recursivo(num):
    if num == 0:
        print(1)
    else:
        for i in range (1,num+1):
            print(f"{i}! = {factorial(i)}")        

numero_ingresado = int(input("Ingrese un numero: "))
factorial_recursivo(numero_ingresado)

# 2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición
# indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario
# especifique.

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
posicion = int(input("Ingrese un numero para mostrar la serie de Fibonacci hasta dicha posicion: "))

for i in range(posicion+1):
    print(f"{i} = {fibonacci(i)}")

# 3) Crea una función recursiva que calcule la potencia de un número base elevado a un
# exponente, utilizando la fórmula 𝑛**𝑚 = 𝑛 ∗ 𝑛**(𝑚−1)
# Prueba esta función en un algoritmo general.

def formula(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * (formula(base, exponente - 1))

base = int(input("Ingrese el valor de la base: "))
exponente = int(input("Ingrese el valor del exponente: "))

print(f"{base}**{exponente} = {formula(base, exponente)}")

# 4) Crear una función recursiva en Python que reciba un número entero positivo en base
# decimal y devuelva su representación en binario como una cadena de texto.

def decimal_a_binario(num):
    if num == 0:
        return "0"
    elif num == 1:
        return "1"
    else:
        return decimal_a_binario(num//2) + str(num%2)
    
num = int(input("Ingrese un numero decimal positivo: "))
print(f"El valor binario de {num} es: {decimal_a_binario(num)}")

# 5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba una
# cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no lo es.

def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    elif palabra[0] != palabra[-1]:
        return False
    else:
        return es_palindromo(palabra[1:-1])

palabra = input("Ingrese una palabra sin espacios ni tildes: ")
print(f"La palabra {palabra} es palindromo: {es_palindromo(palabra)}")

# 6) Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un
# número entero positivo y devuelva la suma de todos sus dígitos.

def suma_digitos(n):
    if n < 10:
        return n
    else:
        resultado = n % 10
        return resultado + suma_digitos(n // 10)

# def suma_digitos(n):
#     resultado=0
#     if n//10 == 0 and n%10 == 0:
#         return n
#     else:
#         resultado += n%10
#         return resultado + suma_digitos(n//10)
    
n = int(input("Ingrese un numero: "))
print(f"La suma de los digitos es: {suma_digitos(n)}")

# 7)  Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n
# bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al
# último nivel con un solo bloque.
# Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el
# nivel más bajo y devuelva el total de bloques que necesita para construir toda la
# pirámide.

def contar_bloques(n):
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n-1)

n_bloques = int(input("Ingrese el numero de bloques inicial: "))
print(f"El total de bloques utilizados para construir la piramide es: {contar_bloques(n_bloques)}")

# 8) Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un
# número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces
# aparece ese dígito dentro del número.

def contar_digitos(numero, digito):
    if numero == 0:
        return 1 if digito == 0 else 0
    elif numero%10 == digito:
        return 1 + contar_digitos(numero//10, digito)
    else:
        return 0 + contar_digitos(numero//10, digito)

digito= int(input("Ingrese un digito del 0 al 9: "))
numero = int(input("Ingrese un numero: "))
print(f"El digito {digito} se repite en el numero {numero} esta cantidad de veces: {contar_digitos(numero, digito)}")