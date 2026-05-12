
#¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨

# Foco: print, input, tipos de dados e cálculos simples.

#¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨

# Exercício 1:
# Perfil de Gamer: Peça o nick (nome) do jogador e o nível atual. Exiba: "O jogador [nick] está no nível [nível] e pronto para a partida!"
# print("Bem-Vindo ao jogo lilly's!")
# nível = int(input("Digite seu nível:"))
# nick = input("Digite seu nick:")
# print("O nick do jogador é:" , nick)
# print("O jogador está no nível:" , nível)     


# Exercicio 2:
#Calculadora de Mesada: Peça o valor que o aluno ganha por semana e multiplique por 4 para mostrar quanto ele terá no final do mês.
# print("Bem-Vindo a calculadora de Mesada!")
# valor = int(input("Qual o valor de sua mesada: "))
# multiplicação = valor * 4
# print("A valor da mesada foi: ", multiplicação)
# print("Obrigada por escolher nossa calculadora")


# Exercício 3:
# Conversor de Internet: Peça um valor em Gigabytes (GB) e converta para Megabytes (MB) (multiplique por 1024).
# print(" Bem-Vindo ao Conversor de internet!")
# valorGB = int(input("Qual o valor de Gigabytes?: "))
# valorMB = 1024
# multiplicação = valorGB * valorMB
# print("A valor convertido foi de: ", multiplicação) 


# Exercício 4:
# Média de Notas: Peça as notas de Matemática e Português. Calcule e mostre a média final.
# FAZER
# print("Bem-Vindo a nota de média!")
# notamat = float(input("Qual foi sua nota em Matemática?:"))
# notaport = float(input("Qual foi sua nota em português?:"))
# médiaf = (notamat + notaport) / 2
# print(" Sua média final foi de: ",  médiaf)


# Exercício 5:
# Seguidores: Peça a quantidade de seguidores atuais e quantos novos seguidores o aluno ganhou hoje. Exiba o total atualizado.
# seguidorA = int(input("Quantos seguidores você tem?: "))
# seguidorN = int(input("Quantos novos seguidores você ganhou?: "))
# total = seguidorA + seguidorN
# print("Seu total de seguidores atualizado é de: " , total)
# print("Você está famosa(o)!")


# Exercício 6:
#Idade em Dias: Peça a idade do aluno e calcule aproximadamente quantos dias ele já viveu (idade * 365).
# print("Bem-Vindo a calculadora da vida!")
# idade = int(input("Qual a sua idade?: "))
# totalidade = idade * 365
# print("Você já viveu: ", totalidade)


# Exercício 7:
# Consumo de Lanche: Peça o preço do salgado e o preço do suco. Exiba o valor total da conta.
# print("Bem-Vindo a cantina Cleusa's")
# print("Gostaria de um suco e salgado, certo?")
# salgado = int(input("Qual o valor do salgado?: "))
# suco = int(input("Qual o valor do suco?: "))
# total = salgado + suco
# print("O valor do dois é:", total)


# Exercício 8:
#Ano de Nascimento: Peça o ano atual e a idade do aluno. Calcule e exiba o ano em que ele nasceu.
# idade = int(input("Quantos anos você tem?:"))
# print("Vamos somar sua idade com o ano atual!")
# atual = 2026
# nascimento = atual - idade
# print("Você nasceu em:" , nascimento)

#¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨

# Foco: if/elif/else, for, while e acumuladores.

#¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨

# Exercício 9:
# Filtro de Idade (TikTok): Peça a idade do usuário. Se for menor que 13, exiba
# "Acesso restrito". Se tiver entre 13 e 17, "Acesso moderado". Se for 18 ou
# mais, "Acesso liberado".

# idade = int(input("Digite a sua idade"))
# if idade < 13:
#     print("Acesso restrito")
# elif idade >  13:
#     print("Acesso moderado")
# elif idade ==  18:
#     print("Acesso liberado!")
# else:
#     print("Você tem idade o suficiente")


# Exercício 10:
# Bateria do Celular: Crie um while que começa com a bateria em 100. A cada
# repetição, subtraia 10 e mostre: "Bateria em [valor]%". O loop para quando
# chegar em 10 e exibe: "Por favor, conecte o carregador!"

# bateria = 90
# while bateria in range(1, 100 ):
#     if bateria < 100:
#         print(f"Bateria em {bateria}% ")
#         bateria -+ 10
# print("Por favor, conecte ao carregador!")

# bateria = 0
# while bateria < 100:
#         print(f"Bateria em descarga {bateria}")
#         bateria += 10
        
# print("Conecte o carregador")


# Exercicio 11:
# Contagem de Curtidas: Use um for para simular a contagem de curtidas em uma
# foto. Peça ao usuário o limite de curtidas (ex: 5). O programa deve contar de 1 até
# esse número, printando: "Curtida no [i] recebida!".

# curtidas = [1,101]
# ncurtidas = print("Quantas curtidas você recebeu?:")
# for curtidas in range:
#     print(f" ♡{curtidas} curtida") 
    
#    NÃO TERMINADO!!!