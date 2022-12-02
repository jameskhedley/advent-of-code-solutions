from collections import deque, defaultdict
from itertools import chain
#h0 = open("day15-ex.txt")
h0 = open("day15.txt")

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
    #iloop = 0
    maxy = 0
    maxx = 0
    print("grid dims: x: %d y: %d" %(len(grid), len(grid[0])))
    
    while levels[-1]:
        #iloop += 1
        #print(iloop)
        if maxx > 30:
            break
        #print_dist(grid, dist)
        frontier = []
        for u in levels[-1]:
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
    #import pdb; pdb.set_trace()
    return parent, dist

def main(grid):
    
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
          
import cProfile
#cProfile.run("main(grid)")
main(grid)
