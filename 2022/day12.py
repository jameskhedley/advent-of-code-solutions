import string
from copy import copy
from itertools import chain
#h0 = open("day12_ex.txt")
h0 = open("day12.txt")
datalines = h0.readlines()

lut = dict([(c,i) for i,c in enumerate(string.ascii_lowercase)])
lut['S']=0
lut['E']=25

alpha_grid = [[x for x in list(line.strip())] for line in datalines]

def find2d(grid, to_find):
    for idy,row in enumerate(grid):
        for idx,val in enumerate(row):
            if val==to_find:
                return (idx,idy)

def find2d_many(grid, to_find):
    results = set()
    for idy,row in enumerate(grid):
        for idx,val in enumerate(row):
            if val==to_find:
                results.add((idx,idy))
    return results

def print_grid(grid, path=[]):
    for y, line in enumerate(grid):
        pl = ""
        for x, cell in enumerate(line):
            if (x,y) in path:
                pl += "*%s" % str(cell)
            else:
                pl += " %s" % str(cell)
        print(pl)
    print("*******************************")

def bfs(grid, origin, direction="up"):
    visited=set() # for performance, use a set not a list for checking
    current,prev = None,None
    distgrid = [[999 for row in line] for line in grid]
    distgrid[origin[1]][origin[0]] = 0
    down, up, right, left = [0, 1],[0, -1],[1,0],[-1,0]

    queue = [copy(origin)]
    iloop=0

    while queue:
        iloop+=1
        #current = queue.pop(0) #BFS uses a queue - iteration explosion, slow
        current = queue.pop() #DFS uses a stack
        visited.add(current)
        current_val = grid[current[1]][current[0]]
        current_dist = distgrid[current[1]][current[0]]
        nlist = [(current[0]+up[0], current[1]+up[1]), (current[0]+down[0], current[1]+down[1]),
                    (current[0]+left[0], current[1]+left[1]), (current[0]+right[0], current[1]+right[1])]
        olist = []   
        for nbor in nlist:  
            if nbor[0] >= len(grid[0]): continue
            if nbor[1] >= len(grid): continue
            if nbor[0] < 0: continue
            if nbor[1] < 0: continue
            if nbor == origin: continue
            nbor_val = grid[nbor[1]][nbor[0]]
            if direction=="up":
                if nbor_val > current_val + 1: continue
            else:
                if nbor_val+1 < current_val: continue
            olist.append(nbor) #olist is reachable cells from here
        for nbor in olist:
            nbor_dist = distgrid[nbor[1]][nbor[0]]
            if nbor_dist>(current_dist):
                # if you always revisit the neighbouring cells you get an iterative explosion
                # as if it were BFS. So only revisit if something changed.
                old = copy(distgrid[nbor[1]][nbor[0]])
                distgrid[nbor[1]][nbor[0]] = current_dist+1
                if old != distgrid[nbor[1]][nbor[0]] and nbor in visited:
                    visited.remove(nbor)
                
        for nbor in olist:
            if nbor not in visited:
                queue.append(nbor)

    print("BFS took %d steps" % iloop)                
    return distgrid

print_grid(alpha_grid)
goal=find2d(alpha_grid,"E")
origin=find2d(alpha_grid,"S")
grid = [[lut[x] for x in list(line.strip())] for line in datalines]

distgrid = bfs(grid, origin)
print("Part 1: Shortest path from %d,%d to %d,%d is %d steps long" % (origin[0],origin[1],goal[0],goal[1],distgrid[goal[1]][goal[0]]))
origin=find2d(alpha_grid,"E")
a_coords=find2d_many(alpha_grid,"a")
distgrid = bfs(grid, origin, "down")
pt2_ans = 999
for goal in a_coords:
    pt2_ans = min(distgrid[goal[1]][goal[0]], pt2_ans)
print("Part 2: Shortest path from %d,%d to any 'a' is %d steps long" % (origin[0],origin[1],pt2_ans))
