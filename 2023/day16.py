def main():
    with open("day16_ex.txt") as h0:
    #with open("day16_data.txt") as h0:
        l0 = [list(x.strip()) for x in h0.readlines()]
    #test()
    for row in l0:
        print(row)
    print("===========================")
    pt1(l0)
    #pt2(l0)

#nxt = {"E": (0,1), "W": (0,-1), "S": (1,0), "N": (-1,0)}
nxt = {"E": (1,0), "W": (-1,0), "S": (0,1), "N": (0,-1)}
#opp = {"E":"W", "W":"E", "N":"S", "S":"N"} # TODO unused
flex = {"/": {"E":"N", "W":"S", "N":"E", "S":"W"},
        "\\": {"E":"S", "W":"N", "N":"W", "S":"E"}}

def new_beam(pos, direction):
    return {"pos": pos, "direction": direction}

def pt1(grid):
    beams = {}
    beams[0] = new_beam((0,0), "E")
    
    
    while beams:
        idx, beam = beams.popitem()
        beam, nb, grid = iterate_beam(grid, beam["pos"], beam["direction"])
        if in_bounds(beam["pos"], grid):
            beams[idx] = beam
        if nb and in_bounds(nb["pos"], grid):
            if beams:
                beams[max(beams.keys())+1] = nb
            else:
                beams[0] = nb
        print(beams)
    pg(grid)

def pg(grid):
    for row in grid:
        print("".join(row))

def in_bounds(pos, grid):
    x,y = pos
    return False if x <0 or x >= len(grid[0]) or y < 0 or y >= len(grid) else True

def iterate_beam(grid, pos, direction):
    x,y = pos
    nb = None
    char = grid[y][x]
    if (x,y) == (1,7):
        print("break")
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
    return curr_beam, nb, grid


main()