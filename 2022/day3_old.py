import string
AB = list(string.ascii_letters)
#l0 = [el.strip() for el in open("day3.txt").readlines()]
l0 = [el.strip() for el in open("day3_ex.txt").readlines()]

calc = lambda x: AB.index(x) +1

def detect(s0):
    set_l = set(list(s0[:int(len(s0)/2)]))
    set_r = set(list(s0[int(len(s0)/2):]))
    temp = set_l.intersection(set_r).pop()
    print(temp)
    print(calc(temp))
    return temp

print(sum([calc(detect(el)) for el in l0]))
