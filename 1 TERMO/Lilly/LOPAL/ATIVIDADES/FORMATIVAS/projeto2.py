# Sistema de Elevador de Prédio
# O prédio possui 10 andares, sendo o térreo o andar 0. O elevador pode se mover para cima ou para baixo, e tem a capacidade de transportar até 5 pessoas.
# O elevador começa no andar 0 e pode ser chamado por qualquer pessoa em qualquer andar.
# O elevador deve se mover para o andar onde a pessoa chamou, e depois para o andar destino da pessoa.
# O elevador deve exibir mensagens indicando o andar atual, o número de pessoas no elevador, e as ações realizadas (subindo, descendo, parando). O programa deve continuar rodando até que o usuário decida encerrar.

while True:

    andar_atual = 0
    try:
  
        print("Bem-vindo ao elevador Lilly's")
        print("Antes de entrar certifique-se de que o chão está alinhado!")
        print("O elevador tem a capacidade de transportar apenas 5 pessoas!")
        # print("Andares: \n 1° andar \n 2° andar \n 3° andar \n 4° andar \n 5° andar \n 6° andar \n 7° andar \n 8° andar \n 9° andar \n 10° andar")

        # andar_usuario = print(f"Andar atual do Elevador {andar_atual}")
        Andar = int(input("Aperte o botão de acordo com o andar que deseja ir (0-10): "))
        if Andar < 0 or Andar > 10:
            raise ValueError("Andar inválido. Por favor, digite um número de 0 a 10.")

        print(f"Elevador se movendo do andar {andar_atual} para o andar {Andar}...")
        andar_atual = Andar 
        print(f"Chegamos ao seu destino {andar_atual}!")
            
        if input("Deseja escolher outro andar? (s/n)").lower() != 's':
            print("Obrigado por usar nosso Elevador lilly's! Até a proxima vinda!")
            break
        for listagem in range(10):
            print(f"Andar {listagem} - {'[X]' if listagem == andar_atual else '[ ]'}")
    except ValueError as erro:
        print(f"Error: {erro}. Tente novamente")
    except Exception as e:
        print(f"Ocorreu um error inesperado! {e}. Tente novamente!")
        print("Programa encerrado. Até mais!") 
        break