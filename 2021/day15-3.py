from collections import deque, defaultdict
from itertools import chain
import copy, sys
from math import sqrt
from pdb import set_trace as qq
#h0 = open("day15-ex.txt")
h0 = open("day15.txt")
#h0 = open("day15-hint.txt")

lines = h0.readlines()

grid = [[int(x) for x in list(line.strip())] for line in lines]

def print_distgrid(grid):
    for y, line in enumerate(grid):
        pl = ""
        for x, cell in enumerate(line):
            #pl += "*%d" % cell
            pl = "%s %03d" % (pl,cell)
        print(pl)
    print("*******************************")



def print_grid(grid, path):
    for y, line in enumerate(grid):
        pl = ""
        for x, cell in enumerate(line):
            if (x,y) in path:
                pl += "*%d" % cell
            else:
                pl += " %d" % cell
        print(pl)
    print("*******************************")

def is_valid(visited, point, dimx):
    if (point[0] < 0 or point[1] < 0 or point[0] >= dimx or point[1] >= dimx):
        return False
    if point in visited:
        return False
    return True

def build_graph(grid):
    visited = set()
    #vrow = [ -1, 0, 1, 0]
    #vcol = [ 0, 1, 0, -1]
    vrow = [0, 1]
    vcol = [1, 0]

    d0 = defaultdict(list)
    for y, line in enumerate(grid):
        for x, cell in enumerate(line):
            point = (x,y)
            for i in range(len(vrow)):
                newx = x + vrow[i]
                newy = y + vcol[i]
                nbor = (newx, newy)
                if is_valid(visited, nbor, len(grid)):
                    d0[point].append(nbor)
    last = (len(grid) -1, len(grid) -1)
    d0[last] = None
    return d0

def dfs(gadj, point, grid):
    def inner(gadj, point, grid, visited = set(), path=[]):
        
        visited.add(point)
        path.append(point)
        if point == (9,9):
            return path
        #for nbor in gadj[point]:
        scores = sorted([(grid[n[1]][n[0]], n) for n in gadj[point]])
        #if point == (0,1):
        #    import pdb; pdb.set_trace()
        cv = 0
        for sc in scores:
            nx = sc[1]
            if nx not in visited: break
            cv += 1
        if cv == len(gadj[point]):
            return path

        print(nx)    
        return inner(gadj, nx, grid, visited, path)      
            

    found = []
    
    loops = 0
    while loops < 1:
        loops += 1
        path = inner(gadj, point, grid)
        found.append(path)
    return found[0]
    
#@profile
def bfs(gadj, s, grid):
    #parent = {k: None for k in gadj}
    #parent[s] = s
    dist = {k: None for k in gadj}
    dist[s] = 1
    levels = [[s]]
    #levels = deque(deque())
    iloop = 0
    maxy = 0
    maxx = 0
    dimx = len(grid)
    dimy = len(grid[0])
    print("grid dims: x: %d y: %d" %(dimx, dimy))
    f0 = sqrt((dimy**2) + (dimx**2))
    f1 = f0 * 0.07 #magical
    f2 = int(f0 + f1)
    while levels[-1]:
        #if maxx > 20:
            #import pdb; pdb.set_trace()
        #    break
        #print_dist(grid, dist)
        frontier = [] #frontier is just the newest level
        for u in levels[-1]:
            iloop += 1
            #ddx = dimx - u[0]
            #ddy = dimy - u[1]
            #dest_dist = sqrt((ddx**2) + (ddy**2))
            #origin_dist = sqrt((u[0]**2) + (u[1]**2))
            #if u == (25,0):
            #    import pdb; pdb.set_trace()
            #if origin_dist + dest_dist > f2: continue
            nlist = gadj[u]
            if not nlist: continue
            for v in nlist:
                
                if v == (0,0): continue
                nv = dist[u] + grid[v[0]][v[1]]
                #if v == (49,49):
                #    import pdb; pdb.set_trace()
                if dist[v]:
                    if dist[v] < nv: 
                        continue
                    else:
                        dist[v] = nv
                else:
                    dist[v] = nv
                if v[0] > maxy and v[1] > maxx:
                    maxy = v[0]
                    maxx = v[1]
                    print("Max coord considered: (%d,%d)" % (maxy, maxx))
                    #if maxy > 98:
                    #    print_dist(grid, dist)
                    
                frontier.append(v)
        levels.append(frontier)
    print(iloop)
    return None, dist
    
