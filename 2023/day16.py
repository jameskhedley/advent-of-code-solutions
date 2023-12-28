from collections import defaultdict
import time

def main():
    #with open("day16_ex.txt") as h0:
    with open("day16_data.txt") as h0:
        l0 = [list(x.strip()) for x in h0.readlines()]
    for row in l0:
        print(row)
    print("===========================")
    #pt1(l0)
    pt2(l0)

nxt = {"E": (1,0), "W": (-1,0), "S": (0,1), "N": (0,-1)}
flex = {"/": {"E":"N", "W":"S", "N":"E", "S":"W"},
        "\\": {"E":"S", "W":"N", "N":"W", "S":"E"}}

def new_beam(pos, direction):
    return {"pos": pos, "direction": direction}

#def pt2

def pt2(grid):
    all_routes = set()
    for y, row in enumerate(grid):
        for x, col in enumerate(row):
            if y == 0 or y == len(grid) - 1 or x ==0 or x == len(row) -1 :
                if y == 0:
                    init_dir = "S"
                elif y ==  len(grid) - 1:
                    init_dir = "N"
                elif x ==0:
                    init_dir = "E"
                elif x == len(row) -1:
                    init_dir = "W"
                ans = calc_beam(grid, (x,y), init_dir, viz=False)
                if len(all_routes) % 10 == 0:
                    print("calc for cell %d, %d and direction %s, is %d" % (x,y, init_dir, ans))
                all_routes.add(ans)

    print(max(all_routes))

def pt1(grid):
    ans = calc_beam(grid, (0,0), "E", viz=True)
    print(ans)

def calc_beam(grid, initial_pos, initial_direction, viz=False):
    beams = {}
    energised = set()
    beams[0] = new_beam(initial_pos, initial_direction)
    loop_detect = defaultdict(list)
   
    while beams:
        idx, beam = beams.popitem()
        
        loop_detect[beam["pos"]].append(beam["direction"])
        
        beam, nb, grid, energised = iterate_beam(grid, beam["pos"], beam["direction"], energised)
        if in_bounds(beam["pos"], grid):
            ldb = loop_detect.get(beam["pos"], [])
            if beam["direction"] not in ldb:
                beams[idx] = beam
        if nb and in_bounds(nb["pos"], grid):
            if beams:
                beams[max(beams.keys())+1] = nb
            else:
                beams[0] = nb
        #print(beams)
        if viz:
            if len(energised) % 500 == 0:
                pg(grid)
                time.sleep(0.5)

    return(len(energised))

def pg(grid):
    for row in grid:
        print("".join(row))

def in_bounds(pos, grid):
    x,y = pos
    return False if x <0 or x >= len(grid[0]) or y < 0 or y >= len(grid) else True

def iterate_beam(grid, pos, direction, energised):
    x,y = pos
    nb = None
    char = grid[y][x]
    #if (x,y) == (1,7):
    #    print("break")
    nd = None
    if char in (".", "#"):
        dx, dy = nxt[direction]
        pos = x+dx, y+dy
    elif char == "-":
        if direction in ("E", "W"):
            # pointy edge, not split
            dx, dy = nxt[direction]
            pos = x+dx, y+dy
        else:    
            # flat edge, split beam
            nd = "E"
            dx, dy = nxt[nd]
            pos = x+dx, y+dy
            # new beam
            ndx, ndy = nxt["W"]
            npos = x+ndx, y+ndy
            nb = new_beam(npos, "W")
    elif char == "|":
        if direction in ("N", "S"):
            # pointy edge, not split
            dx, dy = nxt[direction]
            pos = x+dx, y+dy
        else:
            # flat edge, split beam
            nd = "N"
            dx, dy = nxt[nd]
            pos = x+dx, y+dy
            # new beam
            ndx, ndy = nxt["S"]
            npos = x+ndx, y+ndy
            nb = new_beam(npos, "S")
    else:
        nd = flex[char][direction]
        dx, dy = nxt[nd]
        pos = x+dx, y+dy
        
    if not nd:
        nd = direction
    #curr_beam = new_beam(pos, nd or direction)
    curr_beam = new_beam(pos, nd)
    if char == ".":
        grid[y][x] = "#"
    energised.add((x,y))
    return curr_beam, nb, grid, energised


main()