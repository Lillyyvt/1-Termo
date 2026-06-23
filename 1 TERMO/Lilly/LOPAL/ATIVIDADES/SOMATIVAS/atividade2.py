# Situação de Aprendizagem – Atividade Individual

# Foco: print, input, operações matemáticas e f-strings


# 1. Registro de Operador: Peça o nome do operador e o turno (A, B ou C). Exiba:
# "Operador [Nome] registrado no Turno [Turno]. Boa jornada!"

# 2. Cálculo de Produção: Peça a quantidade de peças produzidas em 1 hora. Calcule e
# exiba quantas peças serão produzidas em um turno de 8 horas.

# 3. Conversor de Unidade: O sistema lê uma pressão em Bar. Converta para PSI (1 Bar
# ≈ 14.5 PSI) e exiba com duas casas decimais.

# 4. Média de Qualidade: Peça 3 notas de inspeção de uma peça (0 a 10). Exiba a média
# aritmética simples delas.


# Foco: if, elif, else e operadores lógicos


# 5. Termostato Inteligente: Peça a temperatura de um motor.
# ● Abaixo de 40°C: "Baixa carga".
# ● Entre 40°C e 70°C: "Normal".
# ● Acima de 70°C: "ALERTA: Resfriamento Ativado!".

# 6. Classificador de Lotes: O usuário insere o código do produto. Se começar com "A",
# exiba "Alimentos". Se "E", "Eletrônicos". Para qualquer outro, "Desconhecido".

# 7. Segurança de Operação: A máquina só liga se o sensor_porta == "fechada" E o
# botao_emergencia == "desligado". Peça esses dois inputs e diga se a máquina pode
# iniciar.

# 8. Cálculo de Descarte: Peça o total de peças produzidas e o total de defeituosas. Se
# o descarte for maior que 5% do total, exiba "Revisar Processo", caso contrário,
# "Processo Otimizado".

# 9. Validação de Medida: Uma peça deve ter entre 9.8mm e 10.2mm. Peça a medida e
# diga se está dentro da tolerância, acima ou abaixo.

# 10.Contagem Regressiva de Setup: Use um for para fazer uma contagem regressiva
# de 10 até 1 para o início de uma prensa, e finalize com "Prensa Ativada!".

# RESPOSTA:

#1.  
# import tkinter as tk
# from tkinter import messagebox
# def registro_operacionais():
#     nome = campo_nome.get()
#     turno = turno_usuario.get()
     
#     if nome == "" and turno == "":
#          messagebox.showwarning("Aviso", "Por favor, digite seu nome!")
#     else:
#          messagebox.showinfo("Bem-Vindo", f"Operador {nome} registrado no Turno {turno}. Boa jornada!")

# app = tk.Tk()
# app.title("Registro OP ★")
# app.geometry("350x200")

# #Nome
# lbl_instrucao = tk.Label(app, text="Digite seu nome abaixo:") 
# lbl_instrucao.pack(pady=5)

# campo_nome = tk.Entry(app, font=("Arial", 11))
# campo_nome.pack(pady=5)

# #Turno
# lbl_instrucao = tk.Label(app, text="Digite seu turno abaixo:") 
# lbl_instrucao.pack(pady=10)

# turno_usuario = tk.Entry(app, font=("Arial", 11))
# turno_usuario.pack(pady=10)

# btn_enviar = tk.Button(app, text="Enviar", bg="#143d24", fg="beige",command=registro_operacionais)
# btn_enviar.pack(pady=15)

# app.mainloop()

#★-★-★-★-★-★-★-★-★-★-★-★-★-★

#2.
# import tkinter as tk
# from tkinter import messagebox
# def Calculo_Producao():
#      pecas = int(campo_pecas.get())
#      horas = int(campo_horas.get())
     
#      if pecas == "":
#           messagebox.showwarning("Aviso", "Por favor, Qual a quantidade de peças feitas em 1hr?")
#      else:
#           quantidade = pecas * horas  
#           messagebox.showinfo("Olá!!:D", f"Resultado: {quantidade}")

