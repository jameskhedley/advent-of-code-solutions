import re
from functools import reduce
h0 = open("day2_data.txt")
#h0 = open("day2_ex.txt")

l0 = [n.strip().lower() if n.strip() else None for n in h0.readlines()]

def parse(l0):
    data = {}
    for game in l0:
        gdata = []
        p0 = game.find(":")
        gid = int(re.findall(r'\d+', game[:p0])[0])
        rounds = game[p0+1:].split(";")
        for r0 in rounds:
            rdata = {}
            pieces = r0.split(',')
            for pp in pieces:
                colour = re.findall(r'[a-z]+', pp)[0]
                count = int(re.findall(r'\d+', pp)[0])
                rdata[colour] = count
                #print(pieces)
            gdata.append(rdata)
        data[gid] = gdata
    return(data)

def pt1():
    data = parse(l0)
    lims = {'red':12, 'green':13, 'blue': 14}

    filtered = []
    for gid, rounds in data.items():
        add = True
        for round in rounds:
            for colour in round.keys():
                if round[colour] > lims[colour]:
                    add = False
        if add:
            filtered.append(gid)
    print(filtered)
    print(sum(filtered))

def pt2():
    data = parse(l0)
    result = []
    for gid, rounds in data.items():
        gmins = {'green':0, 'red': 0, 'blue': 0 }

        for round in rounds:
            for c in gmins.keys():
                if c in round:
                    gmins[c] = max(gmins[c], round[c])
        print(gmins)
        product = reduce(lambda x, y: x*y, gmins.values())
        result.append(product)
    print(result)
    print(sum(result))


#pt1()
pt2()