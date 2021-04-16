N=int(input())
Lista = input().split()
Lista = list ( map ( int, Lista))
lista1=Lista.copy()
lista2=Lista
lista2.sort()
print("Menor valor:",lista2[0])
print("Posicao:",lista1.index(min(lista1)))