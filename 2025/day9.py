# part 2 is slow but works, at least didn't cheat and use shapely!
import math
ex=False

def read_data():
    if ex:
        h0 = open('day9_ex.txt')
    else:
        h0 = open('day9.txt')
    data = [(int(x), int(y)) for x, y in [line.strip().split(',') for line in h0.readlines()]]
    return data

def print_grid(data, rect=[], greens=[]):
    dimx = max([x for x,y in data ]) 
    dimy = max([y for x,y in data ]) 

    grid = []
    for _ in range(dimy+2):
        grid.append(["."]*(dimx+2))
    if greens:
        for (x,y) in greens:
            grid[y][x] = 'X'
    for (x,y) in data:
        grid[y][x] = '#'
    if rect:
        print(rect)
        for x in range(min(rect[0][0], rect[1][0]),max(rect[0][0], rect[1][0])+1):
            for y in range(min(rect[0][1], rect[1][1]),max(rect[0][1], rect[1][1])+1):
                grid[y][x] = 'O'
    for row in grid:
        print(''.join(row))
    print("="*(dimx+2))

def calc_distances(data):
    dist = {}
    for nump, point in enumerate(data):
        print("Calculating distances: %d/%d" % (nump, len(data)))
        for pp in data:
            if point == pp:
                continue
            if (pp,point) in dist.keys():
                continue
            dist[(point, pp)] = math.sqrt((point[0]-pp[0])**2 + (point[1]-pp[1])**2)
    return dist

def part1(data):
    dist = calc_distances(data)
    dist_desc = dict(sorted([(dx,dy) for dx,dy in dist.items()], key=lambda x: x[1], reverse=True))
    if ex:
        for dd in list(dist.keys())[-3:]:
            print_grid(data, dd)
    (x0,y0),(x1,y1) = list(dist_desc.keys())[0]
    mx = max(x0,x1) - min(x0,x1)
    my = max(y0,y1) - min(y0,y1)
    ans = (mx+1)*(my+1)
    return ans

