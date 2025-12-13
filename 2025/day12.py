from collections import defaultdict

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
            areas.append({k: v})
    return shapes, areas

shapes, areas = read_data()
pass