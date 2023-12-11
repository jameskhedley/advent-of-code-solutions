from pprint import pprint as pp

h0 = open("day9_ex.txt")
h0 = open("day9_data.txt")
l0 = [n.strip() if n.strip() else None for n in h0.readlines()]

def pt2(l0):
    acc = accum(l0)
    res=[]
    for a0 in acc:
        a1 = []
        while a0:
            line = a0.pop()
            if all([True if x==0 else False for x in line]):
                line.insert(0,0)
            else:
                nn = line[0] - a1[-1][0]
                line.insert(0, nn)
            a1.append(line) 
        res.append(a1[-1])
    ans = [r[0] for r in res]
    pp(sum(ans))


def pt1(l0):
    acc = accum(l0)
    res=[]
    for a0 in acc:
        a1 = []
        while a0:
            line = a0.pop()
            if all([True if x==0 else False for x in line]):
                line.append(0)
            else:
                nn = line[-1] + a1[-1][-1]
                line.append(nn)
            a1.append(line) 
        res.append(a1[-1])
    ans = [r[-1] for r in res]
    pp(sum(ans))
    
def accum(l0):
    acc=[]
    for line in l0:
        line = [int(x) for x in line.split(" ")]
        nls=[line]
        while not all([True if x==0 else False for x in line]):
            nl=[]
            for idx, val in enumerate(line[:-1]):
                nl.append(line[idx+1]-val)
            line=nl
            nls.append(nl)
        acc.append(nls)
    return acc

#pt1(l0)
pt2(l0)
