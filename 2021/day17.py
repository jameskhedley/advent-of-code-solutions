from pdb import set_trace as qq


#_target = "x=20..30, y=-10..-5"
#target = {"minx":20, "maxx":30, "miny":-10, "maxy":-5}
_target = "target area: x=241..273, y=-97..-63"
target = {"minx":241, "maxx":273, "miny":-97, "maxy":-63}

def fire_away(v, target):
    o = (0,0)
    pos = [o]
    p = list(o)
    v0 = tuple(v)

    for step in range(250):
        p[0] = p[0] + v[0]
        p[1] = p[1] + v[1]
        if v[0] > 0: v[0] -= 1
        v[1] -= 1
        pos.append(tuple(p))
        if p[0] >= target["minx"] and p[0] <= target["maxx"] and p[1] >= target["miny"] and p[1] <= target["maxy"]:
            print("Direct hit! Firing pos (%d,%d)" %(v0[0],v0[1]))
            return True, pos
        #if v[0] == 46 and v[1] == 49:
        #    print(p)
        #    qq()
        if p[0] > target["maxx"] and p[1] > target["maxy"]:
            #print("Missed!")
            return False, pos
    #print("Missed!")
    return False, pos

def main():
    collect = set()
    for x in range(400):
        for y in range(-400, 400):
            v= [x,y]
            #print(v)
            v0 = tuple(v)
#            if v ==[19,-9]:
#                qq()
            hit, pos =  fire_away(v, target)
            if hit:
                collect.add(v0)
                #print("Direct hit! Firing pos (%d,%d)" %(v0[0],v0[1]))
    print(collect)
    print(len(collect))

def test():
    #v =[22,96]
    #v = [8,0]
    #v = [30,-6]
    v = [19,-9]
    hit, pos =  fire_away(v, target)
    print(pos)
    

main()
#test()
