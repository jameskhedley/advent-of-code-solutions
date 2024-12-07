import math, itertools
debug = 1
if debug:
    #lines = ''.join(open("./day7_ex.txt").readlines()).split("\n")
    lines = ''.join(open("./day7_td.txt").readlines()).split("\n")[:30]
else:
    lines = ''.join(open("./day7_data.txt").readlines()).split("\n")

data = []
for s0 in lines:
    n, t = [x.strip() for x in s0.split(":")]
    n = int(n)
    t = [int(x) for x in t.split()]
    #t = [x for x in t.split()]
    data.append([n, t])

def alternator(n):
    for i in range(n):
        if i % 2 == 0:
            yield '*'
        else:
            yield '+'

def pt1(data):
    found = []
    #data = [[292, [11, 6, 16, 20]]]
    #data = [[4558, [4, 2, 894, 9, 4, 1, 851, 4, 4, 55]]]
    #data = [[20592, [46, 62, 81, 97, 72]]]
    data = [[1501, [26, 6, 343, 940, 62]]]
    lc = 0
    lens = [len(t) for n, t in data]
    alts = [x for x in alternator(max(lens))]
    ml = max(lens)
    seq_cache = [0] * (ml+1)
    for idx, (n,t) in enumerate(data):
        if seq_cache[len(t)] != 0:
            continue
        print("warm up: %d" % len(t))
        #seq_cache[len(t)] = set(itertools.permutations(alts[:len(t)]))
        seq_cache[len(t)] = list(itertools.permutations(alts[:len(t)]))
    
    for n, t in data:
        print(lc)
        if sum(t) == n:
            found.append(n)
        elif math.prod(t) == n:
            found.append(n)
        else:
            sops = seq_cache[len(t)]
            print(len(sops))
            itcount = 0
            for ol in sops:
                itcount += 1
                if itcount % 1000 == 0:
                    print(itcount)
                ol = list(ol)
                ol.append('')
                terms = [val for pair in zip(t, ol) for val in pair][:-1]
                equat = ''.join([str(x) for x in terms])
                if debug:
                    print(equat)
                if equat == '26*6+343+940+62':
                    stop = 1
                res = 0
                buf = [terms.pop(0)]
                while len(terms)>1:
                    if res > n:
                        break
                    tmp, terms = terms[:2], terms[2:]
                    buf+=tmp
                    if buf[1] == '+':
                        res = buf[0]+buf[2]
                    elif buf[1] == '*':
                        res = buf[0]*buf[2]
                    buf = [res]
                if res == n:
                    found.append(n)
                    break
        lc+=1    

    print(len(found))
    print(found)
    print(sum(found))

pt1(data)
