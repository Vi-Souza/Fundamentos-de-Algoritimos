km = float(input("Digite sua quilometragem: "))
dias = int(input("Digite seus dias: "))
pagamento = (km * 0.15) + (dias * 60)
print(f"Total a pagar: R${pagamento}")