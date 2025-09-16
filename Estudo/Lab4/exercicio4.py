c=float(input("Digite o valor da compra: "))
p=int(input("Digite a quantidade de parcelas: "))
d=float
vf=float
vp=float
if p==1:
    if c>5000:
        d=c*0.15
        vf=c-d
        print(f"Desconto total: {d:.2f}")
        print(f"Valor final da compra com desconto: {vf:.2f}")
        print(f"Cada parcela será de: {vf:.2f}")
    else:
        d=c*0.10
        vf=c-d
        print(f"Desconto total: {d:.2f}")
        print(f"Valor final da compra com desconto: {vf:.2f}")
        print(f"Cada parcela será de: {vf:.2f}")
elif p==2 or p==3:
        if c>5000:
            d=c*0.10
            vf=c-d
            vp=vf/p
            print(f"Desconto total: {d:.2f}")
            print(f"Valor final da compra com desconto: {vf:.2f}")
            print(f"Cada parcela será de: {vp:.2f}")
        else:
            d=c*0.05
            vf=c-d
            vp=vf/p
            print(f"Desconto total: {d:.2f}")
            print(f"Valor final da compra com desconto: {vf:.2f}")
            print(f"Cada parcela será de: {vp:.2f}")
else:
    if c>5000:
        d=c*0.05
        vf=c-d
        vp=vf/p
        print(f"Desconto total: {d:.2f}")
        print(f"Valor final da compra com desconto: {vf:.2f}")
        print(f"Cada parcela será de: {vp:.2f}")
    else:
        d=0
        vf=c-d
        vp=vf/p
        print(f"Desconto total: {d:.2f}")
        print(f"Valor final da compra com desconto: {vf:.2f}")
        print(f"Cada parcela será de: {vp:.2f}")