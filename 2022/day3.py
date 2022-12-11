import string
calc = lambda x: list(string.ascii_letters).index(x) +1
detect = lambda x: set(list(x[:int(len(x)/2)])).intersection(set(list(x[int(len(x)/2):]))).pop()
print(sum([calc(detect(el)) for el in [el.strip() for el in open("day3.txt").readlines()]]))
