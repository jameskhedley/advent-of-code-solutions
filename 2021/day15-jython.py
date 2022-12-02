import threading
from collections import deque, defaultdict
from itertools import chain
import copy
from math import sqrt
from datetime import datetime as dt
h0 = open("day15-ex.txt")
#h0 = open("day15.txt")

dt_start = dt.now()

lines = h0.readlines()

grid = [[int(x) for x in list(line.strip())] for line in lines]

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
    vrow = [ -1, 0, 1, 0]
    vcol = [ 0, 1, 0, -1]

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
    return d0

def bfs(gadj, s, grid):
    parent = {k: None for k in gadj}
    parent[s] = s
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
    #import pdb; pdb.set_trace()
    
    
    while levels[-1]:
        #if maxx > 30:
        #    break
        #print_dist(grid, dist)
        frontier = []
        for u in levels[-1]:
            iloop += 1
            ddx = dimx - u[0]
            ddy = dimy - u[1]
            dest_dist = sqrt((ddx**2) + (ddy**2))
            origin_dist = sqrt((u[0]**2) + (u[1]**2))
            if origin_dist + dest_dist > f2: continue
            for v in gadj[u]:
                
                if v == (0,0): continue
                nv = dist[u] + grid[v[0]][v[1]]
                                    
                if dist[v]:
                    if dist[v] < nv: 
                        continue
                    else:
                        dist[v] = nv
                        parent[v] = u  
                else:
                    dist[v] = nv
                    parent[v] = u  
                if v[0] > maxy and v[1] > maxx:
                    maxy = v[0]
                    maxx = v[1]
                    print("Max coord considered: (%d,%d)" % (maxy, maxx))
                    #if maxy > 98:
                    #    print_dist(grid, dist)
                    
                frontier.append(v)  # O(1) amortized, add to border
        levels.append(frontier)  # add the new level to levels
    print(iloop)
    return parent, dist

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
        

def main(grid):
    print("Constructing big grid...")
    grid = build_big_grid(grid)
    print("Big grid ready!")
    #print_grid(grid,[])
    print("Building graph...")
    graph = build_graph(grid)
    #print(graph)
    print("Graph built!")
    _, dist = bfs(graph, (0,0), grid)
    print_dist(grid, dist)
        
def print_dist(grid, dist):
    for y in range(len(grid[0])):
        line = ""
        for x in range(len(grid)):
            temp = dist[(y,x)]
            if not temp: temp = 0
            line = "%s %03d" % (line,temp)
        print(line)
    print("*******************************")
          
main(grid)
dt_end = dt.now()
print(dt_end - dt_start)

