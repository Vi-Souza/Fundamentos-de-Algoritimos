hi = int(input("Digite a hora inicial: "))
mi = int(input("Digite o minuto inicial: "))
hf = int(input("Digite a hora final: "))
mf = int(input("Digite o minuto final: "))

# Converte para minutos
inicio = hi * 60 + mi
fim = hf * 60 + mf

# Calcula duração
if fim > inicio:
    dur = fim - inicio
elif fim < inicio:
    dur = (24 * 60 - inicio) + fim
else:
    dur = 24 * 60  # exatamente 24 horas

# Converte para h:m
horas = dur // 60
minutos = dur % 60

print(f"O jogo durou {horas} hora(s) e {minutos} minutos(s)")
