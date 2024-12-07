import copy
debug = 0
if debug:
    lines = ''.join(open("./day4_ex.txt").readlines()).split()
else:
    lines = ''.join(open("./day4.txt").readlines()).split()

grid = [[x for x in list(line.strip())] for line in lines]

limy = len(lines)
limx = len(lines[0])

def print_grid(grid, found=[]):
    for irow, line in enumerate(grid):
        pl = ""
        for icol, char in enumerate(line):
            fill = False
            for path in found:
                if (irow,icol) in path:
                    fill = True
            if fill:
                pl += "%s" % char
            else:
                pl += "."
        print(pl)
    print("*******************************")

def path_from_point(pos, candidate):
    path = []
    for c in candidate:
        new = (pos[0] + c[0], pos[1]+c[1])
        path.append(new)
    return path
    
def pt1(grid, debug):
    up = [(0,0),(0,-1), (0,-2), (0,-3)]
    down = [(0,0),(0,1), (0,2), (0,3)]
    left = [(0,0),(-1,0),(-2,0), (-3,0)]
    right = [(0,0),(1,0),(2,0), (3,0)]
    up_right = [(0,0),(1,-1),(2,-2), (3,-3)]
    down_right = [(0,0),(1,1),(2,2), (3,3)]
    down_left = [(0,0),(-1,1),(-2,2), (-3,3)]
    up_left = [(0,0),(-1,-1),(-2,-2), (-3,-3)]

    candidates = [up, down, left, right, up_right, down_right, down_left, up_left]
    if debug:
        print_grid(grid)
    paths = []
    for irow, line in enumerate(grid):
        for icol, char in enumerate(line):
            if char != 'X':
                continue
            for candidate in candidates:
                np = path_from_point((irow, icol), candidate)
                add = False
                fw = ""
                for p in np:
                    if p[0] < 0 or p[0] >= limx or p[1] < 0 or p[1] >= limy:
                        break
                    nc =  grid[p[0]][p[1]]
                    fw += nc
                if fw == "XMAS":
                    paths.append(np)
    if debug:
        for p0 in paths:
            print(p0)
    return (len(paths))

def rotate(xmas):
    listy = []
    rot = list(zip(*xmas[::-1]))
    for x in rot:
        listy.append(list(x))
    return listy

def pt2(grid, debug):
    paths = []
    X = [(-1,-1), (-1,1), (1,-1),(1,1)]

    XMAS = [['M', 'S'],
            ['M', 'S']]

    for irow, line in enumerate(grid):
        for icol, char in enumerate(line):
            if irow == 3 and icol == 4:
                dbg = 1
            if char != 'A':
                continue
            np = path_from_point((irow, icol), X)
            found = []
            for p in np:
                if p[0] < 0 or p[0] >= limx or p[1] < 0 or p[1] >= limy:
                    break
                nc =  grid[p[0]][p[1]]
                found += nc
            if len(found) < 4:
                continue
            if found.count('M')==2 and found.count('S')==2:
                ok = False
                errm = [found[0:2],found[2:]]
                if errm == XMAS:
                    paths.append(np)
                    continue
                rot = copy.deepcopy(XMAS)
                for t0 in range(3):
                    rot = rotate(rot)
                    if errm == rot:
                        ok = True
                        paths.append(np)
                        break


    if debug:
        for p0 in paths:
            print(p0)
        print_grid(grid, paths)
    return len(paths)

r1 = pt1(grid, debug)
print(r1)
r2 = pt2(grid, debug)
print(r2)