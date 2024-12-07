from collections import defaultdict
#h0 = open("./day1_ex.txt")
h0 = open("./day1.txt")
l0 = [n.strip().split('   ') for n in h0.readlines()]
ll, lr = [], []
for el in l0:
    ll.append(int(el[0]))
    lr.append(int(el[1]))

def pt1():
    ll.sort()
    lr.sort()

    sum = 0

    for idx in range(len(ll)):
        sum += abs(ll[idx] - lr[idx])
    print(sum)


def pt2():
    sum = 0
    freq = defaultdict(int)
    for nr in lr:
        freq[nr] += 1
    for idx, nl in enumerate(ll):
        sum += (nl * freq[nl])
    print(sum)


pt1()
pt2()