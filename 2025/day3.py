# part 1 east, part 2 quite hard, sliding window problem
# key is to resize the window based on how many available slots there are in the output (i think?)

from itertools import chain
ex = False

def get_data():
    if ex:
        h0 = open("./day3_ex.txt")
    else:
        h0 = open("./day3.txt")
    l0 = [[int(x) for x in list(n.strip())] for n in h0.readlines()]
    return l0

def part1(data):
    ans = 0
    for row in data:
        first = max(row[:-1])
        fp = row.index(first)
        second = max(row[fp+1:])
        jolt = int(str(first)+str(second))
        print(jolt)
        ans += jolt
    return ans

def part2(data):
    ans = 0
    for seq in data:
        jolt = []
        p0 = 0
        wl = (len(seq) - 12) + 1
        while len(jolt)<12:
            cand = seq[p0:p0+wl]
            found = max(cand)
            fp = cand.index(found)
            p0 = p0 + fp + 1
            wl = max(1, wl-fp)
            jolt.append(found)

        jolt = int(''.join([str(x) for x in jolt]))
        ans+=jolt
    return(ans)

if 0:
    assert part2([[int(x) for x in list('234234234234278')]]) == 434234234278
    assert part2([[int(x) for x in list('987654321111111')]]) == 987654321111
    assert part2([[int(x) for x in list('811111111111119')]]) == 811111111119
    print("tests passed")

#ex = True
if 1:
    data = get_data()
    #print("part 1 answer: %d" % part1(data))
    print("part 2 answer: %d" % part2(data))


