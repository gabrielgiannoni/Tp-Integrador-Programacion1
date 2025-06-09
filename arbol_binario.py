#Definicion de funciones

def buscar(arbol, valor):
    if arbol is None:
        return False
    if arbol[0] == valor:
        return True
    return buscar(arbol[1], valor) or buscar(arbol[2], valor)


def buscar_inorden(arbol):
    if arbol:
        buscar_inorden(arbol[1])
        print(arbol[0], end=' ')
        buscar_inorden(arbol[2])
        
def buscar_preorden(arbol):
    if arbol:
        print(arbol[0], end=' ')
        buscar_preorden(arbol[1])
        buscar_preorden(arbol[2])
        
        
def buscar_postorden(arbol):
    if arbol:
        buscar_postorden(arbol[1])
        buscar_postorden(arbol[2])
        print(arbol[0], end=' ')


#Programa principal

arbol = [10, 
         [5, 
          [2, None, None], 
          [7, None, None]
         ],
         [15, 
          [12, None, None], 
          [20, None, None]
         ]
        ]

print("Recorrido inorden:")
buscar_inorden(arbol)  # 2 5 7 10 12 15 20

print("\nRecorrido preorden:")
buscar_preorden(arbol)  # 10 5 2 7 15 12 20

print("\nRecorrido postorden:")
buscar_postorden(arbol)  # 2 7 5 12 20 15 10

print("\n¿Está el 12 en el árbol?")
print(buscar(arbol, 13))  # True

