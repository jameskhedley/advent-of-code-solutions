from collections import Counter
h0 = open("day14-ex.txt")
#h0 = open("day14.txt")
data = h0.readlines()

start = list(data[0].strip())

strs = data[2:]
inserts = dict([s.strip().split(" -> ") for s in strs])

def loop(buckets, inserts):
    #print(inserts)
    for insert in inserts:
        tup_ins = tuple(insert)
        #print(insert)
        if tup_ins in buckets.keys():
            #import pdb; pdb.set_trace()
            n = buckets[tup_ins]
            
            triple = tuple([tup_ins[0], inserts[insert], tup_ins[1]])
            if triple in buckets:
                buckets[triple] += 1
            else:
                buckets[triple] = 1
            buckets[tup_ins] -= 1
        
    print(buckets)

    return buckets



def main(start, inserts, STEPS):
    pairs = []
    for x in range(len(start)-1):
        pairs.append([start[x],start[x+1]])
    buckets = dict([(tuple(p), 1) for p in pairs])

    for n in range(STEPS):
        print("Calculating step %d..." % n)
        buckets = loop(buckets, inserts)
        
    print(buckets)

    final = max(buckets.values()) - min(buckets.values())
    print(final)
    
def main_old(start, inserts, STEPS):
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


#import cProfile
STEPS = 10
#STEPS = 20
#STEPS = 40

#cProfile.run('main(start, inserts, STEPS)')
main(start, inserts, STEPS)


