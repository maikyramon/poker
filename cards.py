import random

cards = ['eA', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8', 'e9', 'e10', 'eJ', 'eQ', 'eK',
         'cA', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 'c9', 'c10', 'cJ', 'cQ', 'cK',
         'pA', 'p2', 'p3', 'p4', 'p5', 'p6', 'p7', 'p8', 'p9', 'p10', 'pJ', 'pQ', 'pK',
         'oA', 'o2', 'o3', 'o4', 'o5', 'o6', 'o7', 'o8', 'o9', 'o10', 'oJ', 'oQ', 'oK']


def shuffle():
    deck = []
    while len(deck) < 52:
        rand_card = cards[random.randint(0, 51)]

        if not any(rand_card in c for c in deck):
            deck.append(rand_card)

    return deck
