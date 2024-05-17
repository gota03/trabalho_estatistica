import matplotlib.pyplot as plt

meses_dict = {
    "Janeiro": 0,
    "Fevereiro": 0,
    "Março": 0,
    "Abril": 0,
    "Maio": 0,
    "Junho": 0,
    "Julho": 0,
    "Agosto": 0,
    "Setembro": 0,
    "Outubro": 0,
    "Novembro": 0,
    "Dezembro": 0
}

for i in meses_dict:
    temperatura_mes = float(input(f"temperatura do mês {i}: "))
    meses_dict[i] = temperatura_mes

eixo_x = []
eixo_y = []
media_temperatura_ano = []
for i in meses_dict:
    eixo_x.append(i)
    eixo_y.append(meses_dict[i])
    media_temperatura_ano.append(sum(meses_dict.values()) / len(meses_dict.values()))

print(media_temperatura_ano)

plt.rcParams.update({'font.size': 10})
plt.title("Temperatura dos meses")
plt.xlabel("Meses do ano")
plt.ylabel("Temperatura em graus Celsius")
plt.bar(eixo_x, eixo_y, label="Temperatura por mês", color="g", linewidth=1, alpha=0.4, edgecolor="g")
plt.plot(eixo_x, media_temperatura_ano, label="Média da temperatura no ano", color="r")
plt.legend()
plt.show()
