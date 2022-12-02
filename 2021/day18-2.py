from copy import deepcopy

def adder(x0,x1):
    return [x0,x1]

def split(sf0):
    if sf0:
        lval = sf0.pop(0)
        rval = sf0.pop()
        if type(rval) == type(list()) and type(lval) == type(list()):
            lval = split(lval)
            rval = split(rval)
            return [lval, rval]
        else:
            if type(rval) == type(int()) and  rval > 10:
                temp0 = int(rval/2)
                temp1 = rval - temp0
                rval = [temp0, temp1]
            if type(lval) == type(int()) and  lval > 10:
                temp0 = int(lval/2)
                temp1 = lval - temp0
                lval = [temp0, temp1]
            return [lval, rval]
    #return sf0

def exploder7(sf0):
    done = False
    depth = 0
    rns = []
    lns = []
    rstack = []
    lstack = []
    print("depth %d: %s" % (depth, sf0))
    while not done:
        if sf0:
            lval = sf0.pop(0)
            rval = sf0.pop()
            if type(rval) == type(list()) and type(lval) == type(list()):
                #only go left but keep the other fragments
                rstack.append(rval)
                lstack.append(deepcopy(lval))
                if type(lval) == type(int()):
                    rns.append(lval)
                else:
                    sf0 = lval
            else:    
                if type(rval) == type(int()):
                    lns.append(rval)
                else:
                    sf0 = rval
                if type(lval) == type(int()):
                    rns.append(lval)
                else:
                    sf0 = lval
        depth += 1
        print("depth %d: %s,%s" % (depth, str(lval), str(rval)))
        if type(lval) == type(int()) and type(rval) == type(int()) and depth<=4:
            print("No bang")
            if rstack:
                sf0 = rstack.pop()
                rns = []
                lns = []
                continue
            else:
                break
        if type(lval) == type(int()) and type(rval) == type(int()) and depth>4:
            print("Bang")
            if rstack: # ???
                #lstack = []
                lstack.pop(0) #?!?!?!
                print("hello")
                
            #lose the end val from both ns
            rns.pop() 
            lns.pop()

            nv = 0
            if lns:
                lns[-1] += rval
                while lns:
                    nv = [nv, lns.pop()]
            elif rstack:
                rnv = rstack.pop()
                rnv[0] += rval
                nv = [nv, rnv]
            if rns:
                rns[-1] += lval
                if nv == 0: nv = [rns.pop(),0]
                while rns:
                    nv[0] = [rns.pop(),nv[0]]
            

            done = True
            if lstack:
                while lstack:
                    nv = [lstack.pop(), nv]
            if rstack:
                while rstack:
                    nv = [nv, rstack.pop()]
            return nv
    return(sf0)

def tests0():
    if 0:
        ans = exploder7([1,2])
        assert ans == [1,2]
    if 1:
        ans = exploder7([[[[[9,8],1],2],3],4])
        print(ans)
        assert ans == [[[[0,9],2],3],4]

        ans = exploder7([7,[6,[5,[4,[3,2]]]]])
        print(ans)
        assert ans == [7,[6,[5,[7,0]]]]

        ans = exploder7([[6,[5,[4,[3,2]]]],1])
        assert ans == [[6,[5,[7,0]]],3]
    #if 1:
        ans = exploder7([[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]])
        #print(ans)
        assert ans == [[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]
        #print("**********************")
    #if 1:
        #print(exploder7(exploder7([[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]])))
        ans = exploder7([[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]])
        assert ans == [[[3, [2, [8, 0]]]], [9, [5, [7, 0]]]]
    #if 1:
        ans = split([[[[0,7],4],[15,[0,13]]],[1,1]])
        assert ans == [[[[0, 7], 4], [[7, 8], [0, 13]]], [1, 1]]
    #if 1:
        ans = exploder7([[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]])
        print(ans)
        assert ans == [[[[0,7],4],[7,[[8,4],9]]],[1,1]]
    if 1:
        ans = exploder7([[[[0, 7], 4], [7, [[8, 4], 9]]], [1, 1]])
        print(ans)
        assert ans == [[[[0,7],4],[15,[0,13]]],[1,1]]
    print("Tests all OK")

def main():
    ans = adder([[[[4,3],4],4],[7,[[8,4],9]]], [1,1])
    #temp0 = None
    temp0 = exploder7(deepcopy(ans))
    #while temp0 != ans:
    if temp0 != ans:
        temp1 = exploder7(deepcopy(temp0))
    print(ans)
        
def tests1():

    ans = exploder7([7,[6,[5,[4,[3,2]]]]])
    print(ans)
    assert ans == [7,[6,[5,[7,0]]]]

    # ans = exploder7([[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]])
    # print(ans)
    # assert ans == [[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]

    # ans = exploder7([[[[0, 7], 4], [7, [[8, 4], 9]]], [1, 1]])
    # print(ans)
    # assert ans == [[[[0,7],4],[15,[0,13]]],[1,1]]

tests1()
#main()