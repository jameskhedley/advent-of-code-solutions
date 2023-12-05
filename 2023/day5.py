from pprint import pprint  as pp
from collections import defaultdict
from itertools import chain
h0 = open("day5_data.txt")
#h0 = open("day5_ex.txt")

l0 = [n.strip().lower() if n.strip() else None for n in h0.readlines()]

def pt2(l0):
    maps, gen_seeds = parse(l0)
    seeds = list(gen_seeds)
    start_seeds = [x for x in seeds[::2]]
    seed_lens = [x for x in seeds[1::2]]
    
    print("going to generate seed ranges...")
    seed_ranges = []
    for s0, l0 in zip(start_seeds, seed_lens):
        seed_ranges.append(range(s0, s0+l0))
    print("done")
    
    print("starting to calculate seeds...")
    locs = []
    for s0 in chain(*seed_ranges):
        res = calc_seed(s0, maps)
        locs.append(res)
    print("done")
    print(sorted(locs)[0])



def pt1():
    maps, seeds = parse(l0)

    locs = []
    for s0 in seeds:
        res = calc_seed(s0, maps)
        locs.append(res)
    print(sorted(locs)[0])

def calc_seed(s0, maps):
    print("calculating seed %d" % (s0))
    res = lookup(maps["seed-to-soil map"], s0)
    res = lookup(maps["soil-to-fertilizer map"], res)
    res = lookup(maps["fertilizer-to-water map"], res)
    res = lookup(maps["water-to-light map"], res)
    res = lookup(maps["light-to-temperature map"], res)
    res = lookup(maps["temperature-to-humidity map"], res)
    res = lookup(maps["humidity-to-location map"], res)
    return res

def lookup(map0, value):
    ranges = []
    for triple in map0:
        r0 = range(triple[0], triple[0]+triple[2])
        r1 = range(triple[1], triple[1]+triple[2])
        ranges.append({"source": r1, "dest": r0})
    #print(ranges)
    res = value
    for d0 in ranges:
        if value in d0["source"]:
            res = d0["dest"][d0["source"].index(value)]
            break
    return(res)

def parse(l0):
    maps = defaultdict(list)

    line = l0.pop(0)
    seeds = (int(x) for x in line.split(":")[1].split(" ") if x)

    for line in l0:
        if line:
            if ":" in line:
                mn = line.split(":")[0]
            else:
                maps[mn].append([int(x) for x in line.split(" ") if x])
        else:
            mn = None
    #pp(maps)
    return maps, seeds

#pt1()
pt2(l0)
