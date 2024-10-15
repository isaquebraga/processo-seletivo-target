"""
1) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

IMPORTANTE: Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;
"""

# Função recursiva que verifica se o número n pertence à sequência de Fibonacci
def fib(number, a=0, b=1):
    return number == a or (number > a and fib(number, b, a + b))

# Solicita ao usuário que insira um número e verifica se o número pertence à sequência de Fibonacci e imprime a mensagem adequada
number = int(input("Número: "))
print(f"O número {number} pertence à Fibonacci." if fib(number) else f"O número {number} não pertence à Fibonacci.")
