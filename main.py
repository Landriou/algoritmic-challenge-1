
from avltree import *
from algo1 import *


#Funcion wrapper para la recursividad
def insertR2(NewNode,currentnode):
    NewNode.parent = currentnode
    
    if NewNode.key > currentnode.key: #Si es mayor
        if currentnode.rightnode == None:
            currentnode.rightnode = NewNode
            return NewNode.key #Si esta vacio lo inserto en esa posicion y retorno la key 
        else:
            return insertR(NewNode,currentnode.rightnode)
            #Si no, llamo a la recursividad
    else:
        if NewNode.key == currentnode.key:
            newArray = Array(2,0)
            if NewNode.value[0] < currentnode.value[0]:
                newArray[0] = NewNode.value[0]
                newArray[1] = currentnode.value[0]
            else:
                newArray[1] = NewNode.value[0]
                newArray[0] = currentnode.value[0]   
            currentnode.value = newArray
            return None
        if currentnode.leftnode == None:
            currentnode.leftnode = NewNode
            return NewNode.key #lo mismo pero del lado izquierdo
        else:
            return insertR(NewNode,currentnode.leftnode)
            #Si no, llamo a la recursividad

#Funcion que inserta un nodo
def avl_desaf_insert(AVLtree,e,k):
    NewNode = AVLNode()
    NewNode.key = k
    NewNode.value = e #Creo el nodo y le asigno los valores
    if AVLtree.root == None:
        AVLtree.root = NewNode
        return k
    else:
        keyinserted = insertR2(NewNode,AVLtree.root)
        reBalance(AVLtree)
        return keyinserted

def absolutePivote(A,p):
    print(A)
    print("El pivote es", p)
    avl = AVLTree()
    for n in range(len(A)):
        a = Array(1,0)
        a[0] = A[n]
        avl_desaf_insert(avl,a, abs(A[n]- p))
    L = traverseInOrder(avl)
    currentnode = L.head
    newArray = Array(len(A),0)
    contador = 0
    size = len(newArray)
    while contador < size:
        if len(currentnode.value) == 1:
            newArray[contador] = currentnode.value[0]
        if len(currentnode.value) == 2:
            newArray[contador] = currentnode.value[0]
            contador = contador + 1
            newArray[contador] = currentnode.value[1]
        currentnode = currentnode.nextNode
        contador = contador + 1
    print(newArray)

a = Array(4,0)
a[0] = 5
a[1] = 3
a[2] = 7
a[3] = 10
b = Array(4,0)
b[0] = 4
b[1] = 2
b[2] = 11
b[3] = 8
c = Array(4,0)
c[0] = 2
c[1] = 10
c[2] = 8
c[3] = 4
absolutePivote(a,7)
print("")
absolutePivote(b,7)
print("")
absolutePivote(c,7)