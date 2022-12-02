from collections import Counter

#h0 = open("day12-ex1.txt")
#h0 = open("day12-ex2.txt")
#h0 = open("day12-ex3.txt")
h0 = open("day12.txt")
data = h0.readlines()
pairs = [l.strip().split('-') for l in data]

left = [pair[0] for pair in pairs]
right = [pair[1] for pair in pairs]

#keys = set(left+right)
keys = left+right

g0 = dict([(k, set()) for k in keys])

for pair in pairs:
    g0[pair[0]].add(pair[1])
    g0[pair[1]].add(pair[0])
    
print(g0)
print("****************************")

paths = set()


def recurse_you(g0, node, paths, path):
    path = path + (node,)
    #print(node)
    #print(path)
    if node == "end":
        paths.add(path)
        return paths
    for child in g0[node]:
        if child != path[-1]:
            if (child.lower() == child) and child in path:
                continue
            paths = recurse_you(g0, child, paths, path)

    return paths


def recurse_you_pt2(g0, node, paths, path):
    child_count = Counter(path)
    path = path + (node,)
    #print(node)
    #print(path)
    if node == "end":
        paths.add(path)
        return paths
    for child in g0[node]:
        
        if len(path) == 7 and node == "dc" and child == "kj":
            #print(path)
            #import pdb; pdb.set_trace()
            pass
        if (child != path[-1]) and (child != "start"):
            if (child.lower() == child) and (child != "end"):
                if (child_count[child] > 0) and count_all_smalls(path):
                    continue
            paths = recurse_you_pt2(g0, child, paths, path)

    return paths
    
def count_all_smalls(path):
    child_count = Counter(path)
    smalls = set([c for c in path if c.lower() == c])
    smalls.discard("start")
    smalls.discard("end")
    for s in smalls:
        if child_count[s] > 1:
            return True


            
#paths = recurse_you(g0, "start", paths, tuple())
paths = recurse_you_pt2(g0, "start", paths, tuple())

once_smalls = 0
has_a_small = 0

#for p in paths:
for p in sorted(list(paths)):   
    smalls = len([x for x in p if (x.lower() == x) and (x!="end") and (x!="start")])
    
    #print("%s   :::   %d" % (str(p), smalls))
    #if(len(p) > 8):
    #    print(p)
    print(p)
    if smalls < 2:
        once_smalls+=1
    if smalls > 0:
        has_a_small += 1
#print(once_smalls)
print(len(paths))
#print(has_a_small)        

