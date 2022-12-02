from collections import deque, defaultdict
from itertools import chain
from pdb import set_trace as qq
import random
h0 = open("day15-ex.txt")
#h0 = open("day15.txt")

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
    
def dfs4(grid, start, end=(9,9), dx="fwd"):
    up = [0, -1]
    down = [0, 1]
    left = [-1,0]
    right = [1,0]
    if dx == "fwd":
        vs = [down, right]
    elif dx == "rev":
        vs = [up, left]
    else:
        raise ValueError("bad direction")
    paths = []
    
    point = start
    
    #for attempt in range(500):
    attempt = 0
    while True:
        attempt += 1
        if attempt % 100 == 0: print(attempt)
        path = []
        #qq()
        while point:
            #if len(paths) > 1 and point == (3,2):
            #    qq()
            path.append(point)

            lp = len(path)
            prev_paths = set()
            if paths and lp < len(paths[0])-1:
                #prev_paths = set([p[lp] for p in paths])
                #prev_paths = [p[0:lp] for p in paths]
                prev_paths = set([tuple(p[0:lp+1]) for p in paths])
            
            nbors = [(point[0]+v[0], point[1]+v[1]) for v in vs]
            scores = sorted([(grid[n[1]][n[0]], n) for n in nbors 
                                if n[1] < len(grid) and n[0] < len(grid) 
                                    and n[1] >= 0 and n[0] >= 0])
            
            #qq()
            if scores:
                point = None
                for idx, sc in enumerate(scores):
                    np = sc[1]
                    if tuple(path+[np]) not in prev_paths:
                        point = np
                        break
                if not point:
                    point = random.choice(scores)[1]
            else:
                point = None
        if score_path(path, grid) == 40:
            print("found it!")
            break
        paths.append(path)
        if len(paths) > 500:
            std = sorted([[score_path(path, grid), path] for path in paths])[0:200]
            paths = [p[1] for p in std]
            qq()
        point = start
    
    ps = [[score_path(path, grid), path] for path in paths]
    best = sorted(ps)[0][1]
    for pps in ps:
        if False:
        #if (4,2) in pps[1] and (5,2) in pps[1] and (0,2) in pps[1]:
        #if (4,2) in pps[1]:
            print("4,2 in:")
            print_grid(grid, pps[1])
            print(pps[1])
            print(pps[0])
    return best

def dfs5(grid, start, end=(9,9), dx="fwd"):
    up = [0, -1]
    down = [0, 1]
    left = [-1,0]
    right = [1,0]
    if dx == "fwd":
        vs = [down, right]
    elif dx == "rev":
        vs = [up, left]
    else:
        raise ValueError("bad direction")
    paths = []
    
    point = start
    
    for attempt in range(10000):
        attempt = 0
        #while True:
        attempt += 1
        if attempt % 100 == 0: print(attempt)
        path = []
        #qq()
        while point:
            #if len(paths) > 1 and point == (3,2):
            #    qq()
            path.append(point)

            candidates = [(point[0]+v[0], point[1]+v[1]) for v in vs]
            nbors = [n for n in candidates if n[1] < len(grid) and n[0] < len(grid) 
                                and n[1] >= 0 and n[0] >= 0]
            
            if nbors:
                point = random.choice(nbors)
                #qq()
            else:
                point = None
        if score_path(path, grid) == 40:
            print("found it!")
            break
        
        paths.append(path)
        if len(paths) > 500:
            std = sorted([[score_path(path, grid), path] for path in paths])[0:200]
            paths = [p[1] for p in std]
            #qq()
        point = start
    
    ps = [[score_path(path, grid), path] for path in paths]
    best = sorted(ps)[0][1]
    for pps in ps:
        if False:
        #if (4,2) in pps[1] and (5,2) in pps[1] and (0,2) in pps[1]:
        #if (4,2) in pps[1]:
            print("4,2 in:")
            print_grid(grid, pps[1])
            print(pps[1])
            print(pps[0])
    return best
                

def dfs3(grid, point, end=(9,9), dx="fwd"):
    def inner(point, grid, vs, visited = set(), path=[]):
        visited.add(point)
        if point == end:
            path.append(point)
            return path
        path.append(point)
       
        nbors = [(point[0]+v[0], point[1]+v[1]) for v in vs]
        
        scores = sorted([(grid[n[1]][n[0]], n) for n in nbors 
                            if n[1] < len(grid) and n[0] < len(grid) 
                                and n[1] >= 0 and n[0] >= 0])                      
                      
        nx = scores[0][1]
        #print(nx) 
        path = inner(nx, grid, vs, visited, path)
        print(path) 
        return path
    
    up = [0, -1]
    down = [0, 1]
    left = [-1,0]
    right = [1,0]
    if dx == "fwd":
        vs = [down, right]
    elif dx == "rev":
        vs = [up, left]
    else:
        raise ValueError("bad direction")
    return inner(point, grid, vs)


def dfs2(grid, point, end=(9,9), dx="fwd"):        
    def inner(point, grid, vs, visited = set(), path=[]):
        visited.add(point)
        if point == end:
            path.append(point)
            print("blonk!")
            return path
        path.append(point)
       
        nbors = [(point[0]+v[0], point[1]+v[1]) for v in vs]
        
        scores = sorted([(grid[n[1]][n[0]], n) for n in nbors 
                            if n[1] < len(grid) and n[0] < len(grid) 
                                and n[1] >= 0 and n[0] >= 0])
        cv = 0
        for sc in scores:
            nx = sc[1]
            if nx not in visited: break #not visited before
            cv += 1
        if cv == len(nbors):
            return path
        print(nx) 
        return inner(nx, grid, vs, visited, path)
    
    up = [0, -1]
    down = [0, 1]
    left = [-1,0]
    right = [1,0]
    if dx == "fwd":
        vs = [down, right]
    elif dx == "rev":
        vs = [up, left]
    else:
        raise ValueError("bad direction")
    return inner(point, grid, vs)
    
def dfs(grid, point, end=(9,9), dx="fwd"):        
    def inner(point, grid, vs, visited = set(), path=[], paths=[]):
        
        visited.add(point)
        if point == end:
            path.append(point)
            #qq()
            return [list(path)] 
        path.append(point)
       
        candidates = [(point[0]+v[0], point[1]+v[1]) for v in vs]
        nbors = [n for n in candidates if n[1] < len(grid) and n[0] < len(grid) 
                                and n[1] >= 0 and n[0] >= 0]
        
        for nx in nbors:
            #print(nx)
            #qq()
            new_paths = inner(nx, grid, vs, visited, path, paths)
            
            if len(new_paths) == 1:
                paths.append(new_paths[0])
            else:
                paths = new_paths
            print(path)
            qq()
        
        return paths
    
    up = [0, -1]
    down = [0, 1]
    left = [-1,0]
    right = [1,0]
    if dx == "fwd":
        vs = [down, right]
    elif dx == "rev":
        vs = [up, left]
    else:
        raise ValueError("bad direction")
        
    paths = inner(point, grid, vs)
    qq()
    return paths

def score_path(path, grid):
    return sum([grid[x[1]][x[0]] for x in path])

def main():
    #path = dfs(grid, (0,0))
    #path = dfs4(grid, (9,9), (0,0), "rev")
    #path = dfs4(grid, (0,0))
    path = dfs5(grid, (0,0))
    print(path)
    print_grid(grid, path)
    print(score_path(path, grid))
    
main()
