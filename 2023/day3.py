from itertools import chain
import string
from collections import defaultdict
from functools import reduce

h0 = open("day3_data.txt")
#h0 = open("day3_ex.txt")

l0 = [n.strip().lower() if n.strip() else None for n in h0.readlines()]

def pt2():
    symbol_pos = get_symbols(l0, ['*'])
    all_nums = {}

    for star in symbol_pos:
        nums = {}
        search_pos = get_search_pos(l0, [star])
        print(search_pos)
        if len(search_pos) < 2: 
            continue
        for spp in search_pos:
            num = ""
            scol = spp[1]
            while scol >= 0 and l0[spp[0]][scol] in string.digits:
                scol -= 1
            start = scol+1
            scol = spp[1]
            while scol < len(l0[0]) and l0[spp[0]][scol] in string.digits:
                scol += 1
            end = scol
            num = l0[spp[0]][start:end]
            nums[spp[0],start] = int(num)

        if len(nums) == 2:
            all_nums[star] = nums
    print(all_nums)
    ratios = []
    for gear, nums in all_nums.items():
        product = reduce(lambda x, y: x*y, nums.values())
        ratios.append(product)

    print(sum(ratios))


def get_symbol_key(l0):
    all_symbols = [[x for x in row if x not in string.digits + "."] for row in l0]
    symbol_key = set(chain(*filter(bool, all_symbols)))
    return symbol_key

def get_symbols(l0, symbol_key):
    symbol_pos = set()
    for irow, row in enumerate(l0):
        for icol, cell in enumerate(row):
            if cell in symbol_key:
                symbol_pos.add((irow, icol))
    return symbol_pos

def get_search_pos(l0, symbol_pos):
    search_pos = set()
    for sp in symbol_pos:
        adjacent_8 = adjacent_to_number(sp)
        for cell in adjacent_8:
            if l0[cell[0]][cell[1]] in string.digits:
                search_pos.add((cell[0],cell[1]))
    return search_pos

def pt1():
    
    symbol_key = get_symbol_key(l0)
    symbol_pos = get_symbols(l0, symbol_key)
    search_pos = get_search_pos(l0, symbol_pos)

    nums = {}
    for spp in search_pos:
        num = ""
        scol = spp[1]
        while scol >= 0 and l0[spp[0]][scol] in string.digits:
            scol -= 1
        start = scol+1
        scol = spp[1]
        while scol < len(l0[0]) and l0[spp[0]][scol] in string.digits:
            scol += 1
        end = scol
        num = l0[spp[0]][start:end]
        nums[spp[0],start] = int(num)

    print(nums)
    print(sum(nums.values()))

def adjacent_to_number(pos):
    top_left = (-1,-1)
    top_middle = (-1, 0)
    top_right = (-1, 1)
    left = (0, -1)
    right = (0, 1)
    bottom_left = (1, -1)
    bottom_middle = (1, 0)
    bottom_right = (1,1)
    eight = ((pos[0] + top_left[0], pos[1] + top_left[1]),
             (pos[0] + top_middle[0], pos[1] + top_middle[1]),
             (pos[0] + top_right[0], pos[1] + top_right[1]),
             (pos[0] + left[0], pos[1] + left[1]),
             (pos[0] + right[0], pos[1] + right[1]),
             (pos[0] + bottom_left[0], pos[1] + bottom_left[1]),
             (pos[0] + bottom_middle[0], pos[1] + bottom_middle[1]),
             (pos[0] + bottom_right[0], pos[1] + bottom_right[1]))

    return eight

def pg(data):
    for row in data:
        print(row)

pg(l0)
pt1()
pt2()
