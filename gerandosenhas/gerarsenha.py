from random import randint
caracteres = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "!", "@", "#", "$", "%", "&", "*", "-", "_"]
print("=" * 30)
print("\tGerador de Senhas")
print("=" * 30)
while True:
    try:
        tamanho_senha = int(input("Qual o tamanho da senha que deseja gerar? "))
    except TypeError:
        print("Houve problemas quanto a tipo de dado fornecido. Escreva novamente!")
    else:
        print("=" * 30)
        print("A senha gerada foi: ", end="")
        digitos_senha = ""
        for c in range(0, tamanho_senha):
            digitos_senha += str(caracteres[randint(0, len(caracteres)-1)])
        print(digitos_senha)
        while True:
            try:
                salvar = str(input("Deseja salvar a senha em bloco de notas (S/N)? ")).strip().upper()
                while True:
                    if salvar != "S" or salvar != "SIM":
                        salvar = str(input("Resposta inválida. Digite (S/N) se deseja ou não salvar a senha em bloco de notas: ")).strip().upper()
                    else:
                        break
            except TypeError:
                print("Houve problemas quanto a tipo de dado fornecido. Escreva novamente!")
            else:
                print("Senha salva no bloco de notas com nome de: senha.txt")
                arquivo = open("senha.txt", "w")
                for c in range(0, tamanho_senha):
                    arquivo.write(digitos_senha[c])
                break
    break