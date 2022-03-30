# Instruções

1. A prova é individual e as respostas devem ser feitas no papel
2. Você deve resolver as questões no arquivo correspondente ao nome da questão.
3. Você pode utilizar o computador para testar os programas, mas não pode passar respostas para outros colegas. Quem passar ou receber respostas terá a prova imediatamente anulada.
4. Você pode utilizar um livro de referência ou a documentação do Python.

**Personalização pelo número de matrícula**
Algumas questões estão personalizadas pelo número de matrícula. Para resolvê-las
considere o número de matrícula dividido em 3 partes de 3 dígitos cada:

    18/1234567
    ^^^^---^^^
      A  B  C

No caso temos A=181, B=234 e C=567. Lembre destes três números quando fizer
suas questões pois a própria pergunta pode depender destes números.

**Medalhas e pontuação**

A pontuação de cada questão está entre parênteses ao lado do número. Por exemplo, para a Q1 temos `(print=1, num=2)`, que corresponde a 1 ponto na competência print e 2 na competência num. 

As questões resolvidas durante o período da prova valem o dobro da pontuação especificada. Além disso, o número de questões resolvidas corretamente determina quantas medalhas serão distribuídas pela prova segundo a tabela abaixo.

* 3 ou mais: 1 medalha
* 4, 5: 2 medalhas
* 6, 7: 3 medalhas
* 8+: 4 medalhas

A prova foi concebida com a expectativa de que cada aluno(a) consiga resolver em média 5 questões no período de avaliação.

As questões podem ser entregues fora do período de avaliação para contar pontos de competência, mas sem o bônus na pontuação. Estas questões podem ser entregues até o dia 06/04. 


## Questão 1  (print=1, num=2)

Crie um programa que imprime o resultado de A elevado a B na tela. 

Dica: Trata-se de um número potencialmente grande. 


## Questão 2  (for=1, reduce=2)

Crie um programa que some todos os números no intervalo do menor valor entre A, B e C até o maior valor entre eles. Você não pode utilizar a função sum!

Ex.: se A, B, C forem iguais à 1, 5, 2, respectivamente, o programa deve calcular 1 + 2 + 3 + 4 + 5 = 15.


## Questão 3  (while=2, list=1, seq=1, seq-gen=2)

A sequência de Collatz começa em um número arbitrário e termina no valor `1`. Calculamos cada termo em função do termo anterior utilizando a seguinte  fórmula:

    n -> n / 2    (se n for par)
         3*n + 1  (se n for ímpar)

* Pergunte o valor de "n" para o usuário e salve-o como uma variável inteira.
* Calcule a sequência de Collatz para esse número
* Calcule quantos termos possui a sequência obtida
* Também diga qual é o maior valor atingido nesta sequência.

Ex.: Se n=5, a sequência de Collatz seria [5, 16, 8, 4, 2, 1], contendo 6 termos, cujo maior item seria 16.


## Questão 4  (if=3)

Considere o código abaixo, que possui erros:

```python
A = ...  # Copie aqui o valor obtido da sua matrícula
B = ...  # Copie aqui o valor obtido da sua matrícula
C = ...  # Copie aqui o valor obtido da sua matrícula
minABC = min(A, B, C)  # menor valor entre A e B
maxABC = max(A, B, C)  # maior valor entre A e B

x = int(input("x: "))
if x == 0:
    print('nulo')
elif x == 42:
    print('resposta para *a* pergunta')
elif x > maxABC:
    print('grande')
if x < 0:
    print('negativo')
if minABC < x < maxABC:
    print('médio')
else:
    print('nada de especial')
```

A intenção do programa é imprimir somente uma mensagem, correspondendo à informação sobre a condição mais específica sobre o número x. A ultima condição do  "else" somente deveria ser executada se nenhuma outra mensagem tivesse sido mostrada. 

A condição mais específica corresponde àquela com o menor número de possibilidades. Condições sejam igualmente específicas devem ser 
testadas na mesma ordem que aparecem no programa original.

* Explique porque o código acima está incorreto. Na sua explicação, dê pelo menos um exemplo de como o programa falha e explique o motivo do bug aparecer.
* Modifique o programa para corrigir todos os erros 


## Questão 5 (for=2, while=2, loops=3)

O código abaixo calcula uma soma de valores que por um acaso é uma aproximação para a função `ln(1 - x)`. 

```python
x = float(input("x: "))
n = 0
resultado = 0.0
termo = 1.0

while x < 5:
    n = n + 1
    termo = termo * x
    resultado = resultado + termo / n

print(resultado)
```

Modifique o código acima para utilizar o laço "for" ao invés do while. Você pode aplicar simplificações, mas não pode utilizar o laço while em local nenhum da resposta. Certifique-se que o resultado do programa modificado é igual ao original.


## Questão 6  (dict=3, str=2)

A variável `dest` abaixo representa uma chave de criptografia.

```
orig = "abcdefghijklmnopqrstuvwxyz"
dest = "nvxkrgpszdeailyuhfbocqjmwt"
```

Para codificar a mesagem, convertemos a mesma para letras minúsculas e trocamos cada caracter em `orig` pelo caracter correspondente em `dest`.
Números, espaços e sinais de pontuação permanecem inalterados. Crie um programa que peça uma mensagem para o usuário e imprima a versão codificada da mesma.


## Questão 7  (recur=4)

O máximo divisor comum entre dois números x e y pode ser calculado por uma função recursiva utilizando a seguinte regra:

    mdc(x, 0) --> x
    mdc(x, y) --> mdc(y, x % y)

Crie uma função chamada mdc(x, y) que calcula o máximo divisor comum entre dois números.


## Questão 8  (loops=2, algo=3)

Desenhe alguma das figuras nos desafios 5, 7, 8, 19+ do livro tcbook.pdf sem tirar a caneta do papel (ou seja, sem utilizar as funções pu/penup ou pd/pendown.


## Questão 9

Nesta questão, vamos terminar a implementação do "Jogo da vida". Este é um jogo que simula a evolução de uma vida artificial.

A pontuação é avaliada de forma independente para a resolução correta de cada uma das funções incompletas no código do jogo:

* jogo_pausado(lib=2) 
* jogo_da_vida(if=2, bool=2, func=1)
* n_vizinhos(algo=2, loop=1, func=2)