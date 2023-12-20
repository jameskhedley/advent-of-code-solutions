from collections import defaultdict

def calc(s0):
    l0 = list(s0)
    score = 0
    for char in l0:
        score += ord(char)
        score *= 17
        score = score % 256
    return(score)

def test():
    assert calc("HASH") == 52
    assert calc("rn=1") == 30
    assert calc("cm-") == 253

    test0 = "rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"
    ans = sum([calc(x) for x in test0.split(",")])
    assert ans==1320

    assert pt2(test0.split(",")) == 145

    print("tests passed")

def pt2(l0):
    hashmap = defaultdict(dict)
    for inst in l0:
        if "=" in inst:
            label, foclen = inst.split("=")
            box = calc(label)
            hashmap[box][label] = int(foclen)
        else:
            label = inst.strip("-")
            box = calc(label)
            hashmap[box].pop(label, None)
    ans = 0
    for idx_box, box in hashmap.items():
        explo = [(k,v[0],v[1]) for k,v in enumerate(box.items())]
        for idx_lens, lens, foc in explo:
            ans+= (idx_box+1) * box[lens] * (idx_lens+1)
    return ans


def main():
    test()
    with open("day15_data.txt") as h0:
        l0 = h0.readlines()[0].strip().split(",")
    pt1(l0)
    print(pt2(l0))

def pt1(l0):
    ans = sum([calc(x) for x in l0])
    print(ans)


main()