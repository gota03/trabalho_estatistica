from customtkinter import *

janela = CTk()

set_appearance_mode("System")
janela.state("zoomed")
janela.resizable(True, True)
janela.title("Tela Inicial")

mensagem_tema = CTkLabel(janela, text="Tema: ", font=(("Arial bold"), 20))
mensagem_tema.place(x=1025, y=30)

mensagem_principal = CTkLabel(janela, text="Bem vindo ao sistema, escolha uma das opções abaixo",
                              font=(("Arial bold"), 30))
mensagem_principal.place(x=300, y=100)

tema_padrao = StringVar(value="Padrão do sistema")


def altera_tema(escolha):
    if escolha == "Claro":
        set_appearance_mode("Light")
    elif escolha == "Escuro":
        set_appearance_mode("Dark")
    else:
        set_appearance_mode("System")


temas = ["Claro", "Escuro", "Padrão do sistema"]

opcoes_tema = CTkOptionMenu(janela,
                            values=temas,
                            command=altera_tema,
                            variable=tema_padrao,
                            width=200,
                            height=30,
                            font=("Arial bold", 18)
                            )
opcoes_tema.place(x=1100, y=30)


def abrir_janela_amostragem():
    janela.state("iconic")
    janela_amostragem = CTkToplevel(janela)
    janela_amostragem.title("Amostragem")
    janela_amostragem.geometry("400x400")


btn_amostragem = CTkButton(janela,
                           command=abrir_janela_amostragem,
                           text="Calcular amostragem",
                           height=200,
                           width=200,
                           font=(("Arial bold"), 20))
btn_amostragem.place(x=250, y=250)

janela.mainloop()
