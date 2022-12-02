from math import sqrt
from cython.view cimport array as cvarray
import numpy as np
import sys
from collections import deque
   
def bfs3(s, grid, dimx, dimy):
    npgrid = np.array(grid, dtype=np.int32)
    dist = [[0 for y in x] for x in grid]
    npdist = np.array(dist, dtype=np.int32)
    print(npdist[0][0])
    
    cdef int [:, :] dist_view = npdist
    
    levels = deque()
    levels.append([s])
    
    iloop: cython.int = 0
    maxy: cython.int = 0
    maxx: cython.int = 0

    
    print("grid dims: x: %d y: %d" %(dimx, dimy))
    #########################
    f0:cython.int = sqrt((dimy**2) + (dimx**2))
    f1:cython.float = f0 * 0.07 #magical
    f2:cython.float = int(f0 + f1)
    #########################
    down = [0, 1]
    up = [0, -1]
    right = [1,0]
    left = [-1,0]
    vs = [down, right, left, up]
    #########################
    while levels[-1]:
        frontier = [] #frontier is just the newest level
        for u in levels.pop():
            iloop += 1
            ddx = dimx - u[0]
            ddy = dimy - u[1]
            dest_dist = sqrt((ddx**2) + (ddy**2))
            origin_dist = sqrt((u[0]**2) + (u[1]**2))

            if origin_dist  + dest_dist > f2: continue
            nlist = [(u[0]+vs[0][0], u[1]+vs[0][1]), (u[0]+vs[1][0], u[1]+vs[1][1]),
                        (u[0]+vs[2][0], u[1]+vs[2][1]), (u[0]+vs[3][0], u[1]+vs[3][1])]

            if not nlist: continue
            for v in nlist:
                if v[0] >= len(grid): continue
                if v[1] >= len(grid): continue
                if v[0] < 0: continue
                if v[1] < 0: continue
                
                if v == (0,0): continue
                nv = dist_view[u[0]][u[1]] + grid[v[0]][v[1]]

                val: cython.int = dist_view[v[0]][v[1]]
                if val > 0:
                    if dist_view[v[0]][v[1]] < nv: 
                        continue
                    else:
                        dist_view[v[0]][v[1]] = nv
                else:
                    dist_view[v[0]][v[1]] = nv
                if v[0] > maxy and v[1] > maxx:
                    maxy = v[0]
                    maxx = v[1]
                    print("Max coord considered: (%d,%d)" % (maxy, maxx))
                    
                frontier.append(v)
        levels.append(set(frontier))
        totsize = 0
        for l in levels:
            totsize += sys.getsizeof(l)
        print("levels size: %d" % totsize)

    return dist_view
        
def main(grid):
    dimx: cython.int = len(grid)
    dimy: cython.int = len(grid[0])
    distgrid = bfs3((0,0), grid, dimx, dimy)
    return distgrid


