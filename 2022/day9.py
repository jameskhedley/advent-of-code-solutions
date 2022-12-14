#l0 = [el.replace('\n','') for el in open("day9_ex.txt").readlines()]
l0 = [el.replace('\n','') for el in open("day9.txt").readlines()]

MOVES = {'R':(1,0),'L':(-1,0),'U':(0,-1),'D':(0,1)}
DIM = 200
state = []
for x in range(DIM):
    state.append(['.']*DIM)

def print_grid(grid):
    for y in range(DIM):
        line = ""
        for x in range(DIM):
            line = line+ state[x][y]
        print(line)

#head = [0,DIM-1]
#tail = [0,DIM-1]

head = [10,10]
tail = [10,10]

state[head[0]][head[1]] = "H"
print_grid(state)

tail_record = set()

#import pdb; pdb.set_trace()    
while l0:
    instr = l0.pop(0)
    print(instr)
    direction, mag = instr.split()
    mag = int(mag)
    state[head[0]][head[1]] = "."
    state[tail[0]][tail[1]] = "#"
    
    for x in range(mag):
        head[0] += MOVES[direction][0]
        head[1] += MOVES[direction][1]
        #tail chases head
        distance_h_t = (head[0]-tail[0], head[1]-tail[1])
        print(distance_h_t)
        if abs(distance_h_t[0]) > 1:
            if head[1] != tail[1]:
                if head[1] > tail[1]:
                    tail[1] += MOVES['D'][1]
                elif head[1] < tail[1]:
                    tail[1] += MOVES['U'][1]        
            if head[0] > tail[0]:
                tail[0] += MOVES['R'][0]
            elif head[0] < tail[0]:
                tail[0] += MOVES['L'][0]
        if abs(distance_h_t[1]) > 1:
            if head[0] != tail[0]:
                if head[0] > tail[0]:
                    tail[0] += MOVES['D'][1]
                elif head[0] < tail[0]:
                    tail[0] += MOVES['U'][1]            
            if head[1] > tail[1]:
                tail[1] += MOVES['D'][1]
            elif head[1] < tail[1]:
                tail[1] += MOVES['U'][1]
        state[tail[0]][tail[1]] = "#"
        tail_record.add(tuple(tail))
        debug = 0
        if debug:
            temp_t = state[tail[0]][tail[1]]
            temp_h = state[head[0]][head[1]]
            state[tail[0]][tail[1]] = "t"
            state[head[0]][head[1]] = "h"
            print_grid(state)
            state[tail[0]][tail[1]] = temp_t
            state[head[0]][head[1]] = temp_h
    
    state[tail[0]][tail[1]] = "T"
    state[head[0]][head[1]] = "H"
    
    print("=========================")
    print_grid(state)
    print("=========================")
    
print(tail_record)
print(len(tail_record))
