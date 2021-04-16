lista = []
a = int(input())
maior=0
menor=0
for i in range(a):
    x= int(input())
    lista.append(x)
media=(sum(lista))/(len(lista))
pctmaior=media*1.10
pctmenor=media*0.90
for i in lista:
    if i >=pctmaior:
        maior+=1
    elif i<pctmenor:
        menor+=1
print("%.2f"%media)
print(maior)
print(menor)