# app = tk.Tk()
# app.title("Cálculo de Produção ★")
# app.geometry("350x200")
# app.configure(bg="#3E7243")
 
# lbl_instrucao = tk.Label(app, text="Digite a quantidade abaixo:") 
# lbl_instrucao.pack(pady=5)

# campo_pecas = tk.Entry(app, font=("Arial", 11))
# campo_pecas.pack(pady=5)

 
# lbl_instrucao = tk.Label(app, text="Digite tempo de produção:") 
# lbl_instrucao.pack(pady=10)

# campo_horas = tk.Entry(app, font=("Arial", 11))
# campo_horas.pack(pady=10)

# btn_enviar = tk.Button(app, text="Enviar", bg="#1c1835", fg="yellow",command=Calculo_Producao)
# btn_enviar.pack(pady=15)

# app.mainloop()

#★-★-★-★-★-★-★-★-★-★-★-★-★-★

#3.
# import tkinter as tk
# from tkinter import messagebox
# def Conversor_Unidade():
#       bar = int(campo_barP.get())
     
#       if bar == "":
#            messagebox.showwarning("VAI BRASIL!", "Por Favor, digite o a conversão de Unidade")
#       else:
#            PSI = bar * 14.5 #PSI  
#            messagebox.showinfo("Olá!!:D", f"A pressão convertida é: {PSI}")

# app = tk.Tk()
# app.title("Conversor de Unidade ★")
# app.geometry("350x200")
# app.configure(bg="blue")
 
# lbl_instrucao = tk.Label(app, text="Digite a pressão em Bar:") 
# lbl_instrucao.pack(pady=5)

# campo_barP = tk.Entry(app, font=("Arial", 11))
# campo_barP.pack(pady=5)

 

# btn_enviar = tk.Button(app, text="Enviar", bg="#12270A", fg="yellow",command=Conversor_Unidade)
# btn_enviar.pack(pady=15)

# app.mainloop()

#★-★-★-★-★-★-★-★-★-★-★-★-★-★

#4.
# import tkinter as tk
# from tkinter import messagebox
# def Média_Qualidade():
#       nota1 = int(float(campo_um.get()))
#       nota2 = int(float(campo_dois.get()))
#       nota3 = int(float(campo_tres.get()))

#       if nota1 == "" and nota2 == "" and nota3 == "":
#            messagebox.showwarning("Aviso", "Por Favor, dê uma nota de 0 a 10!")
#       else:
#            total = nota1 + nota2 + nota3 / 3
#            messagebox.showinfo("BRASIL!!", f"Resultado: {total}")

# app = tk.Tk()
# app.title("Média de Qualidade ★")
# app.geometry("350x300")
# app.configure(bg="olive")
 
# lbl_instrucao = tk.Label(app, text="Digite a nota1 abaixo:") 
# lbl_instrucao.pack(pady=5)

# campo_um = tk.Entry(app, font=("Arial", 11))
# campo_um.pack(pady=5)

 
# lbl_instrucao = tk.Label(app, text="Digite a nota2 abaixo:") 
# lbl_instrucao.pack(pady=10)

# campo_dois = tk.Entry(app, font=("Arial", 11))
# campo_dois.pack(pady=10)

# lbl_instrucao = tk.Label(app, text="Digite nota3 abaixo:") 
# lbl_instrucao.pack(pady=15)

# campo_tres = tk.Entry(app, font=("Arial", 11))
# campo_tres.pack(pady=15)

# btn_enviar = tk.Button(app, text="Enviar", bg="#CFCC17", fg="blue",command=Média_Qualidade)
# btn_enviar.pack(pady=15)

# app.mainloop()

#★-★-★-★-★-★-★-★-★-★-★-★-★-★

#5.
# import tkinter as tk
# from tkinter import messagebox
# def Termostato_Inteligente():
#        temp = int(campo_temp.get())

