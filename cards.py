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


def best_cards(hand, table):
    h = []
    i = 0

    while i < len(hand):
        h.append(hand[i][1:])
        i += 1

    i = 0
    while i < len(table):
        h.append(table[i][1:])
        i += 1

    p = jogadas.pair(h)

    print(p)

    del h[5:6]

    h.sort()

    return h
