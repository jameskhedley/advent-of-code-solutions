from collections import deque, defaultdict

line = "[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1)"

# goal = [1 if char=='#' else 0 for char in list(line[:line.index('(')-1].strip('[').strip(']'))] # use for scoring?
goal = tuple([True if char=='#' else False for char in list(line[:line.index('(')-1].strip('[').strip(']'))])
#moves = [list(x.strip('(').strip(')').strip(',')) for x in line[line.index('('):].split(' ')]
moves = [[int(x) for x in list(x.strip('(').strip(')')) if x!=','] for x in line[line.index('('):].split(' ')]
#print(moves)

print(goal)
print(moves)

init_state = tuple([False]*len(goal))

def score(x,y):
    return sum([abs(x[0]-y[0]), abs(x[1]-y[1]), abs(x[2]-y[2])])

def mutate(state, move):
    new_state = list(state)
    for light in move:
        if new_state[light]:
            new_state[light] = False
        else:
            new_state[light] = True
    return tuple(new_state)

def solve(goal, moves):
    #bfs or dfs?
    visited = set()
    queue = deque([[init_state,[]]])
    move = None
    paths = []
    while queue:
        state, path = queue.popleft() #bfs pops from left
        #state = queue.pop() #dfs pops from right
        for move in moves:
            new_path = path + [move]
            print("next_move: %s" % str(move))
            new_state = mutate(state, move)
            if new_state in visited:
                continue
            queue.append([new_state, new_path])
            visited.add(state)
            if new_state == goal:
                print("found!")
                paths.append(new_path)
        
        print("state: %s" % str(state))
    return paths

found_paths = solve(goal, moves)
print(found_paths)


# print("=================================")    
# state=init_state
# print(state)
# for move in moves:
#     print(move)
#     print(mutate(init_state, move))



# zero_one_zero = [False, True, False]
# zero = [False]*3

# zero_one_one = [False, True, True]

# print(score(zero, zero_one_zero))
# print(score(zero, zero_one_one))