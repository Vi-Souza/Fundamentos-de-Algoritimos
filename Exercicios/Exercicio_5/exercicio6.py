count = 0 
soma = 0 
while True: 
    num = int(input("Digite um número (0 para sair): ")) 
    if num == 0: 
        break 
    soma = soma + num 
    count = count + 1 
    
if count > 0: 
    media = soma / count 
else: 
    media = 0 
    
print(f"Quantidade de números digitados: {count}") 
print(f"Somatória dos números digitados: {soma}") 
print(f"Média aritmética dos números digitados: {media}") 