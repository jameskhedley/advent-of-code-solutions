from itertools import chain

def main():
    #with open("day14_ex.txt") as h0:
    with open("day14_data.txt") as h0:
        l0 = [list(x.strip()) for x in h0.readlines()]
    #test()
    for row in l0:
        print(row)
    print("===========================")
    #pt1(l0)
    pt2(l0)

def pt2(l0):
    cache = {}


    for i in range(175): #finger in the air :)
        print("Pass %d, cache size %d" % (i, len(cache)))
        l0 = tilt(l0, "N")
        #pg(l0)
        l0 = tilt(l0, "W")
        #pg(l0)
        l0 = tilt(l0, "S")
        #pg(l0)
        l0 = tilt(l0, "E")
        #pg(l0)
        rec = tuple(chain(*l0))
        cache[rec] = i
    print(list(cache.values()))
    cycles = 1000000000
    ermm = cycles % (len(cache)+1) #????
    whut = [k for k, v in cache.items() if v == ermm][0]
    huhh = []
    while whut:
        row, whut = whut[:100], whut[100:]
        huhh.append(row)
    ok_i_guess = calc_ans(huhh)
    print(ok_i_guess) # I have no idea why this is the right answer lol

def pg(l0):
    for row in l0:
        print("".join(row))
    print("=========================")

def pt1(l0):
    l0 = tilt(l0, "N")
    ans = calc_ans(l0)
    print(ans)

def calc_ans(l0):
    ans = 0
    for y, row in enumerate(l0):
        for x, char in enumerate(row):
            if char=="O":
                ans+=len(l0)-y
    return ans

def tilt(l0, direction):
    if direction == "S":
        l0 = l0[::-1]
    elif direction == "E":
        for y, row in enumerate(l0):
            l0[y] = row[::-1]

    for y, row in enumerate(l0):
        if direction == "N":
            if y == 0:
                continue
        for x, char in enumerate(row):
            #if (x,y) == (6,1) and direction=="E":
            #    print("break")

            if char == "O":
                if direction in ("N","S"):
                    view = [row[x] for row in l0[:y]]
                elif direction in("E","W"):
                    view = row[:x]
                if all([True if (x == 'O' or x == '#') else False for x in view ]):
                    continue # no free spaces in that direction
                else:
                    if "#" in view or "O" in view:
                        cube_pos = len(view)- view[::-1].index("#") if "#" in view else 0
                        round_pos = len(view)- view[::-1].index("O") if "O" in view else 0
                        nxy = max(cube_pos, round_pos)
                        if direction in ("N","S"):
                            if nxy >= len(l0):
                                continue
                            l0[nxy][x] = "O"
                        elif direction in ("W","E"):
                            if nxy >= len(l0[y]):
                                continue
                            l0[y][nxy] = "O"
                    else:
                        nxy = view.index(".")
                        if direction in ("N", "S"):
                            l0[nxy][x] = "O"
                        elif direction in ("E","W"):
                            l0[y][nxy] = "O"
                    #erase old position
                    if direction in ("N","S"):
                        if nxy != y:
                            l0[y][x] = "."
                    elif direction in ("E","W"):
                        if nxy != x:
                            l0[y][x] = "."

    if direction == "S":
        l0 = l0[::-1]
    elif direction == "E":
        for y, row in enumerate(l0):
            l0[y] = row[::-1]

    return l0


main()