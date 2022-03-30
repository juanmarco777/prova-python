# Implementação original do código na q5.
#
# Não modifique! O arquivo existe apenas para facilitar
# a comparação com o código da resposta na q5.py

x = float(input("x: "))
n = 0
resultado = 0.0
termo = 1.0

while x < 5:
    n = n + 1
    termo = termo * x
    resultado = resultado + termo / n

print(resultado)
