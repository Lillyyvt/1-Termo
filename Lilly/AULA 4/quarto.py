# 1. O laçoo while (Repetições Indeterminadas)
# Use o while quando você não sabe quando vai parar. Ele depender de uma condição (como um sensor de segurança ou um tbotão de emergência).
# Exemplo: o monitor de Temperatura (LOop infinito Controlado)
# Repete enquando a temperatura estiver segura
# Início
# Exemplo 1:
# import time 
# temperatura = 25
# while temperatura < 40:
#     print(f"Temperatura atual: {temperatura} °C. Sistema operando...")
#    # time.sleep(1)
#     temperatura += 3 # Simulando o aquecimento global da máquina
# print("ALERTA! Temperatura atingiu o limite. Desligando motor...")

# Lista de temperaturas lidas pelo sensor por minuto

#Exemplo 2: Monitoramento de temperatura com Lista de Leituras
# Lista de temperaturas lidas pelo sensor por minuto
# leituras = [70, 75, 82, 98, 110, 85, 80]

# for temp in leituras:
#     if temp > 100:
#         print(f"CRÍTICO: {temp} °C detectado! Acionando parada de emergência.")
#         break  # O loop para aqui e NÃO lê os próximos valores (85 e 80)
#     print(f"Temperatura está em {temp}°C. Operação normal.")

# print("Sistema desligado. Aguandando manutenção.")

#Exemplo 3
# materiais= ["metal", "metal", "plastico", "metal", "vidro", "metal"]
# for peca in materiais:
#     if peca != "metal":
#         print(f"Aviso: Peça de {peca} detectada. Desviando para descarte...")
#         continue # Pula o restante do codigo abaixo e vai para a próxima peça
#     # Este codigo só roda se a peça for de metal
#     print(f"Processando peça de {peca}. Furando e polindo...")

# print("Fim do lote de produçao.")




# Exercício 1
# Tente criar uma lista que conte de 1 a 10, mas use o continue para não imprimir o número 5 (simulando uma falha de sensor especifica no item 5)

# import time
# lista = [1,10]
# for número in range[1,11]:
#     if número == 5:
#        import time
#         print(f"Aviso: {número} com falha.") 
#         print(f"{número} sem falha")                       
#     continue
#     print("Sistema desligando")

# Exercicio 2
# Simule um semáforo com parada para cada cor. Determine um tempo que deseja para que qunado mudar para tal cor ele represente uma pausa para cada cor.
# Use o contiue para pular a cor amarela (simulando um semáforo com defeito que nao acende a luz amarela.)

# import time
# semáforo = ["verde", "amarelo", "vermelho"]
# for cor in semáforo:
#         if cor == "amarelo":
#               time.sleep(3)
#         print(f"sinal {cor} com falha")
#         continue
#         print(f"sensor {semáforo} sem falha")
# print("Bom passeio")
              
#Exercercio 3 - Soma de Cargas de Energia (for)
# Uma fabrica tem 5 máquinas. Peça ao usuário (via input dentro do loop) o consumo de kwh de cada umas das 5 máquinas. Ao final do loop,\n
#  programa deve exibir o conumo total da fabrica.

# total_consumo = 0
# for maquina in range(1,6):
#     consumo = float(input(f"Quantas {maquina} kwh de cada maquina foram consumidas ao todo?"))
# total_consumo += consumo # Acumula o consumo total
# print(f"O total de consumo foi de {total_consumo} kwh:")
