import pyximport; pyximport.install()
import day15cy
import copy

import time

#h0 = open("day15-ex.txt")
h0 = open("day15.txt")

lines = h0.readlines()

grid = [[int(x) for x in list(line.strip())] for line in lines]

def build_big_grid(grid):
    big_grid = copy.deepcopy(grid)
    dimy = len(grid)
    dimx = len(grid[0])
    
    cg = grid
    
    for gx in range(4):
        ng = []
        for line in cg:
            nl = [(x % 9) +1  for x in line]
            ng.append(nl)
        for y, line in enumerate(ng):
            big_grid[y] += line
        cg = ng
    for gy in range(4):
        for i, line in enumerate(big_grid[gy*dimx:(gy*dimx)+dimx]):
            nl = [(x % 9) +1  for x in line]
            big_grid.append(nl)

    return big_grid

def print_distgrid(grid):
    for y, line in enumerate(grid):
        pl = ""
        for x, cell in enumerate(line):
            #pl += "*%d" % cell
            pl = "%s %03d" % (pl,cell)
        print(pl)
    print("*******************************")



def main(grid):
    grid = build_big_grid(grid)
    dg = day15cy.main(grid)

    print_distgrid(dg)
    
#main(grid)
import cProfile; cProfile.run("main(grid)")
