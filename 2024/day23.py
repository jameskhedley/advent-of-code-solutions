from collections import defaultdict, deque
from pprint import pprint
from copy import deepcopy

def read_data(fn):
    lines = [x.strip() for x in open(fn).readlines()]
    data = [x.split('-') for x in lines]
    return data

def build_graph(data):
    graph = defaultdict(list)
    for (c,s) in data:
        graph[c].append(s)
        graph[s].append(c)
    return graph

def part1(data):
    graph = build_graph(data)
    paths = find_cycles(graph, 4)
    pprint(paths)
    final = 0
    for path in paths:
        ptest = [x for x in path if x.startswith('t')]
        if ptest:
            final+=1
    print("Part 1...")
    pprint(len(paths))
    print(final)

def part2_slooow(data): # fine on example but too slow on input
    graph = build_graph(data)
    perfects = set()
    longest = 0   
    nvert = len(graph.keys())
    #for start_pos in graph.keys():
    for start_pos in ['de']:
        q = deque([(start_pos, [start_pos], defaultdict(set))])
        pprint(graph)
        while q:
            u, cliq, sg = q.popleft() # bfs
            if len(cliq) > nvert * 0.75:
                break # heuristic, very long paths aren't likely to be perfect
            if len(cliq) > longest:
                print(len(cliq))
            longest = max(longest, len(cliq))
            if cliq == ['de', 'co', 'ta', 'ka', 'de','ta','co', 'ka', 'de']:
                stop = 1
            # perfect graph? is every computer connected to every other in the subnet
            lc = len(set(cliq))
            if lc > 3:
                if all([True if len(v)== len(sg.keys())-1 else False for _,v in sg.items()]):
                    perfects.add(frozenset(cliq))
            nbors = graph[u]
            for nbor in nbors:
                if len(cliq) > 2 and nbor == cliq[-2]: # don't immediately reverse course
                    continue
                nsg = deepcopy(sg)
                nsg[u].add(nbor)
                nsg[nbor].add(u)
                ncliq = list(cliq)+[nbor]
                if len(set(ncliq)) > nvert//3:
                    continue # heuristic, large sets probably aren't perfect
                q.append((nbor, ncliq, nsg))
    pprint(perfects)
    top = sorted([list(x) for x in perfects], key=lambda x: len(x), reverse=True)[0]
    print("Part 2: " + ','.join(sorted(top)))

def part2_cycles(data): # also too slow, tries to find loops and then checks them
    graph = build_graph(data)
    nvert = len(graph.keys())
    cycles = set()
    perfects = set()
    #for ll in range(4,6):
    for ll in [9]:
        print(ll)
        lc = find_cycles(graph, ll)
        for llc in lc:
            if len(llc) > 3:
                cycles.add(llc)
    for cyc in cycles: # build a graph for each to see if they're perfect
    #for cyc in {frozenset({'ka', 'de', 'ta', 'co'})}: 
        sg = {}
        for node in cyc:
            sg[node]=[x for x in graph[node] if x in cyc]
        if all([True if len(v)== len(sg.keys())-1 else False for _,v in sg.items()]):
            print(sg)
            perfects.add(frozenset(cyc))
    print(len(perfects))
    if len(perfects)==1:
        print(perfects)

def find_cycles(graph, length):
    paths = set()
    count = 0
    for start_pos in graph.keys():
    #for start_pos in ['yn']:
        q = deque([(start_pos, [start_pos], set())])
        while q:
            u, cliq, vizedge = q.popleft()
            if len(cliq) > length:
                continue
            count += 1
            if count %10000 == 0: print(count)
            if cliq == ['co', 'de', 'ka', 'ta', 'co']:
            #if cliq == ['co']:
                stop = 1
            if len(cliq) == length:
                if cliq[0] == cliq[length-1]: #cycle detection
                    paths.add(frozenset(cliq))
                continue
            nbors = graph[u]
            for nbor in nbors:
                if (u,nbor) in vizedge:
                    continue
                if len(cliq) > 2 and nbor == cliq[-2]: # don't immediately reverse course
                    continue
                ncliq = list(cliq)+[nbor]
                if ncliq == ['co', 'de']:
                    stop =1
                sg = {}
                for node in ncliq:
                    sg[node]=[x for x in graph[node] if x in ncliq]
                if not all([True if len(v)== len(sg.keys())-1 else False for _,v in sg.items()]):
                    continue
                nvz = set(vizedge)
                nvz.add((nbor,u))
                #nvz.add((u,nbor))
                q.append((nbor, ncliq, nvz))
    print(count)
    return paths

def part2(data):
    graph = build_graph(data)
    result = bron_kerbosch(graph, [], list(graph.keys()), [], None)
    print(result)
    result.sort()
    print("Part 2 result: %s" % ','.join(result))

def bron_kerbosch(graph, r, p, x, found): # this is absolutely magic, courtesy of wikipedia lol
    if not(p) and not(x): #end state
        return r
    for node in list(p):
        nr = list(r)
        nr.append(node)
        nbors = graph[node]
        np = [v for v in p if v in nbors]
        nx = [v for v in x if v in nbors]
        res = bron_kerbosch(graph, nr, np, nx, found)
        if (res and found and len(res) > len(found)) or not found:
            found = res
        p.remove(node)
        x.append(node)
    return found

#data = read_data('day23_ex.txt')
data = read_data('day23_data.txt')

#part1(data)
#part2_cycles(data)
part2(data)
