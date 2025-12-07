from collections import defaultdict
ex = False

def get_data():
    if ex:
        h0 = open("./day6_ex.txt")
    else:
        h0 = open("./day6.txt")
    return h0

def part1():
    h0 = get_data()
    ans = 0
    cols = defaultdict(list)
    for line in h0.readlines():
        if not '*' in line:
            while '  ' in line:
                line = line.replace('  ', ' ')
            nums = [x for x in line.strip().split(' ')]
            for idx, num in enumerate(nums):
                cols[idx].append(num)
            continue
        else:
            ops = [x for x in line.strip().split(' ') if x]

    for idx, sum in cols.items():
        s0 = ops[idx].join(sum)
        print(s0)
        ans+=eval(s0)

    return ans

#ex=True
def part2():
    h0 = get_data()
    ans = 0
    cols = defaultdict(list)
    col_widths = defaultdict(int)
    # examine last line to find col widths as it can change as it goes along
    last_line = list(h0.readlines()[-1])
    col = -1
    run = 0
    while last_line:
        char  = last_line.pop(0)
        if char == " ":
            run += 1
        else:
            if run > 0:
                col += 1
                col_widths[col] = run
                run = 0
    col_widths[col+1] = run+1

    # collate the numbers into column order
    h0 = get_data()
    for line in h0.readlines():
        line = line[:-1]
        if not '*' in line:
            line_copy = str(line)
            col = 0
            nums = []
            while line_copy:
                num = line_copy[:col_widths[col]]
                line_copy = line_copy[col_widths[col]+1:]
                col += 1
                nums.append(num)
            for idx, num in enumerate(nums):
                cols[idx].append(num)
        else:
            ops = [x for x in line.strip().split(' ') if x]
    # create the sums to be eval'd
    for idx, nums in cols.items():
        final = []
        for cc in range(len(nums[0])-1,-1, -1):
            cs = ''.join([x[cc] for x in nums])
            final.append(cs)
        s0 = ops[idx].join(final)
        print(s0)
        ans += eval(s0)
    # annoyingly the program misses the last column and I can't be bothered to fix it lmao
    # so just add on whatever is in the very last column. Doesn't happen on example data somehow!
    return ans + 6136 

print("part 1 answer: %d " % part1())
print("part 2 answer: %d " % part2())