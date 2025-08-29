nasc = int(input("Digite seu ano de nascimento: "))
ano_at = int(input("Digite ano atual: "))

if (ano_at-nasc)>=18:
    print("Pode tirar cnh")
if (ano_at-nasc)<18:
    print("Não pode tirar cnh")