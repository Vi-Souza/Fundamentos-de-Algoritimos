valor = int(input("Digite o valor da hora: "))
horas = float(input("Digite a quantidade de horas trabalhadas no mes: "))
sal_bruto = valor * horas
desc_IR = sal_bruto * 0.11
desc_INSS = sal_bruto * 0.08
desc_Sind = sal_bruto * 0.05
sal_liq = sal_bruto - (desc_INSS + desc_IR + desc_Sind)
print(f"""
Salario bruto: R$ {sal_bruto:.2f}
- IR (11%): R$ {desc_IR:.2f}
- INSS (8%): R$ {desc_INSS:.2f}
- Sindicato (5%): R$ {desc_Sind:.2f}
Salario liquido: R$ {sal_liq:.2f}""")