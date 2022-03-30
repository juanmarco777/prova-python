import pyxel

# Tamanho do tabuleiro
SIZE = 64

# Cores ligado/desligado
ON = pyxel.COLOR_RED
EDIT = pyxel.COLOR_YELLOW
OFF = pyxel.COLOR_BLACK


def jogo_pausado(i, j):
    """
    Atualiza o tabuleiro quando o jogo está pausado.

    A função recebe a posição atual do mouse no tabuleiro e
    pode matar ou reviver este ponto. As regras são simples:

    * matar_ponto(i, j), caso o botão esquerdo do mouse estiver pressionado
    * reviver_ponto(i, j), caso o botão direito do mouse estiver pressionado
    """
    # Implementar corretamente!
    matar_ponto(i, j)
    reviver_ponto(i, j)


def jogo_da_vida() -> list:
    """
    A função deve retornar uma lista com todos os pontos vivos
    da próxima geração. Os pontos são duplas no formato (i, j)
    com as coordenadas i e j no tabuleiro.

    As regras para calcular os pontos vivos na próxima geração
    dependem do número n de vizinhos vivos.

    * se n < 2, o ponto morre de solidão
    * se n = 2, o ponto fica do jeito que está
    * se n = 3, o ponto fica vivo, independentemente do estado anterior
    * se n > 3, o ponto morre de superpopulação

    Utilize a função n_vizinhos(i, j) para descobrir o número de vizinhos e implementar
    a lógica anterior em cada ponto no intervalo `i ∈ 0..63` e
    `j ∈ 0..63`
    """
    # Implementar corretamente!
    pontos = []
    pt = 20, 20
    pontos.append(pt)
    return pontos


def n_vizinhos(i, j):
    """
    Retorna o número de vizinhos vivos ao ponto (i, j).

    Utilize a função esta_vivo(x, y) para determinar se cada ponto
    (x, y) vizinho a (i, j) está vivo ou não.
    """
    # Implementar corretamente!
    return 2


#
# Daqui para baixo, não é necessário editar o código
#
def reviver_ponto(i, j):
    """
    Marca o ponto (i, j) como vivo.
    """
    pyxel.points.add((i, j))


def matar_ponto(i, j):
    """
    Marca o ponto (i, j) como morto.
    """

    pyxel.points.discard((i, j))


def esta_vivo(i, j):
    """
    Retorna True se o ponto i, j estiver vivo e Falso, caso contrário.

    Um ponto fora do tabuleiro será sempre considerado como morto
    """
    return (i, j) in pyxel.points


def init():
    """
    Inicializa o jogo
    """
    pyxel.pausado = True
    pyxel.points = set()
    pyxel.init(4 * SIZE, 4 * SIZE)
    pyxel.cls(OFF)


def update():
    """
    Atualiza um frame de jogo.
    """
    global pausado

    if pyxel.btnp(pyxel.KEY_SPACE):
        pyxel.pausado = not pyxel.pausado
    pyxel.mouse(pyxel.pausado)

    if pyxel.pausado:
        i, j = pyxel.mouse_x // 4, pyxel.mouse_y // 4
        jogo_pausado(i, j)
    elif pyxel.frame_count % 3 == 0:
        new = jogo_da_vida()
        pyxel.points.clear()
        pyxel.points.update(map(tuple, new))


def draw():
    """
    Desenha o tabuleiro.
    """
    pyxel.cls(OFF)
    if pyxel.frame_count // 10 % 2 == 0:
        pyxel.text(0, 0, "aperte espaco", pyxel.COLOR_WHITE)

    col = EDIT if pyxel.pausado else ON
    for x, y in pyxel.points:
        pyxel.rect(4 * x, 4 * y, 4, 4, col)


init()
pyxel.run(update, draw)
