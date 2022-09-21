from random import randint
caracteres = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "!", "@", "#", "$", "%", "&", "*", "-", "_"]
print("\033[1;33m=\033[m" * 30)
print("\t\033[1;33mGerador de Senhas\033[m")
print("\033[1;33m=\033[m" * 30)
while True:
    try:
        tamanho_senha = int(input("Qual o tamanho [em caracteres] da senha que deseja gerar? "))
    except TypeError:
        print("\033[1;31mHouve problemas quanto a tipo de dado fornecido. Escreva novamente!\033[m")
    else:
        print("=" * 30)
        print("A senha gerada foi: ", end="")
        digitos_senha = ""
        for c in range(0, tamanho_senha):
            digitos_senha += str(caracteres[randint(0, len(caracteres)-1)])
        print(digitos_senha)
        while True:
            try:
                salvar = str(input("\033[1;36mDeseja salvar a senha em um bloco de notas (S/N)? \033[m")).strip().upper()
                while True:
                    if salvar == "S" or salvar == "SIM":
                        break
                    salvar = str(input("\033[1;31mResposta inválida. Digite (S/N) se deseja ou não salvar a senha em bloco de notas: \033[m")).strip().upper()
            except TypeError:
                print("\033[1;31mHouve problemas quanto a tipo de dado fornecido. Escreva novamente!\033[m")
            else:
                print("\033[32mSenha salva no bloco de notas com nome de:\033[m \033[1;4;34msenha.txt\033[m")
                arquivo = open("senha.txt", "w")
                arquivo.write("Senha gerada: ")
                for c in range(0, tamanho_senha):
                    arquivo.write(digitos_senha[c])
                break
    break