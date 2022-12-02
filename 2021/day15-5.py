from collections import deque, defaultdict
from itertools import chain
from pdb import set_trace as qq
import random
h0 = open("day15-ex.txt")
#h0 = open("day15.txt")

lines = h0.readlines()
grid = [[int(x) for x in list(line.strip())] for line in lines]


def print_grid(grid, path):
    for y, line in enumerate(grid):
        pl = ""
        for x, cell in enumerate(line):
            if (x,y) in path:
                pl += "*%d" % cell
            else:
                pl += " %d" % cell
        print(pl)
    print("*******************************")


