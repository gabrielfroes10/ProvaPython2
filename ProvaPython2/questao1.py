def eh_palindromo(frase):

    frase = frase.replace(" ", "").lower()

    return frase == frase[::-1]

entrada = input("Digite uma palavra ou frase: ")

if entrada.strip() == "":
    print("Entrada inválida! Por favor, insira uma palavra ou frase")
else:
    if eh_palindromo(entrada):
        print(f'"{entrada}" é um palindromo.')
    else:
        print(f'"{entrada}" não é um palindromo')

