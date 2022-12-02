from collections import Counter
h0 = open("day14-ex.txt")
#h0 = open("day14.txt")
data = h0.readlines()

start = list(data[0].strip())

strs = data[2:]
inserts = dict([s.strip().split(" -> ") for s in strs])

def loop(chain, inserts):
    pairs = []
    for x in range(len(chain)-1):
        pairs.append([chain[x],chain[x+1]])
        
    #print(pairs)
    for pair in pairs:
        found = inserts["".join(pair)]
        pair.insert(1,found)
        
    #print(pairs)

    result = ""
    all_pairs = []
    for idx, pair in enumerate(pairs):
        if idx > 0:
            pair = pair[1:]
        result += "".join(pair)
        #temp = "".join(pair)
        #result = "".join([result, temp])
    return result

def main(start, inserts, STEPS):
    result = list(start)

    for n in range(STEPS):
        print("Calculating step %d..." % n)
        result = loop(result, inserts)
        print("Result length %d" % len(result))
        
    #print(result)

    ct = Counter(result)
    print(ct)
    final = max(ct.values()) - min(ct.values())
    print(final)

import cProfile
#STEPS = 10
STEPS = 23
#STEPS = 40

cProfile.run('main(start, inserts, STEPS)')
#main(start, inserts, STEPS)


