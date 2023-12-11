h0 = open("day6_data.txt")
#h0 = open("day6_ex.txt")

l0 = [n.strip().lower() if n.strip() else None for n in h0.readlines()]

def pt2(l0):
    # Yes yes I know, quadratic equations blah
    t0 = int(l0[0].split(":")[1].replace(" ",""))
    d0 = int(l0[1].split(":")[1].replace(" ",""))
    
    wins = 0
    print(t0)
    for sec in range(t0+1):
        if sec % 1000 == 0:
            print(sec)
        spd = sec
        trav = spd * (t0 - sec)
        if trav > d0:
            wins += 1
    print(wins)


def pt1(l0):
    t0 = [int(x) for x in l0[0].split(":")[1].split(" ") if x]
    d0 = [int(x) for x in l0[1].split(":")[1].split(" ") if x]

    score = 1
    for time, dist in zip(t0,d0):
        wins = []
        for sec in range(time+1):
            spd = sec
            trav = spd * (time - sec)
            if trav > dist:
                wins.append(sec)
        print(wins)
        score *= len(wins)
    print(score)

#pt1(l0)
pt2(l0)
