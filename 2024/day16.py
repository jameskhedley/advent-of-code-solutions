
from collections import deque

up, right, down, left = (-1,0), (0,1), (1,0), (0,-1)
dirs = (up, right, down, left)
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

def print_grid(arr, path):
    for y, line in enumerate(arr):
        pl = ""
        for x, cell in enumerate(line):
            if (y,x) in path:
                pl += " *"
            else:
                pl += " %s" % str(cell)
        print(pl + " " + str(y))
    print(" 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4")
    print("*******************************")

def new_path_entry(direction, path, score):
    return {'direction': direction, 'path': path, 'score': score}

def search(maze, start_pos, end_pos):
    #queue = deque([start_pos, end_pos])
    queue = deque([start_pos])
    paths = set()
    visited = set()
    fwd_path = [start_pos]

    FWD, REV  = 0, 1
    #direction = up

    while queue:
        u = queue.pop()
        if u in visited:
            continue
        visited.add(u)
        if maze[u[0]][u[1]] == '#':
            continue
        search = [direction, turn_right[direction], turn_left[direction]]
        for look in search: # TODO prefer going in the same direction?
            nbor = (u[0] + look[0], u[1] + look[1])
            if nbor[0] > (len(maze) - 1) or nbor[0] < 0 or nbor[1] > (len(maze[0]) -1) or nbor[1] < 0:
                continue
            if maze[nbor[0]][nbor[1]] == '#':
                continue
            if nbor in visited: continue
            fwd_path.append(nbor)
            if (nbor == end_pos):
                paths.add(tuple(fwd_path))
                print("found it!")
                print(len(fwd_path))
                break
            queue.append(nbor)
        print_grid(maze, fwd_path)
    return paths


maze, start_pos, end_pos = read_data('day16_ex.txt')
print_grid(maze, [])
shortest = search(maze, start_pos, end_pos)

