import sys
from collections import deque, defaultdict

MAXINT = sys.maxsize

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
    visited = set()
    start_dir = right
    queue = deque([(start_pos, 0, start_dir)])
    scores = defaultdict(lambda: MAXINT)
    fwd_path = []
    parents = defaultdict(list)
    scores[start_pos] = 0

    FWD, REV  = 0, 1
    while queue:
        #u, uscore, d = queue.pop() #dfs
        u, uscore, d = queue.popleft() #bfs
        dn = dir_names[d]
        if u == (7,1):
            stop = 1
        fwd_path.append((u, d, dir_names[d]))

        search = [d, turn_right[d], turn_left[d], opps[d]]
        for look in search:
            nbor = (u[0] + look[0], u[1] + look[1])
            if maze[nbor[0]][nbor[1]] == '#':
                continue
            score = 1
            if look == opps[d]:
                score += 2000
            elif look != d:
                score += 1000
            new_score = uscore + score
            #if ((nbor, look) not in visited) or (new_score < scores[nbor]):
            if ((nbor, look) not in visited) and (new_score < scores[nbor]):
                scores[nbor] = new_score
                parents[(nbor, look)]  = (u, d)
            else:
                continue
            if (nbor == end_pos):
                print("reached end!")
            else:
                queue.append((nbor, new_score, look))
        visited.add((u,d))
        if viz:
            print_grid(maze, fwd_path)
            import time; time.sleep(0.1)
    print_grid(maze, fwd_path)

    end_runs = [(parent,child) for parent,child  in parents.items() if parent[0]==end_pos]
 
    final_scores=[]
    for epidx, epos in enumerate(end_runs):
        print("%d / %d" % (epidx, len(end_runs)))
        pos = epos[0]
        final = 0
        visited =  set()
        while pos != (start_pos, start_dir):
            # print(pos)
            if pos in visited:
                pos = parents[pos]
                print("looped!")
                print(pos)
                break

            visited.add(pos)

            new_pos = parents[pos]
            old_dir = pos[1]
            new_dir = new_pos[1]
            if old_dir != new_dir:
                final+=1001
            else:
                final+=1
            pos = parents[pos]
        final_scores.append(final)

    #return scores[end_pos]
    return min(final_scores)

#viz=True
viz=False

#maze, start_pos, end_pos = read_data('day16_ex.txt') #7036
#maze, start_pos, end_pos = read_data('day16_ex1.txt') #11048
#maze, start_pos, end_pos = read_data('day16_ex2.txt') #21148
#maze, start_pos, end_pos = read_data('day16_ex3.txt') #21110
#maze, start_pos, end_pos = read_data('day16_ex4.txt') #4013
maze, start_pos, end_pos = read_data('day16_ex5.txt') #
#maze, start_pos, end_pos = read_data('day16_data.txt')
#wat = [((40, 139), (-1, 0)),((41, 139), (-1, 0)),((42, 139), (-1, 0)),((43, 139), (0, 1)),((43, 138), (0, 1)),((43, 137), (1, 0)),((42, 137), (1, 0)),((41, 137), (1, 0)),((40, 137), (1, 0)),((39, 137), (0, 1)),((39, 136), (0, 1)),((39, 135), (-1, 0)),((40, 135), (-1, 0)),((41, 135), (-1, 0)),((42, 135), (-1, 0)),((43, 135), (0, 1)),((43, 134), (0, 1)),((43, 133), (1, 0)),((42, 133), (1, 0)),((41, 133), (0, 1)),((41, 132), (0, 1)),((41, 131), (1, 0)),((40, 131), (1, 0)),((39, 131), (1, 0)),((38, 131), (1, 0)),((37, 131), (1, 0)),((36, 131), (1, 0)),((35, 131), (0, -1)),((35, 132), (0, -1)),((35, 133), (0, -1)),((35, 134), (0, -1)),((35, 135), (-1, 0)),((36, 135), (-1, 0)),((37, 135), (0, -1)),((37, 136), (0, -1)),((37, 137), (1, 0)),((36, 137), (1, 0)),((35, 137), (1, 0)),((34, 137), (1, 0)),((33, 137), (0, -1)),((33, 138), (0, -1)),((33, 139), (-1, 0)),((34, 139), (-1, 0)),((35, 139), (-1, 0)),((36, 139), (-1, 0)),((37, 139), (-1, 0)),((38, 139), (-1, 0)),((39, 139), (-1, 0))]
#print_grid(maze, wat)
shortest = search(maze, start_pos, end_pos)
print(shortest)

