#part 1 quite slow but only 30 seconds, could use cprofile to find hotspots
from collections import deque
ex = False

def p1solve(goal, moves, init_state):
    visited = set()
    queue = deque([[init_state,tuple()]])
    move, paths, done = None, [], False
    while queue:
        state, path = queue.popleft() #bfs pops from left
        #state = queue.pop() #dfs pops from right
        for move in moves:
            if tuple(move) in path:
                continue # I sink is pointless to do same button twice in any sequence
            new_path = path + (tuple(move),)
            if paths and len(paths[0]) < len(new_path):
                done = True # we'll find the shortest paths first so can just bail once we start finding longer ones
                break
            visited.add(new_path)
            new_state = mutate(state, move)
            queue.append([new_state, new_path])
            if new_state == goal:
                paths.append(new_path)
        if done: break
    return len(paths[0])

def mutate(state, move):
    new_state = list(state)
    for light in move:
        if new_state[light]:
            new_state[light] = False
        else:
            new_state[light] = True
    return tuple(new_state)

#ex=True
def part1():
    ans = 0
    if ex:
        h0 = open('day10_ex.txt')
    else:
        h0 = open('day10.txt')
    for idx, line in enumerate(h0.readlines()):
        print(idx)
        goal = tuple([True if char=='#' else False for char in list(line[:line.index('(')-1].strip('[').strip(']'))])
        line = line.split(']')[1].split('{')[0][1:-1]
        moves = [[int(x) for x in list(x.strip('(').strip(')')) if x!=','] for x in line[line.index('('):].split(' ')]
        init_state = tuple([False]*len(goal))
        res = p1solve(goal, moves, init_state)
        print("shortest seq: %d, moveset: %s" % (res, str(moves)))
        ans+=res
    print("part 1 answer: %s" % ans)

part1()

def score(x,y):
    return sum([abs(x[0]-y[0]), abs(x[1]-y[1]), abs(x[2]-y[2])])

def render(lights):
    s0 = '['+''.join(['#' if x else '.' for x in lights])+']'
    return s0

if 0:
    path0 = [[0, 3, 4]]
    state = mutate([True, False, False, False, False, False], path0[0])
    print(render(state))

if 0:
    path0 = [[1, 3], [2, 3]]
    state = mutate(init_state, path0[0])
    print(render(state))
    state = mutate(state, path0[1])
    print(render(state))
