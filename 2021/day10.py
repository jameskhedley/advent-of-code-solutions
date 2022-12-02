#h0 = open("day10-ex.txt")
h0 = open("day10.txt")
lines = [list(l.strip()) for l in h0.readlines()]
#print(lines[0])

chars = [("(",")"),("{","}"),("<",">"),("[","]")]
openings = [pair[0] for pair in chars]
closings = [pair[1] for pair in chars]
matches = {pair[0]:pair[1] for pair in chars}


def pt1():
    points = {")": 3, "]": 57, "}": 1197, ">": 25137}
    stack = []

    corrupts = []
    bad = False
    bad_chars = []

    for one_line in lines:
        for c in one_line:
            if c in openings:
                stack.append(c)
            elif c in closings:
                closer = c
                opener = stack.pop()
                if matches[opener] == closer:
                    #print("found a pair: %s,%s" %(opener, closer))
                    pass
                else:
                    #print("doesn't match: %s,%s" %(opener, closer))
                    corrupts.append(one_line)
                    bad_chars.append(closer)
                    bad = True
                    break
                #print(stack)
                #print("*******************")
        if bad:
            bad = False
            continue

    for corr in corrupts:
        print(corr)
    
    print(bad_chars)
    scores = [points[x] for x in bad_chars]
    print(scores)
    print(sum(scores))

def pt2():
    incompletes = []
    
    completed = []
    bad = False
    points = {")": 1, "]": 2, "}": 3, ">": 4}
    scores = []

    for one_line in lines:
        stack = []
        score = 0
        for c in one_line:
            if c in openings:
                stack.append(c)
            elif c in closings:
                closer = c
                opener = stack.pop()
                if matches[opener] == closer:
                    #print("found a pair: %s,%s" %(opener, closer))
                    pass                    
                else:
                    bad = True
                    break
                #print(stack)
                #print("*******************")
        if bad:
            bad = False
            continue
        else:
            #import pdb; pdb.set_trace()
            incompletes.append(one_line)
            #print(one_line)
            #print(stack)
            #complete = list(one_line)
            complete = []
            while stack:
                score = score * 5
                popped = stack.pop()
                new_char = matches[popped]
                score += points[new_char]
                complete.append(new_char)
        completed.append(complete)
        scores.append(score)        
        #print("*******************")
    #for l in incompletes:
    #    print(l)
    #for l in completed:
    #for i,l in enumerate(scores):
        #print(completed[i])
    #    print(l)
        
    scores.sort()
    middle = int((len(scores) - 1)/2)
    final = scores[middle]
    print(final)


#pt1()
pt2()
