count = 0 
maior = 0 
while count < 6: 
    num = int(input("Digite um número inteiro positivo: ")) 
    if num > maior: 
        maior = num 
    count = count + 1 
    
print(f"O maior número digitado foi: {maior}") 

#ou

maior = 0 
for count in range(6): 
    num = int(input("Digite um número inteiro positivo: ")) 
    if num > maior: 
        maior = num 
        
print(f"O maior número digitado foi: {maior}") 