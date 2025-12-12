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

def dist(map, start, end, path, cache={}):
    if not path: path = (start,)
    paths = set()
    if start == "eee":
        pass
    if start == end:
        if "dac" in path and "fft" in path:
            paths.add(path)
        return 0, paths
    if start in cache:
        return cache[start], paths
    if start == 'out':
        return math.inf, paths
    lengths = []
    for move in map[start]:
        new_path = path + (move,)
        length, new_paths = dist(map, move, end, new_path, cache)
        paths = paths.union(new_paths)
        lengths.append(length)
    cache[start] = min(lengths)+1
    #print("called with start: %s, end %s, returned length %d" % (start, end, cache[start]))
    return cache[start], paths

ex=True
pts = [2]
if 1 in pts:
    data = read_data(1)
    print("part 1 answer: %d" % solve_old(data, "you", "out"))
if 2 in pts:
    data = read_data(2)
    if 1:
        c0 = {}
        ans0, paths = dist(data, "svr", "out", None, c0)
        print(len(paths))
    if 0:
        c0 = {}
        ans0, paths = dist(data, "svr", "fft", c0)
        print(len(paths))

        c1 = {}
        ans1, paths = dist(data, "svr", "dac", c1)
        print(len(paths))

        c2 = {}
        ans2, paths = dist(data, "fft", "dac", c2)
        print(len(paths))

        c3 = {}
        ans3, paths = dist(data, "dac", "fft", c3) #INFINITY!!
        print(len(paths))
        
        c4 = {}
        ans4, paths = dist(data, "dac", "out", c4)
        print(len(paths))
        pass
    #print("part 2 answer: %d" % )
