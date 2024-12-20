import sys
from collections import deque, defaultdict

MAXINT = sys.maxsize

up, right, down, left = (-1,0), (0,1), (1,0), (0,-1)
dir_names = {up: "up", right: "right", down: "down", left: "left"}
dirs = {"up": up, "right": right, "down": down, "left": left}
turn_right = {up: right, right: down, down: left, left: up}
turn_left = {up: left, right: up, down: right, left: down}
opps = {up: down, left: right, down: up, right: left}

def read_data(fn):
    maze = []
    start_pos, end_pos = None, None
    h0 = open(fn)
    lines=h0.readlines()
    maze = [list(line.strip()) for line in lines]
    for irow, row in enumerate(maze):
        if "E" in row:
            icol = row.index('E')
            end_pos = (irow,icol)
        if "S" in row:
            icol = row.index('S')
            start_pos = (irow,icol)
    return maze, start_pos, end_pos

def print_grid(arr, path):
    dpath = dict( [(x[0], x[1]) for x in path])
    sym = {right: '>', left: '<', up: '^', down: 'v'}
    for y, line in enumerate(arr):
        pl = ""
        for x, cell in enumerate(line):
            if (y,x) in dpath:
                pl += " %s" % sym[dpath[(y,x)]]
            else:
                pl += " %s" % str(cell)
        print(pl + " " + str(y))
    print(" 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4")
    print("*******************************")

def new_path_entry(direction, path, score):
    return {'direction': direction, 'path': path, 'score': score}

def search(maze, start_pos, end_pos):
    start_dir = right
    queue = deque([(start_pos, 0, start_dir)])
    scores = defaultdict(lambda: MAXINT)
    fwd_path = []
    parents = defaultdict(list)
    scores[(start_pos, start_dir)] = 0

    FWD, REV  = 0, 1
    while queue:
        #u, uscore, d = queue.pop() #dfs
        u, uscore, d = queue.popleft() #bfs
        dn = dir_names[d]
        if u == (7,1):
            stop = 1
        fwd_path.append((u, d, dir_names[d]))
        if maze[u[0]][u[1]] == '#':
            continue
        if scores[(u,d)] < uscore: #key point - if we already had a lower score, just move on
            continue
        scores[(u,d)] = uscore # key point - only do scoring when actually visited, not when looking at neighbours
        if u == end_pos:
            continue

        search = [d, turn_right[d], turn_left[d]]
        for look in search:
            nbor = (u[0] + look[0], u[1] + look[1])
            if maze[nbor[0]][nbor[1]] == '#':
                continue
            score = 1
            if look != d:
                score += 1000
            queue.append((nbor, uscore + score, look)) # key point - keep temporary score in the queue
        if viz:
            print_grid(maze, fwd_path)
            import time; time.sleep(0.1)
    print_grid(maze, fwd_path)
    end_scores = [score for (pos, dir), score in scores.items() if pos==end_pos]
    return(min(end_scores))

#viz=True
viz=False

#maze, start_pos, end_pos = read_data('day16_ex.txt') #7036
#maze, start_pos, end_pos = read_data('day16_ex1.txt') #11048
#maze, start_pos, end_pos = read_data('day16_ex2.txt') #21148
#maze, start_pos, end_pos = read_data('day16_ex3.txt') #21110
#maze, start_pos, end_pos = read_data('day16_ex4.txt') #4013
#maze, start_pos, end_pos = read_data('day16_ex5.txt') #
maze, start_pos, end_pos = read_data('day16_data.txt')
shortest = search(maze, start_pos, end_pos)
print(shortest)

