import string
AB = list(string.ascii_letters)
l0 = [el.strip() for el in open("day3.txt").readlines()]

calc = lambda x: AB.index(x) +1

total = 0
idx=0
while idx < len(l0):
    total += calc(set(l0[idx]).intersection(set(l0[idx+1])).intersection(set(l0[idx+2])).pop()) 
    idx+=3

print(total)