def bfs2(s, grid):
    dist = defaultdict(list)
    for y, line in enumerate(grid):
        for x, cell in enumerate(line):
            point = (x,y)
            dist[point] = None
    
    dist[s] = 1
    levels = [[s]]
    #levels = deque(deque())
    iloop = 0
    maxy = 0
    maxx = 0
    dimx = len(grid)
    dimy = len(grid[0])
    print("grid dims: x: %d y: %d" %(dimx, dimy))
    f0 = sqrt((dimy**2) + (dimx**2))
    f1 = f0 * 0.07 #magical
    f2 = int(f0 + f1)
    #########################
    down = [0, 1]
    right = [1,0]
    vs = [down, right]
    #########################
    while levels[-1]:
        #if maxx > 20:
            #import pdb; pdb.set_trace()
        #    break
        #print_dist(grid, dist)
        frontier = [] #frontier is just the newest level
        for u in levels[-1]:
            iloop += 1
            ddx = dimx - u[0]
            ddy = dimy - u[1]
            dest_dist = sqrt((ddx**2) + (ddy**2))
            origin_dist = sqrt((u[0]**2) + (u[1]**2))
            #if u == (25,0):
            #    import pdb; pdb.set_trace()
            if origin_dist  + dest_dist > f2: continue
            #nlist = gadj[u]
            nlist = [(u[0]+v[0], u[1]+v[1]) for v in vs]
            #nlist = [n for n in candidates if n[1] < len(grid) and n[0] < len(grid) 
            #                    and n[1] >= 0 and n[0] >= 0]
            
            if not nlist: continue
            for v in nlist:
                if v[0] >= len(grid): continue
                if v[1] >= len(grid): continue
                if v == (0,0): continue
                nv = dist[u] + grid[v[0]][v[1]]
                #if v == (49,49):
                #    import pdb; pdb.set_trace()
                if dist[v]:
                    if dist[v] < nv: 
                        continue
                    else:
                        dist[v] = nv
                else:
                    dist[v] = nv
                if v[0] > maxy and v[1] > maxx:
                    maxy = v[0]
                    maxx = v[1]
                    print("Max coord considered: (%d,%d)" % (maxy, maxx))
                    #if maxy > 98:
                    #    print_dist(grid, dist)
                    
                frontier.append(v)
        levels.append(frontier)
    print(iloop)
    return None, dist
    
def bfs3(s, grid):
    dist = [[0 for y in x] for x in grid]
    levels = [[s]]
    iloop = 0
    maxy = 0
    maxx = 0
    #########################
    down = [0, 1]
    up = [0, -1]
    right = [1,0]
    left = [-1,0]
    vs = [down, right, left, up]
    #########################
    while levels[-1]:
        #if maxx > 25: break
        frontier = [] #frontier is just the newest level
        for u in levels.pop():
            iloop += 1
            nlist = [(u[0]+vs[0][0], u[1]+vs[0][1]), (u[0]+vs[1][0], u[1]+vs[1][1]),
                        (u[0]+vs[2][0], u[1]+vs[2][1]), (u[0]+vs[3][0], u[1]+vs[3][1])]

            if not nlist: continue
            for v in nlist:
                if v[0] >= len(grid): continue
                if v[1] >= len(grid): continue
                if v[0] < 0: continue
                if v[1] < 0: continue
                if v == (0,0): continue
                nv = dist[u[0]][u[1]] + grid[v[0]][v[1]]

                #if v == (2,3):
                #    qq()
                if dist[v[0]][v[1]]:
                    if dist[v[0]][v[1]] < nv: 
                        continue
                    else:
                        dist[v[0]][v[1]] = nv
                else:
                    dist[v[0]][v[1]] = nv
                if v[0] > maxy and v[1] > maxx:
                    maxy = v[0]
                    maxx = v[1]
                    print("Max coord considered: (%d,%d)" % (maxy, maxx))
                    
                frontier.append(v)
        levels.append(set(frontier))
        totsize = 0
        for l in levels:
            totsize += sys.getsizeof(l)
        #if maxx == 25:
        #    qq()
        print("levels size: %d" % totsize)
    return dist

def build_big_grid(grid):
    big_grid = copy.deepcopy(grid)
    dimy = len(grid)
    dimx = len(grid[0])
    
    cg = grid
    
    for gx in range(4):
        ng = []
        for line in cg:
            nl = [(x % 9) +1  for x in line]
            ng.append(nl)
        for y, line in enumerate(ng):
            big_grid[y] += line
        cg = ng
    for gy in range(4):
        for i, line in enumerate(big_grid[gy*dimx:(gy*dimx)+dimx]):
            nl = [(x % 9) +1  for x in line]
            big_grid.append(nl)
            
        
            
    #print_grid(big_grid, [])
    return big_grid
    
def score_path(path, grid):
    return sum([grid[x[1]][x[0]] for x in path])
        
def main_dfs(grid):
    print("Constructing big grid...")
    #grid = build_big_grid(grid)
    print("Big grid ready!")
    #print_grid(grid,[])
    print("Building graph...")
    graph = build_graph(grid)
    #print(graph)
    print("Graph built!")
    path = dfs(graph, (0,0), grid)
    print(path)
    print_grid(grid, path)
    print("score: %d" % score_path(path, grid))

def main(grid):
    print("Constructing big grid...")
    grid = build_big_grid(grid)
    print("Big grid ready!")
    #print_grid(grid,[])
    print("Building graph...")
    graph = build_graph(grid)
    #print(graph)
    print("Graph built!")
    #_, dist = bfs(graph, (0,0), grid)
    #_, dist = bfs2((0,0), grid)
    distgrid = bfs3((0,0), grid)
    print_distgrid(distgrid)
    #print_dist(grid, dist)

        
def print_dist(grid, dist):
    for y in range(len(grid[0])):
        line = ""
        for x in range(len(grid)):
            temp = dist[(y,x)]
            if not temp: temp = 0
            line = "%s %03d" % (line,temp)
        print(line)
    print("*******************************")
          
import cProfile
cProfile.run("main(grid)")
#main(grid)
#main_dfs(grid)
