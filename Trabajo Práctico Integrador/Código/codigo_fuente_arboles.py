from collections import deque

# 1. Crear un árbol vacío
def crear_arbol():
    # Devuelve un árbol vacío representado por una lista vacía.
    return []

# 2. Crear un nodo con valor n
def crear_nodo(valor):
    """
    Crea un nodo como lista de tres elementos:
    [valor, subárbol_izquierdo, subárbol_derecho]
    Inicialmente ambos subárboles están vacíos.
    """
    return [valor, [], []]

# 3. Insertar hijo izquierdo
def insertar_izquierda(nodo, nuevo_valor):
    """
    Si no existe hijo izquierdo, lo crea.
    Si existe, empuja el subárbol existente como hijo izquierdo del nuevo nodo.
    """
    if nodo[1] == []:
        nodo[1] = crear_nodo(nuevo_valor)
    else:
        nodo[1] = [nuevo_valor, nodo[1], []]

# 4. Insertar hijo derecho
def insertar_derecha(nodo, nuevo_valor):
    """
    Igual que insertar_izquierda, pero para el subárbol derecho.
    """
    if nodo[2] == []:
        nodo[2] = crear_nodo(nuevo_valor)
    else:
        nodo[2] = [nuevo_valor, [], nodo[2]]

# 5. Recorridos clásicos
def preorden(nodo):
    """Visita: raíz → izquierdo → derecho."""
    if nodo != []:
        print(nodo[0], end=" ")
        preorden(nodo[1])
        preorden(nodo[2])

def inorden(nodo):
    """Visita: izquierdo → raíz → derecho."""
    if nodo != []:
        inorden(nodo[1])
        print(nodo[0], end=" ")
        inorden(nodo[2])

def postorden(nodo):
    """Visita: izquierdo → derecho → raíz."""
    if nodo != []:
        postorden(nodo[1])
        postorden(nodo[2])
        print(nodo[0], end=" ")

# 6. Recorrido por niveles
def recorrido_por_niveles(arbol):
    """
    Visita nivel por nivel de izquierda a derecha
    usando una cola auxiliar.
    """
    if arbol == []:
        return
    cola = deque([arbol])
    while cola:
        nodo = cola.popleft()
        print(nodo[0], end=" ")
        if nodo[1] != []:
            cola.append(nodo[1])
        if nodo[2] != []:
            cola.append(nodo[2])

# 7. Visualizar la estructura
def visualizar_arbol(nodo, nivel=0):
    """
    Imprime el árbol "girado" 90°.
    El hijo derecho aparece arriba y el izquierdo abajo.
    """
    if nodo != []:
        visualizar_arbol(nodo[2], nivel + 1)
        print("   " * nivel + str(nodo[0]))
        visualizar_arbol(nodo[1], nivel + 1)


# --- Ejecución de código
if __name__ == "__main__":
    # Crear raíz
    arbol = crear_nodo(10)

    # Agregar varios nodos
    insertar_izquierda(arbol, 5)
    insertar_derecha(arbol, 15)
    insertar_izquierda(arbol[1], 3)
    insertar_derecha(arbol[1], 7)
    insertar_derecha(arbol[2], 20)

    # 1) Visualización
    print("Visualización del árbol:")
    visualizar_arbol(arbol)

    # 2) Recorridos
    print("\nRecorrido Preorden: ", end="")
    preorden(arbol)
    print("\nRecorrido Inorden:  ", end="")
    inorden(arbol)
    print("\nRecorrido Postorden:", end=" ")
    postorden(arbol)
    print("\nRecorrido por niveles:", end=" ")
    recorrido_por_niveles(arbol)
    print()