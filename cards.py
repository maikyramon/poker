import random
import jogadas


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


def showdown(hand, table, player):
    h = []
    i = 0

    while i < len(hand):
        h.append(hand[i])
        i += 1

    i = 0
    while i < len(table):
        h.append(table[i])
        i += 1

    player += 1

    if jogadas.royal_straight_flush(h):
        return 'PLAYER {0} FEZ UM ROYAL STRAIGHT FLUSH!!'.format(str(player))

    if jogadas.straight_flush(h):
        return 'PLAYER {0} FEZ UM STRAIGHT FLUSH!!'.format(str(player))

    p = jogadas.flush(h)
    if p > 0:
        return 'PLAYER {0} FEZ UM FLUSH!!'.format(str(player))

    p = jogadas.straight(h)
    if p > 0:
        return 'PLAYER {0} FEZ UMA SEQUÊNCIA!!'.format(str(player))

    p = jogadas.four(h)
    if p > 0:
        return 'PLAYER {0} FEZ UMA QUADRA!!'.format(str(player))

    p = jogadas.full_house(h)
    if len(p) > 0:
        return 'PLAYER {0} FEZ UM FULL HOUSE!!'.format(str(player))

    p = jogadas.three(h, 1)
    if p > 0:
        return 'PLAYER {0} FEZ UMA TRINCA!!'.format(str(player))

    p = jogadas.two_pairs(h)
    if len(p) > 0:
        return 'PLAYER {0} FEZ DOIS PARES!'.format(str(player))

    p = jogadas.pair(h, 1)
    if p > 0:
        return 'PLAYER {0} FEZ UM PAR!'.format(str(player))

    return 'PLAYER {0} NÃO FEZ NADA!'.format(str(player))