# Torres de Hanoi. Programación Dinámica
# Referencia: https://www.geeksforgeeks.org/iterative-tower-of-hanoi/
# Explicación de variables:
    # n: Cantidad de discos 
    # stackA: nombre de la primera varilla (varilla de origen)
    # stackB: nombre de la segunda varilla (varilla de destino)
    # stackC:: nombre de la tercera varilla (varilla auxiliar)
# El disco # 1 es el más pequeño
# El disco # n es el más grande
import sys
n = 2

class Stack:
    def __init__(self):
        self.top = -1
        self.array = [0]*n

def isFull(stack):
    return (stack.top == (n - 1))

def isEmpty(stack):
    return (stack.top == -1)

def add(stack, item):
    if not (isFull(stack)):
        stack.top += 1
        stack.array[stack.top] = item
    else:
        return

def remove(stack):
    if not (isEmpty(stack)):
        stackTop = stack.top
        stack.top -= 1
        return stack.array[stackTop]
    else:
        return -sys.maxsize

def moveDisksBetweenTwoPoles(stackOrigen, stackDestino, torreOrigen, torreDestino):
    origenTopDisk = remove(stackOrigen)
    destinoTopDisk = remove(stackDestino)
 
    # Si stackOrigen esta vacia
    if (origenTopDisk == -sys.maxsize):
        add(stackOrigen, destinoTopDisk)
        print("Moviendo el disco", destinoTopDisk, "desde la varilla origen '", torreDestino, "' a la varilla destino '", torreOrigen, "'")
       
    # Si stackDestino esta vacia
    elif (destinoTopDisk == -sys.maxsize):
        add(stackDestino, origenTopDisk)
        print("Moviendo el disco", origenTopDisk, "desde la varilla origen '", torreOrigen, "' a la varilla destino '", torreDestino, "'")
       
    # Si el disco de stackOrigen es de mayor peso que el disco de stackDestino
    elif (origenTopDisk > destinoTopDisk):
        add(stackOrigen, origenTopDisk)
        add(stackOrigen, destinoTopDisk)
        print("Moviendo el disco", destinoTopDisk, "desde la varilla origen '", torreDestino, "' a la varilla destino '", torreOrigen, "'")
       
    # Si el disco de stackOrigen es de menor peso que el disco de stackDestino
    else:
        add(stackDestino, destinoTopDisk)
        add(stackDestino, origenTopDisk)
        print("Moviendo el disco", origenTopDisk, "desde la varilla origen '", torreOrigen, "' a la varilla destino '", torreDestino, "'")
   
def TOH(stackOrigen, stackAuxiliar, stackDestino):
    torreOrigen, torreDestino, torreAuxiliar = 'A', 'B', 'C'
    totalMovimientos = 2**n
    # Si n es par, intercambiamos la torreDestino y torreAuxiliar para que el disco # 1 se mueva a B en vez de a C
    if (n % 2 == 0):
        temp = torreDestino
        torreDestino = torreAuxiliar
        torreAuxiliar = temp
   
    # Se mueven al stack los discos del más grande al más pequeño
    for i in range(n, 0, -1):
        add(stackOrigen, i)

    # Se realizan los movimientos respectivos siguiendo el patrón a continuación
    for i in range(1, totalMovimientos):
        if (i % 3 == 1):
            moveDisksBetweenTwoPoles(stackOrigen, stackDestino, torreOrigen, torreDestino)
   
        elif (i % 3 == 2):
            moveDisksBetweenTwoPoles(stackOrigen, stackAuxiliar, torreOrigen, torreAuxiliar)
   
        elif (i % 3 == 0):
            moveDisksBetweenTwoPoles(stackAuxiliar, stackDestino, torreAuxiliar, torreDestino)

stackA = Stack()
stackB = Stack()
stackC = Stack()
 
TOH(stackA, stackC, stackB)
