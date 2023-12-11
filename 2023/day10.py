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
    #if cur == ".":
    #    return []

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
        #print(adj)
        print("%s %s" % (cur, adj))
        if cur == "S":
            if OPP[dir] in pipes[adj]:
                #found.append((ny, nx))
                found.append((nx, ny))
        else:
            try:
                if OPP[dir] in pipes[adj] and dir in pipes[cur]:
                    #found.append((ny, nx))
                    found.append((nx, ny))
            except KeyError:
                print("HEY")
        
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
        print("###########")
        fx, fy = frontier.pop()
        found = set(it(l0, fx, fy, pipes, dirs))
        for fffx, fffy in found:
            if l0[fffy][fffx] == ".":
                print("ffffffffff")
        frontier = frontier.union(found)
        frontier = frontier.difference(path)
        path.add((fx,fy))
        print(frontier)
    
    print("########")
    print(path)
    ans = int(len(path)/2)
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

def main():
    with open("day10_data.txt") as h0:
        l0 = [list(x.strip()) for x in h0.readlines()]
    ans = pt1(l0)
    print(ans)

test()
main()