"""
Explique no comentário porque o código do exemplo estava incorreto:





"""

# Substitua os valores de A, B e C e modifique o código para corrigir
# os erros
A = ...
B = ...
C = ...
minABC = min(A, B, C)
maxABC = max(A, B, C)

x = int(input("x: "))
if x == 0:
    print("nulo")
elif x == 42:
    print("resposta para *a* pergunta")
elif x > maxABC:
    print("grande")
if x < 0:
    print("negativo")
if minABC < x < maxABC:
    print("médio")
else:
    print("nada de especial")
