from collections import Counter, defaultdict

def mutate(state):
    # naive method - correct but slow
    new_state = {}
    ns_pos_offset = 0
    for pos, stone in enumerate(state):
        #If the stone is engraved with the number 0, it is replaced by a stone engraved with the number 1.
        if stone == 0:
            new_state[pos+ns_pos_offset] = 1
        #If the stone is engraved with a number that has an even number of digits, it is replaced by two stones. 
        #The left half of the digits are engraved on the new left stone, and the right half of the digits are engraved on the new right stone. 
        # (The new numbers don't keep extra leading zeroes: 1000 would become stones 10 and 0.)
        elif len(str(stone)) %2 == 0:
            digits = str(stone)
            ld = int(digits[:len(digits)//2])
            rd = int(digits[len(digits)//2:])
            new_state[pos+ns_pos_offset] = ld
            new_state[pos+1+ns_pos_offset] = rd
            ns_pos_offset += 1
        #If none of the other rules apply, the stone is replaced by a new stone; the old stone's number multiplied by 2024 is engraved on the new stone.
        else:
            new_state[pos+ns_pos_offset] = stone * 2024
        state = list(new_state.values())
    print(state)
    print("")
    return ' '.join([str(x) for x in state]), len(state)

def pt1(sd, cycles):
    for i in range(cycles):
        state = [int(x) for x in sd.split()]
        sd, count = mutate(state)
        print(sd)
        print("blinked %d times" % (i+1))
    return count

def pt2(sd, cycles):
    state = [int(x) for x in sd.split()]
    ns = state
    for i in range(cycles):
        ns, count = fast_mutate(ns)
        #print(ns)
        print("blinked %d times" % (i+1))
    return count

def fast_mutate(state):
    counter = Counter(state)
    new_state = Counter(counter)
    #cache_size = 0 #100000
    #cache = [(None,None)]*cache_size

    for stone, count in counter.items():
        if count == 0:
            continue
        if stone == 0:
            new_state[0]-=count
            new_state[1]+=count
        elif len(str(stone)) %2 == 0:
            digits = str(stone)
            ld = int(digits[:len(digits)//2])
            rd = int(digits[len(digits)//2:])
            new_state[stone]-=count
            new_state[ld]+=count
            new_state[rd]+=count
        else:
            new_state[stone*2024]+=count
            new_state[stone]-=count
    nz = [(n, v) for n, v in new_state.items() if v>0]
    res = sum([v[1] for v in nz])
    return new_state, res

def test():
    sd = "125 17"
    state = [int(x) for x in sd.split()]
    assert mutate(state)[0] == "253000 1 7"
    
    sd = "253000 1 7"
    state = [int(x) for x in sd.split()]
    assert mutate(state)[0] == "253 0 2024 14168"

    sd = "253 0 2024 14168"
    state = [int(x) for x in sd.split()]
    assert mutate(state)[0] == "512072 1 20 24 28676032"

    sd = "0 1 10 99 999"
    state = [int(x) for x in sd.split()]
    assert mutate(state)[0] == "1 2024 1 0 9 9 2021976"

    sd = "253000 1 7"
    state = [int(x) for x in sd.split()]
    assert mutate(state)[0] == "253 0 2024 14168"

    print("tests passed")

test()
#print("part 1: %d" % pt1("125 17", 6)) # example 0 - 22
#print("part 1: %d" % pt1("125 17", 25)) # example 1 - 55312
#print("part 1: %d" % pt1("0 27 5409930 828979 4471 3 68524 170", 25)) # real data

#print("part 2: %d" % pt2("125 17", 25)) # example 1 - 55312
#print("part 2: %d" % pt2("125 17", 6)) # example 1 - 22
import cProfile
cProfile.run("print(\"part 2: %d\" % pt2(\"0 27 5409930 828979 4471 3 68524 170\", 75))") # 0.6 seconds - not bad!
#print("part 2: %d" % pt2("0 27 5409930 828979 4471 3 68524 170", 25)) # real data
#print("part 2: %d" % pt2("0 27 5409930 828979 4471 3 68524 170", 75)) # real data