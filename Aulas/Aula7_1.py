def multiplo(x,y):
    if x%y==0:
        return "a é multiplo de b"
    else:
        return "a não é multiplo de b"

a=int(input("digite 1 numero: "))
b=int(input("digite 2 numero: "))
print(f"{multiplo(a,b)}")
