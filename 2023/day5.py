from collections import defaultdict
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

    print("starting to calculate locations...")
    n = 59999999 #finger in the air... worked for me! :)
    lowest = n

    maps_ranges = {}
    maps_ranges["humidity-to-location map"] = range_for_map(maps["humidity-to-location map"])
    maps_ranges["temperature-to-humidity map"] = range_for_map(maps["temperature-to-humidity map"])
    maps_ranges["light-to-temperature map"] = range_for_map(maps["light-to-temperature map"])
    maps_ranges["water-to-light map"] = range_for_map(maps["water-to-light map"])
    maps_ranges["fertilizer-to-water map"] = range_for_map(maps["fertilizer-to-water map"])
    maps_ranges["soil-to-fertilizer map"] = range_for_map(maps["soil-to-fertilizer map"])
    maps_ranges["seed-to-soil map"] = range_for_map(maps["seed-to-soil map"])

    while n > 0:
        if n % 10000 == 0:
            print("cycle %d, lowest so far: %d" % (n, lowest))
        seed = calc_seed_rev(n, maps_ranges)
        for sr in seed_ranges:
            if seed in sr:
                lowest = min(lowest, n)
                break
        n -= 1
    print(lowest)

def range_for_map(map0):
    ranges = []
    for triple in map0:
        r0 = range(triple[0], triple[0]+triple[2])
        r1 = range(triple[1], triple[1]+triple[2])
        ranges.append({"source": r1, "dest": r0})
    return ranges

def calc_seed_rev(location, maps_ranges):
    humid = rlookup(maps_ranges["humidity-to-location map"], location)
    temp = rlookup(maps_ranges["temperature-to-humidity map"], humid)
    light = rlookup(maps_ranges["light-to-temperature map"], temp)
    water = rlookup(maps_ranges["water-to-light map"], light)
    ferti = rlookup(maps_ranges["fertilizer-to-water map"], water)
    soil = rlookup(maps_ranges["soil-to-fertilizer map"], ferti)
    s0 = rlookup(maps_ranges["seed-to-soil map"], soil)
    return s0

def rlookup(ranges, value):
    res = value
    for d0 in ranges:
        if value in d0["dest"]:
            res = d0["source"][d0["dest"].index(value)]
            break
    return(res)

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
    return maps, seeds

#pt1()
pt2(l0)
