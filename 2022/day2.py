# Opponent - A for Rock, B for Paper, and C for Scissors
# Response - X for Rock, Y for Paper, and Z for Scissors

h0 = open("day2.txt")
l0 = h0.readlines()[:-1]
l0 = [el.strip().split(" ") for el in l0]

def move_points(p0):
    rules = {"X": 1, "Y": 2, "Z": 3}
    return rules[p0]

def win_points(p0, p1):
    rules ={ ("X","C"): 6, ("Y","A"): 6, ("Z","B"): 6, 
             ("X","A"): 3, ("Y","B"): 3, ("Z","C"): 3,
             ("X","B"): 0, ("Y","C"): 0, ("Z","A"): 0
           }
    points = rules[(p0,p1)]
    return points

points = sum([win_points(round[1],round[0]) + move_points(round[1]) for round in l0])
print(points)

    
