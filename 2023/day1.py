import string
h0 = open("day1_data.txt")
#h0 = open("day1_ex.txt")
#h0 = open("day1_ex2.txt")
l0 = [n.strip().lower() if n.strip() else None for n in h0.readlines()]

nums = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

def f0(line, direction):
    if direction > 0:
        line = line[::-1]
    for x in list(line):
        if x not in string.ascii_lowercase:
            return x

def pt1():
    l1 = [ (f0(line, 0), f0(line, 1)) for line in l0]
    l2 = [int(x[0] + x[1]) for x in l1]
    print(sum(l2))

def test():
    assert preprocess("one") == "o1e"
    assert preprocess("two") == "t2o"
    assert preprocess("aone") == "ao1e"
    assert preprocess("onetwo") == "o1et2o"
    assert preprocess("eightwo") == "e8t2o"
    assert preprocess("ninesixmlfjxhscninehqcdvxf8nzfivetwonehhd") == "n9es6xmlfjxhscn9ehqcdvxf8nzf5et2o1ehhd"
    print("all good")

def preprocess(line):
    len0 = 3
    start = 0
    while start < len(line)-2:
        while len0 <= len(line):
            for idx, num in enumerate(nums):
                if line[start:len0+start] == num[:len0]:
                    if len0 == len(num):
                        line = line[:start+1] + str(idx+1) + line[len0+start-1:]
                        break
            len0 += 1
        start+=1
        len0 = 3
                
    return line
    
def pt2():
    l1 = [preprocess(x) for x in l0]
    l2 = [ (f0(line, 0), f0(line, 1)) for line in l1]
    l3 = [int(x[0] + x[1]) for x in l2]
    print(sum(l3))    

test()

pt1()
pt2()



