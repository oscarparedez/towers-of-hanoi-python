# Torres de Hanoi. Recursividad (Divide and Conquer)
# Referencia: https://www.geeksforgeeks.org/python-program-for-tower-of-hanoi/
# Explicación de variables:
    # n: Cantidad de discos 
    # stackA: nombre de la primera varilla (varilla de origen)
    # stackB: nombre de la segunda varilla (varilla de destino)
    # stackC:: nombre de la tercera varilla (varilla auxiliar)
# El disco # 1 es el más pequeño
# El disco # n es el más grande

import time

n = 18
stackA = 'A'
stackB = 'B'
stackC = 'C'

def TOH(n, origen, destino, aux):
    if n == 1:
        print ("Moviendo el disco # 1 desde la varilla origen (", origen, ") a la varilla destino (", destino, ")")
        return
    TOH(n-1, origen, aux, destino)
    print ("Moviendo el disco #", n, "desde la varilla origen (", origen, ") a la varilla destino (", destino, ")")
    TOH(n-1, aux, destino, origen)

start_time = time.time()
TOH(n, stackA, stackB, stackC)
print("Total time: ", time.time() - start_time)