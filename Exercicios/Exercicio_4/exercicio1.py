a = int(input("numero a: "))
b = int(input("numero b: "))
c = int(input("numero c: "))
if a>b and a>c:
    if b>c:
        print(f"a:{a}>b:{b}>c:{c}")
    else:
        print(f"a:{a}>c:{c}>b:{b}")
elif b>a and b>c:
    if a>c:
        print(f"b:{b}>a:{a}>c:{c}")
    else:
        print(f"b:{b}>c:{c}>a:{a}")
else:
    if a>b:
        print(f"c:{c}>a:{a}>b:{b}")
    else:
        print(f"c:{c}>b:{b}>a:{a}")
