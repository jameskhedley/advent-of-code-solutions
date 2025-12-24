#part 1 quite slow but only 30 seconds, could use cprofile to find hotspots
#part 2 is beyond my linear algebra capabilities so had a look at z3 and bang, solved
from collections import deque
import z3
ex = False

def p1solve(goal, moves, init_state):
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
            new_state = mutatep1(state, move)
            queue.append([new_state, new_path])
            if new_state == goal:
                paths.append(new_path)
        if done: break
    return len(paths[0])

def mutatep1(state, move):
    new_state = list(state)
    for light in move:
        if new_state[light]:
            new_state[light] = False
        else:
            new_state[light] = True
    return tuple(new_state)

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

def part2():
    ans = 0
    if ex:
        h0 = open('day10_ex.txt')
    else:
        h0 = open('day10.txt')
    for idx, line in enumerate(h0.readlines()):
        print(idx)
        goal = tuple([int(x) for x in line.strip()[line.index('{')+1:-1].split(',')])
        line = line.split(']')[1].split('{')[0][1:-1]
        moves = [[int(x) for x in list(x.strip('(').strip(')')) if x!=','] for x in line[line.index('('):].split(' ')]
        bs = [z3.Int(f"b{i}") for i in range(len(moves))]
        optimizer = z3.Optimize()
        optimizer.add(
            [
                z3.Sum(bs[b] for b, button in enumerate(moves) if j in button)
                == joltage
                for (j, joltage) in enumerate(goal)
            ]
        )
        optimizer.add([b >= 0 for b in bs])
        optimizer.minimize(z3.Sum(bs))
        optimizer.check()
        model = optimizer.model()
        res = sum(model[b].as_long() for b in bs)
        print("shortest seq: %d, moveset: %s" % (res, str(moves)))
        ans+=res
    print("part 2 answer: %s" % ans)

#ex=True
part1()
part2()

def score(x,y):
    return sum([abs(x[0]-y[0]), abs(x[1]-y[1]), abs(x[2]-y[2])])

def renderp1(lights):
    s0 = '['+''.join(['#' if x else '.' for x in lights])+']'
    return s0

#tests p2
if 0:
    state = mutatep2((0,1,2,3), (1,3))
    assert state == (0, 2, 2, 4)
    
    #(3) once, (1,3) three times, (2,3) three times, (0,2) once, and (0,1) twice
    state = mutatep2((0,0,0,0), (3,))
    state = mutatep2(state, (1,3))
    state = mutatep2(state, (1,3))
    state = mutatep2(state, (1,3))
    state = mutatep2(state, (2,3))
    state = mutatep2(state, (2,3))
    state = mutatep2(state, (2,3))
    state = mutatep2(state, (0,2))
    state = mutatep2(state, (0,1))
    state = mutatep2(state, (0,1))
    assert state == (3, 5, 4, 7)
    print("p2 tests passed")

#tests p1
if 0:
    path0 = [[0, 3, 4]]
    state = mutatep1([True, False, False, False, False, False], path0[0])
    print(renderp1(state))

if 0:
    path0 = [[1, 3], [2, 3]]
    state = mutatep1(init_state, path0[0])
    print(renderp1(state))
    state = mutatep1(state, path0[1])
    print(renderp1(state))
