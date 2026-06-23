# Situação de Aprendizagem – Atividade Individual
# Exercícios de Programação Python: "O Caça-Erros"

# 1. O Problema da Idade

# idade = input("Digite sua idade:")
# if idade >=18:
#     print("Você é maior de idade.")

# 2. A Escrita Fiel

# nome = "Mariana"
# print("Seja Bem-vinda,nome!")

# 3. Falta de Espaço

# numero = 10
# if numero >5:
#     print("O numero é maior que cinco.")
# else:
#     print("O número é o menor ou igual a cinco.")

# 4. Esquecimento Fatal

# usuario = "aluno123"
# if usuario == "alun123"
# print("Login realizado com sucesso.")

# 5. Atribuição vs. Comparação

# clima = "ensolarado"
# if clima = "chuvoso":
#  print("Login realizado com sucesso!")

# 6. Misturando Alhos com Bugalhos

# pontos = 50
# print("Parabéns! Você fez " + pontos +"pontos.")


# 7. A Ordem dos Fatores
# nota = 9.5
# if nota >=7:
#  print("Aprovado!")
# elif nota >=9:
#  print("Excelente!")


# 8. O Contador de 1 a 5
# for i in range  (5):
#   print("i")

# 9. O Loop Eterno

# tentativas = 1
# while tentativas <= 3:
#  print("Tentando conectar...")
 

# 10. A Senha Teimosa

# senha = ""
# while senha == "python123":
#  senha = input("Digite a senha secreta:")
# print("Acesso concedido!")





# CORRIGIDO e MELHORIAS:

# idade =  int(input("Digite sua idade:"))
# if idade == [18]:
#      print("Você é maior de idade.")
# else:
#       print("Você é menor de idade.")


("*************************************")

# nome = "Mariana"
# print("Seja Bem-vinda!", nome)

# Melhoria

# nome = input("Qual o seu nome?")
# if nome == "Mariana":
#     print("Bem-Vinda, Mariana")
# else:
#     print("Você não é a Mariana!, saia!")
("*************************************")

# numero = 10
# if numero > 5:
#  print("O número é maior que cinco.")
# else:
#  print("O número é menor ou igual a cinco.")

#Melhoria
# numero = input("Digite um número:")
# if numero > "5":
#       print("O numero é maior que cinco.")
# elif numero == "5":
#       print("Seu número é igual a cinco!")
# else:
#       print("O número é menor do que o cinco.") 
    

("*************************************")

# usuario = input("Digite a senha secreta:")
# if usuario == "aluno123":  
#      print("Login realizado com sucesso.")
# else:
#      print("ERROR no login!")


("************************************")


# clima = input("qual o clima de hoje?")
# if clima == "chuvoso":
#  print("Leve um guarda-chuva!")
# elif clima == "ensolarado":
#  print("Use óculos de sol")

("************************************")

# pontos = 50
# print("Parabéns! Você fez ", + pontos,  + pontos)


("***********************************")

# nota = int(input("qual foi sua nota?"))
# if nota ==7:
#      print("Aprovado!")
# elif nota >=9:
#    print("Excelente!")
# else:
#    print("Que horror!")

("***********************************")

# i = ["1, 2, 3, 4, 5, 6"]
# for i in range  (6):
#     print("Mostrar na tela os números", i)


("***********************************")

# tentativas = 1
# while tentativas <= 3:
#   print("Tentando conectar...")
#   break

("****************************************")

# senha = input("Digite a senha secreta:")
# if senha == "python123":
#     print("Acesso Concedido!")
# else:
#     print("Acesso Negado!")
