def find_start(l0):
    for y, row in enumerate(l0):
        print("".join(row))
        if "S" in row:
            startx = row.index("S")
            starty = y
    return startx, starty


def it(l0, xx,yy, pipes, dirs):
    OPP = {"N" :"S", "E":"W", "S":"N", "W":"E"}
    cur = l0[yy][xx]

    found = []
    for dir, vec in dirs.items():
        print(dir)
        nx = xx+vec[0]
        ny = yy+vec[1]
        if nx < 0 or ny < 0:
            continue
        if nx > (len(l0[0])-1) or ny > (len(l0)-1):
            continue
        adj = l0[ny][nx]
        if adj in (".", "S"):
            continue
        print("%s %s" % (cur, adj))
        if cur == "S":
            if OPP[dir] in pipes[adj]:
                found.append((nx, ny))
        else:
            if OPP[dir] in pipes[adj] and dir in pipes[cur]:
                found.append((nx, ny))
        
    return found

def pt1(l0):
    path = find_path(l0)
    ans = int(len(path)/2) # the shortest route is just half the path length!!
    print(ans)
    return ans

def find_path(l0):
    startx, starty = find_start(l0)
    #print(l0[starty][startx])

    dirs={}
    dirs["N"] = (0,-1)
    dirs["E"] = (1,0)
    dirs["S"] = (0,1)
    dirs["W"] = (-1,0)

    pipes={}
    pipes["|"] = ("N","S")
    pipes["-"] = ("E","W")
    pipes["L"] = ("N","E")
    pipes["J"] = ("N","W")
    pipes["7"] = ("S","W")
    pipes["F"] = ("S","E")

    path = set()
    path.add((startx, starty))

    frontier = set(it(l0, startx, starty, pipes, dirs))

    while frontier:
        fx, fy = frontier.pop()
        found = set(it(l0, fx, fy, pipes, dirs))
        frontier = frontier.union(found)
        frontier = frontier.difference(path)
        path.add((fx,fy))
    
    print("########")
    print(path)
    return path

def test():
    with open("day10_ex.txt") as h0:
        l0 = [list(x.strip()) for x in h0.readlines()]
    ans = pt1(l0)
    assert ans == 4
    
    with open("day10_ex1.txt") as h0:
        l0 = [list(x.strip()) for x in h0.readlines()]
    ans = pt1(l0)
    assert ans == 4

    with open("day10_ex2.txt") as h0:
        l0 = [list(x.strip()) for x in h0.readlines()]
    ans = pt1(l0)
    assert ans == 8

    with open("day10_ex3.txt") as h0:
        l0 = [list(x.strip()) for x in h0.readlines()]
    ans = pt1(l0)
    assert ans == 8

def pt1_main():
    with open("day10_data.txt") as h0:
        l0 = [list(x.strip()) for x in h0.readlines()]
    ans = pt1(l0)
    print(ans)

def pt2():
    #with open("day10_pt2_ex0.txt") as h0:
    #with open("day10_pt2_ex1.txt") as h0:
    #with open("day10_pt2_ex2.txt") as h0:
    #with open("day10_pt2_ex3.txt") as h0:
    with open("day10_data.txt") as h0:
        l0 = [list(x.strip()) for x in h0.readlines()]

    path = find_path(l0) # this from part 1 - came in handy!

    candi = set()
    for y, row in enumerate(l0):
        print("".join(row))
        for x, char in enumerate(row):
            if char == ".":
                candi.add((x,y))
            elif (x,y) not in path:
                candi.add((x,y))
    print(sorted(sorted(list(candi), key= lambda x: x[1]), key= lambda x: x[0])) # sanity check

    inside = set()
    for x,y in candi:
        print((x,y))

        # ray casting method - just look either left or right (depending on where S is)
        #look left
        #l_col_old = l0[y][0:x] # this doesn't work because it includes non-loop pipes
        l_col = []
        for xx in range(0,x):
            if (xx,y) in path:
                l_col.append(l0[y][xx])

        #look right
        #r_col_old = l0[y][x+1:len(l0[y])] # this doesn't work because it includes non-loop pipes
        r_col = []
        for xx in range(x+1,len(l0[y])):
            if (xx,y) in path:
                r_col.append(l0[y][xx])

        if "S" in r_col: # S can be anything so breaks the 
            edges = l_col.count("7") + l_col.count("|") + l_col.count("F")
        else:
            edges = r_col.count("7") + r_col.count("|") + r_col.count("F")
        if edges % 2 == 1: # odd means inside, even means outside... maths or sth!
            inside.add((x,y))
        
    for y, row in enumerate(l0):
        for x, char in enumerate(row):
            if (x,y) in inside:
                #l0[y][x] = "I"
                l0[y][x] = "*"

    for y, row in enumerate(l0):
        print("".join(row))

    print(inside)
    print(len(inside))

test()
#pt1_main()
pt2()
