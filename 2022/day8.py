from copy import deepcopy
from itertools import chain
#l0 = [list(el.replace('\n','')) for el in open("day8_ex.txt").readlines()]
l0 = [list(el.replace('\n','')) for el in open("day8.txt").readlines()]

def print_grid(grid):
    for row in grid:
        print(''.join(row))

print_grid(l0)
print("="*len(l0[0]))

overlay = deepcopy(l0)
scenics = deepcopy(l0)

def next_tree_of_size(size, direction, trees):
    count = 0
    nxt = 0
    while trees and int(nxt)<int(size):
        if direction == "left" or direction == "up":
            nxt = trees.pop()
        elif direction == "right" or direction == "down":
            nxt = trees.pop(0)
        count += 1
    return count

for idy, row in enumerate(l0):
    if idy == 0 or idy == len(l0)-1:
        overlay[idy] = ["X"]*len(row)
        scenics[idy] = ['0']*len(row)
    else:
        for idx, val in enumerate(row):
            if idx == 0 or idx == len(row)-1:
                overlay[idy][idx] = "X"
                scenics[idy][idx] = "0"
            else:
                u_nbors = [row[idx] for row in l0[:idy]]
                d_nbors = [row[idx] for row in l0[idy+1:]]
                l_nbors = row[:idx]
                r_nbors = row[idx+1:]
                if max(l_nbors) < val or max(r_nbors) < val or max(u_nbors) < val or max(d_nbors) < val:
                    overlay[idy][idx] = "X"
                else:
                    overlay[idy][idx] = "O"
                    
                score = next_tree_of_size(val, "left", l_nbors) * next_tree_of_size(val, "up", u_nbors) * next_tree_of_size(val, "right", r_nbors) * next_tree_of_size(val, "down", d_nbors)
                #import pdb; pdb.set_trace()
                scenics[idy][idx] = str(score)


flat = list(chain.from_iterable(overlay))
res1 = sum([1 if c=="X" else 0 for c in flat])
print("Part 1 result: %d" % res1)

flat = list(chain.from_iterable(scenics))
res2 = max([int(x) for x in flat])
print("Part 2 result: %d" % res2)


