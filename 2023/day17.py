import heapq as hq # priority queue
from collections import defaultdict
from copy import deepcopy

# Modified Dijkstra

def main():
    #with open("day17_ex2.txt") as h0: #16 p1
    #with open("day17_ex.txt") as h0: #102 p1, 94 p2
    with open("day17_data.txt") as h0:
    #with open("day17_ex3.txt") as h0: # 71 p2 ???
        l0 = [list(x.strip()) for x in h0.readlines()]
    #ans, path = pt1(l0)
    #print(path)
    #print(ans)
    ans2, path2 =pt2(l0)
    print(path2)
    print(ans2)
    for pos in path2:
        l0[pos[1]][pos[0]] = "*"
    pg(l0)

def pg(g):
    for row in g:
        print("".join(row))
    print("===========================")

def gxy(g, x, y): #sugary
    return int(g[y][x])

OPP = {"N" :"S", "E":"W", "S":"N", "W":"E"}

def pt2(g):
    spos = (0,0)
    visited = set()
    visited.add((spos, "", 0))

    #score, pos, direction,  step count, path
    pq = [(0, spos, "", 0, [])]

    while len(pq) > 0:
        val, pos, curdir, scount, path = hq.heappop(pq)
        #if pos == (8,2):
        #if pos == (8,0):
        #    print("break")
        if pos == (len(g[0])-1, len(g)-1):
            # reached destination, return result
            return val, path

        for ndir, nbor in connect4(pos).items():
            nx, ny = nbor
            # bounds check
            if (0 > nx or nx > len(g[0])-1) or (0 > ny or ny > len(g)-1):
                continue

            nscount = 1
            # disallow based on turn after 10 rule
            if curdir == ndir or curdir == '':
                # same direction as before
                if scount > 9:
                    continue
                else:
                    nscount = scount + 1
            else:
                # can we turn yet?
                if scount < 4:
                    continue
                else:
                    nscount = 1
                    
            # can't reverse
            if curdir != "" and OPP[curdir] == ndir:
                continue
                
            # calc score and reject duplicate states
            distance = val + gxy(g, nx, ny)
            state = (nbor, ndir, nscount)
            if state in visited:
                continue
    
            # all good, store visited state and push next node
            visited.add(state)

            npath = path[:] #copy list
            npath.append(nbor)
            hq.heappush(pq, (distance, nbor, ndir, nscount, npath))
    return "oops", "opps"

def pt1(g):
    spos = (0,0)
    visited = set()
    visited.add((spos, "", 0))

    #score, pos, direction,  step count, path
    pq = [(0, spos, "", 0, [])]

    while len(pq) > 0:
        val, pos, curdir, scount, path = hq.heappop(pq)
        if pos == (2,0):
            print("break")
        if pos == (len(g)-1, len(g[0])-1):
            # reached destination, return result
            return val, path

        for ndir, nbor in connect4(pos).items():
            nx, ny = nbor
            # bounds check
            if (0 > nx or nx > len(g[0])-1) or (0 > ny or ny > len(g)-1):
                continue

            nscount = 1
            # disallow based on turn after 3 rule
            if curdir == ndir or curdir == '':
                if scount > 2:
                    continue
                else:
                    nscount = scount + 1
            # can't reverse
            if curdir != "" and OPP[curdir] == ndir:
                continue
                
            # calc score and reject duplicate states
            distance = val + gxy(g, nx, ny)
            state = (nbor, ndir, nscount)
            if state in visited:
                continue
    
            # all good, store visited state and push next node
            visited.add(state)

            npath = path[:] #copy list
            npath.append(nbor)
            hq.heappush(pq, (distance, nbor, ndir, nscount, npath))

def connect4(pos):
    x,y = pos
    north = (x,y-1)
    south = (x, y+1)
    east = (x+1, y)
    west = (x-1, y)
    return {"N": north, "E": east, "S": south, "W": west}

main()