#        if temp <= 40:
#             messagebox.showwarning("Aviso", "Baixa carga")
#        elif temp >= 40 and temp < 70:
#              messagebox.showwarning("Aviso", "Normal")
#        elif temp > 70:
#              messagebox.showwarning("Aviso", "ALERTA: Resfriamento Ativado!")
#        else:
#             messagebox.showinfo("BRASIL!!", f" A temperatura está em estado de {temp}")

# app = tk.Tk()
# app.title("Termostato Inteligente ★")
# app.geometry("350x300")
# app.configure(bg="#C4961A")
 
# lbl_instrucao = tk.Label(app, text="Digite a temperatura abaixo:") 
# lbl_instrucao.pack(pady=5)

# campo_temp = tk.Entry(app, font=("Arial", 11))
# campo_temp.pack(pady=5)


# btn_enviar = tk.Button(app, text="Enviar", bg="#422408", fg="beige",command=Termostato_Inteligente)
# btn_enviar.pack(pady=15)

# app.mainloop()

#★-★-★-★-★-★-★-★-★-★-★-★-★-★

#6.
# import tkinter as tk
# from tkinter import messagebox
# def Classificador_Lotes():
#         usuario = (campo_person.get())

#         if usuario == "A":
#              messagebox.showwarning("Aviso", "Alimentos")
#         elif usuario == "E":
#               messagebox.showwarning("Aviso", "Eletrônicos")
#         elif usuario == "":
#               messagebox.showwarning("Aviso", "Desconhecido")
#         else:
#              messagebox.showinfo("Classificando os Lotes...", f"O codigo de produto {usuario}")

# app = tk.Tk()
# app.title("Classificador de Lotes ★")
# app.geometry("350x300")
# app.configure(bg="#053A03")
 
# lbl_instrucao = tk.Label(app, text="Digite o código:", bg="#080969", fg="yellow") 
# lbl_instrucao.pack(pady=5)

# campo_person = tk.Entry(app, font=("Arial", 11))
# campo_person.pack(pady=5)


# btn_enviar = tk.Button(app, text="Enviar", bg="#080969", fg="yellow",command=Classificador_Lotes)
# btn_enviar.pack(pady=15)

# app.mainloop()

#★-★-★-★-★-★-★-★-★-★-★-★-★-★

#7.
# import tkinter as tk
# from tkinter import messagebox
# def Segurança_Operação():
#          sensor = (sensor_porta.get())
#          botao = (botao_emergencia.get())
#          if sensor == "fechada":
#               messagebox.showwarning("Aviso", "É possivel ligar o Sensor?")
#          elif botao == "desligado":
#                messagebox.showwarning("Aviso", "É possivel ligar o Botão?")
#          elif sensor and botao == "Ligado":
#              messagebox.showwarning("Aviso", "Continue sua Operação!")  
#          else:
#               messagebox.showinfo("Iniciando Segurança de OPeração...", f"Ligando as Máquinas...")

# app = tk.Tk()
# app.title("Segurança de Operação ★")
# app.geometry("350x300")
# app.configure(bg="#29033A")
 
# #Sensor
# lbl_instrucao = tk.Label(app, text="DIgite o estado do Sensor:", bg="#A9A3FD", fg="yellow") 
# lbl_instrucao.pack(pady=5)

# sensor_porta = tk.Entry(app, font=("Arial", 11))
# sensor_porta.pack(pady=5)

# #Botão
# lbl_instrucao = tk.Label(app, text="DIgite o estado do Botão:", bg="#A9A3FD", fg="yellow") 
# lbl_instrucao.pack(pady=5)

# botao_emergencia = tk.Entry(app, font=("Arial", 11))
# botao_emergencia.pack(pady=5)

# btn_enviar = tk.Button(app, text="Enviar", bg="#DEDEF0", fg="white",command=Segurança_Operação)
# btn_enviar.pack(pady=15)

# app.mainloop()

#★-★-★-★-★-★-★-★-★-★-★-★-★-★

