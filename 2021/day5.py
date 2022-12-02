import itertools

#h0 = open("day5-ex.txt")
h0 = open("day5.txt")
rl = h0.readlines()

strings = [l.strip().split(' -> ') for l in rl]
lines = [[[int(x) for x in y.split(',')] for y in z] for z in strings]

DIM = max(list(itertools.chain(*list(itertools.chain(*lines))))) + 1
print("DIM: %d" % DIM)

print(lines)

board = []
for row in range(DIM):
    row = ['.']*DIM
    board.append(row)

def pb():
    for row in board:
        print([str(x) for x in row])
        
def vector_range(v0, v1):
    lx = list(range(min(v0[0], v1[0]), max(v0[0], v1[0])+1))
    ly = list(range(min(v0[1], v1[1]), max(v0[1], v1[1])+1))
    print("lx: %s" % str(lx))
    print("ly: %s" % str(ly))
    return lx, ly

#for line in lines:
for line in lines:
    if line[0][0] == line[1][0]:
        print("Vertical")
    elif line[0][1] == line[1][1]:
        print("Horizontal")
    else:
        print("Diagonal, skipping")
        continue
    start = line[0]
    end = line[1]
    lx, ly = vector_range(start, end)
    for x in lx:
        for y in ly:
            #print(x,y)
            if board[y][x] ==".":
                board[y][x] = 1
            else:
                board[y][x] += 1

#pb()

print("*********************")
print(len([x for x in list(itertools.chain(*board)) if x != '.' and x > 1]))

