# Condições de Lógicas e Decisões
# O prgrama toma caminhos diferentes dependendo da condição.
# Funções de Lógicas SE e Senão
# If , elif e else
#if = SE (verdadeiro)
 
# elif = continua sendo (verdadeiro)
# else Falso

# # Exemplo 1 
# print("Bem-vindo as Lógicas e Decisões")
# print("Para iniciar digite a opção desejada")
# print("Digite 1 para filmes e 2 para Séries e 3 para Novelas")

# escolha = int(input("Digite a opção que deseja: "))
 

# if escolha == 1:
#      print("Você escolheu filmes")
# elif escolha == 2: 
#      print("Você escolheu Séries")
# elif escolha == 3: 
#      print("Você escolheu novela")
# else:
#     print("Você não escolheu nenhum opção do catalogo")

#     # Exemplo 2print(" Pokémon")
#     print("Escolha seu  personagens")
#     print("Pikachu = P")
#     print("Chirizard = C")
#     print("Mewtwo = M")

# Pokemons = input("Digite a letra do seu persoangem")
# if Pokemons == "P":
#      print("Você escolheu PIKACHU")
# elif Pokemons == "C":
#      print("Você escolheu o CHARIZARD")
# elif Pokemons == "M":
#      print("Você escolheu Mewtwo")
# else:
#      print("Espero você na proxima, até mais!1")

# # Exemplo 3
# Valores númericos e flutuantes
print("Valores")
print("Comparações de número")

números = int(input("Digite um número"))

if números > 100:
     print("Número alto")
elif números < 100: 
     print("Números Baixos")
else:
     print("Escolher um valor que não temos")