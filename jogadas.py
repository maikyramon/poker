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


def has_flush(hand):
    i = 0
    suits = [0, 0, 0, 0]
    while i < len(hand):
        suits[suit(hand[i].get_suit())] += 1
        i += 1

    return max(suits) >= 5


def has_straight(h):
    i = 0
    seq = []

    while i < len(h):
        if i > 0:
            if (h[i-1].get_value() - h[i].get_value() == 1) or (h[0].get_value() == 14 and h[i].get_value() == 2):
                if len(seq) == 0:
                    seq.append(h[i-1])
                    seq.append(h[i])
                else:
                    seq.append(h[i])

                if h[0].get_value() == 14 and h[i].get_value() == 2:
                    seq.append(h[0])
            else:
                seq.clear()

        i += 1
        if len(seq) > 4:
            break

    if len(seq) > 4:
        if has_flush(seq):
            return [1, seq[4]]
        else:
            return [0, seq[4]]
    else:
        return []


def pair(hand, n):
    c = count_duplicates(hand, n)
    if len(c) > 0:
        if c[0][1] == 2:
            return c[0][0]
        elif n == 2 and c[1][1] == 2:
            return c[1][0]
        else:
            return 0


def three(hand, n):
    c = count_duplicates(hand, n)
    if len(c) > 0:
        if c[0][1] == 3:
            return c[0][0]
        elif n == 2 and c[1][1] == 3:
            return c[1][0]
        else:
            return 0


def four(hand):
    c = count_duplicates(hand, 1)
    if len(c) > 0:
        if c[0][1] == 4:
            return c[0][0]
        else:
            return 0


def two_pairs(hand):
    c = count_duplicates(hand, 2)
    if len(c) > 1 and (c[0][1] == 2 and c[1][1] == 2):
        return [c[0][0], c[1][0]]
    else:
        return []


def return_values(hand):
    h = []
    i = 0

    while i < len(hand):
        h.append(hand[i].get_value())
        i += 1

    return h


def count_duplicates(hand, n):
    h = sort_hand(hand)
    h = return_values(h)
    count = collections.Counter(h)
    return count.most_common(n)


def full_house(hand):
    fh = [three(hand, 2), pair(hand, 2)]
    if fh[0] > 0 and fh[1] > 0:
        return fh
    else:
        return []


def straight_flush(hand):
    h = sort_hand(hand)
    i = has_straight(h)
    if len(i) > 0 and i[0] > 0:
        return i[1].get_value()
    else:
        return 0


def royal_straight_flush(hand):
    h = sort_hand(hand)
    i = has_straight(h)
    if len(i) > 0:
        return i[0] > 0 and (i[1].get_value() == 10)
    else:
        return False


def flush(hand):
    h = sort_hand(hand)
    if has_flush(h):
        return h[0].get_value()
    else:
        return 0


def straight(hand):
    h = sort_hand(hand)
    i = has_straight(h)
    if len(i) > 0:
        return i[1].get_value()
    else:
        return 0


def higher_card(hand):
    h = sort_hand(hand)

    return h[0].get_value()
