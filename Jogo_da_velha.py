import itertools

def exibe_tabuleiro(tab):
    print('\n'.join([' | '.join(linha) for linha in tab]))
    print()

def verifica_vitoria(tab):
    linhas = tab + list(zip(*tab))
    diag1 = [tab[i][i] for i in range(3)]
    diag2 = [tab[i][2 - i] for i in range(3)]
    for seq in linhas + [diag1, diag2]:
        if seq.count(seq[0]) == 3 and seq[0] != ' ':
            return seq[0]
    return None

def jogo_da_velha():
    tabuleiro = [['']*3 for _ in range(3)]
    jogadores = itertools.cycle(['X', 'O'])
    movimentos = 0

    while True:
        jogador = next(jogadores)
        exibe_tabuleiro(tabuleiro)
        try:
            x, y = map(int, input(f'Jogador {jogador}, digite linha e coluna (0-2): ').split())
            assert tabuleiro[x][y] == ''
        except (ValueError, AssertionError, IndexError):
            print('Movimento Inválido. Tente novamente.')
            continue

        tabuleiro[x][y] = jogador
        movimentos += 1

        vencedor = verifica_vitoria(tabuleiro)
        if vencedor:
            exibe_tabuleiro(tabuleiro)
            print(f'Jogador {vencedor} venceu!')
            break
        if movimentos == 9:
            exibe_tabuleiro(tabuleiro)
            print('Empate!')
            break

if __name__ == '__main__':
    jogo_da_velha()