import collections
import Card


def suit(card):
    return{
        '♠': 0,
        '♥': 1,
        '♣': 2,
        '♦': 3
    }.get(card)


def sort_hand(hand):
    h = []
    i = 0

    while i < len(hand):
        c = {'J': 11, 'Q': 12, 'K': 13, 'A': 14}.get(hand[i][1], 0)

        if c < 11:
            c = int(hand[i][1])

            if c == 1:
                c = 10

        h.append(Card.Card(hand[i][0], c))
        i += 1

    h = sorted(h, key=Card.Card.get_value, reverse=True)

    return h


def flush(hand):
    i = 0
    suits = [0, 0, 0, 0]
    while i < len(hand):
        suits[suit(hand[i].get_suit())] += 1
        i += 1

    return max(suits) >= 5


def straight(h):
    i = 0
    seq = []

    while i < len(h):
        if i > 0:
            if (h[i-1].get_value() - h[i].get_value() == 1) or (h[i-1].get_value() == 14 and h[i].get_value() == 2):
                if i == 1:
                    seq.append(h[0])
                    seq.append(h[1])
                else:
                    seq.append(h[i])
            else:
                seq.clear()

        i += 1
        if len(seq) > 4:
            break

    if len(seq) > 4:
        if flush(seq):
            return [1, seq[0]]
        else:
            return [0, seq[0]]
    else:
        return 0


def three(hand):
    if count_duplicates(hand)[1] == 3:
        return count_duplicates(hand)[0]
    else:
        return 0


def four(hand):
    if count_duplicates(hand)[1] == 4:
        return count_duplicates(hand)[0]
    else:
        return 0


def pair(hand):
    c = count_duplicates(hand, 1)
    if c[0][0] > 0:
        return c[0][0]
    else:
        return 0


def two_pairs(hand):
    h = count_duplicates(hand, 2)

    if h[0][1] == 2 and h[1][1] == 2:
        return h


def count_duplicates(hand, n):
    h = sort_hand(hand)
    count = collections.Counter(h)
    return count.most_common(n)


def full_house(hand):
    fh = [three(hand), pair(hand)]
    if fh[0] > 0 and fh[1] > 0:
        return fh
    else:
        return []


def straight_flush(hand):
    i = straight(hand)
    if flush(hand) and i > 0:
        return i
    else:
        return 0


def royal_straight_flush(hand):
    h = sort_hand(hand)
    i = straight(h)
    return i[0] > 0 and (h[len(h)] == 14)