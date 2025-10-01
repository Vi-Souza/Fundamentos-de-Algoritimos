lista=[]
for _ in range(10):
    n=int(input("valor: "))
    lista.append(n)
maior = lista[0]
indice_do_maior =  0
for indice in range(len(lista)):
    print(lista[indice], indice)
    if lista[indice]>maior:
        maior = lista[indice]
        indice_do_maior = indice

print(f"Maior valor {maior} indice {indice_do_maior}")