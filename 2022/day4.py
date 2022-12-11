p1c,p2c = 0,0
for pair in [el.strip().split(",") for el in open("day4.txt").readlines()]:
    se0 = set(range(int(pair[0].split("-")[0]), int(pair[0].split("-")[1])+1))
    se1 = set(range(int(pair[1].split("-")[0]), int(pair[1].split("-")[1])+1))
    if se0.issubset(se1) or se1.issubset(se0):
        p1c+=1
    if se0.intersection(se1):
        p2c+=1
print("Part 1 answer: %d, Part 2 answer: %d" % (p1c,p2c))


