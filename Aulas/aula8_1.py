lista=[]
for _ in range(10):
    n=int(input("valor: "))
    lista.append(n)
soma_pares = 0
soma_indice_par = 0
for indice in range(len(lista)):
    print(lista[indice], indice)
    if lista[indice]%2==0:
        soma_pares=soma_pares+lista[indice]
    if indice%2==0:
        soma_indice_par+=lista[indice]
print(soma_indice_par)
print(soma_pares)