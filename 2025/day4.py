from copy import deepcopy
from collections import deque, defaultdict

def adjacent_to_number(pos):
    top_left = (-1,-1)
    top_middle = (-1, 0)
    top_right = (-1, 1)
    left = (0, -1)
    right = (0, 1)
    bottom_left = (1, -1)
    bottom_middle = (1, 0)
    bottom_right = (1,1)
    eight = ((pos[0] + top_left[0], pos[1] + top_left[1]),
             (pos[0] + top_middle[0], pos[1] + top_middle[1]),
             (pos[0] + top_right[0], pos[1] + top_right[1]),
             (pos[0] + left[0], pos[1] + left[1]),
             (pos[0] + right[0], pos[1] + right[1]),
             (pos[0] + bottom_left[0], pos[1] + bottom_left[1]),
             (pos[0] + bottom_middle[0], pos[1] + bottom_middle[1]),
             (pos[0] + bottom_right[0], pos[1] + bottom_right[1]))

    return eight

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
        tmp_maze[pos[0]][pos[1]] = 'x'
    for row in tmp_maze:
        #print(' '.join(row))
        print(''.join(row))
        
#maze = read_data("./day4_ex.txt")
maze = read_data("./day4.txt")
#print_grid(maze)

def part1(maze):
    ans = 0
    seen = find_avail(maze)
    print_grid(maze, seen)
    return len(seen)

def part2(maze):
    ans = 0
    seen = find_avail(maze)
    ans += len(seen)
    while seen:
        maze = remove_rolls(maze, seen)
        seen = find_avail(maze)
        #print_grid(maze, seen)
        ans += len(seen)
    return ans
    
def remove_rolls(maze, xs):
    for pos in xs:
        maze[pos[0]][pos[1]] = '.'
    return maze

def find_avail(maze):
    dim_x = len(maze)
    dim_y = len(maze[0])
    seen = set()
    for y, row in enumerate(maze):
        for x, cell in enumerate(row):
            if cell == '.': continue
            adj = 0
            eight = adjacent_to_number((y,x))
            for cand in eight:
                if cand[0] >= 0 and cand[0] < dim_x and cand[1] >= 0 and cand[1] < dim_y:
                    if y == 0 and x == 2:
                        print('break')
                    if maze[cand[0]][cand[1]] == '@':
                        adj += 1
            if adj < 4:
                seen.add((y,x))
    return seen


#print("part 1 answer: %d " % part1(maze))
print("part 2 answer: %d " % part2(maze))