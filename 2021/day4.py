import copy
#h0 = open("day4-ex.txt")
#h0 = open("day4-ex2.txt")
h0 = open("day4.txt")
lines = h0.readlines()

DIM = 5

boards = []

calls = [int(n) for n in lines.pop(0).split(',')]

lines = [l.strip() for l in lines if l.strip()]

temp_board = []
for count, line in enumerate(lines):
    
    group = [int(num) for num in line.split()]
    temp_board.append(group)
    if count % 5 == 4:
        boards.append(list(temp_board))
        temp_board = []

for bd in boards:
    print(bd)

#pre-pop scoreboards
scores = copy.deepcopy(boards)
for b, board in enumerate(boards):
    for r, row in enumerate(board):
        for n, num in enumerate(row):
            scores[b][r][n] = 0
print("*****")
print(scores)            

print("*****")
print("calls: %s" % str(calls))

DEBUG= False
#DEBUG= True

def check_board(sbd):
    check_col = 0
    for row in sbd:
        if sum(row) == 5:
            print("Winning row!")
            return True
    for col in range(len(sbd[0])):
        check_col = [row[col] for row in sbd]
        if sum(check_col) == 5:
            print("Winning column! Col no %d" % col)
            return True
    return False



def loop():
    for call in calls:
        print("CALL: %d" % call)
        for b, board in enumerate(boards):
            for r, row in enumerate(board):
                for n, num in enumerate(row):
                    if num == call:
                        scores[b][r][n] = 1
                        print("Marked board %d, col %d, row %r" % (b,n,r))
                    
                    if check_board(scores[b]):
                        print("Winning board was number %d!" % b)
                        return b, call

                    if num == call and DEBUG:
                        print("DEBUG START")
                        print(call)
                        print("%d, %d, %d" % (b,r,n))
                        print(scores[b])
                        print(sum(scores[b][r]))
                        print("DEBUG END")
                    
winner, win_call = loop()

print("Winning board...")
print(boards[winner])
print("Winning score...")
print(scores[winner])

wb = boards[winner]

score_sum = 0
for r, row in enumerate(wb):
    for n, num in enumerate(row):
        if scores[winner][r][n] == 0:
            score_sum += wb[r][n]

print(score_sum)
print(score_sum*win_call)
            


