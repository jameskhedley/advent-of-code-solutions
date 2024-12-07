#h0 = open("./day2_ex.txt")
h0 = open("./day2.txt")
l0 = [list(map(int, n.strip().split(' '))) for n in h0.readlines()]

def safe(row):
    safe = True
    old_delta = 0
    for idx, x in enumerate(row[:len(row)-1]):
        delta = row[idx+1] -x
        if abs(delta) > 3 or delta == 0:
            safe = False
            break
        if (old_delta > 0 and delta < 0) or  (old_delta < 0 and delta > 0):
            safe = False
            break
        old_delta = delta
    return safe, idx

def calc(damp=False):
    count = 0
    for idx, row in enumerate(l0):
        res, _ = safe(row)
        if (not res) and damp:
            for xx in range(len(row)):
                rr = row[:xx:]+row[xx+1::]
                res, _ = safe(rr)
                if res: break
        count += int(res)
    return count

print("pt1: %d" % calc(False))
print("pt2: %d" % calc(True))