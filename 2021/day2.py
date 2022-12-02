h0 = open("day2.txt")
lines = [l.split() for l in h0.readlines()]

x = 0
depth = 0
aim = 0

for l in lines:
    m = int(l[1])
    print(l[0])
    if l[0] == "forward":
        x += m
        depth += m * aim
    elif l[0] == "down":
        aim += m
    elif l[0] == "up":
        aim -= m

print("x = %d" % x)
print("depth = %d " % depth)
print("answer = %d" % (x*depth))
