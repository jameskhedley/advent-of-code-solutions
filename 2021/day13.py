#h0 = open("day13-ex.txt")
h0 = open("day13.txt")
data = h0.readlines()

blank_line = data.index("\n")
#print(blank_line)

number_of_folds = len(data) - blank_line

strs = [x.strip().split(',') for x in data[:-number_of_folds]]
#print(strs)
arr = [[int(x[0]), int(x[1])] for x in strs]


folds = data[-(number_of_folds-1):]

all_folds = []

for f in folds:
    print(f)
    if "fold along y" in f:
        all_folds.append("Y:" + f.strip().split("fold along y=")[1])
    elif "fold along x" in f:
        all_folds.append("X:" + f.strip().split("fold along x=")[1])
    else:
        raise RuntimeError("Ya dun goofed")
        
print("ALL FOLDS: %s" % str(all_folds))

dim_x = max([p[0] for p in arr]) + 1
dim_y = max([p[1] for p in arr]) + 1

def pp(p, text):
    count_dots = 0
    print("************** %s **************" % text)
    for line in p:
        print(" ".join(line))
        count_dots += sum([1 for x in line if x=="#"])
    print("****************************")
    print("Total dot count: %d" % count_dots)


paper = []
for y in range(dim_y):
    line = list(["."])*dim_x
    paper.append(line)

for pair in arr:
    print(pair)
    paper[pair[1]][pair[0]] = "#"    
    #break

#for y, line in enumerate(arr):
#    for x, point in enumerate(line):
#        paper[y][x] = "#"

        
pp(paper, "Original")

#fold away
fx = None
fy = None

for f in all_folds:
#for f in all_folds[:1]:
    if "Y" in f:
        fy = int(f.split(":")[1])
        for y, line in enumerate(paper):
            if y<fy: continue
            for x, char in enumerate(paper[y]):
                if char == "#":
                    #print("found # at %d,%d" % (x,y))
                    diff_y = y - fy
                    new_y = fy - diff_y
                    paper[new_y][x] = "#"
                    #print("coloured in %d,%d" % (x,new_y))
        #drop the bottom lines
        paper = paper[0:fy] 
    elif "X" in f:
        fx = int(f.split(":")[1])
        #import pdb; pdb.set_trace()
        for y, line in enumerate(paper):
            for x, char in enumerate(line):
                if x<fx: continue
                if char == "#":
                    diff_x = x - fx
                    new_x = fx - diff_x
                    paper[y][new_x] = "#"
                    #print("coloured in %d,%d" % (new_x,y))
        #drop the rightmost cols
        temp_paper = []
        for y, line in enumerate(paper):
            temp_paper.append(line[:fx])
        paper = temp_paper
    pp(paper, "After fold %s" % str(f))

#if fy:
#    paper1 = paper[0:fy]
#    pp(paper1)
#else:
#    paper1 = paper
#if fx:
#    paper2 = []
#    for line in paper1:
#        paper2.append(line[:fx])
#
#    pp(paper2)

            
        



