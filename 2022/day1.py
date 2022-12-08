h0 = open("day1.txt")
l0 = h0.readlines()
l0 = [int(n.strip()) if n.strip() else None for n in l0]
groups = {}
pointer = 0

for idx, n in enumerate(l0):
    if not n:
        groups[idx] = sum(l0[pointer:idx])
        pointer = idx+1

print(groups)
print(max(groups.values()))
