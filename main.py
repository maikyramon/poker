import cards
import player

print("bem vindo a simulacao de poker kkk")
print("nosso projeto visa criar um jogador de poker que calcula a jogada na sua mão.")
print("usamos como base o estilo Texas Hold'em.")
print("ainda não levamos em conta dados como valor de apostas e etc, apenas os turns e as mãos de cada jogador.")

print("vamos começar com uma partida simples")

s = 's'
while s == 's':
    num_players = 0
    while num_players < 2 or num_players > 10:
        print("Informe o número de jogadores que irão jogar (2-10): ")
        num_players = int(input())

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
    input("aperte enter para o turn")

    deck = deck[:-1]  # deck sem a ultima carta
    table_cards.append(deck.pop(len(deck)-1))

    print(table_cards[0] + ' ' + table_cards[1] + ' ' + table_cards[2] + ' ' + table_cards[3])

    input("aperte enter para o river")

    deck = deck[:-1]  # deck sem a ultima carta
    table_cards.append(deck.pop(len(deck)-1))

    print(table_cards[0] + ' ' + table_cards[1] + ' ' + table_cards[2] + ' ' + table_cards[3] + ' ' + table_cards[4])

    print("cartas dos " + str(num_players) + " jogadores: ")

    i = 0
    while i < num_players:
        print("jogador " + str(i+1) + ": " + players[i].hand[0] + ' ' + players[i].hand[1] + ' ' +
              cards.showdown(players[i].hand, table_cards, i))
        i += 1

    print("Deseja jogar novamente? ")
    s = input()
