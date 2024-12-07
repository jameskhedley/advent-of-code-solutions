debug = 0
if debug:
    lines = ''.join(open("./day5_ex.txt").readlines()).split()
    print(lines)
else:
    lines = ''.join(open("./day5.txt").readlines()).split()


rules = []
updates = []
for line in lines:
    if not line.strip():
        continue
    elif '|' in line:
        rules.append(tuple(int(x) for x in line.split('|')))
    else:
        updates.append(tuple(int(x) for x in line.split(',')))
if debug:
    print(rules)
    print(updates)

def part1(updates, rules):
    accept = []

    for u in updates:
        good = True
        for rule in rules:
            bef, aft = rule
            if bef in u and aft in u:
                pos_bef = u.index(bef)
                pos_aft = u.index(aft)
                if pos_bef > pos_aft:
                    good = False
                    continue
        if good:
            accept.append(u)
    if debug:
        print(accept)
    sum = 0
    for a in accept:
        sum += a[len(a)//2]
    return sum

def violations(u, rules):
    v = 0
    for rule in rules:
        bef, aft = rule
        if bef in u and aft in u:
            pos_bef = u.index(bef)
            pos_aft = u.index(aft)
            if pos_bef > pos_aft:
                v+=1
                
    return v

def part2(updates, rules):
    accept = []
    count = 0
    for u in updates:
        print('loop %d' % count)
        keep = False
        v0 = violations(u, rules)
        while v0 > 0:
            for rule in rules:
                bef, aft = rule
                if bef in u and aft in u:
                    pos_bef = u.index(bef)
                    pos_aft = u.index(aft)
                    if pos_bef > pos_aft:
                        nu = list(u)
                        nu[pos_bef] = aft
                        nu[pos_aft] = bef
                        u = nu
                        keep = True
                        continue
            v0 = violations(u, rules)
        if keep:
            accept.append(u)
        count += 1
    if debug:
        print(accept)
    sum = 0
    for a in accept:
        sum += a[len(a)//2]
    return sum

#print("pt1: %d" % part1(updates, rules))

# test= ((75,97,47,61,53), (61,13,29), (97,13,75,29,47),
#        (97,75,47,61,53), (61,29,13), (97,75,47,29,13))
# for t0 in test:
#     v0 = violations(t0, rules)
#     print("Found %d violations in update %s " % (v0, t0))


print("pt2: %d" % part2(updates, rules))