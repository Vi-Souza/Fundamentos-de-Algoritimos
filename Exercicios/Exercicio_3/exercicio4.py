sal = float(input("digite seu salario: "))
if sal>1250:
    sal=sal*1.1
    print(f"Seu novo salario: {sal:.2f}")
else:
    sal=sal*1.15
    print(f"Seu novo salario: {sal:.2f}")