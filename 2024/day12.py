from collections import deque, defaultdict
import itertools

def read_data(fn):
    h0 = open(fn)
    lines = h0.readlines()
    return [[x for x in list(line.strip())] for line in lines]

#data = read_data('day12_ex.txt') #p2 1206
#data = read_data('day12_ex0.txt') #p2 80
#data = read_data('day12_ex1.txt') #p2 236 
#data = read_data('day12_ex2.txt') #p 2368
data = read_data('day12_data.txt')

def tests():
    print("part 2 tests")

    data = [['O', 'O', 'O'],
            ['X', 'X', 'O'],
            ['X', 'X', 'O']]
    res = sides_from_garden(data, 'X')
    #assert res==1
    assert res==4

    data = [['O', 'O', 'X'],
            ['X', 'X', 'X'],
            ['O', 'O', 'X']]
    res = sides_from_garden(data, 'X')
    assert res==8

    data = [['O', 'O', 'O'],
            ['X', 'X', 'X'],
            ['O', 'O', 'O']]
    res = sides_from_garden(data, 'X')
    assert res==4

    data = [['O', 'O', 'O'],
            ['X', 'X', 'O'],
            ['O', 'O', 'O']]
    res = sides_from_garden(data, 'X')
    assert res==4

    # X inside Os - 4 corners/sides
    data = [['O', 'O', 'O'],
            ['O', 'X', 'O'],
            ['O', 'O', 'O']]
    res = sides_from_garden(data, 'X')
    assert res==4
    

    print("tests passed")

def sides_from_garden(garden, search_plant):
    plots = garden_bfs(garden)
    for plant, regions in plots.items():
        if plant != search_plant: continue
        for region in regions:
            sid = sides(region, plant, garden)
    return sid

def sides(region, plant, garden):
    ex_corners = 0
    in_corners = 0
    up, upleft, left, downleft, down, downright, right, upright = (0, -1), (-1, -1), (-1,0), (-1,1), (0,1), (1,1), (1,0) , (1,-1)
    dirs = (up, upleft, left, downleft, down, downright, right, upright)

    region = list(region)
    for cell in region:
        if cell == (0,0):
            stop = 1
        nbors = []
        for d0 in dirs:
            nbors.append((cell[0] + d0[0], cell[1] + d0[1]))
    
        # check 4 corners of 9-grid for outside corners to centre cell
        ctl = up, upleft, left
        ctr = up, upright, right
        cdl = left, downleft, down
        cdr = right, downright, down
        for corna in (ctl, ctr, cdl, cdr):
            corna_cells = []
            for cdir in corna:
                #these are actual grid coords so can't be less than 0 or gt then garden size (?)
                nc = (cell[0] + cdir[0], cell[1] + cdir[1])
                #if nc[0] < 0 or nc[1] < 0 or nc[0] >= len(garden) or nc[1] >= len(garden[0]): #TODO make this proper size
                #    continue
                corna_cells.append(nc)
            if len(corna_cells) < 3:
                continue
            found = [] # list of cells with the same plant
            for x in corna_cells:
                if x in region:
                    found.append(x)
            if len(found) == 0:
                ex_corners += 1 #found an 3-sized l-shape at the corner
            elif len(found) == 2:
                if not cells_are_neighbours(*found):
                    in_corners += 1
            elif len(found) == 1:
                if cells_are_diagonal_opposite(cell, found[0]):
                    in_corners += 1
               
    return ex_corners + in_corners

def cells_are_neighbours(cell0, cell1):
    x0, y0 = cell0
    x1, y1 = cell1
    if (x0 == x1 and abs(y0-y1) == 1) or (y0 == y1 and abs(x0-x1)==1):
        return True
    else:
        return False

def cells_are_diagonal_opposite(cell0, cell1):
    x0, y0 = cell0
    x1, y1 = cell1
    if (abs(x0-x1) + abs(y0-y1) == 2):
        return True
    else:
        return False

def part2(garden):
    price = 0
    plots = garden_bfs(garden)
    for plant, regions in plots.items():
        for region in regions:
            area = len(region)
            s0 = sides(region, plant, garden)
            print("Region with plant %s, area %d sides %d price %d" % (plant, area, s0, area*s0))
            price += (area*s0)
    print("part 2: %d" % price)

def part1(garden):
    plots = garden_bfs(garden)
    print(plots)

    total = 0
    for plant, regions in plots.items():
        for region in regions:
            area = len(region)
            perim = perimeter(region)
            print("Region with plant %s, score %d" % (plant, area*perim))
            total += area*perim
    print("part 1: %d" % total)

def perimeter(region):
    perim = 0
    up, down, left, right = (0, -1), (0, 1), (-1, 0), (1, 0)
    for cell in region:
        ubor = (cell[0] + up[0], cell[1] + up[1])
        dbor = (cell[0] + down[0], cell[1] + down[1])
        lbor = (cell[0] + left[0], cell[1] + left[1])
        rbor = (cell[0] + right[0], cell[1] + right[1])
        for nbor in (ubor, dbor, lbor, rbor):
            if nbor not in region:
                perim+=1
    return perim

def garden_bfs(maze):
    mode = 'bfs'
    queue = deque()
    plots = defaultdict(list)
    cells = [[(x,y) for x in range(len(maze))] for y in range(len(maze[0]))]
    not_visited = set(itertools.chain.from_iterable(cells))
    while not_visited:
        start = list(not_visited)[0]
        queue.append(start)
        region = set()
        plant = maze[start[0]][start[1]]
        while queue:
            if mode == 'dfs':
                u = queue.pop()
            elif mode == 'bfs':
                u = queue.popleft()
            if not u in not_visited:
                continue
            region.add(u)
            not_visited.remove(u)
            if maze[u[0]][u[1]] != plant:
                continue
            for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0)]: # Adjacent squares
                nbor = (u[0] + new_position[0], u[1] + new_position[1])
                if nbor[0] > (len(maze) - 1) or nbor[0] < 0 or nbor[1] > (len(maze[0]) -1) or nbor[1] < 0:
                    continue
                if maze[nbor[0]][nbor[1]] != plant:
                    continue
                if nbor in not_visited:
                    queue.append(nbor)
        plots[plant].append(region)
            

    return plots

#tests()
#part1(data)
part2(data)
