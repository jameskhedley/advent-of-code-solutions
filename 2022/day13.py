import copy, functools, pprint
#lines = [line.strip() for line in open("day13_ex.txt").readlines()]
lines = [line.strip() for line in open("day13.txt").readlines()]

def prepair(left, right):
    l2, r2 = list(left), list(right)
    while len(l2) < len(r2): l2.append(None)
    while len(r2) < len(l2): r2.append(None)
    return list(zip(l2, r2))

def compare(left, right, debug=False):
    if debug:
        print(left)
        print(right)
    if type(left) == type(0) and type(right) == type(0):
        if left < right:
            return 1
        if left > right:
            return -1
    elif type(left) == type([]) and type(right) == type([]):
        zipped = prepair(left,right)
        for l,r in zipped:
            if l == None:
                return 1
            elif r == None:
                return -1
            if type(l) == type([]) or type(r) == type([]):
                if type(l) == type([]) and type(r) == type([]):
                    result = compare(l,r, debug)
                elif type(l) == type([]) and type(r) == type(0):
                    result = compare(l,[r], debug)
                elif type(l) == type(0) and type(r) == type([]):
                    result = compare([l],r, debug)
                if result == 0:
                    continue
                else:
                    return result
            elif l < r:
                return 1
            elif l > r:
                return -1
    elif type(left) == type([]) and type(right) == type(0):
        return compare(left,[right], debug)
    elif type(left) == type(0) and type(right) == type([]):
        return compare([left],right, debug)
    return 0

# Part 1
tt = {-1:False, 0:None, 1:True}
left,right="",""
count = 0
results = []
lines.append(None) #hacky hack
p2_lines = copy.deepcopy(lines)
while lines:
    line = lines.pop(0)
    if not line:
        count+=1
        print("== Pair %d ==" % count)
        ordered = compare(left, right)
        print(tt[ordered])
        if ordered>0:
            results.append(count)
        left,right="",""
    elif left == "":
        exec("left = " + line)
    else:
        exec("right = " + line)

print("Part 1 results:")
print(results)
print(sum(results))

# Part 2
results = []
while p2_lines:
    line = p2_lines.pop(0)
    if not line:
        results.append(left)
        results.append(right)
        left,right="",""
    elif left == "":
        exec("left = " + line)
    else:
        exec("right = " + line)
results.append([[2]])
results.append([[6]])

print("Part 2 results:")
results.sort(key=functools.cmp_to_key(compare), reverse=True)
pprint.pprint(results)
p1,p2 = results.index([[2]])+1, results.index([[6]])+1
print(p1*p2)

