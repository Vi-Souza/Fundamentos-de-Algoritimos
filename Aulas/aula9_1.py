lista = []
while True:
    n = input("valor: ")
    if n=="":
        break
    if n not in lista:
        lista.append(n)
for elemento in lista:
    print(elemento)

    