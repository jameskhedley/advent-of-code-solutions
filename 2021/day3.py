h0 = open("day3.txt")
lines = h0.readlines()

l0 = [list(l.strip()) for l in lines]
#print(l0)
groups = [list(l.strip()) for l in lines]

gamma = "0b"
epsilon = "0b"

BYTE_LEN = len(groups[0])
print(BYTE_LEN)

for i in range(BYTE_LEN):
    print("***************")
    bytes0 = [int(l[i]) for l in groups]
    print(bytes0)

    g = 1 if sum(bytes0) > (len(bytes0)/2) else 0
    e = 0 if sum(bytes0) > (len(bytes0)/2) else 1
    #print(g)
    gamma = gamma + str(g)
    epsilon = epsilon + str(e)
    
print(gamma)
print(epsilon)

ig = int(gamma,2)
ie = int(epsilon,2)
print(ig)
print(ie)

print(ig*ie)
    

