from collections import defaultdict
from copy import deepcopy, copy
from random import randint
ex = False
def read_data(filename):
    maze = []
    h0 = open(filename)
    lines=h0.readlines()
    dim_x = len(lines[0].strip())
    dim_y = len(lines)
    maze = [list(line.strip()) for line in lines]
    return maze

def print_grid(maze, xs=[]):
    tmp_maze = deepcopy(maze)
    for pos in xs:
        tmp_maze[pos[0]][pos[1]] = '|'
    for row in tmp_maze:
        print(''.join(row))
    print("#"*len(maze[0]))

def part2_doctor_strange(maze):
    #this actually works for the sample data!
    spos = maze[0].index('S')
    timelines = set()
    for universe in range(1000): # maybe 14,000,605 universes would be enough??
        visited = set()
        ypos = 0
        lxpos = set([spos])
        while ypos < len(maze)-1:
            nlxpos = copy(lxpos)
            for xpos in lxpos:
                visited.add((ypos,xpos))
                if maze[ypos+1][xpos] == '^':
                    if randint(1,10) > 5:
                        nlxpos.add(xpos-1)
                    else:
                        nlxpos.add(xpos+1)
                    nlxpos.remove(xpos)
            lxpos = nlxpos
            ypos += 1 
            lxpos = nlxpos
        print_grid(maze, visited)
        if universe %100 == 0:
            print(universe)
        timelines.add(tuple(visited))
    return len(timelines)

def part2_beams(maze):
    #ugh, doesn't work, overcounts
    ypos = 0
    spos = maze[0].index('S')
    lxpos = set([spos])
    visited = set()
    beam1 = ((ypos, spos),)
    beams = set([beam1])
    while ypos < len(maze)-1:
        nlxpos = copy(lxpos)
        for xpos in lxpos:
            visited.add((ypos,xpos))
            if maze[ypos+1][xpos] == '^':
                nlxpos.add(xpos-1)
                nlxpos.add(xpos+1)
                nlxpos.remove(xpos)
        lxpos = nlxpos
        ypos += 1
        newbeams = set()
        while beams:
            oldbeam = beams.pop()
            for xpos in lxpos:
                if abs(xpos - oldbeam[-1][1]) > 1:
                    continue
                temp = list(oldbeam)
                temp.append((ypos,xpos))
                newbeams.add(tuple(temp))
        beams = newbeams
        lxpos = nlxpos
    #print_grid(maze, visited)
    return len(beams)

def part1(maze):
    ypos = 0
    spos = maze[0].index('S')
    lxpos = set([spos])
    splits = 0
    visited = set()
    while ypos < len(maze)-1:
        nlxpos = copy(lxpos)
        for xpos in lxpos:
            visited.add((ypos,xpos))
            if maze[ypos+1][xpos] == '^':
                splits += 1
                nlxpos.add(xpos-1)
                nlxpos.add(xpos+1)
                nlxpos.remove(xpos)
        lxpos = nlxpos
        #print_grid(maze, visited)
        ypos += 1 
        lxpos = nlxpos
        print(lxpos)
    print_grid(maze, visited)
    return splits

def part2(maze):
    ypos = 0
    spos = maze[0].index('S')
    lxpos = [spos]
    visited = set()
    while ypos < len(maze)-1:
        print(ypos)
        for xpos in lxpos:
            visited.add((ypos,xpos))
            if maze[ypos+1][xpos] == '^':
                lxpos.append(xpos-1)
                lxpos.append(xpos+1)
                lxpos = [p for p in lxpos if p != xpos] #xpos is on a splitter so can't be visited in next row
        ypos += 1 
        #print(lxpos)
    print_grid(maze, visited)
    return sum([lxpos.count(x) for x in set(lxpos)])

#ex = True
if ex:
    maze = read_data("./day7_ex.txt")
    #print_grid(maze)
else:
    maze = read_data("./day7.txt")

#print("part 1 answer: %d " % part1(maze))
#print("part 2 answer: %d " % part2_doctor_strange(maze))
print("part 2 answer: %d " % part2(maze))
