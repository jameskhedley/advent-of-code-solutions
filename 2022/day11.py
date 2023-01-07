from pprint import pprint
import operator, functools
#l0 = [el.replace('\n','') for el in open("day11_ex.txt").readlines()]
l0 = [el.replace('\n','') for el in open("day11.txt").readlines()]

ops = { "+": operator.add, "*": operator.mul }

def parse_input(lines):
    data = {}
    for line in lines:
        if not line.strip():
            data[key]['ic'] = 0
            key=None
            continue
        if 'Monkey' in line:
            key = int(line.split()[1].replace(':',''))
            data[key]={}
        if 'Starting' in line:
            data[key]['items']=[int(x.strip()) for x in line.split(':')[1].split(',')]
        if 'Test' in line:
            data[key]['div_by']=int(line.split()[-1])
        if 'true' in line:
            data[key]['true']=int(line.split()[-1])
        if 'false' in line:
            data[key]['false']=int(line.split()[-1])
        if 'Operation' in line:
            data[key]['op'] = [line.split()[-2:-1]][0]
            check = line.split()[-1]
            if check =='old':
                data[key]['op'].append('old')    
            else:
                data[key]['op'].append(int(check))
    return data

state = parse_input(l0)
magic = functools.reduce(operator.mul, [v['div_by'] for v in state.values()], 1)

loop = 1
while loop <= 10000:
    print("Loop %d" % loop)
    for monke,v in state.items():
        while v['items']:
            v['ic']+=1
            item = v['items'].pop(0)
            if v['op'][1]=='old':
                worry = item*item
            else:
                worry = ops[v['op'][0]](item, v['op'][1])
            old_worry = int(worry)
            worry = worry % magic
            if worry % v['div_by']==0:
                next_monke = v['true']
            else:
                next_monke = v['false']
            state[next_monke]['items'].append(worry)
    pprint(state)
    print('===========================================================')
    loop += 1

top2 = sorted([v['ic'] for k,v in state.items()])[-2:]
print("Part 1 answer: %d" % (top2[0] * top2[1]))

