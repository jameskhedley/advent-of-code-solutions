from pprint import pprint  as pp
h0 = open("day4_data.txt")
#h0 = open("day4_ex.txt")

l0 = [n.strip().lower() if n.strip() else None for n in h0.readlines()]

def pt2():
    winners = [set([int(x) for x in w0 if x]) for w0 in [x[:x.find("|")].split(" ") for x in [x[x.find(":")+1:] for x in l0]]]
    nums = [set([int(x) for x in w0 if x]) for w0 in [x[x.find("|")+1:].split( " ") for x in [x[x.find(":")+1:] for x in l0]]]
    cards = [list(a) for a in zip(winners, nums, [1]*len(nums))]
    i = 0
    while i < len(cards):
        s0 = len(cards[i][0].intersection(cards[i][1]))
        for _ in range(cards[i][2]):
            for j in range(i+1, i+s0+1):
                if j < len(winners):
                    cards[j][2] += 1
        i+=1
    print(sum([c[2] for c in cards]))

def pt1():
    winners = [set([int(x) for x in w0 if x]) for w0 in [x[:x.find("|")].split(" ") for x in [x[x.find(":")+1:] for x in l0]]]
    nums = [set([int(x) for x in w0 if x]) for w0 in [x[x.find("|")+1:].split( " ") for x in [x[x.find(":")+1:] for x in l0]]]
    score = 0
    for i in range(len(winners)):
        s0 = len(winners[i].intersection(nums[i]))
        score += 2**(s0-1) if s0 else 0
    print(score)

pt1()
pt2()
