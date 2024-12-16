from copy import deepcopy
import time
from collections import deque, defaultdict

def read_data(fn):
    maze = []
    pos = None
    h0 = open(fn)
    lines=h0.readlines()
    for idx, line in enumerate(lines):
        if line.strip() == '':
            empty = idx
    moves = ''.join([line.strip() for line in lines[empty:]])
    lines = lines[:empty]
    maze = [list(line.strip()) for line in lines]
    for irow, row in enumerate(maze):
        if "@" in row:
            icol = row.index('@')
            pos = (irow,icol)
            maze[irow][icol] = '.' # delete the @
    return maze, moves, pos

def print_grid(maze, pos):
    tmp_maze = deepcopy(maze)
    if pos:
        tmp_maze[pos[0]][pos[1]] = "@"
    for row in tmp_maze:
        print(''.join(row))

def execute_p1(moves, maze, pos):
    for count, mv in enumerate(moves):
        irow, icol = pos[0], pos[1]
        if mv == '<':
            look = maze[irow][0:icol][::-1]
            dir = (0,-1)
        elif mv == '^':
            look = [x[icol] for x in maze][0:irow][::-1]
            dir = (-1,0)
        elif mv == '>':
            look = maze[irow][icol+1:]
            dir = (0,1)
        elif mv == 'v':
            look = [x[icol] for x in maze][irow+1:]
            dir = (1,0)
        if '.' in look:
            first_free = look.index('.')
        if '#' in look:
            first_wall = look.index('#')
        if not '.' in look or first_wall < first_free:
            pass #unsquishable 
        elif look[0] == '.': # just move into free space, don't move boxes
            pos = pos[0] + dir[0], pos[1] + dir[1]
        else:
            run_length = first_free
            boxes_to_move = look[:run_length]
            for this_box in range(run_length):
                look[this_box] = '.'
            look[1:run_length+1] = boxes_to_move
            if mv == '<':
                maze[irow] = look[::-1] + maze[irow][icol:]
            elif mv == '^':
                look = look[::-1]
                for jdx, jrow in enumerate(maze[:irow]):
                    jrow[icol] = look[jdx]
            elif mv == '>':
                maze[irow] = maze[irow][:icol+1] + look
            elif mv == 'v':
                for jdx, jrow in enumerate(maze[irow+1:]):
                    jrow[icol] = look[jdx]
            pos = pos[0] + dir[0], pos[1] + dir[1]
        if debug:
            print_grid(maze, pos)
            print("%d, %s" % (count, mv))
    return maze


def execute_p2(moves, maze, pos):
    for count, mv in enumerate(moves):
        if count == 190:
            stop=1 # stop the count!!
        irow, icol = pos[0], pos[1]
        if mv == '<':
            look = maze[irow][0:icol][::-1]
            dir = (0,-1)
        elif mv == '^':
            look = [x[icol] for x in maze][0:irow][::-1]
            dir = (-1,0)
        elif mv == '>':
            look = maze[irow][icol+1:]
            dir = (0,1)
        elif mv == 'v':
            look = [x[icol] for x in maze][irow+1:]
            dir = (1,0)
        if '.' in look:
            first_free = look.index('.')
        if '#' in look:
            first_wall = look.index('#')
        if not '.' in look or first_wall < first_free:
            pass #unsquishable 
        elif look[0] == '.': # just move into free space, don't move boxes
            pos = pos[0] + dir[0], pos[1] + dir[1]
        else:
            run_length = first_free
            boxes_to_move = look[:run_length]
            for this_box in range(run_length):
                look[this_box] = '.'
            look[1:run_length+1] = boxes_to_move
            if mv == '<':
                maze[irow] = look[::-1] + maze[irow][icol:]
            elif mv in ('^','v'):
                boxes_to_move = find_connected_boxes(look, maze, pos, dir)
                box_pieces = dict()
                abort = False
                for box in boxes_to_move:
                    new_pos = box[0] + dir[0], box[1] + dir[1]
                    box_pieces[box] = {'piece': maze[box[0]][box[1]], 'new_pos': new_pos}
                    if maze[new_pos[0]][new_pos[1]] == '#':
                        abort = True
                        break
                if abort: # ah crap, forget the whole thing
                    continue
                for box in boxes_to_move:
                    maze[box[0]][box[1]] = '.'
                for box in boxes_to_move:
                    new_pos = box_pieces[box]['new_pos']
                    maze[new_pos[0]][new_pos[1]] = box_pieces[box]['piece']
            elif mv == '>':
                maze[irow] = maze[irow][:icol+1] + look
            pos = pos[0] + dir[0], pos[1] + dir[1]

        if debug:
            print_grid(maze, pos)
            #time.sleep(1)
            print("%d, %s" % (count, mv))
    return maze, pos

def find_connected_boxes(look, maze, pos, dir):
    # do a quick bfs to find all boxes
    queue = deque([pos])
    boxes = set()
    bp = ('[', ']')
    visited = set()
    while queue:
        u = queue.popleft()
        if u in visited:
            continue
        visited.add(u)
        if maze[u[0]][u[1]] == '.':
            pos = pos[0] + dir[0], pos[1] + dir[1] #keep looking in direction indicated
            queue.append(pos)
            continue
        if maze[u[0]][u[1]] in bp:
            boxes.add(u)
        #for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0)]: # Adjacent squares
        search = [dir]
        if maze[u[0]][u[1]] == '[':
            search.append((0,1))
        if maze[u[0]][u[1]] == ']':
            search.append((0,-1))
        for new_position in search: # only in the direction indicated
            nbor = (u[0] + new_position[0], u[1] + new_position[1])
            if nbor[0] > (len(maze) - 1) or nbor[0] < 0 or nbor[1] > (len(maze[0]) -1) or nbor[1] < 0:
                continue
            if maze[nbor[0]][nbor[1]] not in bp:
                continue
            if not nbor in visited:
                queue.append(nbor)
    return boxes

# part1 
#maze, moves, pos = read_data('day15_ex0.txt')
#maze, moves, pos = read_data('day15_ex1.txt')
#maze, moves, pos = read_data('day15_ex.txt')

# part2
#maze, moves, pos = read_data('day15_ex_p2.txt')
#maze, moves, pos = read_data('day15_ex_p2_2.txt')
maze, moves, pos = read_data('day15_data_p2.txt')
debug = 0
#print_grid(maze, pos)
if debug:
    print(moves)

part1, part2 = 0,1
if part1:
    maze = execute_p1(moves, maze, pos)
    score = 0
    for irow, row in enumerate(maze):
        for icol, char in enumerate(row):
            if char == 'O':
                score += (100*irow)+(icol)

    print("part 1 %d" % score)

if part2:
    maze, pos = execute_p2(moves, maze, pos)
    score = 0
    for irow, row in enumerate(maze):
        for icol, char in enumerate(row):
            if char == '[':
                score += (100*irow)+(icol)
    print("part 2 %d" % score)
