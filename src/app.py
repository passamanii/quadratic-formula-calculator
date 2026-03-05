import tkinter as tk
from calculator import *


def calcular():

    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        c = float(entry_c.get())

        x1, x2 = calcula_raizes(a, b, c)
            
        if (x1 is None):
                resultado_label.config(text='Não existem raízes reais.')
        else:
                resultado_label.config(text=f'Raízes: {x1} e {x2}.')
        
    except ValueError as error:
        resultado_label.config(text=f'Erro: {error}.')


#Janela
janela = tk.Tk()
janela.title('Calculadora de Bhaskara')
janela.geometry('350x300')
janela.resizable(False,False)

#Título
titulo = tk.Label(
      janela,
      text='Equação do 2º Grau',
      font=('Arial', 14, 'bold'),
)
titulo.pack(pady=10)

#Inputs
tk.Label(janela, text='Coeficiente a:').pack()
entry_a = tk.Entry(janela)
entry_a.pack()

tk.Label(janela, text='Coeficiente b:').pack()
entry_b = tk.Entry(janela)
entry_b.pack()

tk.Label(janela, text='Coeficiente c:').pack()
entry_c = tk.Entry(janela)
entry_c.pack()

#Botão
botao = tk.Button(
      janela,
      text='Calcular',
      command=calcular
)
botao.pack(pady=15)

#Resultado
resultado_label = tk.Label(
      janela,
      text='',
      font=('Arial', 11)
)
resultado_label.pack()

#Loop
janela.mainloop()