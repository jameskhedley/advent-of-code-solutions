import math
from collections import deque
ex=False

def read_data():
    if ex:
        h0 = open('day9_ex.txt')
    else:
        h0 = open('day9.txt')
    data = [(int(x), int(y)) for x, y in [line.strip().split(',') for line in h0.readlines()]]
    #print(data)
    #print_grid(data, dim_x, dim_y)
    return data

def print_grid(data, rect=[], greens=[]):
    dimx = max([x for x,y in data ]) 
    dimy = max([y for x,y in data ]) 

    grid = []
    for _ in range(dimy+2):
        grid.append(["."]*(dimx+2))
    for (x,y) in data:
        grid[y][x] = '#'
    if greens:
        for (x,y) in greens:
            grid[y][x] = 'X'
    #grid[4][3] = 'O'
    if rect:
        print(rect)
        for x in range(min(rect[0][0], rect[1][0]),max(rect[0][0], rect[1][0])+1):
            for y in range(min(rect[0][1], rect[1][1]),max(rect[0][1], rect[1][1])+1):
                grid[y][x] = 'O'
    for row in grid:
        print(''.join(row))
    print("="*(dimx+2))

def part1(data):
    dist = calc_distances(data)
    #for dd in list(dist.keys())[-3:]:
    #    print_grid(data, dd)
    ans = dist
    (x0,y0),(x1,y1) = list(dist.keys())[-1]
    mx = max(x0,x1) - min(x0,x1)
    my = max(y0,y1) - min(y0,y1)
    ans = (mx+1)*(my+1)
    return ans

def calc_distances(data):
    dist = {}
    for nump, point in enumerate(data):
        print("%d/%d" % (nump, len(data)))
        for pp in data:
            if point == pp:
                continue
            if (pp,point) in dist.keys():
                continue
            dist[(point, pp)] = math.sqrt((point[0]-pp[0])**2 + (point[1]-pp[1])**2)
    dist = dict(sorted([(dx,dy) for dx,dy in dist.items()], key=lambda x: x[1]))
    return dist

def adjacent_to(pos):
    #top_left = (-1,-1)
    top_middle = (-1, 0)
    #top_right = (-1, 1)
    left = (0, -1)
    right = (0, 1)
    #bottom_left = (1, -1)
    bottom_middle = (1, 0)
    #bottom_right = (1,1)
    four = (
            #(pos[0] + top_left[0], pos[1] + top_left[1]),
             (pos[0] + top_middle[0], pos[1] + top_middle[1]),
             #(pos[0] + top_right[0], pos[1] + top_right[1]),
             (pos[0] + left[0], pos[1] + left[1]),
             (pos[0] + right[0], pos[1] + right[1]),
             #(pos[0] + bottom_left[0], pos[1] + bottom_left[1]),
             (pos[0] + bottom_middle[0], pos[1] + bottom_middle[1]),
             #(pos[0] + bottom_right[0], pos[1] + bottom_right[1])
             )

    return four

def bfs(data, start):
    queue = deque([start])
    filled = set()
    while queue:
        pos = queue.popleft() #bfs pops from left
        filled.add(pos)
        for npos in adjacent_to(pos):
            if npos in filled:
                continue
            if npos not in data:
                queue.append(npos)
    return filled



def part2(data):
    ans = 0
    greens = []
    # find outline
    for idx in range(len(data)):
        cell0 = data[idx]
        cell1 = data[(idx+1) % len(data)]
        for x in range(min(cell0[0], cell1[0])+1, max(cell0[0], cell1[0])):
            greens.append((x,cell0[1]))
        for y in range(min(cell0[1], cell1[1]), max(cell0[1], cell1[1])):
            greens.append((cell0[0],y))
    print_grid(data, None, greens)
    # fill outline
    if ex:
        start = (3,4)
        red_green = set(data+greens)
        filled = bfs(red_green, start)
        red_green = red_green.union(filled)
        print_grid(data, None, red_green)
    else:
        start = (0,0) #TODO figure this out
    
    return ans
    
    
ex=True
data = read_data()
#print("part1 answer: %d" % part1(data))
print("part2 answer: %d" % part2(data))

