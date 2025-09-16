somatoria=0

while True:
    entrada= int(input("Digiteum nmero a somar ou 0 pra sair:"))
    if entrada==0:
        print("Resultado:",somatoria)
        break
    else:
        somatoria= somatoria + entrada
        print("Somatoria:",somatoria)