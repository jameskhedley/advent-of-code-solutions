import sys
from collections import deque, defaultdict

MAXINT = sys.maxsize

up, right, down, left = (-1,0), (0,1), (1,0), (0,-1)
dir_names = {up: "up", right: "right", down: "down", left: "left"}
turn_right = {up: right, right: down, down: left, left: up}
turn_left = {up: left, right: up, down: right, left: down}
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

def print_grid_part2(arr, path):
    for y, line in enumerate(arr):
        pl = ""
        for x, cell in enumerate(line):
            if (y,x) in path:
                pl += " O"
            else:
                pl += " "+cell
        print(pl + " " + str(y))
    print(" 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4")
    print("*******************************")

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

def pt1(maze, start_pos, end_pos):
    scores, _ = search(maze, start_pos, end_pos)
    end_scores = [score for (pos, dir), score in scores.items() if pos==end_pos]
    print(min(end_scores))
    return min(end_scores)

def search(maze, start_pos, end_pos):
    start_dir = right
    queue = deque([(start_pos, 0, start_dir)])
    scores = defaultdict(lambda: MAXINT)
    reached_from = {}
    fwd_path = [] # only for drawing a path visualisation
    scores[(start_pos, start_dir)] = 0

    while queue:
        #u, uscore, d = queue.pop() #dfs - not suitable for this problem
        u, uscore, d = queue.popleft() #bfs
        dn = dir_names[d]
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
            reached_from[(nbor, look)] = (u, d, uscore)
        if viz:
            print_grid(maze, fwd_path)
            import time; time.sleep(0.1)
    print_grid(maze, fwd_path)
    return scores, reached_from
    
def pt2(maze, start_pos, end_pos):
    scores, reached_from = search(maze, start_pos, end_pos)
    end_scores = [(score, dir) for (pos, dir), score in scores.items() if pos==end_pos]
    end_scores.sort(key=lambda x: x[0])
    found = check_route_distance(start_pos, end_pos, min(end_scores)[0], min(end_scores)[1], reached_from, scores)
    print_grid_part2(maze, found)
    print(min(end_scores))
    print("part 2: %d" % (len(found)+1))

def check_route_distance(start_pos, end_pos, end_score, end_dir, reached_from, scores):
    tpos = end_pos
    visited = set()
    found = set([end_pos])
    queue = deque([(end_pos, end_dir)])
    while queue:
        tpos = queue.popleft()
        if tpos in visited:
            continue
        score = scores[tpos]
        if tpos[0] == start_pos:
            continue

        from_cells = [(from_cell, tdir, ddir, score) 
            for (dest_cell, ddir), (from_cell, tdir, score) in reached_from.items() 
            if dest_cell == tpos[0] ] #this is probably quite slow
        for (nxpos, nxdir, _, _) in from_cells:
            if (nxpos, nxdir) in visited:
                continue
            #check all direction scores for the cell, can basically tell if it was traversed by score delta
            for dir in (up, right, down, left):
                dscore = scores[nxpos, dir]
                if score-dscore in (1,1001):
                    queue.append((nxpos, dir))

        visited.add(tpos)
        found.add(tpos[0])

    print(len(found))
    return found

#viz=True
viz=False
#maze, start_pos, end_pos = read_data('day16_ex.txt') #p1 7036 p2 45
#maze, start_pos, end_pos = read_data('day16_ex1.txt') #11048 p2 64
#maze, start_pos, end_pos = read_data('day16_ex2.txt') #21148
#maze, start_pos, end_pos = read_data('day16_ex3.txt') #21110
#maze, start_pos, end_pos = read_data('day16_ex4.txt') #4013
maze, start_pos, end_pos = read_data('day16_data.txt')
#print("part1: %d" % pt1(maze, start_pos, end_pos))

pt2(maze, start_pos, end_pos)

