from collections import defaultdict
from itertools import chain

def read_data():
    shapes = defaultdict(list)
    areas = []
    h0 = open('day12.txt')
    num = -1
    for line in h0.readlines():
        line=line.strip()
        if line == "": continue
        if ":" in line and line.split(":")[1] == "":
            num = int(line.split(":")[0])
        elif "#" in line:
            shapes[num].append(line)
        elif "x" in line:
            k = tuple([int(x) for x in line.split(":")[0].split("x")])
            v = [int(x) for x in line.split(":")[1][1:].split(" ")]
            areas.append((k, v))
    return shapes, areas

def part1(): # wtf is this input?? super easy as it turns out
    ans = 0
    shapes, areas = read_data()
    shape_sizes = dict((k, tuple(chain(*v)).count('#')) for k,v in shapes.items())
    for area in areas:
        size, counts = area
        total_space_needed = [ cc * shape_sizes[idx] for idx, cc in enumerate(counts)]
        if size[0]*size[1] > sum(total_space_needed):
            ans+=1
    return(ans)

print("part 1 answer: %d" % part1())