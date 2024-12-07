import copy
debug = 0
if debug:
    #lines = ''.join(open("./day6_ex.txt").readlines()).split()
    lines = ''.join(open("./day6_t3.txt").readlines()).split()
else:
    lines = ''.join(open("./day6.txt").readlines()).split()

grid = [[x for x in list(line.strip())] for line in lines]

limy = len(lines)
limx = len(lines[0])

def print_grid(grid, found=[]):
    for irow, line in enumerate(grid):
        pl = ""
        for icol, char in enumerate(line):
            fill = False
            if (irow,icol) in found:
                pl += "X"
            else:
                pl += char
        print(pl)
    print("*******************************")

def find_start_pos(grid):
    for irow, line in enumerate(grid):
        for icol, char in enumerate(line):
            if char == '^':
                return (irow,icol)

up, right, down, left = (-1,0), (0,1), (1,0), (0,-1)
dirs = (up, right, down, left)

def pt2(grid):
    found = set()
    #all_pos = itertools.chain.from_iterable([[(x,y) for x in range(limx)] for y in range(limy)])
    start_pos = find_start_pos(grid)
    paths = set()
    walkable = walkies((0,0), grid, start_pos,paths, True)
    #plops = [(6,3), (7,6), (7,7), (0,0)]
    plops = walkable
    
    oc = 0
    for plop in plops:
        oc += 1
        if oc % 100 == 0:
            print(plop)

        res = walkies(plop, grid, start_pos, paths)
        if res:
            found.add(res)
    #print(path)
    if debug:
        tmp = set(found)
        tmp.add(start_pos)
        print_grid(grid, tmp)
    print("pt2: %d" % len(found))

def walkies(plop, ogrid, start_pos, paths, no_plop=False):
    grid = copy.deepcopy(ogrid)
    path = set()
    if plop == (3,4):
        stop = 0
    if debug == 1:
        print("plopped to %s" % str(plop))
    #if grid[plop[0]][plop[1]] != '.':
    #    return
    #if (plop[0],plop[1]) == start_pos:
    #    return
    if not no_plop:
        grid[plop[0]][plop[1]] = 'O'
    goidx = 0
    go = dirs[goidx]
    cyc = False
    pos = start_pos
    count = 0
    #while not cyc:
    while True:
        count += 1
        if no_plop:
            path.add(pos)
        grid[pos[0]][pos[1]] = "%"
        look = pos[0] + go[0], pos[1] + go[1]
        lr, lc = look
        if lr >= limy or lc >= limx or lr <0 or lc < 0:
            #print("leaving map")
            break
        if count > 17000:
            print("found cycle at %s" % str(look))
            cyc = True
            break
        next = grid[lr][lc]
        if next in ('#', 'O'):
            goidx += 1
            goidx = goidx % len(dirs)
            go = dirs[goidx]
            look = pos[0] + go[0], pos[1] + go[1]
            lr, lc = look
            if grid[lr][lc] in ('#', 'O'):
                goidx += 1
                goidx = goidx % len(dirs)
                go = dirs[goidx]
                look = pos[0] + go[0], pos[1] + go[1]
                lr, lc = look
                if grid[lr][lc] in ('#', 'O'):
                    break
        pos = look
    grid[plop[0]][plop[1]] = '.'
    res = None
    if path in paths:
        return
    if cyc:
        res = plop
    elif no_plop:
        res = path
    return res

def pt1(grid):
    if debug:
        print_grid(grid)
    goidx = 0
    go = dirs[goidx]
    path = set()
    pos = find_start_pos(grid)
    print(pos)
    while True:
        path.add(pos)
        look = pos[0] + go[0], pos[1] + go[1]
        lr, lc = look
        if lr >= limy or lc >= limx or lr <0 or lc < 0:
            print("leaving map")
            break
        next = grid[lr][lc]
        if next == '#':
            goidx += 1
            goidx = goidx % len(dirs)
            go = dirs[goidx]
            look = pos[0] + go[0], pos[1] + go[1]
        pos = look
    print(path)
    print_grid(grid, path)
    print("pt1: %d" % len(path))

#pt1(grid)
pt2(grid)
