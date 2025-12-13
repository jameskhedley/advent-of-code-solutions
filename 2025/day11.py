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

def dist(map, start, end, cache={}, visited=set()):
    if start in visited:
        return 0
    if start == end:
        return 1
    if start == 'out':
        return 0
    if start in cache:
        return cache[start]
    paths = 0
    visited.add(start)
    for move in map[start]:
        paths += dist(map, move, end, cache, visited)
    visited.remove(start)
    cache[start] = paths
    return paths

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
        print(ans0)
    if 0:
        c0 = {}
        svr_fft = dist(data, "svr", "fft", c0)
        print(svr_fft)

        c1 = {}
        svr_dac = dist(data, "svr", "dac", c1)
        print(svr_dac)

        c2 = {}
        fft_dac = dist(data, "fft", "dac", c2)
        print(fft_dac)

        c3 = {}
        dac_fft = dist(data, "dac", "fft", c3) #INFINITY!!
        print(dac_fft)
        
        c4 = {}
        dac_out = dist(data, "dac", "out", c4)
        print(dac_out)
        pass
        ans = svr_fft*fft_dac*dac_out
        print(ans)
        
    #print("part 2 answer: %d" % )
