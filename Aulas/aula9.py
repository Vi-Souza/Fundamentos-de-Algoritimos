lista = []
for i in range(10):
    n = int(input("valor: "))
    lista.append(n)

print(lista)

for i in range(2, len(lista)): 
    if lista[i] > lista[i - 1] + lista[i - 2]:
        print(lista[i])
