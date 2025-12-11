from collections import deque
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
        pos, path = queue.popleft()
        for move in map[pos]:
            new_path = path + (move,)
            if move == end:
                paths.add(new_path)
                continue
            queue.append([move, new_path])
    for pp in paths:
        print(pp)
    return len(paths)

def solve_fast(map, start, end): # this time only remember counts between start and end
    queue = deque([{'pos': start, 'plen': 0}])
    count=0
    cache = {}
    while queue:
        count+=1
        if count % 100000==0:
            print(count)
        pos, plen = queue.popleft().values()
        #if (start, pos) in cache:
        for move in map[pos]:
            if move == end:
                #return cache[(start,pos)]+1
                return plen+1
            #if (start, move) in cache:
            queue.append({'pos': move, 'plen': plen+1})

ex=True
pts = [2]
if 1 in pts:
    data = read_data(1)
    print("part 1 answer: %d" % solve_old(data, "you", "out"))
if 2 in pts:
    data = read_data(2)
    if 0:
        print(solve_fast(data, "svr", "out"))
    if 1:
        a0 = solve_fast(data, "svr", "fft")
        a1 = solve_fast(data, "svr", "dac")
        a2 = solve_fast(data, "fft", "out")
        a3 = solve_fast(data, "dac", "out")
        print(a0*a1*a2*a3)
    #print("part 2 answer: %d" % solve(data, "svr", set(["fft","dac"])))
