def main():
    #with open("day11_ex.txt") as h0:
    with open("day11_data.txt") as h0:
        l0 = [list(x.strip()) for x in h0.readlines()]
    #pt1(l0)
    pt2(l0)

def pt1(l0):
    univ = expand_space(l0)
    univ, galaxies = mark_galaxies(univ)
   
    dist = {}
    for iglx, (x,y) in galaxies.items():
        dist[iglx] = {}
        for jglx, (xx,yy) in galaxies.items():
            if iglx == jglx: 
                continue
            cd = abs(x-xx) + abs(y-yy)
            dist[iglx][jglx] = cd
        
    ans = 0
    for iglx, cds in dist.items():
        ans += sum(cds.values())
    print(ans/2) # double counting trips
    
def pt2(l0):
    void = 1000000
    #void = 10
    #void = 100
    insert_rows, insert_cols = expand_space_pt2(l0)
    univ, galaxies = mark_galaxies(l0, insert_rows, insert_cols)
   
    dist = {}
    for iglx, (x,y) in galaxies.items():
        dist[iglx] = {}
        for jglx, (xx,yy) in galaxies.items():
            if iglx == jglx: 
                continue
            cd = abs(x-xx) + abs(y-yy)
            for ic in insert_cols:
                if ic in range(min(x,xx),max(x,xx)):
                    cd += (void-1)
            for ir in insert_rows:
                if ir in range(min(y,yy),max(y,yy)):
                    cd += (void-1)
            dist[iglx][jglx] = cd
    print(dist)
    ans = 0
    for iglx, cds in dist.items():
        ans += sum(cds.values())
    for row in univ:
        print(''.join(row))
    print(ans/2)

def mark_galaxies(univ, insert_rows=None, insert_cols=None):
    count = 1
    galaxies = {}
    for y, row in enumerate(univ):
        for x, char in enumerate(row):
            if insert_rows and y in insert_rows:
                univ[y][x] = "-"
            if insert_cols and x in insert_cols:
                univ[y][x] = "|"
            if char == "#":
                univ[y][x] = str(count)
                galaxies[count] = (x,y)
                count += 1
    return univ, galaxies


def expand_space(l0):
    univ = []
    for y in l0:
        if all([x=="." for x in y]):
            univ.append(["."]*len(y))
        univ.append(y)
    inserts = []
    for x, char in enumerate(univ[0]):
        col = [y[x] for y in univ]
        if all([x=="." for x in col]):
            inserts.append(x)

    for ins in sorted(inserts, reverse=True):
        for row in univ:
            row.insert(ins, ".")
    return univ

def expand_space_pt2(l0):
    insert_rows = []
    insert_cols = []
    for y, row in enumerate(l0):
        if all([x=="." for x in row]):
            insert_rows.append(y)
    
    for x, _ in enumerate(l0[0]):
        col = [y[x] for y in l0]
        if all([x=="." for x in col]):
            insert_cols.append(x)

    return insert_rows, insert_cols

main()