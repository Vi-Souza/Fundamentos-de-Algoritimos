n=int(input("Entre com a quantidade de números que serão digitados: "))
cont=0
maior= 0
while True:
    if n<=cont:
        break
    else:
        cont=cont+1
        num=int(input(f"número {cont}: "))
        if cont == 1:
            maior = num 
        elif num > maior:
            maior = num
print(f"Maior número digitado: {maior}")