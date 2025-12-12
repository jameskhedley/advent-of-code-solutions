from collections import deque, defaultdict
from copy import copy
import math
ex = False

def read_data(part):
    if ex:
        if part == 1:
            h0 = open('day11_ex.txt')
        else:
            h0 = open('day11_ex2.txt')
    else:
        h0 = open('day11.txt')
    data = {}
    for line in h0.readlines():
        k,rest = line.strip().split(": ")
        lv = rest.split(' ')
        data[k] = tuple(lv)
    return data

def solve_old(map, start, end): # this remembers whole paths, not just counts. fast enough for part 1
    queue = deque([[start,(start,)]])
    paths = set()
    while queue:
        pos, path = queue.popleft() # todo should be pop right for DFS?
        for move in map[pos]:
            new_path = path + (move,)
            if move == end:
                paths.add(new_path)
                continue
            queue.append([move, new_path])
    for pp in paths:
        print(pp)
    return len(paths)

def dist(map, start, end, cache={}):
    if start == end:
        return 0
    if start in cache:
        return cache[start]
    if start == 'out':
        return math.inf
    lengths = []
    for move in map[start]:
        lengths.append(dist(map, move, end, cache))
    cache[start] = min(lengths)+1
    #print("called with start: %s, end %s, returned length %d" % (start, end, cache[start]))
    return cache[start]

ex=True
pts = [2]
if 1 in pts:
    data = read_data(1)
    print("part 1 answer: %d" % solve_old(data, "you", "out"))
if 2 in pts:
    data = read_data(2)
    if 1:
        c0 = {}
        ans0 = dist(data, "svr", "out", c0)
        #print(ans0)
        keys0 = set([y for x,y in c0.items() if y<math.inf])
        routes0 = sorted([(x,y) for x,y in c0.items() if y<math.inf], key=lambda xx: xx[1])
        print(max([[y for x,y in routes0].count(k) for k in keys0]))
        pass
    if 0:
        c0 = {}
        ans0 = dist(data, "svr", "fft", c0)
        #print(ans0)
        keys0 = set([y for x,y in c0.items() if y<math.inf])
        routes0 = sorted([(x,y) for x,y in c0.items() if y<math.inf], key=lambda xx: xx[1])
        print(max([[y for x,y in routes0].count(k) for k in keys0]))
        #c1 = {}
        #ans1 = dist(data, "svr", "dac", c1)
        #print(ans1)
        c2 = {}
        ans2 = dist(data, "fft", "dac", c2)
        #print(ans2)
        keys2 = set([y for x,y in c2.items() if y<math.inf])
        routes2 = sorted([(x,y) for x,y in c2.items() if y<math.inf], key=lambda xx: xx[1])
        print(max([[y for x,y in routes2].count(k) for k in keys2]))
        #c3 = {}
        #ans3 = dist(data, "dac", "fft", c3) #INFINITY!!
        #print(ans3)
        c4 = {}
        ans4 = dist(data, "dac", "out", c4)
        #print(ans4)
        keys4 = set([y for x,y in c4.items() if y<math.inf])
        routes4 = sorted([(x,y) for x,y in c4.items() if y<math.inf], key=lambda xx: xx[1])
        print(max([[y for x,y in routes4].count(k) for k in keys4]))
        pass
    #print("part 2 answer: %d" % )
