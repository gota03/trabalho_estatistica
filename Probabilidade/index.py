import math

media_sucessos = float(input("media de sucessos: "))
sucesso_esperado = float(input("sucesso esperado: "))

num = sucesso_esperado
fatorial = 1
while num > 1:
    fatorial *= num
    num -= 1

# print(math.e)
formula = ((media_sucessos ** sucesso_esperado)/fatorial) * math.e ** - media_sucessos
print(f"{formula:.3f} ou {formula*100:.2f}%")
