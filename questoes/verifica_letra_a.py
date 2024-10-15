"""
2) Escreva um programa que verifique, em uma string, a existência da letra "a", seja maiúscula ou minúscula, além de informar a quantidade de vezes em que ela ocorre.
"""

# Solicita ao usuário que insira uma string
string = input("Digite uma string: ")

# Converte a string para letras minúsculas e conta quantas vezes a letra 'a' aparece
print(f"'a' encontrado {string.lower().count('a')} vezes.")