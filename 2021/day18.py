from pdb import set_trace as qq
from copy import deepcopy
sf0 = [[1,2]] + [[[3,4],5]]
#print(sf0)

def exploder(pf1):
    
    sploded = False
    direction = "right"
    #qq() 
    while not sploded:
        lstack = deepcopy(pf1)
        depth = 0
        rstack = []
        while lstack:
            if direction == "right":
                #qq() 
                lval = lstack.pop(0) #pop left
                if lstack:
                    rval = lstack.pop()  #pop right
                else:
                    lstack.append(lval)
                    break
            elif direction == "left":
                #qq()
                lval = lstack.pop()
                if lstack:
                    rval = lstack.pop(0)
                else:
                    lstack.append(lval)
                    break
            else:
                raise ValueError("bad direction")
            print("loop 1, depth %d: %s,%s" % (depth, str(lval), str(rval)))
            if type(lval) == type(int()) and type(rval) == type(int()) and depth<=3:
                break
            if type(lval) == type(int()) and type(rval) == type(int()) and depth>3:
                print("Bang") #will leave loop as lstack is empty
                if direction == "right":
                    lval = [0, rval + rstack.pop()]
                elif direction == "left":
                    lval = [rval + rstack.pop(), 0]
                else:
                    raise ValueError("bad direction")
                sploded = True
            else:
                if type(lval) == type(int()): lval = [lval]
                if type(rval) == type(int()): rval = [rval]
                depth += 1
                lstack += lval
                rstack += rval
        if direction == "right" and not sploded:
            direction = "left"
        else:
            break
    
    if sploded:
        lstack.insert(0, lval)
        while rstack:
            if direction == "right":
                lstack[0] = [lstack[0], rstack.pop()]
            elif direction == "left":
                lstack[0] = [rstack.pop(), lstack[0]]
            else:
                raise ValueError("bad direction")
    else:
        lstack = deepcopy(pf1)
    
    return lstack
    
if 0:
    print(exploder([1,2]))
    print(exploder([[1,2],3]))

if 0:
    sf1 = [[[[[9,8],1],2],3],4]
    um = exploder(sf1)
    print(um)
    print("****************************")


if 0:
    sf2 = [7,[6,[5,[4,[3,2]]]]]
    um = exploder(sf2)
    print(um)
    print("****************************")

if 1:
    #sf3 = [[6,[5,[4,[3,2]]]],1]
    sf3 = [6,[5,[4,[3,2]]]]
    um = exploder(sf3)
    print(um)
    print("****************************")
    

