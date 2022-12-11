#l0 = [el.replace('\n','') for el in open("day5_ex.txt").readlines()]
l0 = [el.replace('\n','') for el in open("day5.txt").readlines()]

initial_state = l0[:l0.index('')]
moves = l0[l0.index('')+1:]

def read_stacks(state):
    num_of_states = int((len(state[-1])+1)/4)
    stacks = dict([(i, []) for i in range(num_of_states)])
    pos = [(i+0,i+3) for i in range(num_of_states*4)[::4]]
    for line in initial_state[::-1][1:]:
        for idx, p in enumerate(pos):
            crate = line[p[0]:p[1]]
            if crate and crate != '   ':
                stacks[idx].append(crate)
    return stacks

state = read_stacks(initial_state)

for move in moves:
    q, f, t = (int(move.split(' ')[1:][0]), int(move.split(' ')[1:][2]), int(move.split(' ')[1:][-1]))
    temp = []
    for i in range(q):
        temp.append(state[f-1].pop())
    #for crate in temp: #pt1
    for crate in temp[::-1]: # pt2
        state[t-1].append(crate)

print(state)
res = ""
for (k,v) in state.items():
    tmp = v.pop().strip("[").strip("]")
    res=res+tmp
print(res)
