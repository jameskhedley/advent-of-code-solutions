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
        #print(frontier)
    
    print("########")
    print(path)
    ans = int(len(path)/2) # the shortest route is just half the path length!!
    print(ans)
    return ans

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
    with open("day10_pt2_ex2.txt") as h0:
        l0 = [list(x.strip()) for x in h0.readlines()]

    candi = set()
    for y, row in enumerate(l0):
        print("".join(row))
        for x, char in enumerate(row):
            if char == ".":
                candi.add((x,y))
    print(sorted(sorted(list(candi), key= lambda x: x[1]), key= lambda x: x[0]))

    inside = set()
    for x,y in candi:
        print((x,y))
        #look left
        l_col = l0[y][0:x]

        #look right
        r_col = l0[y][x+1:len(l0[y])]
        print(r_col)
        #look up
        up_col = []
        for _yy, row in enumerate(l0[:y+1]):
            up_col.append(row[x])
        #look down
        down_col = []
        for _yy, row in enumerate(l0[y+1:]):
            down_col.append(row[x])
        if (x,y) == (3,2):
            print("break")

        if (("|" in l_col or "F" in l_col or "L" in l_col)
         and ("|" in r_col or "7" in r_col or "J" in r_col)
         and ("-" in up_col or "F" in up_col or "7" in up_col)
         and ("-" in down_col or "L" in down_col or "J" in down_col)):
            inside.add((x,y))

    print(inside)
    print(len(inside))
    for y, row in enumerate(l0):
        for x, char in enumerate(row):
            if (x,y) in inside:
                #l0[y][x] = "I"
                l0[y][x] = "*"

    for y, row in enumerate(l0):
        print("".join(row))

    dirs={}
    dirs["N"] = (0,-1)
    dirs["E"] = (1,0)
    dirs["S"] = (0,1)
    dirs["W"] = (-1,0)
    
    remove = set()
    for x,y in inside:
        for _, vec in dirs.items():
            nx = x+vec[0]
            ny = y+vec[1]
            if l0[ny][nx] == ".":
                remove.add((x,y))
    inside -= remove
    print(inside)
    print(len(inside))

#test()
#pt1_main()
pt2()
