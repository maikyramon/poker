import cards
import player
import random

print("bem vindo a simulacao de poker kkk")
print("nosso projeto visa criar um jogador de poker que calcula a porcentagem de sua mão ser a melhor.")
print("usamos como base o estilo Texas Hold'em.")
print("ainda não levamos em conta dados como valor de apostas e etc, apenas os turns e as mãos de cada jogador.")

cmd = input('vamos começar? digite s para começar ou n para sair: ')

if cmd == 's':

    num_players = int(input(
            "vamos começar com uma partida simples, informe o número de jogadores que irão jogar com o robô (1-4): "))
    
    while num_players == 0 or num_players > 5:
        num_players = input(
            "Informe o número de jogadores que irão jogar com o robô (1-4): ")
    
    
    deck = cards.shuffle();
    
    players = []
    player_cards = []
    hand = []
    
    while len(players) < num_players+1:
        while len(hand) < 2:
            card = random.randint(0, 51)
    
            while card in player_cards:
                card = random.randint(0, 51)
    
            player_cards.append(card)
            hand.append(cards.cards[card])
    
        if len(players) == num_players:
            robot = player.Player(hand)
            players.append(robot)
        else:
            players.append(player.Player(hand))
    
        hand = []
    
    print("as cartas foram dadas! as cartas do robo são as seguintes: ")
    print(str(robot.hand[0]) + ' ' + str(robot.hand[1]));
    
    
    table_cards = []
    discard_cards = []
    while len(table_cards) < 5:
        card = random.randint(0, 51)
    
        while (card in player_cards) or (card in table_cards):
            card = random.randint(0, 51)
    
        table_cards.append(cards.cards[card])
    
    print("a primeira rodada de 3 cartas foi lançada!")
    print("segue as cartas em mesa: ")
    
    print(table_cards[0] + ' ' + table_cards[1] + ' ' + table_cards[2])
    
    print("deseja virar mais uma carta?")
