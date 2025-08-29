num = int(input("Digite um numero: "))

if num in [1, 8, 15, 22, 29]:
    print(f"{num} - Domingo")
elif num in [2, 9, 16, 23, 30]:
    print(f"{num} - Segunda")
elif num in [3, 10, 17, 24, 31]:
    print(f"{num} - Terça")
elif num in [4, 11, 18, 25]:
    print(f"{num} - Quarta")
elif num in [5, 12, 19, 26]:
    print(f"{num} - Quinta")
elif num in [6, 13, 20, 27]:
    print(f"{num} - Sexta")
elif num in [7, 14, 19, 28]:
    print(f"{num} - Sábado")
else:
    print("Numero invalido digite um numero de 1 a 31")