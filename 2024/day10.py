from collections import deque
import string

def read_data(fn):
    h0 = open(fn)
    lines = h0.readlines()
    return [[int(x) if x in string.digits else '.' for x in list(line.strip())] for line in lines]

def tests():
    # pt1 tests 
    grid = read_data("day10_ex.txt") #36
    assert(pt1(grid, debug=True) == 36)
    grid = read_data("day10_ex0.txt") #2
    assert(pt1(grid, debug=True) == 2)
    grid = read_data("day10_ex1.txt") #4
    assert(pt1(grid, debug=True) == 4)
    grid = read_data("day10_ex2.txt") #3
    assert(pt1(grid, debug=True) == 3)
    print("pt1 tests passed")

    # pt1 tests 
    grid = read_data("day10_ex3.txt") #3
    assert(pt2(grid, debug=True) == 3)
    grid = read_data("day10_ex4.txt") #13
    assert(pt2(grid, debug=True) == 13)
    grid = read_data("day10_ex5.txt") #227
    assert(pt2(grid, debug=True) == 227)
    grid = read_data("day10_ex.txt") #81
    assert(pt2(grid, debug=True) == 81)
    print("pt2 tests passed")

def print_grid(arr, path):
    for y, line in enumerate(arr):
        pl = ""
        for x, cell in enumerate(line):
            #if (x,y) in path:
            if (y,x) in path:
                pl += "*%s" % str(cell)
            else:
                pl += " %s" % str(cell)
        print(pl)
    print("*******************************")

def find_zeros(grid):
    zeros = set()
    for y, line in enumerate(grid):
        for x, cell in enumerate(line):
            try:
                if int(cell) == 0:
                    zeros.add((y,x))
            except ValueError:
                continue
    return zeros

def pt1(grid, debug=False):
    zeros = find_zeros(grid)
    if debug:
        print_grid(grid, zeros)
    res = []
    for start in zeros:
        res.append(search_p1(grid, start, debug))
    sum = 0 
    for end in res:
        sum += len(end)
    return sum

def search_p1(maze, start, debug=False):
    queue = deque()
    queue.append(start)
    ends = set()
    path = [start]
    while queue:
        u = queue.popleft()
        height = int(maze[u[0]][u[1]])
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0)   ]: # Adjacent squares
            nbor = (u[0] + new_position[0], u[1] + new_position[1])
            if nbor[0] > (len(maze) - 1) or nbor[0] < 0 or nbor[1] > (len(maze[0]) -1) or nbor[1] < 0:
                continue
            if maze[nbor[0]][nbor[1]] == '.' or maze[nbor[0]][nbor[1]] != height+1:
                continue
            if nbor not in path:
                path.append(nbor)
                queue.append(nbor)
            if maze[nbor[0]][nbor[1]] == 9:
                ends.add(nbor)
    if debug:
        print_grid(maze, path)
    return ends

def pt2(grid, debug=False):
    zeros = find_zeros(grid)
    if debug:
        print_grid(grid, zeros)
    sum = 0
    for start in zeros:
        sum += bfs_dfs(grid, start, "dfs", debug) # either bfs or dfs works somehow
    return sum

def bfs_dfs(maze, start, mode, debug=False):
    queue = deque()
    queue.append(start)
    paths = []
    path = [start]
    while queue:
        if mode == 'dfs':
            u = queue.pop()
        elif mode == 'bfs':
            u = queue.popleft()
        height = int(maze[u[0]][u[1]])
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0)   ]: # Adjacent squares
            nbor = (u[0] + new_position[0], u[1] + new_position[1])
            if nbor[0] > (len(maze) - 1) or nbor[0] < 0 or nbor[1] > (len(maze[0]) -1) or nbor[1] < 0:
                continue
            if maze[nbor[0]][nbor[1]] == '.' or maze[nbor[0]][nbor[1]] != height+1:
                continue
            path.append(nbor)
            if maze[nbor[0]][nbor[1]] == 9:
                if debug:
                    print_grid(maze, path)
                paths.append(path)
                path = []
            else:
                queue.append(nbor)
    return len(paths)

tests()
grid = read_data("day10_data.txt")
print("pt1: %d" % pt1(grid))
print("pt2: %d" % pt2(grid))
