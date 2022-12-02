from collections import defaultdict
from itertools import chain
#h0 = open("day11-ex.txt")
h0 = open("day11.txt")

lines = h0.readlines()

arr = [[int(x) for x in list(line.strip())] for line in lines]

def print_arr(arr):
    for r in arr:
        print(r)
    print("*******************************")

def pt1(arr):
    LOOPS = 500
    total_flash_count = 0
    print_arr(arr)
    for x in range(LOOPS):
        print("Loop: %d" % x)
        total_flash_count += loop(arr, x)
    print("Total: %d" % total_flash_count)
    
def loop(arr, iloop):
    flash_count = 0
    
    for y, line in enumerate(arr):
        for x, cell in enumerate(line):
            point = arr[y][x]
            arr[y][x] = point + 1
            
    #print("Initial increments")
    #print_arr(arr)        

    check_chain = list(chain(*arr))
    while 10 in check_chain:
        check_chain = list(chain(*arr))
        for y, line in enumerate(arr):
            for x, cell in enumerate(line):
                point = arr[y][x]
                if point == 10:
                    arr = flash_neighbours(x,y,arr)
                    arr[y][x] = 99 #literally ablaze
                    flash_count += 1

    #print("Nbor increments")
    #print_arr(arr)
    
    check_chain = list(chain(*arr))
    check_set = set(check_chain)
    if (len(check_set) == 1 and 99 in check_set):
        #import pdb; pdb.set_trace()
        print("All flashes at loop %d" % (iloop+1))
        import sys; sys.exit(0)
    
    #reset flashers
    for y, line in enumerate(arr):
        for x, cell in enumerate(line):
            point = arr[y][x]
            if point == 99:
                arr[y][x] = 0
                pass

    print("Loop end")
    print_arr(arr)
    return flash_count

def flash_neighbours(x,y,arr):
    #print("flash at %d,%d" % (x,y))
    neighbours = defaultdict(tuple)
    if x>0:
        neighbours['left']=(x-1,y)
    if x<len(arr[0])-1:
        neighbours['right']=(x+1,y)
    if y>0:
        neighbours['up']=(x,y-1)
    if y<len(arr)-1:
        neighbours['down']=(x,y+1)
    if x>0 and y>0:
        neighbours['upleft']=(x-1,y-1)
    if (x<len(arr[0])-1) and (y>0):
        neighbours['upright']=(x+1,y-1)
    if (x<len(arr[0])-1) and (y<len(arr)-1):
        neighbours['downright']=(x+1,y+1)
    if (y<len(arr)-1) and (x>0):
        neighbours['downleft']=(x-1,y+1)
        
    for k, v in neighbours.items():
        nbor_val = arr[v[1]][v[0]]
        if nbor_val < 10:
            arr[v[1]][v[0]] = nbor_val+1
            #print("bumped nbor at %d,%d" % (v[0],v[1]))
        
    return arr


pt1(arr)








