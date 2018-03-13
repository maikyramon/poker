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

    deck = cards.shuffle()
    
    players = []
    player_cards = []

    while len(players) < num_players:
        players.append(player.Player([]))

    j = 0
    while j < 2:
        i = 0
        while i < num_players:
            card = deck.pop(len(deck)-1)
            player_cards.append(card)
            players[i].hand.append(card)
            deck = deck[:-1]  # deck sem a ultima carta
            i += 1
        j += 1

    table_cards = []
    deck = deck[:-1]  # deck sem a ultima carta

    while len(table_cards) < 3:
        table_cards.append(deck.pop(len(deck)-1))
        deck = deck[:-1]  # deck sem a ultima carta
    
    print("flop foi lançado!")
    print("segue as cartas em mesa: ")
    
    print(table_cards[0] + ' ' + table_cards[1] + ' ' + table_cards[2])
    
    print("deseja virar mais uma carta?")
    input("aperte enter para virar o turn")

    deck = deck[:-1]  # deck sem a ultima carta
    table_cards.append(deck.pop(len(deck)-1))

    print(table_cards[3])
    print("segue as cartas em mesa:")
    print(table_cards[0] + ' ' + table_cards[1] + ' ' + table_cards[2] + ' ' + table_cards[3])

    input("aperte enter para o river")

    deck = deck[:-1]  # deck sem a ultima carta
    table_cards.append(deck.pop(len(deck)-1))

    print(table_cards[4])
    print("segue as cartas em mesa:")
    print(table_cards[0] + ' ' + table_cards[1] + ' ' + table_cards[2] + ' ' + table_cards[3] + ' ' + table_cards[4])

    print("cartas dos " + str(num_players) + " jogadores: ")

    i = 0
    while i < num_players:
        print("jogador " + str(i+1) + ": " + players[i].hand[0] + ' ' + players[i].hand[1])
        i += 1
