import re
from itertools import permutations, product

def main():
    #with open("day12_ex0.txt") as h0:
    with open("day12_data.txt") as h0:
        l0 = [x.strip() for x in h0.readlines()]
    pt1(l0)
    #pt2(l0)

def pt1(l0):
    lens = []
    for s0 in l0:
        s1 = s0.split(" ")[0]
        t1 = tuple([int(x) for x in s0.split(" ")[1].split(",")])
        nl = pt1_calc(s1,t1)
        lens.append(nl)
    print(lens)

def pt1_calc(s1,t1, length=0):
    if not s1:
        return 0
    char = s1[0]
    s1 = s1[1:]
    t0 = t1[0]
    t2 = t1[1:]

    if char == "?":
        return pt1_calc("#"+s1,t1) + pt1_calc("."+s1,t1)
    if char == "#":
        if length > t0:
            return 0
        else:
            return pt1_calc(s1,t1,length+1)
    if char == '.':
        if length == 0:
            return pt1_calc(s1, t1, 0)
        elif length == t0:
            return pt1_calc(s1, t2, 0)
        else:
            return 0


def pt1_brut_force(l0):
    # sigh... I thought it was clever but it just doesn't scale
    lens = []
    for s0 in l0:
        s1 = s0.split(" ")[0]
        t1 = tuple([int(x) for x in s0.split(" ")[1].split(",")])
        nl = pt1_calc_brut(s1,t1)
        lens.append(nl)
    print(lens)
    
def pt1_calc_brut(s1,t1):
    print(s1)
    pgs = []
    for group in re.finditer("\?+", s1):
        lg = len(group.group())
        temp0 = set(permutations("#."*(int(lg/2)+1), lg))
        temp0.add(tuple("#"*lg))
        pgs.append(temp0)

    #for p in pgs:
    #    print(p)
    prod = set(product(*pgs))
    res = []
    loop = 0
    for combo in prod:
        ns = str(s1)
        for idx, group in enumerate(re.finditer("\?+", ns)):
            gs = group.span()
            ns = ns[:gs[0]] + "".join(combo[idx]) + ns[gs[1]:]
        res.append(ns)
        loop += 1
        if loop % 100 == 0:
            print(loop)

    filtered = set()
    for rr in res:
        groups = re.findall("\#+", rr)
        if len(groups) == len(t1):
            b_add = True
            for i,g in enumerate(groups):
                if len(g) != t1[i]:
                    b_add = False
                    break
            if b_add:
                filtered.add(rr)
    #for f in filtered:
    #    print(f)
    #print(len(filtered))
    return len(filtered)

main()


#s1 = "???.###"
#t1 = (1,1,3)

#s1 = ".??..??...?##."
#t1 = (1,1,3)
#s1 = "??.??"
#t1 = (1,1)
#s1 = "?###????????"
#t1 = (3,2,1)
