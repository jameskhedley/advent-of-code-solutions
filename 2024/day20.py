from collections import deque, defaultdict

up, right, down, left = (-1,0), (0,1), (1,0), (0,-1)
dirs = (up, right, down, left)

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

def print_grid(arr, dimx, dimy, path=None):
    for y, line in enumerate(arr[:dimx]):
        pl = ""
        for x, cell in enumerate(line[:dimy]):
            if path and (y,x) in path:
                pl += " O"
            else:
                pl += " "+cell
        print(pl + " " + str(y))
    print(' ' + ' '.join([str(x%10) for x in range(dimx)]))
    print('*' * (dimy)*2)

def search(maze, size, start_pos, end_pos):
    queue = deque([(start_pos, 0, [start_pos])]) 
    visited = set()
    exited = False
    scores = defaultdict(int)
    while queue:
        u, score, path = queue.popleft() #bfs
        #u, path = queue.pop() #dfs
        if maze[u[0]][u[1]] == '#':
            continue
        if u in visited:
            continue
        scores[u] = score
        visited.add(u)
        if u == end_pos:
            exited = True
            break
        for ndir in dirs:
            nbor = u[0]+ndir[0], u[1]+ndir[1]
            npath = list(path)
            if nbor[0] < 0 or nbor[0] > size or nbor[1] < 0 or nbor[1] > size:
                continue
            if maze[nbor[0]][nbor[1]] == '#':
                continue
            npath.append(nbor)
            queue.append((nbor, score+1, npath))
        if viz:
            print_grid(maze, size+1, size+1, path)
            import time; time.sleep(0.2)
    if exited:
        return path, scores
    return None, None

def find_potential_cheats(maze, path, size):
    pcheats = set()
    for u in path:
        for ndir in dirs:
            nbor = u[0]+ndir[0], u[1]+ndir[1]
            if nbor[0] < 0 or nbor[0] > size or nbor[1] < 0 or nbor[1] > size:
                continue
            if maze[nbor[0]][nbor[1]] != '#':
                continue
            other_side = u[0]+ndir[0]+ndir[0], u[1]+ndir[1]+ndir[1]
            if other_side[0] < 0 or other_side[0] > size or other_side[1] < 0 or other_side[1] > size:
                continue
            if maze[other_side[0]][other_side[1]] in ('.','E'):
                    pcheats.add(nbor)
    return pcheats

def calc_saving_for_cheat(maze, cheat, scores, end_pos):
    up, right, down, left = (-1,0), (0,1), (1,0), (0,-1)
    save = 0
    h, v = 0,0
    #is it a horizontal or vertical cheat?
    open_chars = ('.', 'E', 'S')
    if maze[cheat[0]+right[0]][cheat[1]+right[1]] in open_chars and maze[cheat[0]+left[0]][cheat[1]+left[1]] in open_chars:
        h = 1
    if maze[cheat[0]+up[0]][cheat[1]+up[1]] in open_chars and maze[cheat[0]+down[0]][cheat[1]+down[1]] in open_chars:
        v = 1
    if h and v:
        raise RuntimeError("wat do")
    if h:
        left = scores[(cheat[0], cheat[1]-1)]
        right = scores[(cheat[0], cheat[1]+1)]
        save = abs( left - right ) - 2
    elif v:
        up = left = scores[(cheat[0]-1, cheat[1])]
        down = left = scores[(cheat[0]+1, cheat[1])]
        save = abs( up - down) - 2
    return save

#viz=True
viz=False

#fn, show_grid = 'day20_ex.txt', True
fn, show_grid = 'day20_data.txt', False

maze, start_pos, end_pos = read_data(fn)
dimx = len(maze)
dimy = len(maze[0])
if show_grid:
    print_grid(maze, dimx, dimy)
# find the base path and distance scores
path, scores = search(maze, dimx, start_pos, end_pos)
if show_grid:
    print_grid(maze, dimx, dimy, path)
base_length = len(path)-1

# identify potential shortcuts
pcheats = find_potential_cheats(maze, path, dimx-1)
if show_grid:
    print_grid(maze, dimx, dimy, pcheats)

# final answer
results = defaultdict(int)
final = 0
for count, cheat in enumerate(pcheats):
    saving = calc_saving_for_cheat(maze, cheat, scores, end_pos)
    if saving >= 100:
        results[saving] += 1
        final+=1
from pprint import pprint; pprint(results)
print(final)
