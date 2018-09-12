def main():
    print("\nBem-vindo ao jogo do NIM! Escolha:\n")
    opcao = int(input("1 - Para jogar apenas uma partida \n2 - Para jogar um campeonato\n"))
    while opcao != 1 and opcao != 2:
        print("\nNúmero inválido, digite novamente!\n")
        opcao = int(input())
    if opcao == 1:
        print("\nVocê escolheu uma partida avulsa!\n")
        partida()
    elif opcao == 2:
        print("\nVocê escolheu um campeonato!\n")
        campeonato()

def computador_escolhe_jogada(n, m):
    if n <= m:
        return n
    else:
        jogada = n % (m + 1)
        if jogada > 0:
            return jogada

    return m
    

def usuario_escolhe_jogada(n, m):
    jogada = int(input("Quantas peças você vai tirar?\n"))
    while jogada > m or jogada <= 0:
        print("Oops! Jogada inválida! Tente de novo.")
        jogada = int(input())
    return jogada      

def partida():
    n = int(input("\nQuantas peças?\n"))
    m = int(input("\nLimite de peças por jogador?\n"))
    vezDoUsuario = False
    vezDoComputador = False
    usuarioGanhou = False
    computadorGanhou = False
    if n % (m + 1) == 0:
        print("\nVocê começa!\n")
        vezDoUsuario = True
    else:
        print("\nO computador começa!\n")
        vezDoComputador = True

    jogando = True

    while jogando:
        retiradasUsuario = 0
        retiradasComputador = 0
        if vezDoUsuario:
            while vezDoUsuario:
                retiradasUsuario = usuario_escolhe_jogada(n, m)
                n -= retiradasUsuario
                if retiradasUsuario == 1:
                    print("Você tirou uma peça.")
                else:
                    print("Você tirou", retiradasUsuario, "peças.")
                vezDoComputador = True
                vezDoUsuario = False
                if n == 0:
                    usuarioGanhou = True
                
        elif vezDoComputador:
            while vezDoComputador:
                retiradasComputador = computador_escolhe_jogada(n, m)
                n -= retiradasComputador
                if retiradasComputador == 1:
                    print("O computador tirou uma peça.")
                else:
                    print("O computador tirou", retiradasComputador, "peças.")
                vezDoComputador = False
                vezDoUsuario = True
                if n == 0:
                    computadorGanhou = True
            
            
        if n == 1:
            print("Agora resta apenas uma peça no tabuleiro.\n")
        else:
            print("Agora restam", n, "peças no tabuleiro.\n")
            
        if usuarioGanhou:
            print("Você ganhou!")
            jogando = False
        elif computadorGanhou:
            print("O computador ganhou!")
            jogando = False


def campeonato():
    usuario = 0
    computador = 0
    rodadas = 1
    while rodadas <= 3:
        print("\n**** Rodada", rodadas, "****\n")
        partida()
        rodadas += 1
        computador += 1
    print("\n****Fim do campeonato****")
    print("\nPlacar: Você", usuario, "X", computador, "Computador")

main()
    





    

