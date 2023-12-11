from functools import cmp_to_key

h0 = open("day7_data.txt")
#h0 = open("day7_ex.txt")

l0 = [n.strip() if n.strip() else None for n in h0.readlines()]

PT1_CARDS = ("A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2")
PT2_CARDS = ("A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J")

def parse(l0):
    hands = [x.split(" ")[0] for x in l0]
    bids = [int(x.split(" ")[1]) for x in l0]
    hbs = list(zip(hands, bids))
    return hbs

def pt2(l0):
    solve(l0, winner_pt2)

def pt1(l0):
    solve(l0, winner_pt1)

def solve(l0, fcmp):
    hbs = parse(l0)
    ranked = sorted(hbs, key=cmp_to_key(fcmp), reverse=True)
    print(ranked)
    score = 0
    for idx, h0 in enumerate(ranked):
        score += (h0[1] * (idx+1))
    print(score)

def winner_pt2(lc,rc):
    l, r = lc[0], rc[0]
    hl, hr = htype_pt2(l), htype_pt2(r)
    if l==r:
        return 0
    elif hl > hr:
        return -1
    elif hl < hr:
        return 1
    else:
        for idx in range(5):
            if PT2_CARDS.index(l[idx]) > PT2_CARDS.index(r[idx]):
                return 1
            elif PT2_CARDS.index(l[idx]) < PT2_CARDS.index(r[idx]):
                return -1

def winner_pt1(lc,rc):
    l, r = lc[0], rc[0]
    hl, hr = htype(l), htype(r)
    if l==r:
        return 0
    elif hl > hr:
        return -1
    elif hl < hr:
        return 1
    else:
        for idx in range(5):
            if PT1_CARDS.index(l[idx]) > PT1_CARDS.index(r[idx]):
                return 1
            elif PT1_CARDS.index(l[idx]) < PT1_CARDS.index(r[idx]):
                return -1

def htype_pt2(hand):
    t0 = tuple(hand)
    s0 = set(t0)

    type0 = htype(hand)

    if 'J' in s0:
        s0.remove("J")
        for card in s0:
            type1 = htype([card if x=='J' else x for x in t0])
            type0 = max(type0, type1)
    return type0


def htype(hand):
    if len(hand)!=5:
        raise RuntimeError("Bad hand")
    t0 = tuple(hand)
    s0 = set(t0)
    if len(s0) == 1:
        return 6 #5 of a kind
    elif len(s0) == 5:
        return 0 # jack s***
    elif len(s0) == 4:
        return 1 # one pair 
    elif len(s0) == 2:
        if t0.count(t0[0]) in (2,3):
            return 4 #full house
        else:
            return 5 #4 of a kind
    elif len(s0) == 3:
        mx = max([t0.count(x) for x in t0])
        if mx==2:
            return 2 #two pair
        else:
            return 3 #3 of a kind

def test():
    assert htype("AAAAA") == 6
    assert htype("AAAA8") == 5
    assert htype("8AAAA") == 5
    assert htype("8AAA8") == 4
    assert htype("88AA8") == 4
    assert htype("23332") == 4
    assert htype("TTT98") == 3
    assert htype("23432") == 2
    assert htype("A23A4") == 1
    assert htype("23456") == 0

    assert winner_pt1(("AAAAA",0), ("AAAA8",0)) == -1
    assert winner_pt1(("AAAA8",0), ("AAAAA",0)) == 1
    assert winner_pt1(("AAAAA",0), ("AAAAA",0)) == 0
    assert winner_pt1(("8AAA8",0), ("88AA8",0)) == -1
    assert winner_pt1(("TTT98",0), ("23432",0)) == -1

    assert htype_pt2("QJJQ2") == 5
    assert htype_pt2("T55J5") == 5
    assert htype_pt2("KTJJT") == 5
    assert htype_pt2("QQQJA") == 5
    
    print("Tests OK")

test()
#pt1(l0)
pt2(l0)
