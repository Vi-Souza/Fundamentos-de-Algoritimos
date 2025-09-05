dias = int(input("Digite a quantidade de dias: "))
horas = int(input("Digite a quantidade de horas: "))
min = int(input("Digite a quantidade de minutos: "))
seg = int(input("Digite a quantidade de segundos: "))
total_seg = (dias*86400)+(horas*3600)+(min*60)+seg
print(f"A quantidade total de segundos é: {total_seg:,d}")