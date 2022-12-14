#l0 = [el.replace('\n','') for el in open("day10_ex.txt").readlines()]
lines = [el.replace('\n','') for el in open("day10.txt").readlines()]

cycle,x = 0,1
samples = []

while lines:
    line = lines.pop(0).split()
    inst = line[0]
    if len(line)==2:
        ops=2
        val = int(line[1])
    else:
        ops=1
        val = None
    for loop in range(ops):
        cycle+=1
        samples.append((cycle,x))
    if val and loop==1:
        x+=val
        
vs = (-1,0,1)
grid = [[""]*40, [""]*40,[""]*40,[""]*40,[""]*40,[""]*40]
start,end = 0,40

for row,line in enumerate(grid):
    #import pdb;pdb.set_trace()
    offset = row*40
    for cycle in samples[start:end]:
        xval = cycle[1]
        sprite = (vs[0]+xval, vs[1]+xval, vs[2]+xval)
        pos = (cycle[0]- offset)-1
        if pos in sprite:
            line[pos]="#"
        else:
            line[pos]="."
    start+=40
    end+=40
    print("".join(line))
    

if 0: #pt1
    req = [20, 60, 100, 140, 180, 220]
    for r in samples:
        print(r)
        
    final = []
    for r in samples:
        if r[0] in req:
            final.append(r[0]*r[1])
            
    print(final)
    print(sum(final))
