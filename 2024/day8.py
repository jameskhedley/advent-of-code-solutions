from collections import defaultdict
debug = 0
if debug:
    lines = ''.join(open("./day8_ex.txt").readlines()).split()
else:
    lines = ''.join(open("./day8_data.txt").readlines()).split()

grid = [[x for x in list(line.strip())] for line in lines]

limy = len(lines)
limx = len(lines[0])

def print_grid(grid, found=[]):
    for irow, line in enumerate(grid):
        pl = ""
        for icol, char in enumerate(line):
            fill = False
            if (irow,icol) in found:
                pl += "#"
            else:
                pl += char
        print(pl)
    print("*******************************")

def find_antennas(grid):
    ants = defaultdict(list)
    for irow, line in enumerate(grid):
        for icol, char in enumerate(line):
            if char != '.':
                ants[char].append((irow, icol))
    return ants

def test_findantinodes():
    found = find_antinodesp1((1,1), (2,2))
    assert found == set([(0,0), (3,3)])
    found = find_antinodesp1((1,2), (2,4))
    assert found == set([(0,0), (3,6)])
    found = find_antinodesp1((0,0), (1,1))
    assert found == set([(2,2)])
    print("pt 1 tests passed")
    found = find_antinodesp2((0,0), (2,1), 10)
    assert found == set([(4,2), (6,3), (8,4)])

def find_antinodesp2(antx, anty, size):
    antinodes = set()
    rel0 = (antx[0]-anty[0], antx[1]-anty[1])
    rel1 = (anty[0]-antx[0], anty[1]-antx[1])

    repeat = 1
    oob0, oob1 = False, False
    while True:
        anti0 = (antx[0]+(rel0[0]*repeat), antx[1]+(rel0[1]*repeat))
        anti1 = (anty[0]+(rel1[0]*repeat), anty[1]+(rel1[1]*repeat))
        if anti0[0] < 0 or anti0[0] >= size or anti0[1] < 0 or anti0[1] >= size:
            oob0 = True
        if anti1[0] < 0 or anti1[0] >= size or anti1[1] < 0 or anti1[1] >= size:
            oob1 = True
        if not oob0:
            antinodes.add(anti0)
        if not oob1:
            antinodes.add(anti1)
        repeat+=1
        if oob0 and oob1:
            break
    return antinodes

def find_antinodesp1(antx, anty, size=10):
    antinodes = set()
    rel0 = (antx[0]-anty[0], antx[1]-anty[1])
    rel1 = (anty[0]-antx[0], anty[1]-antx[1])
    anti0 = (antx[0]+rel0[0], antx[1]+rel0[1])
    anti1 = (anty[0]+rel1[0], anty[1]+rel1[1])
    if anti0[0] >= 0 and anti0[0] < limy and anti0[1] >= 0 and anti0[1] < limx:
        antinodes.add(anti0)
    if anti1[0] >= 0 and anti1[0] < limy and anti1[1] >= 0 and anti1[1] < limx:
        antinodes.add(anti1)
    return antinodes

def smash(grid, func, part):
    antinodes = set()
    print_grid(grid)
    antennas = find_antennas(grid)
    print(antennas)
    for char in antennas.keys():
        ant_list = antennas[char]
        for idx, ant in enumerate(ant_list):
            others = ant_list[:idx] + ant_list[idx+1:]
            for other in others:
                antinodes= antinodes.union(func(ant, other, limx))
            
    print_grid(grid, antinodes)
    if part == 2:
        print(antennas)
        antennas_set = set()
        for k, l in antennas.items():
            antennas_set= antennas_set.union(set(l))
        antinodes = antinodes.union(antennas_set)

    print("pt%d: %d)" % (part,len(antinodes)))

test_findantinodes()
smash(grid,find_antinodesp1, 1) 
smash(grid,find_antinodesp2, 2)