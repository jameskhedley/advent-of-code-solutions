from collections import deque
from copy import copy
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
    #for pp in paths:
    #    print(pp)
    return len(paths)

def dist(map, start, end, cache={}, visited=set()): # much faster due to cache and visited set
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

#ex=True
pts = [1,2]
if 1 in pts:
    data = read_data(1)
    print("part 1 answer: %d" % solve_old(data, "you", "out"))
if 2 in pts:
    data = read_data(2)
    if ex:
        ans0 = dist(data, "svr", "fft", {})
        ans1 = dist(data, "fft", "dac", {})
        ans2 = dist(data, "dac", "out", {})
        ans = ans0*ans1*ans2
        print("part 2 answer: %d" % ans)
    else:
        svr_fft = dist(data, "svr", "fft", {})
        fft_dac = dist(data, "fft", "dac", {})
        #dac_fft = dist(data, "dac", "fft") #INFINITY??
        dac_out = dist(data, "dac", "out", {})
        ans = svr_fft*fft_dac*dac_out
        print("part 2 answer: %d" % ans)
        
    
