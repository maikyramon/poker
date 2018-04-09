import random
import jogadas

import Card


cards = ['♠A', '♠2', '♠3', '♠4', '♠5', '♠6', '♠7', '♠8', '♠9', '♠10', '♠J', '♠Q', '♠K',
         '♥A', '♥2', '♥3', '♥4', '♥5', '♥6', '♥7', '♥8', '♥9', '♥10', '♥J', '♥Q', '♥K',
         '♣A', '♣2', '♣3', '♣4', '♣5', '♣6', '♣7', '♣8', '♣9', '♣10', '♣J', '♣Q', '♣K',
         '♦A', '♦2', '♦3', '♦4', '♦5', '♦6', '♦7', '♦8', '♦9', '♦10', '♦J', '♦Q', '♦K']


def shuffle():
    deck = []
    while len(deck) < 52:
        rand_card = cards[random.randint(0, 51)]

        if not any(rand_card in c for c in deck):
            deck.append(rand_card)

    return deck


def best_cards(hand, table, player):
    h = []
    i = 0

    while i < len(hand):
        h.append(hand[i])
        i += 1

    i = 0
    while i < len(table):
        h.append(table[i])
        i += 1

    h = ['♣6', '♣7', '♦10', '♦J', '♦Q', '♦K', '♦A']

    if jogadas.royal_straight_flush(h):
        print('PLAYER {0} FEZ UM ROYAL STRAIGHT FLUSH!!'.format(str(player)))
        return
    p = jogadas.straight_flush(h)
    if p > 0:
        print('PLAYER {0} FEZ UM STRAIGHT FLUSH!!'.format(str(player)))
        return
    p = jogadas.flush(h)
    if p > 0:
        print('PLAYER {0} FEZ UM FLUSH!!'.format(str(player)))
        return
    p = jogadas.straight(h)
    if p > 0:
        print('PLAYER {0} FEZ UMA SEQUÊNCIA!!'.format(str(player)))
        return
    p = jogadas.four(h)
    if p > 0:
        print('PLAYER {0} FEZ UMA QUADRA!!'.format(str(player)))
        return
    p = jogadas.full_house(h)
    if p > 0:
        print('PLAYER {0} FEZ UM FULL HOUSE!!'.format(str(player)))
        return
    p = jogadas.three(h)
    if p > 0:
        print('PLAYER {0} FEZ UMA TRINCA!!'.format(str(player)))
        return
    p = jogadas.two_pairs(h)
    if p > 0:
        print('PLAYER {0} FEZ DOIS PARES!!'.format(str(player)))
        return
    p = jogadas.pair(h)
    if p > 0:
        print('PLAYER {0} FEZ UM PAR!!'.format(str(player)))
        return


    print(p)

    del h[5:6]

    h.sort()

    return h
