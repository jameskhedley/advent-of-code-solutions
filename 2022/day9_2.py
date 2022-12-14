from copy import deepcopy
#l0 = [el.replace('\n','') for el in open("day9_2_ex.txt").readlines()]
l0 = [el.replace('\n','') for el in open("day9.txt").readlines()]

MOVES = {'R':(1,0),'L':(-1,0),'U':(0,-1),'D':(0,1)}
DIM = 300
state = []
for x in range(DIM):
    state.append(['.']*DIM)
    
CLEAN_STATE = deepcopy(state)    

def print_grid(grid):
    for y in range(DIM):
        line = ""
        for x in range(DIM):
            line = line+ state[x][y]
        print(line)

mid = int(DIM/2)
head = [mid,mid]
#head = [0,0]
num_knots = 9
knots = []
for n in range(num_knots):
    knots.append([mid,mid])

state[head[0]][head[1]] = "H"
print_grid(state)

tail_record = set()

def set_state(head, knots):
    state = deepcopy(CLEAN_STATE)
    for idx, knot in enumerate(knots):
        state[knot[0]][knot[1]] = str(idx+1)
    state[head[0]][head[1]] = "H"
    return state

def compare_states(state0, state1):
    for idy, row in enumerate(state0):
        for idx, val in enumerate(row):
            if val!=state1[idy][idx]:
                return False
    return True

count = 0
while l0:
    instr = l0.pop(0)
    print(instr)
    count += 1
    if count % 10 == 0:
        print("**"+str(count))
    direction, mag = instr.split()
    mag = int(mag)
    for x in range(mag):
        head[0] += MOVES[direction][0]
        head[1] += MOVES[direction][1]
        #knots chase head
        for idx, knot in enumerate(knots):
            if idx == 0:
                lead = deepcopy(head)
            else:
                lead = knots[idx-1]
            distance_h_t = (lead[0]-knot[0], lead[1]-knot[1])
            if abs(distance_h_t[0]) > 1 and distance_h_t[1]==0:
                if lead[0] > knot[0]:
                    knot[0] += MOVES['R'][0]
                elif lead[0] < knot[0]:
                    knot[0] += MOVES['L'][0]
            elif abs(distance_h_t[1]) > 1 and distance_h_t[0]==0:
                if lead[1] > knot[1]:
                    knot[1] += MOVES['D'][1]
                elif lead[1] < knot[1]:
                    knot[1] += MOVES['U'][1]
            elif abs(distance_h_t[0]) > 1 and abs(distance_h_t[1])>0:
                if lead[0] > knot[0]:
                    knot[0] += MOVES['R'][0]
                elif lead[0] < knot[0]:
                    knot[0] += MOVES['L'][0]
                if lead[1] > knot[1]:
                    knot[1] += MOVES['D'][1]
                elif lead[1] < knot[1]:
                    knot[1] += MOVES['U'][1]
            elif abs(distance_h_t[1]) > 1 and abs(distance_h_t[0])>0:
                if lead[1] > knot[1]:
                    knot[1] += MOVES['D'][1]
                elif lead[1] < knot[1]:
                    knot[1] += MOVES['U'][1]
                if lead[0] > knot[0]:
                    knot[0] += MOVES['R'][0]
                elif lead[0] < knot[0]:
                    knot[0] += MOVES['L'][0]
            
            if idx == 8:
                tail_record.add(tuple(knot))
                    
    state = set_state(head, knots)
    for tail in tail_record:
        state[tail[0]][tail[1]] = "#"
    if 0:
        print("=========================")
        print_grid(state)
        print("=========================")
    
print_grid(state)
print(tail_record)
print(len(tail_record))

