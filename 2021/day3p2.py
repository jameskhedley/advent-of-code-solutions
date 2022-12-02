h0 = open("day3.txt")
data = h0.readlines()

groups = [list(l.strip()) for l in data]

BYTE_LEN = len(groups[0])

ogr = "0b"

for byte_num in range(BYTE_LEN):
    print("***************")
    bytes0 = [int(l[byte_num]) for l in groups]
    crit = 1 if sum(bytes0) >= (len(bytes0)/2) else 0
    print(crit)
    groups = [g for g in groups if g[byte_num] == str(crit)]
    print(groups)
    if len(groups) == 1:
        ans_ogr = int(ogr + ''.join(groups[0]),2)
        break

print("OGR: %d" % ans_ogr)
print("***************")


cor = "0b"

groups = [list(l.strip()) for l in data]
for byte_num in range(BYTE_LEN):
    print("***************")
    bytes0 = [int(l[byte_num]) for l in groups]
    crit = 1 if sum(bytes0) < (len(bytes0)/2) else 0
    print(crit)
    groups = [g for g in groups if g[byte_num] == str(crit)]
    print(groups)
    if len(groups) == 1:
        ans_cor = int(cor + ''.join(groups[0]),2)
        break

print("C02R: %d" % ans_cor)

print("ANS: %d" % (ans_cor*ans_ogr))
