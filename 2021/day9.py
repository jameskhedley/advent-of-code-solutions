#h0 = open("day9-ex.txt")
h0 = open("day9.txt")

lines = h0.readlines()

arr = [[int(x) for x in list(line.strip())] for line in lines]

DIM = max(len(arr),len(arr[0]))

def lowpoints(arr):
    lows = []

    for y, line in enumerate(arr):
        for x, cell in enumerate(line):
            #print(arr[y][x])
            point = arr[y][x]
            
            left = DIM
            if x>0:
                left = arr[y][x-1]
            right = DIM
            if x<len(line)-1:
                right = arr[y][x+1]
                
            up = DIM
            if y>0:
                up = arr[y-1][x]
            down = DIM
            if y<len(arr)-1:
                down = arr[y+1][x]
                
            if point < min([left, right, up, down]):
                lows.append((y,x))
    return lows
                
def recurse_neighbours(arr, lowpoint, basin):
    print("Considering point %s" % str(lowpoint))
    basin.add(lowpoint)
    neighbours = {'left':None, 'right':None, 'up':None, 'down':None}
    
    y,x = lowpoint
    
    if x>0:
        if arr[y][x-1] < 9:
            neighbours['left']=(y,x-1)
    if x<DIM-1:
        print(arr[y][x+1])
        if arr[y][x+1] < 9:
            neighbours['right']=(y,x+1)
    if y>0:
        if arr[y-1][x] < 9:
            neighbours['up']=(y-1,x)
    if y<len(arr)-1:
        if arr[y+1][x] < 9:
            neighbours['down']=(y+1,x)
    print("neighbours: %s " % str(neighbours))
    
    for nbor in neighbours.values():
        if nbor and not nbor in basin:
            basin = basin.union(recurse_neighbours(arr, nbor, basin))
    return basin
    
basins = []
lows = lowpoints(arr)
for low in lows:
    print("finding basin starting at: %s" % str(low))
    basins.append(recurse_neighbours(arr, low, set()))

lengths = []    
for basin in basins:
    print(basin)
    lengths.append(len(basin))
lengths.sort(reverse=True)
lengths = lengths[:3]
print(lengths)
total = 1
for l in lengths:
    total = total * l
print(total)
            
#print(lows)
#print(sum([1+x for x in lows]))

