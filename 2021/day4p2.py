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
    winning_boards = []
    last_board = None
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
                        winning_boards.append(b)
                        set_boards = set(list(range(len(boards))))
                        set_wb = set(winning_boards)
                        diff = list(set_wb.symmetric_difference(set_boards))
                        if len(diff) == 1:
                            last_board = diff[0]
                        elif len(diff) == 0:
                            return last_board, call
                    
loser, last_call = loop()

print("All scores...")
for s0 in scores:
    print(s0)

print("Losing board...")
print(boards[loser])
print("Losing score...")
print(scores[loser])

lb = boards[loser]

score_sum = 0
for r, row in enumerate(lb):
    for n, num in enumerate(row):
        if scores[loser][r][n] == 0:
            score_sum += lb[r][n]

print(score_sum)
print(score_sum*last_call)
            


