def print_model(model, x0, xmax):
    for row in model:
        print(''.join(row[x0+1:xmax+1]))    

def setup_cave(lines, add_floor=False):
    rock_lines = set()
    for line in lines:
        line_points = [[int(x) for x in lp.strip().split(',')] for lp in line.split("->")]
        print(line_points)
        for idx,lp in enumerate(line_points[:-1]):
            nx_lp = line_points[idx+1]
            xr = sorted([lp[0],nx_lp[0]])
            yr = sorted([lp[1],nx_lp[1]])
            print(xr)
            print(yr)
            #import pdb; pdb.set_trace()
            for xx in range(xr[0],xr[1]+1):
                for yy in range(yr[0],yr[1]+1):
                    rock_lines.add((xx,yy))

    xmax = max([x[0] for x in rock_lines]) + 200
    xmin = min([x[0] for x in rock_lines]) - 200
    ymax = max([x[1] for x in rock_lines])
    ymin = min([x[1] for x in rock_lines])

    x0 = xmin-1
    x1 = xmax+1

    model = []
    for x in range(0,ymax+1):
        row = []
        for line in range(0,xmax+1):
            row.append('.')
        model.append(row)

    for rl in rock_lines:
        model[rl[1]][rl[0]] = '#'
        
    if add_floor:
        row = []
        for line in range(0,xmax+1):
            row.append('.')
        model.append(row)
        row = []
        for line in range(0,xmax+1):
            row.append('#')
        model.append(row)
    return model, x0, xmax, ymax
    
def pt1(lines):
    model, x0, xmax, ymax = setup_cave(lines)
    print_model(model, x0, xmax)
    origin = (500,0)
    sand_count = 0
    full = False
    while not full:
        plus = list(origin)
        px,py = plus[0], plus[1]
        while True:
            try:
                _ = model[py+1][px] 
            except:
                full = True
                print("Part1. Full up! At turn %d" % sand_count)
                break
            if model[py+1][px] == '.':
                py+=1
            elif model[py+1][px-1] == '.':
                py+=1
                px-=1
            elif model[py+1][px+1] == '.':
                py+=1
                px+=1   
            else:
                model[py][px] = 'o'
                sand_count += 1
                print_model(model, x0, xmax)
                print('*****************************************')
                break

def pt2(lines):
    model, x0, xmax, ymax = setup_cave(lines, add_floor=True)
    print_model(model, x0, xmax)
    origin = (500,0)
    sand_count = 0
    full = False
    while not full:
        plus = list(origin)
        px,py = plus[0], plus[1]
        while True:
            _ = model[py+1][px] 
            if model[py+1][px] == '.':
                py+=1
            elif model[py+1][px-1] == '.':
                py+=1
                px-=1
            elif model[py+1][px+1] == '.':
                py+=1
                px+=1   
            else:
                model[py][px] = 'o'
                sand_count += 1
                if sand_count %1000 == 0:
                    print(sand_count)
                if (px,py)==origin:
                    full = True
                    print_model(model, x0, xmax)
                    print("Part2. Full up! At turn %d" % sand_count)
                break


ex_lines = [el.replace('\n','') for el in open("day14_ex.txt").readlines()]
lines = [el.replace('\n','') for el in open("day14.txt").readlines()]

#pt1(ex_lines)
pt2(lines)

