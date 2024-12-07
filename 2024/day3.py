import re
#s0 = ''.join(open("./day3_ex.txt").readlines())
#s0 = ''.join(open("./day3_ex2.txt").readlines())
s0 = ''.join(open("./day3.txt").readlines())

mul_pattern = r"mul\(\d+,\d+\)"
mul_matches = re.findall(mul_pattern, s0 )

mul_pos, do_pos, no_pos = [], [], []
for mm in re.finditer(mul_pattern, s0 ):
    mul_pos.append(mm.span())

do_pattern = r"do\(\)"
for dp in re.finditer(do_pattern, s0 ):
    do_pos.append(dp.span())

dont_pattern = r"don't\(\)"
for dn in re.finditer(dont_pattern, s0 ):
    no_pos.append(dn.span())

sum = 0

do_or_dont = {}
doit = True
nx_do = do_pos.pop(0)
nx_dont = no_pos.pop(0)
for char in range(len(s0)):
    if char > nx_do[0] and char < nx_do[1]:
        doit = True
    elif char > nx_dont[0] and char < nx_dont[1]:
        doit = False
    if char > nx_do[1]:
        if do_pos:
            nx_do = do_pos.pop(0)
        else:
            nx_do = (999999,999999)
    if char > nx_dont[1]:
        if no_pos:
            nx_dont = no_pos.pop(0)
        else:
            nx_dont = (999999,999999)
    do_or_dont[char] = doit

debug = False

for mulcount, mul in enumerate(mul_matches):
    m0 = mul_pos[mulcount][0]
    m1 = mul_pos[mulcount][1]
    if do_or_dont[m0+1]:
        clean = mul.strip('mul(').strip(')')
        terms = [int(dig) for dig in clean.split(',')]
        print(terms)
        sum += terms[0] * terms[1]

print(sum)