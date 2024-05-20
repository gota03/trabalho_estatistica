import customtkinter as ctk
import matplotlib.pyplot as plt

janela = ctk.CTk()
ctk.set_appearance_mode("system")
width = janela.winfo_screenwidth()
height = janela.winfo_screenheight()
janela.geometry("%dx%d" % (width, height))
janela.title("Sistema de cálculo de temperatura")


def alterar_tema(escolha):
    if escolha == "Padrão do sistema":
        ctk.set_appearance_mode("system")
    elif escolha == "Claro":
        ctk.set_appearance_mode("light")
    else:
        ctk.set_appearance_mode("dark")


label_tema = ctk.CTkLabel(janela, text="Tema:", font=("Arial bold", 15))
label_tema.place(x=10, y=30)

tema = ctk.CTkOptionMenu(janela, values=["Padrão do sistema", "Claro", "Escuro"], command=alterar_tema, width=170,
                         font=("Arial bold", 15))
tema.place(x=60, y=30)

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

mensagem_sistema = ctk.CTkLabel(janela, text="Bem vindo ao sistema de cálculo de temperatura", font=("Arial bold", 35))
mensagem_sistema.pack(pady=30)

meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto",
         "Setembro", "Outubro", "Novembro", "Dezembro"]
indice_mes = 0

mensagem_escolha = ctk.CTkLabel(janela, text="Informe a temperatura para o mês: ", font=("Arial bold", 20))
mensagem_escolha.place(x=300, y=120)

label = ctk.CTkLabel(janela, text=meses[indice_mes], font=("Arial bold", 20))
label.pack(pady=20)

temperatura = ctk.CTkEntry(janela, placeholder_text="Digite aqui a temperatura...", width=300, height=40)
temperatura.pack()


def enviar_temperatura():
    global indice_mes
    temperatura_dict = temperatura.get()
    if temperatura.get() != "":
        meses_dict[meses[indice_mes]] = float(temperatura_dict)

        if indice_mes == len(meses) - 1:
            temperatura.configure(state="disabled")
            btn_enviar_temperatura.configure(state="disabled")
        else:
            # Atualiza o índice e o rótulo do mês
            indice_mes = (indice_mes + 1)
            label.configure(text=meses[indice_mes])
            temperatura.delete(0, 'end')
            temperatura.delete(0, 'end')  # Limpa o campo de entrada após o envio


def gerar_grafico():
    meses_rotulos = list(meses_dict.keys())
    temperaturas_reais = list(meses_dict.values())

    sensacao_termica = [temp * 1.1 for temp in temperaturas_reais]

    media_temperatura_ano = sum(meses_dict.values()) / len(meses_dict)

    # Cria um gráfico de barras para as temperaturas reais
    plt.figure(figsize=(10, 6))
    plt.bar(meses_rotulos, temperaturas_reais, color='lightblue', label='Temperatura Real')

    # Plota a linha para a sensação térmica
    plt.plot(meses_rotulos, sensacao_termica, color='orange', marker='o', label='Sensação Térmica')

    # Adiciona a média da temperatura no ano como uma linha horizontal
    plt.axhline(y=media_temperatura_ano, color='red', linestyle='--', label='Média Anual')

    plt.title('Estatísticas da temperatura ao longo do ano')
    plt.xlabel('Meses do ano')
    plt.ylabel('Temperatura (°C)')
    plt.legend()
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()


def calcular_variancia():
    media_temperaturas = sum(meses_dict.values()) / len(meses_dict)

    variancia = sum((temp - media_temperaturas) ** 2 for temp in meses_dict.values()) / len(meses_dict)
    print(variancia)
    exibir_resultado(f"Variância: {variancia:.2f}")


def calcular_desvio_padrao():
    media_temperaturas = sum(meses_dict.values()) / len(meses_dict)

    desvio_padrao = (sum((temp - media_temperaturas) ** 2 for temp in meses_dict.values()) / len(meses_dict)) ** 0.5
    print(desvio_padrao)
    exibir_resultado(f"Desvio padrão: {desvio_padrao:.2f}")


def calcular_coeficiente_variacao():
    media_temperaturas = sum(meses_dict.values()) / len(meses_dict)

    desvio_padrao = (sum((temp - media_temperaturas) ** 2 for temp in meses_dict.values()) / len(meses_dict)) ** 0.5

    coeficiente_variacao = (desvio_padrao / media_temperaturas) * 100
    print(coeficiente_variacao)
    exibir_resultado(f"Coeficiente de variação: {coeficiente_variacao:.2f}%")


def calcular_amplitude_total():
    amplitude_total = max(meses_dict.values()) - min(meses_dict.values())
    print(amplitude_total)
    exibir_resultado(f"Amplitude Total: {amplitude_total:.2f}")


# Frame para exibir os resultados
frame_resultados = ctk.CTkFrame(janela)
frame_resultados.pack(fill="both", expand=True, pady=20)


# Função para exibir o resultado no frame de resultados
def exibir_resultado(texto):
    # Limpa o conteúdo do frame de resultados
    for widget in frame_resultados.winfo_children():
        widget.destroy()
    # Exibe o texto do resultado no frame
    label_resultado = ctk.CTkLabel(frame_resultados, text=texto, font=("Arial bold", 20))
    label_resultado.pack(pady=250)


btn_enviar_temperatura = ctk.CTkButton(janela, text="Enviar temperatura", command=enviar_temperatura, width=200,
                                       height=40, font=("Arial bold", 15))
btn_enviar_temperatura.place(x=590, y=240)

btn_gerar_grafico = ctk.CTkButton(janela, text="Gerar gráfico", command=gerar_grafico, width=200, height=40,
                                  fg_color="green", font=("Arial bold", 15), hover_color="green")
btn_gerar_grafico.place(x=590, y=600)

btn_variancia = ctk.CTkButton(janela, text="Calcular variância", command=calcular_variancia, width=200, height=40,
                              font=("Arial bold", 15))
btn_variancia.place(x=200, y=350)

btn_coeficiente_variacao = ctk.CTkButton(janela, text="Calcular coeficiente de variação",
                                         command=calcular_coeficiente_variacao, width=200, height=40,
                                         font=("Arial bold", 15))
btn_coeficiente_variacao.place(x=430, y=350)

btn_amplitude_total = ctk.CTkButton(janela, text="Calcular amplitude total", command=calcular_amplitude_total,
                                    width=200, height=40, font=("Arial bold", 15))
btn_amplitude_total.place(x=690, y=350)

btn_desvio_padrao = ctk.CTkButton(janela, text="Calcular desvio padrão", command=calcular_desvio_padrao, width=200,
                                  height=40, font=("Arial bold", 15))
btn_desvio_padrao.place(x=920, y=350)

janela.mainloop()
