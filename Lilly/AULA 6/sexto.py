# Clean Code - Aula 6
# Para que usar?
# Como usar?
# print("Clean Code - Aula 6")
# Aula = 6
# print(f"Estamos na aula {Aula} de Clean Code")

# # Manipulação de arquivos e Texto
# texto = " Pyton é muito legal!! "
# print(texto.strip().upper()) # "PYTHON"
# print(texto.strip().lower()) # "python"
# print(texto.strip().capitalize()) # "Python"
# print(texto.strip().title()) # "Python"
# print(texto.strip().replace(" ", "_")) # "Python"
# print(texto.strip().split())  # ["Python"]

# Escrevendo
# with open("notas.txt", "w") as arquivo:
#     arquivo.write("Estudar Python hoje!")
#     arquivo.write("\nLer sobre Clean Code.")

# #Lendo
# with open("notas.txt", "r") as arquivo:
#     conteudo = arquivo.read()
#     print(conteudo)

# Exercicio 1:
# As vezes eu quero demais e eu nunca sei se eu mereço...
# Crie um programa que peça ao usuário para inserir uma frase e, em seguida, exiba a frase com as seguintes transformações:
# - Remova os espaços extras no início e no final da frase.
# frase = input("Insira uma frase")
# print(frase.strip().replace(" ", "_"))

# Exemplo 1:
# Crie um programa que leia o conteúdo de um arquivo de texto e conte quantas vezes a palavra "Python" aparece no arquivo. Exiba o resultado para o usuário.
# print("Contador de palavras de arquivo")
# with open("notas.txt", "r") as arquivo:
#     conteudo = arquivo.read()
#     contagem = conteudo.count("Python")
#     print(f"A contagem de palavras {contagem} é de...")

# Execução de comandos do sistema
#import os # importa o módulo os para interagir com o sistema operacional 
# Onde estou?
# print(os.getcwd())
# Listar arquivos na pasta
# print(os.listdir())
# print(os.listdir("..")) # lista arquivos da pasta pai
# print(os.listdir("..\\..")) # lista arquivos da pasta vô
# print(os.listdir("C:\\")) # lista arquivos da raiz do C
# print(os.listdir("C:\\Users")) # lista arquivos da pasta Users
# print(os.listdir("C:\\Users\\Publico")) # lista arquivos da pasta Public

# Os outros comandos úteis:
# # Criar pasta
# os.mkdir("nova pasta")
# # Renomear pasta

# os.rename("nova pasta", "pasta_renomeada")
# # # Excluir pasta
# os.rmdir("pasta_renomeada")

# Exercicio 2:
# Crie um script que mostre o caminho da pasta atual
# print(os.getcwd())

# # Exercicio 3:

# # liste os arquivos da pasta atual.
# print(os.listdir())


# # Exercicio 4:
# # # Crie uma pasta chamada "projetos" e depois renomeie para "Meus_projetos". Por fim, exclua a pasta.
# os.mkdir("projetos")
# os.mkdir("projetos", "Meus_projetos")
# os.rmdir("Meus_projetos")

# Exercicio 5:
# # Crie uma arquivo chamado "log.txt" e escreva a mensagem "Log de atividades". Depois, leia o conteúdo do arquivo e exiba na tela.
# import os
# os.mkdir("log.txt")
# with open("log.txt", "w") as arquivo:
#      arquivo.write("Log de atividades")
# with open("log.txt", "r") as arquivo:
#      conteudo = arquivo.read()
#      print(conteudo)

# # Exemplo Dicionario
# # Crie um dicionario com informações sobre uma pessoa e acesse um valor usando uma chave.
# pessoa = { 
#     "nome": "Livia",
#     "idade": 16,
#     "Cidade": "São Paulo",
#     "profissão": "Cuidadora de Crianças"
# }
# pessoa2 = {
#     "nome": "Marcelo",
#     "idade": 16,
#     "Cidade": "São Paulo",
#     "profissão": "Baterista"
# }
# print(pessoa["profissão"])
# print(pessoa2["nome"], pessoa["idade"])

# spider man = {
#     "nome": "Peter Parker",
#      "idade": 17,
#      "Cidade": "NYC",
#      "profissão": "fotógrafo freelancer"
#  }
# spider man2 = {
#     "nome": "Miles Morales",
#      "idade": 15,
#      "Cidade": "NY",
#      "profissão": "estudante elite"
#  }
# spider man3 = {
#     "nome": "Ben Reilly",
#      "idade": 25,
#      "Cidade": "NewYork",
#      "profissão": "cientista/inventor."
#  }

# # Exemplo 2: Desligar o PC (comando para Windowns)
with open("desliga.bat", "w") as desligar:
    desligar.write("shutdown -s -t 3600 -c \"Desligando programado para daqui a 60 segundos. Salve seu trabalho!\"")
#      # -s comando para desligar
#      # -t tempo definir
#      # -a cancelar desligamento

# with open("desligar.bat", "r") as desligar:
