# Projeto de Revisão: Sistema de Empréstimo "Biblioteca Digital"

# Contexto: Você foi contratado para desenvolver o módulo de validação de
# empréstimos de livros de uma biblioteca comunitária. O sistema precisa coletar os dados
# do usuário, do livro e decidir se o empréstimo será aprovado, negado ou se haverá
# cobrança de taxa de segurança.

# Regras de Negócio (O que o sistema deve fazer):

# 1. Classificação do Usuário: A biblioteca atende [1] Alunos e [2] Comunidade
# Geral.

# 2. Limite de Dias: * Alunos podem ficar com o livro por até 14 dias de graça.
# ○ A Comunidade Geral pode ficar por até 7 dias de graça.

# 3. Taxa de Renovação: Se o usuário quiser ficar mais tempo do que o limite do seu
# perfil, será cobrada uma taxa fixa de R$ 5,00 por dia adicional.

# 4. Restrição de Categoria: Livros da categoria "Raros" não podem ser emprestados
# para a Comunidade Geral, apenas para Alunos.

# print("Bem-Vindo a biblioteca Lilly's")
# usuario = input("Qual o seu usuário?:")
# for login in usuario:
#   if usuario == "comunidade":
#      print(Poderá apenas )
     
     
# livros = input("Qual livro deseja pegar?:")
# raro = input("O livro desejado tem alguma raridade?:")
# if livros == raro:
#     print("")
# data = int(input("Por quantos dias deseja fazer o emprestimo"))


# import tkinter as tk
# from tkinter import messagebox, ttk

# def janela_bemvindo():
#     nome = nome_usuario.get()
#     livro = livro_usuario.get()



#     if nome ==  "":
#         messagebox.showwarning("Aviso", "Digite o login:")
#     else:
#         messagebox.showinfo("Bem-Vindo a Biblioteca Lilly's")

# def segunda_janela():
#     segunda_janela = tk.Toplevel(janela)
#     segunda_janela.tilte("Biblioteca Comunitária Lilly's")
#     segunda_janela.geometry("300x300")
  
#     if livro == "":
#         messagebox.showwarning("Cuidado. Caso o livro seja da categoria 'Raros',não será possivel emprestar a Comunidade Geral, apenas para Alunos.")

#     else:
#         messagebox.showinfo("")

# janela = tk.Tk()
# janela.title("Exemplo 2")
# janela.geometry("300x300")
# janela.configure(bg="maroon")


# lbl_mensagem = tk.Label(janela, text="Digite o nome:")
# lbl_mensagem.grid(row=0, column=0, pady=10, padx=10)
# lbl_livro = tk.Label(janela, text="Digite o livro desejado:")
# lbl_livro.grid(row=1, column=0, pady=10, padx=10)


# nome_usuario = tk.Entry(janela, font=("Arial", 12))
# nome_usuario.grid(row=0, column=1, pady=10, padx=10)
# livro_usuario = tk.Entry(janela, font=("Arial", 12))
# livro_usuario.grid(row=1, column=1, pady=10, padx=10)



# btn_segunda_janela = tk.Button(janela, text="Enter", command=segunda_janela)
# btn_segunda_janela.grid(row=3, column=0, pady=10, padx=10)

# # Rodar interface
# janela.mainloop()
