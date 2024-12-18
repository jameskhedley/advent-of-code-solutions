
from collections import deque, defaultdict

up, right, down, left = (-1,0), (0,1), (1,0), (0,-1)
#dirs = (up, right, down, left)
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
    #paths = defaultdict(int)
    paths = []
    visited = set()
    start_dir = right

    queue = deque([(start_pos, start_dir)])
    fwd_path = [(start_pos, start_dir, dir_names[start_dir])]
    #paths[tuple(fwd_path)] = 0
    graph = defaultdict(int)
    branch_paths = []
    last_branch = None

    FWD, REV  = 0, 1
    while queue:
        u, d = queue.pop() #dfs
        #u, d = queue.popleft() #bfs
        #if u==(7,3) and d == right:
        if u==(1,3):
            stop = 1
        # print(u)
        dn = dir_names[d]
        #if maze[u[0]][u[1]] == '#':
        #    continue
        visited.add((u,d))
        fwd_path.append((u, d, dir_names[d]))
        search = [d, turn_right[d], turn_left[d]]
        next_cells = []
        for look in search:
            nbor = (u[0] + look[0], u[1] + look[1])
            if maze[nbor[0]][nbor[1]] == '#':
                continue
            #if (nbor, d) in visited or (nbor, opps[d]) in visited:
            if (nbor, opps[d]) in visited:
                continue
            next_cells.append((nbor, look))
        if len(next_cells) > 1:
            #print("branch!")
            last_branch = u
        if not next_cells and last_branch:
            #print("popping branch!")
            while True:
                prev = fwd_path.pop()
                if prev[0] == last_branch:
                    fwd_path.append(prev)
                    break
        for nbor, look in next_cells:            
            score = 1
            if look != d:
                #print("turn!")
                score += 1000
            graph[(u, nbor)] += score
            if (nbor == end_pos):
                # print("reached end!")
                # print(len(fwd_path))
                paths.append(fwd_path)
                while True:
                    prev = fwd_path.pop()
                    if prev[0] == last_branch:
                        fwd_path.append(prev)
                        #queue.append((prev[0], prev[1]))
                        queue.append((prev[0], turn_right[prev[1]]))
                        queue.append((prev[0], turn_left[prev[1]]))
                        break
            else:
                queue.append((nbor, look))
        tmp_path = [x[0] for x in fwd_path]
        print_grid(maze, tmp_path)
        import time; time.sleep(0.1)
    for idx, path in enumerate(paths):
        print("Found path %d:" % idx)
        tmp_path = [x[0] for x in fwd_path]
        print_grid(maze, tmp_path)
    return paths


maze, start_pos, end_pos = read_data('day16_ex.txt')
print_grid(maze, [])
shortest = search(maze, start_pos, end_pos)
print(shortest)

