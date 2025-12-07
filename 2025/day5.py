ex = False

def get_data():
    if ex:
        h0 = open("./day5_ex.txt")
    else:
        h0 = open("./day5.txt")
    section = 0
    ranges = []
    ids = []
    for line in h0.readlines():
        line = line.strip()
        if not line:
            section = 1
            continue
        if section == 0:
            ranges.append([int(x) for x in tuple(line.split('-'))])
        else:
            ids.append(int(line))
    return ranges, ids

#ex = True
def part1():
    ranges, ids = get_data()
    fresh = 0
    for ing in ids:
        for r in ranges:
            r[1] = r[1]+1
            if ing in range(*r):
                print("%d is fresh" % ing)
                fresh += 1
                break
    return fresh

#ex = True
def part2():
    rl, _ = get_data()
    ranges = set([tuple(x) for x in rl])
    count = 0
    while True:
        flat = set()
        for r in ranges:
            nr = tuple(r)
            for rr in ranges:
                if r==rr: continue
                if max(r[0],r[1]) < min(rr[0],rr[1]):
                    continue
                if min(r[0],r[1]) > max(rr[0],rr[1]):
                    continue
                nr = (min(r[0],rr[0]), max(r[1],rr[1])) # ranges overlap so merge
            flat.add(nr)
        if len(flat) == len(ranges):
            break # no more work to do
        ranges = flat
        count += 1
    nfresh = sum([(x[1]-x[0]) +1 for x in flat])
    print(len(ranges))
    print(count)
    return nfresh

#print("Part 1 answer: %d" % part1())
print("Part 2 answer: %d" % part2())