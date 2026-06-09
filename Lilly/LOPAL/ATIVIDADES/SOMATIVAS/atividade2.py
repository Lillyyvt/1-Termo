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
def janela_bemvindo():
    nome = nome_usuario.get()
    turno = turno_usuario.get()

    if nome == "" and turno =="":

        messagebox.showwarning("Aviso", "Digite seu nome e seu turno ★")

    else:
        messagebox.showinfo("Bem-Vindo", f"Operador [Nome] registrado no Turno [Turno]. Boa jornada!")

lbl_titulo_pagina = tk.Label(janela, text="Bem-Vindo Registro de Operador!", font=("Arial", 14, "bold"))
btn_clique_pagina = tk.Button(janela, text="Digite seu nome", font=("Antiqua Moderna", 14), bg="#3b0505", fg="beige", command=mostrar_mensagem)
btn_fechar_janela = tk.Button(janela, text="Fechar", font=("Antiqua Moderna", 14), bg="#3d3214", fg="beige", command=janela.destroy)

lbl_titulo_pagina.pack(pady=20) 
btn_clique_pagina.pack(pady=15)
btn_fechar_janela.pack(pady=10)

janela.mainloop()