#8.
# import tkinter as tk
# from tkinter import messagebox
# def Cálculo_Descarte():
#           produzida = int(peca_poduzida.get())
#           defeituosa = int(total_defeituosas.get())
#           if produzida < 5:
#                messagebox.showwarning("Aviso", "Processo Otimizado")
#           elif defeituosa > 5:
#                 messagebox.showwarning("Aviso", "Revisar Processo")
#           else:
#                total = produzida - defeituosa
#                messagebox.showinfo("Cálculo de Descarte", f"O total de peças é {total}")

# app = tk.Tk()
# app.title("Cálculo de Descarte ★")
# app.geometry("350x300")
# app.configure(bg="#53728B")

# lbl_instrucao = tk.Label(app, text="DIgite a porcentagem de peças produzidas:", bg="#09072B", fg="white") 
# lbl_instrucao.pack(pady=5)

# peca_poduzida = tk.Entry(app, font=("Arial", 11))
# peca_poduzida.pack(pady=5)


# #defeituosa
# lbl_instrucao = tk.Label(app, text="DIgite a porcentagem de peças defeituosas:", bg="#09072B", fg="white") 
# lbl_instrucao.pack(pady=10)

# total_defeituosas = tk.Entry(app, font=("Arial", 11))
# total_defeituosas.pack(pady=10)

# #enviar

# btn_enviar = tk.Button(app, text="Enviar", bg="#DEDEF0", fg="white",activebackground= "#05051F",command=Cálculo_Descarte)
# btn_enviar.pack(pady=15)

# app.mainloop()

#★-★-★-★-★-★-★-★-★-★-★-★-★-★
#9.
# import tkinter as tk
# from tkinter import messagebox
# def Validação_Medida():
#           medida = int(float(peca_medida.get()))
#           if medida > 10.2:
#                messagebox.showwarning("Aviso", "Tolerância acima. A peça deve ter entre 9.8mm e 10.2mm")
#           elif medida < 9.8:
#                messagebox.showwarning("Aviso", "Tolerância abaixo. A peça deve ter entre 9.8mm e 10.2mm")
#           else:
#                messagebox.showinfo("Validação de Medida ★", f"Tolerância aceitável")

# app = tk.Tk()
# app.title("Validação de Medida ★")
# app.geometry("350x300")
# app.configure(bg="#8B5353")

# # peça
# lbl_instrucao = tk.Label(app, text="Digite mm da peça :", bg="#2B0707", fg="white") 
# lbl_instrucao.pack(pady=5)

# peca_medida = tk.Entry(app, font=("Arial", 11))
# peca_medida.pack(pady=5)


# #enviar
# btn_enviar = tk.Button(app, text="Enviar", bg="#F0DEDE", fg="white",activebackground= "#1F0505",command=Validação_Medida)
# btn_enviar.pack(pady=15)

# app.mainloop()

#★-★-★-★-★-★-★-★-★-★-★-★-★-★
#10. 
# import tkinter as tk
# from tkinter import messagebox
# def Contagem_Regressiva_Setup():
#           contagem = int(contagem_regressiva.get())
# import time
# # contagem = [1,10]
# for número in range(10,0,-1):
#       if número == "":
#        import time
#        messagebox.showwarning("Contagem Regressiva de Setup ★",{número})                      
#        continue
#       else:
#        messagebox.showwarning("Contagem Regressiva de Setup ★", {número})  


# app = tk.Tk()
# app.title("Contagem Regressiva de Setup ★")
# app.geometry("350x300")
# app.configure(bg="#8B5353")

# # peça
# lbl_instrucao = tk.Label(app, text=" ", bg="#2B0707", fg="white") 
# lbl_instrucao.pack(pady=5)

# contagem_regressiva = tk.Entry(app, font=("Arial", 11))
# contagem_regressiva.pack(pady=5)


# #enviar
# btn_enviar = tk.Button(app, text="Enviar", bg="#F0DEDE", fg="white",activebackground= "#1F0505",command=Contagem_Regressiva_Setup)
# btn_enviar.pack(pady=15)

# app.mainloop()