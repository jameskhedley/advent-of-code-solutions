import math
ex=False

def read_data():
    if ex:
        h0 = open('day9_ex.txt')
    else:
        h0 = open('day9.txt')
    data = [(int(x), int(y)) for x, y in [line.strip().split(',') for line in h0.readlines()]]
    #print(data)
    dim_x = max([x for x,y in data ]) 
    dim_y = max([y for x,y in data ]) 
    #print_grid(data, dim_x, dim_y)
    return data, dim_x, dim_y

def print_grid(data, dimx, dimy, rect=[]):
    grid = []
    for irow in range(dimy+2):
        grid.append(["."]*(dimx+2))
    for (x,y) in data:
        grid[y][x] = '#'
    if rect:
        print(rect)
        for x in range(min(rect[0][0], rect[1][0]),max(rect[0][0], rect[1][0])+1):
            for y in range(min(rect[0][1], rect[1][1]),max(rect[0][1], rect[1][1])+1):
                grid[y][x] = 'O'
    for row in grid:
        print(''.join(row))
    print("#"*dimx)

def part1(data, dimx, dimy):
    dist = calc_distances(data)
    #print(dist)
    #for dd in list(dist.keys())[-3:]:
    #    print_grid(data, dimx, dimy, dd)
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

#ex=True
data, dimx, dimy = read_data()
print("part1 answer: %d" % part1(data, dimx, dimy))

