from math import ceil
ex = False

def get_data():
    if ex:
        h0 = open("./day1_ex.txt")
    else:
        h0 = open("./day1.txt")
    l0 = [(n[0], int(n[1:].strip())) for n in h0.readlines()]
    l1 = [n[1] if n[0] =='R' else -n[1] for n in l0]
    return l1

def part1(l1):
    pos = 50
    count = 0
    for turn in l1:
        pos = (pos + turn) % 100
        if pos == 0:
            count += 1
    return count

#ex = True
def part2(l1):
    pos = 50
    count = 0
    for turn in l1:
        old = int(pos)
        pos = (old + turn) % 100
        spins, rot = divmod(abs(turn), 100)
        count += spins
        if old == 0:
            continue
        if turn < 0:
            rot =  -rot
            if old + rot < 1:
                clicks = ceil(abs(rot)/100)
                count += clicks
        else:
            if old + rot > 99:
                clicks = ceil(abs(rot)/100)
                count += clicks
    return count

data = get_data()

print("Part 1 answer: %d" % part1(data))
print("Part 2 answer: %d" % part2(data))
