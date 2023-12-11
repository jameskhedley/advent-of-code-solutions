from pprint import pprint as pp
from math import lcm

h0 = open("day8_data.txt")
#h0 = open("day8_ex.txt")
#h0 = open("day8_ex2.txt")
#h0 = open("day8_ex3.txt")

l0 = [n.strip() if n.strip() else None for n in h0.readlines()]

def pt2(l0):
    dirs = list(l0[0])
    nodes = {x.split(" = ")[0]: x.split(" = ")[1].strip("(").strip(")").split(", ") for x in l0[2:]} 

    KEY = {'L':0,'R':1}
    idir = 0
    count = 0
    counts = []

    n0 = [x for x in nodes.keys() if x[2] == 'A'] #starting points

    while n0:
        step = dirs[idir]
        n0 = [nodes[node][KEY[step]] for node in n0] #advance each of the paths
        n1 = [x for x in n0 if x[2] != 'Z'] #detect end nodes
        count += 1
        if len(n1) < len(n0):
            counts.append(count) #we found one
        idir = (idir + 1) % len(dirs)
        n0 = n1
        
    print(counts)
    print(lcm(*counts)) #idk... maths?

def pt1(l0):
    dirs = list(l0[0])
    nodes = {x.split(" = ")[0]: x.split(" = ")[1].strip("(").strip(")").split(", ") for x in l0[2:]} 
    n0 = 'AAA'
    KEY = {'L':0,'R':1}
    idir = 0
    count = 0

    while n0 != 'ZZZ':
        step = dirs[idir]
        n0 = nodes[n0][KEY[step]]
        idir = (idir + 1) % len(dirs)
        count += 1
    print(count)

pt1(l0)
pt2(l0)
