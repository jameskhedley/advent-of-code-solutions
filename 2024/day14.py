
def read_data(fn):
    bots = []
    h0 = open(fn)
    for raw in h0.readlines():
        line = raw.strip()
        # p=0,4 v=3,-3
        sp, sv = line.split(' ')
        p = [int(x) for x in sp.strip('p=').split(',')]
        v = [int(x) for x in sv.strip('v=').split(',')]
        bots.append((p,v))
    return bots

def print_grid(bots, width, height):
    floor = []
    for y in range(height):
        row = []
        for x in range(width):
            row.append(0)
        floor.append(row)
    for bot in bots:
        pos = bot[0]
        try:
            floor[pos[1]][pos[0]] += 1
        except IndexError:
            stop = 1
    for y in range(height):
        print(''.join([str(x) if x > 0 else '.' for x in floor[y]]))
    print('*'*width)

def simulate_test(bots, width, height):
    bots = [([2, 4], [2, -3])]
    bot = bots[0]
    print_grid([bot], width, height)
    pos = bot[0] # col, row
    v = bot[1]
    for i in range(5):
        pos[0] = (pos[0]+v[0]) % width
        pos[1] = (pos[1]+v[1]) % height
        bot = ([pos[0], pos[1]], v)
        #print(pos)
        print_grid([bot], width, height)

def simulate(bots, width, height, loops):
    for loop in range(loops):
        for idx,bot in enumerate(bots):
            pos = bot[0] # col, row
            v = bot[1]
            pos[0] = (pos[0]+v[0]) % width
            pos[1] = (pos[1]+v[1]) % height
            bots[idx] = ([pos[0], pos[1]], v)
            #print(pos)
    #print_grid(bots, width, height)
    return bots

def calc_score(bots, width, height):
    cols = list(range(width))
    rows = list(range(height))
    left_cols = cols[:width//2]
    right_cols = cols[(width//2)+1:]
    up_rows = rows[:height//2]
    down_rows = rows[(height//2)+1:]

    tl_score, tr_score, dl_score, dr_score, dropped = 0,0,0,0,0

    for bot in bots:
        col, row = bot[0]
        if col in left_cols and row in up_rows:
            tl_score+=1
        elif col in right_cols and row in up_rows:
            tr_score+=1
        elif col in left_cols and row in down_rows:
            dl_score+=1
        elif col in right_cols and row in down_rows:
            dr_score+=1
        else:
            dropped+=1
    score = tl_score*tr_score*dl_score*dr_score
    return score

example = 0
if example:
    bots = read_data('day14_ex.txt') # ans: 12
    width = 11
    height = 7
    print_grid(bots, width, height)
else:
    bots = read_data('day14_data.txt')
    width=101
    height=103

def part1(bots, width, height):
    bots = simulate(bots, width, height, 100)    
    ans = calc_score(bots, width, height)
    print("part1: %d" % (ans))

def part2(bots, width, height):
    loops = 0
    while True:
        loops += 1
        bots = simulate(bots, width, height, 1)
        uniq = set([tuple(p) for p,v in bots])
        if len(uniq) == len(bots):
            print_grid(bots, width, height)
            break
    print("part2: %d" % (loops))

#part1(bots, width, height)
part2(bots, width, height)