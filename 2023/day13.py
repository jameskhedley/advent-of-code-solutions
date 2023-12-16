from itertools import chain

def main():
    #with open("day13_ex.txt") as h0:
    #with open("day13_ex2.txt") as h0:
    with open("day13.txt") as h0:
        l0 = [x.strip() for x in h0.readlines()]
    test()
    #pt1(l0)
    pt2(l0)

def test():
    test0 = "#.##..##."

    assert(try_mirror_pos_vert(test0, 1) == ("#", "."))          # 0:1, 1:2 len=1
    assert(try_mirror_pos_vert(test0, 2) == ("#.", "##"))        # 0:2, 2:4 len=2
    assert(try_mirror_pos_vert(test0, 3) == ("#.#", "#.."))      # 0:3, 3:6 len=3
    assert(try_mirror_pos_vert(test0, 4) == ("#.##", "..##"))    # 0:4, 4:8 len=4
    assert(try_mirror_pos_vert(test0, 5) == (".##.", ".##."))    # 1:5, 5:9 len=4
    assert(try_mirror_pos_vert(test0, 6) == ("#..", "##."))      # 3:6, 6:9 len=3
    assert(try_mirror_pos_vert(test0, 7) == (".#", "#."))        # 5:7, 7:9 len=2
    assert(try_mirror_pos_vert(test0, 8) == ("#", "."))          # 7:8, 8:9 len=1

    assert(5 in find_mirrors(test0)) # returns set
    print("Tests passed")

def find_mirrors(row):
    vmirrors = set()
    for c in range(1,len(row)):
        l,r = try_mirror_pos_vert(row, c)
        if l == r[::-1]:
            vmirrors.add(c)
    return vmirrors
    
def try_mirror_pos_vert(row, c):
    #            123456789
    # example = "#.##..##."
    end = min(len(row), c*2)
    l0 = row[c-(end-c):c]
    r0 = row[c:end]
    return l0, r0

def parse(l0):
    grids = []
    grid = []
    for line in l0:
        if line:
            grid.append(tuple(line))
        else:
            grids.append(grid)
            grid = []
    grids.append(grid)
    #print(grids)
    return grids

def pt1(l0):
    grids = parse(l0)
    ans = 0
    for grid in grids:
        grid_ans = 0
        vms = []
        for row in grid:
            vms.append(find_mirrors(row))
        if vms:
            intersect = vms[0].intersection(*vms)
            if intersect:
                grid_ans += intersect.pop()
                continue
        rotated = zip(*grid[::1])
        vms = []
        for row in rotated:
            vms.append(find_mirrors(row))
        if vms:
            intersect = vms[0].intersection(*vms)
            if intersect:
                grid_ans += intersect.pop() * 100
        print(grid_ans)
        ans += grid_ans
    print(ans)

def pt2(l0):
    grids = parse(l0)
    ans = 0
    for grid in grids:
        grid_ans = 0
        vms = []
        for row in grid:
            vms.append(find_mirrors(row))
        grid_ans += calc_p2(vms)
        rotated = zip(*grid[::1])
        vms = []
        for row in rotated:
            vms.append(find_mirrors(row))
        grid_ans += calc_p2(vms) * 100
        print(grid_ans)
        ans += grid_ans
    print(ans)

def calc_p2(vms):
    ans = 0
    if vms:
        counts = list(chain(*vms))
        sc = set(counts)
        for c in sc:
            if counts.count(c) == len(vms)-1:
                ans += c
    #print(ans)
    return ans

main()