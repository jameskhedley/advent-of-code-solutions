from collections import Counter, defaultdict
#h0 = open("day14-ex.txt")
h0 = open("day14.txt")
data = h0.readlines()

start = list(data[0].strip())

strs = data[2:]
inserts = dict([s.strip().split(" -> ") for s in strs])

def loop(counts, i):
    chars = defaultdict(int)
    
    old_counts = dict(counts)
    new_counts = {}
    for pair, value in old_counts.items():
        if old_counts[pair] < 1: continue
        #for instance in range(old_counts[pair]): #sloooooow
        ocp = old_counts[pair]

        if pair not in new_counts:
            new_counts[pair] = 0
        change = inserts[pair]
        np0 = pair[0] + change
        np1 = change + pair[1]
        for np in (np0, np1):
            if np in new_counts:
                new_counts[np]+=ocp
            else:
                new_counts[np]=ocp

        chars[pair[1]]+=ocp
        chars[change]+=ocp
    return new_counts, chars

def main(STEPS):
    pairs = []
    for x in range(len(start)-1):
        pairs.append(start[x]+start[x+1])

    counts = dict(Counter(pairs))
    print("0")
    print(counts)

    for i in range(1,STEPS+1):
        print(i)
        counts, chars = loop(counts, i)
        print(counts)
        chars[start[0]] += 1 #haaaaack
        print(chars)

    print("Length: %d" % (sum([v for v in counts.values()])+1))
    final = max(chars.values()) - min(chars.values())
    print(final)

#import pdb; pdb.set_trace()

import cProfile
#STEPS = 10
#STEPS = 22
STEPS = 40

#cProfile.run('main(STEPS)')
main(STEPS)
