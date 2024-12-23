# I must admit I got stuck on part 2 and had to look for solutions, thanks to /u/zniperr

import regex
from itertools import combinations
from collections import defaultdict
from functools import cache
#fn = "day19_ex.txt"
fn = "day19_data.txt"
lines = open(fn).readlines()
towels = tuple(lines[0].strip().split(', '))
designs = [x.strip() for x in lines[2:]]

def part1(towels, designs):
    template = '^(' + ''.join(["%s|"]*len(towels))[:-1] + ')+$' 
    pattern = template % tuple(towels)

    count = 0
    for d0 in designs:
        if regex.match(pattern, d0):
            print(d0)
            count+=1
    print("part 1 %d" % count)

def part2slow(towels, designs): # works on example but would take until end of universe on input lol
    ways = 0
    possible = defaultdict(set)
    for idx, d0 in enumerate(designs):
        print(idx)
        for i in range(len(towels)):
            template = '^(' + ''.join(["%s|"]*(i+1))[:-1] + ')+$' 
            print("debug 0")
            combos = set(combinations(towels, i+1))
            print("debug 1")
            for ic, com in enumerate(combos):
                if ic % 1000 == 0:
                    print("%d/%d" %(ic, len(combos)))
                lcom = list(com)
                lcom.sort(key=lambda x: len(x), reverse=True) # weird one but we want longer groups to be consumed first
                com = tuple(lcom)
                if set(com) == set(['r', 'b', 'g', 'br']): 
                    stop = 1
                pattern = template % com
                m0 = regex.match(pattern, d0)
                if m0:
                    allcaps = tuple(m0.allcaptures()[1])
                    if set(allcaps) == set(com):
                        possible[d0].add(tuple(com))
                        ways+=1
    print(possible)
    print(ways)

@cache # this makes a vast difference in execution times!!
def possible(design, towels):
    # this approach really makes it beautifully simple. Just knock off the first bit of the design when matched,
    # then the recursion means it's easy to try every towel one after against whatever is left.
    # By consuming the design, you're really reducing complexity.
    if not design:
        return 1
    ways = 0
    for towel in towels:
        if design.startswith(towel):
            ways += possible(design[len(towel):], towels)
    return ways

def part2(towels, designs):
    found = []
    for d0 in designs:
        found.append(possible(d0, towels))
    print(sum(found))

#part1(towels, designs)
#part2slow(towels, designs)
part2(towels, designs)