def part2(data):
    borderlines = {}
    dist = calc_distances(data)
    dist_asc = dict(sorted([(dx,dy) for dx,dy in dist.items()], key=lambda x: x[1], reverse=False))
    #connect each point to its nearest neighbour
    # find outline as set of lines, each point will have one nearest vertically and one nearest horizontally
    for count, point in enumerate(data):
        if count % 50 == 0:
            print("Connecting points: %d/%d" % (count, len(data)))
        new_bl = {"horiz": None, "vert": None}
        candis = [(k[0],k[1]) for k in dist_asc.keys() if k[0]==point or k[1]==point]
        for cand in candis:
            c = cand[0] if cand[1] == point else cand[1]
            if c[0] == point[0]:
                if not new_bl['vert']:
                    new_bl['vert'] = c
            elif c[1] == point[1]:
                if not new_bl['horiz']:
                    new_bl['horiz'] = c
            if new_bl['vert'] and new_bl['horiz']:
                borderlines[point] = new_bl
                break
    
    border_points = set()
    # draw each line as set of points
    for point in borderlines:
        for dir in ['horiz', 'vert']:
            cell0 = borderlines[point][dir]
            cell1 = point
            for x in range(min(cell0[0], cell1[0])+1, max(cell0[0], cell1[0])):
                border_points.add((x,cell0[1]))
            for y in range(min(cell0[1], cell1[1]), max(cell0[1], cell1[1])):
                border_points.add((cell0[0],y))
    if ex:
        print_grid(data, None, border_points)

    #in puzzle input, the longest horizontal line is far longer than longest vertical
    longest_h = max([max(k[0]-v['horiz'][0], v['horiz'][0]-k[0]) for k,v  in borderlines.items()]) 
    longest_v = max([max(k[1]-v['vert'][1], v['horiz'][1]-k[1]) for k,v  in borderlines.items()])
    print("Longest horizontal line: %d. longest vertical line: %d)" % (longest_h, longest_v))
    h_lines = [(k,v['horiz']) for k,v  in borderlines.items()]
    v_lines = [(k,v['vert']) for k,v  in borderlines.items()]
    all_border_points = set(data).union(border_points)

    dist_desc = dict(sorted([(dx,dy) for dx,dy in dist.items()], key=lambda x: int(((max(x[0][0][0],x[0][1][0]) - min(x[0][0][0],x[0][1][0]))+1)*((max(x[0][0][1],x[0][1][1]) - min(x[0][0][1],x[0][1][1]))+1)), reverse=True))
    for count, ((x0,y0),(x1,y1)) in enumerate(dist_desc.keys()):
        mx = max(x0,x1) - min(x0,x1)
        my = max(y0,y1) - min(y0,y1)
        area = (mx+1)*(my+1)
        if count % 10 == 0:
            print("Checking candidate rects: %d/%d, current area: %d" % (count,len(dist_desc.keys()), area))
        #this is a candidate rectangle but are all points inside the border?
        #first check the corners are all inside or on the border
        for point in [(x0,y0),(x1,y1), (x0,y1), (x1, y0)]:
            inside = point_inside_border(point, all_border_points)
            if not inside:
                break
        if not inside:
            continue
        # now check each line against the border to see if it crosses
        intersect = False
        vert0 = (x1, y1),(x1,y0)
        vert1 = (x0, y1),(x0,y0)
        horiz0 = (x1,y1),(x0,y1)
        horiz1 = (x1,y0),(x0,y0)

        #it's ok if the tip of each line in the rect touches the border!
        #horiz0_min, horiz0_max = min(horiz0[0][0]+1,horiz0[1][0]), max(horiz0[0][0]+1,horiz0[1][0])
        #horiz1_min, horiz1_max = min(horiz1[0][0]+1,horiz1[1][0]), max(horiz1[0][0]+1,horiz1[1][0])
        #TODO - change this to use arithmetic on the ranges rather than generating a set
        candi_points_h0 = set([(x,horiz0[0][1]) for x in range(min(horiz0[0][0]+1,horiz0[1][0]), max(horiz0[0][0]+1,horiz0[1][0]))])
        candi_points_h1 = set([(x,horiz1[0][1]) for x in range(min(horiz1[0][0]+1,horiz1[1][0]), max(horiz1[0][0]+1,horiz1[1][0]))])
        for vl in v_lines:
            v_border= set([(vl[0][0],x) for x in range(min(vl[0][1],vl[1][1])+1, max(vl[0][1],vl[1][1]))])
            if v_border.intersection(candi_points_h0):
                intersect = True
                break
            if v_border.intersection(candi_points_h1):
                intersect = True
                break
        if intersect:
            continue

        candi_points_v0 = set([(vert0[0][0],x) for x in range(min(vert0[0][1]+1,vert0[1][1]), max(vert0[0][1]+1,vert0[1][1]))])
        candi_points_v1 = set([(vert1[0][0],x) for x in range(min(vert1[0][1]+1,vert1[1][1]), max(vert1[0][1]+1,vert1[1][1]))])
        for hl in h_lines:
            h_border= set([(x, hl[0][1]) for x in range(min(hl[0][0]+1,hl[1][0]+1), max(hl[0][0],hl[1][0]))])
            if h_border.intersection(candi_points_v0):
                intersect = True
                break
            if h_border.intersection(candi_points_v1): 
                intersect = True
                break
        if intersect:
            continue
        break
    return area

def point_inside_border(point, border_points):
    #draw a horizontal ray left and right until it reaches min and max values, counting how many lines it crosses
    inside = None
    if point in border_points:
        return True
    if ex:
        max = 14
    else:
        max = 100000
    xpos, ypos = int(point[0]), int(point[1])
    lcount, rcount = 0,0
    while xpos >= 0:
        if (xpos,ypos) in border_points:
            lcount+=1
        xpos -= 1
    xpos, ypos = int(point[0]), int(point[1])
    while xpos < max:
        if (xpos,ypos) in border_points:
            rcount+=1
        xpos += 1
    if lcount == 0 or rcount == 0:
        inside = False #completely outside
    elif lcount % 2 == 0 and rcount %2 == 0:
        inside = False # in a gulf
    else:
        inside = True
    return inside

ex=True
data = read_data()
#print("part1 answer: %d" % part1(data))
print("part2 answer: %d" % part2(data))