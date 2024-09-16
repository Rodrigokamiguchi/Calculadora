import math
import tkinter as tk
from tkinter import messagebox

# Função  de cálculo
def calcular_opercacao(expressao):
    try:
        resultado = eval(expressao)
        return resultado
    except ZeroDivisionError:
        return "Erro: Divisão por zero"
    except Exception:
        return "Erro: Expressão inválida"
    
# Função para atualizar o display
def atualizar_display(valor):
    atual = display_var.get()
    display_var.set(atual + str(valor))

# Função para limpar o display
def limpar_display():
    display_var.set("")

# Funçao para calcular o resultado
def exibir_resultado():
    expressao = display_var.get()
    resultado = calcular_opercacao(expressao)
    display_var.set(str(resultado))

# Função para criar o layout da calculadora
def criar_calculadora():
    root = tk.Tk()
    root.title("Calculadora")

    global display_var
    display_var = tk.StringVar()

     # Display onde os números e resultados aparecerão
    display = tk.Entry(root, textvariable=display_var, font=("Arial", 20), bd=10, insertwidth=2, width=14, borderwidth=4, justify="right")
    display.grid(row=0, column=0, columnspan=4)
    # Lista de botões
    botoes = [
        '7', '8', '9', '/', 
        '4', '5', '6', '*', 
        '1', '2', '3', '-', 
        '0', '.', '=', '+'
    ]

    # Criação dos botões numéricos e de operação
    row_val = 1
    col_val = 0
    for botao in botoes:
        action = lambda x=botao: atualizar_display(x) if x != '=' else exibir_resultado()
        tk.Button(root, text=botao, padx=20, pady=20, font=("Arial", 18), command=action).grid(row=row_val, column=col_val)
        col_val += 1
        if col_val > 3:
            col_val = 0
            row_val += 1

    # Botão para limpar o display
    tk.Button(root, text="C", padx=20, pady=20, font=("Arial", 18), command=limpar_display).grid(row=row_val, column=0, columnspan=4, sticky="we")

    root.mainloop()

# Iniciar a calculadora
criar_calculadora()