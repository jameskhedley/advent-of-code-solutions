from collections import deque

data_ex = [3,4,3,1,2]

data = [4,3,3,5,4,1,2,1,3,1,1,1,1,1,2,4,1,3,3,1,1,1,1,2,3,1,1,1,4,1,1,2,1,2,2,1,1,1,1,1,5,1,1,2,1,1,1,1,1,1,1,1,1,3,1,1,1,1,1,1,1,1,5,1,4,2,1,1,2,1,3,1,1,2,2,1,1,1,1,1,1,1,1,1,1,4,1,3,2,2,3,1,1,1,4,1,1,1,1,5,1,1,1,5,1,1,3,1,1,2,4,1,1,3,2,4,1,1,1,1,1,5,5,1,1,1,1,1,1,4,1,1,1,3,2,1,1,5,1,1,1,1,1,1,1,5,4,1,5,1,3,4,1,1,1,1,2,1,2,1,1,1,2,2,1,2,3,5,1,1,1,1,3,5,1,1,1,2,1,1,4,1,1,5,1,4,1,2,1,3,1,5,1,4,3,1,3,2,1,1,1,2,2,1,1,1,1,4,5,1,1,1,1,1,3,1,3,4,1,1,4,1,1,3,1,3,1,1,4,5,4,3,2,5,1,1,1,1,1,1,2,1,5,2,5,3,1,1,1,1,1,3,1,1,1,1,5,1,2,1,2,1,1,1,1,2,1,1,1,1,1,1,1,3,3,1,1,5,1,3,5,5,1,1,1,2,1,2,1,5,1,1,1,1,2,1,1,1,2,1]


def main(fishes_in, days):
    #fishes = deque(fishes_in)
    fishes = list(fishes_in)
    for day in range(days):
        #fry = deque([])
        #fry = []
        fry = 0
        for idx, fish in enumerate(fishes):
            if fish == 0:
                fry += 1
                fishes[idx] = 6
            else:
                fishes[idx] = fish - 1
        fishes += [8]*fry
        print("Day %d, %d fishes" % (day, len(fishes)))
        #print(fishes)
    print(len(fishes))

def main_pop(fishes_in, days):
    fishes = deque(fishes_in)
    for day in range(days):
        new_fishes = deque([])
        fry = deque([])
        while fishes:
            fish = fishes.pop()
            if fish == 0:
                fry.append(8)
                new_fishes.append(6)
            else:
                new_fishes.append(fish-1)
        #fishes = new_fishes[::-1]
        fishes = new_fishes
        fishes += fry
        #print(fishes)
        #print(".\r")
        print("Day %d, %d fishes" % (day, len(fishes)))

    print(len(fishes))
    
import cProfile
DAYS = 120
#DAYS = 100
#DAYS = 18
#DAYS = 80
#DAYS = 256

cProfile.run('main(data, DAYS)')
#cProfile.run('main_pop(data, DAYS)')
#main(data, 80)
