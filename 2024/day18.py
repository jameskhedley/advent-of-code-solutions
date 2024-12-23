from collections import deque, defaultdict

up, right, down, left = (-1,0), (0,1), (1,0), (0,-1)
dirs = (up, right, down, left)

def init_maze():
    maze = []
    for x in range(FULL_SIZE+1):
        maze.append(list(['.']*(FULL_SIZE+1)))
    return maze

def read_data(fn):
    h0 = open(fn)
    lines= h0.readlines()
    s0 = [line.split(',') for line in lines]
    l0 = [[int(x.strip()) for x in s] for s in s0]
    return l0

def print_grid(arr, dimx, dimy, path=None):
    for y, line in enumerate(arr[:dimx]):
        pl = ""
        for x, cell in enumerate(line[:dimy]):
            if path and (x,y) in path:
                pl += " O"
            else:
                pl += " "+cell
        print(pl + " " + str(y))
    print('*' * (dimy)*2)

def search(maze, size):
    end_pos = (size, size)
    queue = deque([((0,0), [(0,0)])]) # yuck
    visited = set()
    exited = False
    while queue:
        u, path = queue.popleft() #bfs
        #u, path = queue.pop() #dfs
        if maze[u[1]][u[0]] == '#':
            continue
        if u in visited:
            continue
        if u == (2,0):
            stop = 1
        visited.add(u)
        if u == end_pos:
            exited = True
            break
        for ndir in dirs:
            nbor = u[0]+ndir[0], u[1]+ndir[1]
            npath = list(path)
            if nbor[0] < 0 or nbor[0] > size or nbor[1] < 0 or nbor[1] > size:
                continue
            if maze[nbor[1]][nbor[0]] == '#':
                continue
            npath.append(nbor)
            queue.append((nbor, npath))
        if viz:
            print_grid(maze, size+1, size+1, path)
            import time; time.sleep(0.5)
    if exited:
        return path
    return None

#viz=True
viz=False
FULL_SIZE = 70

def part2():
    #data, n_instructions = read_data('day18_ex.txt'), 20 # all good
    #data, n_instructions = read_data('day18_ex.txt'), 21 # blocked
    data, n_instructions = read_data('day18_data.txt'), 1024
    maze = init_maze()
    maxcol,maxrow = 0,0
    for (col, row) in data[:n_instructions]:
        maze[row][col] = '#'
        maxcol = max(maxcol, col)
        maxrow = max(maxrow, row)
    print_grid(maze, maxcol+1, maxrow+1)

    blocked = False
    loop = 1
    while not blocked: # should probably do a binary chop search but it's quick enough to just loop until failure
        for (col, row) in data[n_instructions:n_instructions+loop]:
            maze[row][col] = '#'
            maxcol = max(maxcol, col)
            maxrow = max(maxrow, row)

        path = search(maze, maxcol)
        if path:
            print("Path found, loop %d length %d" % (loop, len(path)-1))
            loop += 1
        else:
            blocked = True
    print("Blocked after byte %d" % (n_instructions+loop)) #just looked up the line number in the data! cba do this properly lol

def part1():
    #data, n_instructions = read_data('day18_ex.txt'), 12
    data, n_instructions = read_data('day18_data.txt'), 1024
    maze = init_maze()
    maxcol,maxrow = 0,0
    for (col, row) in data[:n_instructions]:
        maze[row][col] = '#'
        maxcol = max(maxcol, col)
        maxrow = max(maxrow, row)

    print_grid(maze, maxcol+1, maxrow+1)
    path = search(maze, maxcol)
    print_grid(maze, maxrow+1, maxcol+1, path)
    print(len(path)-1)

#part1()
part2()