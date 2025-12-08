# quite slow but ran out of time to optimise it much
from itertools import chain
import math
ex=False
def get_data():
    if ex:
        h0 = open("./day8_ex.txt")
    else:
        h0 = open("./day8.txt")
    l0 = [tuple([int(x) for x in n.strip().split(',')]) for n in h0.readlines()]
    return l0

def calc_distances(data):
    dist = {}
    for point in data:
        for pp in data:
            if point == pp:
                continue
            if (pp,point) in dist.keys():
                continue
            dist[(point, pp)] = math.sqrt((point[0]-pp[0])**2 + (point[1]-pp[1])**2 + (point[2]-pp[2])**2)
    dist = dict(sorted([(dx,dy) for dx,dy in dist.items()], key=lambda x: x[1]))
    return dist

def part1(data):
    dist = calc_distances(data)
    circuits = []
    cables = 10 if ex else 1000
    unconnected = set(data)
    for x in range(cables):
        if x%10 == 0: print(x)
        dist, circuits, first, second, unconnected = connectify(dist, circuits, unconnected)
    return math.prod([len(x) for x in sorted(circuits, key=lambda y: len(y), reverse=True)][:3])

def part2(data):
    dist = calc_distances(data)
    circuits = []
    cables = 0
    unconnected = set(data)
    while unconnected:
        cables += 1
        if cables % 10 == 0: print(cables)
        dist, circuits, first, second, unconnected = connectify(dist, circuits, unconnected)
    return first[0] * second[0]

def connectify(dist, circuits, unconnected):
    closest = list(dist.items())[0][0]
    first, second = sorted(closest,key=lambda x: x[0])
    del dist[closest]
    found = [] # ((906, 360, 560), (984, 92, 344)) is in two circuits!
    for cc in circuits:
        if first in cc and second in cc:
            found.append(cc)
        elif first in cc and not second in cc:
            cc.append(second)
            found.append(cc)
        elif first not in cc and second in cc:
            cc.append(first)
            found.append(cc)
        if len(found) > 1: #merge shared circuits
            ncc = list(set(chain(*found)))
            for fl in found:
                circuits.remove(fl)
            circuits.append(ncc)
            break
    if not found:
        circuits.append([first,second])
    if first in unconnected:
        unconnected.remove(first)
    if second in unconnected:
        unconnected.remove(second)
    return dist, circuits, first, second, unconnected
    
ex = True
data = get_data()

print("part 1 answer: %d" % part1(data))
print("part 2 answer: %d" % part2(data))