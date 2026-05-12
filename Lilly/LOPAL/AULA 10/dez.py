# Projeto 1:
# Projeto: Precisamos de um algoritmo para gerenciamento de cancelas para um shopping.
# Toda entrada e saída irá ser sinalizada
# Valores para entrada e permanência do veículo deverá ser pergutado
# As entrada deverão ser registradas por placa.
#
# Passo 1:  
# Perguntar informações sobre o veiculo ou forma acesso
# Pressionar o botao para emitir ticket
# Verificar se possui TAG para acesso liberado
# Se possuir erros informar ao usuário

# Passo 2:
# Verificar tempo de permanência
# Valor a ser cobrado

# Passo 3:
# Saída como será?
# Calcular tempo de permanência
# Se for TAG gerar na fatura da TAG
# Pagar ticket
# Devolver ticket na saída

# Passo 4:
# Gerar relatório de entradas e saídas
# Tratamento de Erros
# Revisão do código


print("Bem-vindo ao estacionamento do Shopping lilly's")
informações = int(input("Qual sua marca e placa do carro"))
acesso = input("Como deseja seu acesso?")
if acesso == "TAG":
    print("Acesso liberado!")
elif acesso == "Ticket":
    print("Aperte o botão para emitir o ticket!")
elif acesso == "Intefone":
    print("Estamos lhe encaminhando para a ligação!")
else:
    print("Error! Tente novamente.")

# 　ﾟ･｡･ﾟ　ﾟ･｡･ﾟ　ﾟ･｡･ﾟ　ﾟ･｡･ﾟ　ﾟ･｡･ﾟ　ﾟ･｡･ﾟ　ﾟ･｡･ﾟ
tempo = input("Qual foi seu tempo de permanência?")
preço = 4# $ por hora
total == tempo * 4


for saída in acesso:
    if acesso == "Ticket":
        print("Você deve pagar {total}")
    elif acesso == "TAG":
        print("")