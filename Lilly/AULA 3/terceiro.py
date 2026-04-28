#1. Laço 'for' (Repetições Determinadas)
#Use 'for quando você sabe exatamente quantas vezes algo deve acontecer (como ler 10 sensores ou processar uma lista de peças). 
#Exemplo: Relátorio de Produção Diária 
#Imagine que você tem uma meta de produzir 5 lotes e quer numerar cada um:

# Exemplo 1
# for lote in range(1, 6):
#     print(F"Processando lote número {lote}...")
#     print("Qualidade verificada. {OK}")
#     print("Produção do dia finalização")


# Exemplo 2
# for b in range(20):
#     print(f"Quantidade total {b} foi")


# Exemplo 3
# Imagine o seguinte cenário, iremos produzir 20 discos de vinil.
# for disco in range(21):
#     print(f"Quantidade total {disco} foi")
#     print("Qualidade verificada. {OK}")
#     print("Produção do dia finalização")

# Exemplo 4
# pecas = "Engrenagem", "Eixo", "Rolamento", "Parafuso", "Martelo"
# itempecas = ["Cilindricas, "Eixo Cônico", "Radicais", "Madeira", "Bola", "Cabeça Chata", "Chave Metálica]


# for item in pecas:
#     print(f"item em estoque:{pecas} ")
#     for item2 in itempecas:
#         print(f"Item de pecas em estoque: {itempecas}")


# Exemplo 5
# Imagine a seguinte situação, gostaria de ter um menu onde pudesse perguntar qual opção você deseja e a partir da seleção, ele listar os produtos.
# print("Loja lilly's hughry")
# print("Opção 1 - massa")
# print("Opção 2 - carnes")
# menu = int(input("Escolha a opção desejada"))

# massa = ["Pão,Pastel, Lasanha,Raviolli, macarrão"]
# carnes = ["carne, frango, peixe, bovino, linguiça"]

# if menu == 1:
#      for item in massa:
#       print(f"item em estoque:{massa}" , são...)
# elif menu == 2:
#      for item in carnes:
#       print(f"Sua lista de comida {carnes}" , são...)
# else: 
#       print("Opção inválida: Encerrando o sistema")



# Exercício 1
# 1. Contado de Produção (for)
# Umas esteira processa apenas 10 ciclo. Crie um programa que use um for para contar de 1 a 10 e, para cada número, imprima: "Peça n X processada com sucesso". No final, exiba "Ciclo de produção conclusão"

# for ciclo  in range(10):
#     print(F"Processando ciclo  número {esteira}...")
#     print("Peça n X processada com sucesso")
#     print("Ciclo de produção conclusão")


# Exercicio 2 
# Imagine a produçaõ de fruta em uma feira . DEsejo apresentar as fruntas: banana, manga, melancia, abacaxi. Com um quantidade de 10 bananas, 45 mangas, 10 melancias e 13 abcaxi.

# frutas = ["Banana", "Manga", "Kiwi", "Melancia", "Abacaxi", "Ameixa"]

# for frutas in range(10):
#      print("quantidade de {banana}")

# for frutas in range(45):
#      print("quantidade de {manga}")

# for frutas in range(15): 
#     print("quantidade de {kiwi}")

# for frutas in range(10): 
#      print("quantidade e {melancia}")

# for frutas in range(13): 
#      print("quantidade de abacaxi")

# for frutas in range(20): 
#      print("quantidade de {ameixa}")
# total = 10 + 45 + 15 + 10 + 13
# print("a soma é" , total)

# Exercicio 3
# Montar uma tabuada inicialmente pode ser usado por uma valor fixo e depois usar a pergunta.

# tabuada = int(input("Qual tabuada deseja usar?"))
# for número in range(1,11):
#     multiplicação = (número * tabuada)
#     print(f"{número} X {tabuada} =  {multiplicação}")
