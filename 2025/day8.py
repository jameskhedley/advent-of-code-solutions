from collections import defaultdict
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


ex = True
data = get_data()
#print(data)

def part1(data):
    dist = {}

    for point in data:
        for pp in data:
            if point == pp:
                continue
            if (pp,point) in dist.keys():
                continue
            dist[(point, pp)] = math.sqrt((point[0]-pp[0])**2 + (point[1]-pp[1])**2 + (point[2]-pp[2])**2)

    dist = dict(sorted([(dx,dy) for dx,dy in dist.items()], key=lambda x: x[1]))
    circuits = []
    cables = 10 if ex else 1000
    for x in range(cables):
        if x%10 == 0: print(x)
        closest = list(dist.items())[0][0]
        del dist[closest]
        first = sorted(closest,key=lambda x: x[0])[0]
        second = sorted(closest,key=lambda x: x[0])[1]
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
        
    print(circuits)

    return math.prod([len(x) for x in sorted(circuits, key=lambda y: len(y), reverse=True)][:3])

print("part 1 answer: %d" % part1(data))