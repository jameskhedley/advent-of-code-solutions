from collections import deque 
from itertools import chain
h0 = open("day15-ex.txt")
#h0 = open("day11.txt")

lines = h0.readlines()

arr = [[int(x) for x in list(line.strip())] for line in lines]

def print_arr(arr, path):
    for y, line in enumerate(arr):
        pl = ""
        for x, cell in enumerate(line):
            if (x,y) in path:
                pl += "*%d" % cell
            else:
                pl += " %d" % cell
        print(pl)
    print("*******************************")
    


class Node():
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position


def astar(maze, start, end):
    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0

    # Initialize both open and closed list
    open_list = []
    closed_list = []

    # Add the start node
    open_list.append(start_node)

    ijkh = 0
    # Loop until you find the end
    while len(open_list) > 0:
        if ijkh % 100 == 0:
            print(ijkh)
        ijkh += 1
        # Get the current node
        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        # Pop current off open list, add to closed list
        open_list.pop(current_index)
        closed_list.append(current_node)

        # Found the goal
        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1] # Return reversed path

        # Generate children
        children = []
        #for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]: # Adjacent squares
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0)   ]: # Adjacent squares

            # Get node position
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            # Make sure within range
            if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (len(maze[len(maze)-1]) -1) or node_position[1] < 0:
                continue

            # Make sure walkable terrain
            if maze[node_position[0]][node_position[1]] > 6:
                continue

            # Create new node
            new_node = Node(current_node, node_position)

            # Append
            children.append(new_node)

        # Loop through children
        for child in children:

            # Child is on the closed list
            for closed_child in closed_list:
                if child == closed_child:
                    continue

            # Create the f, g, and h values
            child.g = current_node.g + 1
            child.h = ((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1]) ** 2)
            child.f = child.g + child.h

            # Child is already in the open list
            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    continue

            # Add the child to the open list
            open_list.append(child)

def bfs(maze, s):
    parent = {s: None}
    d0 = {s: 0}

    queue = deque()
    queue.append(s)

    while queue:
        u = queue.popleft()
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0)   ]: # Adjacent squares
            # Get node position
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            # Make sure within range
            if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (len(maze[0]) -1) or node_position[1] < 0:
                continue
            if node_position not in d0:
                parent[node_position] = u
                d0[node_position] = d0[u] + 1
                queue.append(node_position)
        return parent, d0


def recurses(gadj, path, node, score, grid):
    end = (len(grid)-1, len(grid[0])-1)
    #import pdb; pdb.set_trace()
    #print("path is %s" % path)
    #print("considering node %s" % (str(node)))
    for child in gadj[node]:
        score += grid[node[0]][node[1]]
        path.append(node)
        if node == end:
            return gadj, path, node, score
        if child in path:
            continue
        gadj, path, node, score = recurses(gadj, path, child, score, grid)
        
    return gadj, path, node, score


def main(maze):
    start = (0, 0)
    end = (9, 9)

    #path = astar(maze, start, end)
    erm = bfs(maze, start)
    print(erm)
    
    #print_arr(maze, path)


main(arr)
