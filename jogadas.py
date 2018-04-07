import collections


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
        c = {'J': 11, 'Q': 12, 'K': 13, 'A': 14}.get(hand[i][0], 0)

        if c < 11:
            c = int(hand[i][0])

            if c == 0:
                c = 10

        h.append(c)
        i += 1

    h.sort(reverse=True)

    return h


def flush(hand):
    i = 0
    seq = [0, 0, 0, 0, 0]
    while i < len(hand):
        seq[suit(hand[i][0])] += 1

    if max(seq) >= 5:
        return True


def sequence(hand):
    h = sort_hand(hand)
    i = 0
    seq = []

    while i < len(h):
        if i > 0:
            if (h[i-1] - h[i] == 1) or (h[i-1] == 14 and h[i] == 2):
                if i == 1:
                    seq.append(h[0])
                    seq.append(h[1])
                else:
                    seq.append(h[i])

        return len(seq) > 4


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
    return three(hand) and pair(hand)


def straight_flush(hand):
    return flush(hand) and sequence(hand)


def royal_straight_flush(hand):
    h = sort_hand(hand)
    return flush(hand) and sequence(hand) and (h[len(h)] == 14)
