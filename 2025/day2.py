ex = False

def test_invalidity():
    assert invalidity('222220') == False
    assert invalidity('222221') == False
    assert invalidity('222223') == False
    assert invalidity('824824824') == True
    assert invalidity('123') == False
    assert invalidity('1') == False
    assert invalidity('11') == True
    assert invalidity('999') == True
    assert invalidity('1010') == True
    assert invalidity('565656') == True
    count = 0
    for t0 in range(11,23):
        if invalidity(str(t0)):
            count+=1
    assert count == 2
    count = 0
    for t0 in range(99,112):
        if invalidity(str(t0)):
            count+=1
    assert count == 2
    count = 0
    for t0 in range(998,1012):
        if invalidity(str(t0)):
            count+=1
    assert count == 2
    count = 0
    for t0 in range(1188511880,1188511890):
        if invalidity(str(t0)):
            count+=1
    assert count == 1
    count = 0
    for t0 in range(222220,222224):
        if invalidity(str(t0)):
            count+=1
    assert count == 1
    count = 0
    for t0 in range(1698522,1698528):
        if invalidity(str(t0)):
            count+=1
    assert count == 0
    count = 0
    for t0 in range(446443,446449):
        if invalidity(str(t0)):
            count+=1
    assert count == 1
    count = 0
    for t0 in range(38593856,38593862):
        if invalidity(str(t0)):
            count+=1
    assert count == 1
    count = 0
    for t0 in range(565653,565659):
        if invalidity(str(t0)):
            count+=1
    assert count == 1
    count = 0
    for t0 in range(824824821,824824827):
        if invalidity(str(t0)):
            count+=1
    assert count == 1
    
    print('Tests passed')

def get_data():
    if ex:
        h0 = open("./day2_ex.txt")
    else:
        h0 = open("./day2.txt")
    l0 = h0.readlines()[0].strip().split(',')
    l1 = [(int(n.split('-')[0]),int(n.split('-')[1])) for n in l0]
    return l1

def part1(data):
    ans = 0
    #print(data)
    for pair in data:
        rr = list(pair)
        rr[1] = pair[1]+1
        for idn in range(*rr):
            ids  = str(idn)
            l,r = ids[0:len(ids)//2], ids[len(ids)//2:]
            if l==r:
                #print(idn)
                ans+=idn
    return ans

def part2(data):
    ans = 0
    #print(data)
    for pair in data:
        rr = list(pair)
        rr[1] = pair[1]+1
        for idn in range(*rr):
            if invalidity(str(idn)):
                #print(idn)
                ans+=idn
    return ans

def invalidity(ids):
    if len(ids) == 1:
        return False #lmao sneaky!
    if len(set(list(ids))) == 1:
        return True
    for sublen in range(2,(len(ids)//2+1)):
        mult = len(ids) // sublen
        if ids[:sublen] * mult == ids:
            return True

    l,r = ids[0:len(ids)//2], ids[len(ids)//2:]
    return l==r


#ex = True
data = get_data()
test_invalidity()
print("Part 1 answer: %d" % part1(data))
print("Part 2 answer: %d" % part2(data))


