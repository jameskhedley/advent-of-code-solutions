h0 = open("/tmp/aoc.txt")
l0 = h0.readlines()
n0 = [int(n.split()[0]) for n in l0]

g0 = []

for i, n in enumerate(n0):
    t0 = n0[0+i : 3+i]
    if len(t0) == 3: g0.append(t0)

print(g0)

sums = [sum(g) for g in g0]
print(sums)

ans = 0
series = []

for i in range(len(sums)-1):
   if sums[i+1] > sums[i]:
      ans += 1
      series.append(1)
   else:
      series.append(0)

print(series)
print(ans)

