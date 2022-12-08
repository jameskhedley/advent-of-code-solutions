l0 = [el.strip().split(" ") for el in open("day2.txt").readlines()]

def move_points(p0, p1):
    rules ={ ("X","C"): "Y", ("Y","A"): "X", ("Z","B"): "Z", ("X","A"): "Z", ("Y","B"): "Y", ("Z","C"): "X",("X","B"): "X", ("Y","C"): "Z", ("Z","A"): "Y" }
    points = {"X": 1, "Y": 2, "Z": 3}
    return points[rules[(p0,p1)]]

win_points = lambda p0: {"X":0, "Y":3, "Z":6}[p0]

print(sum([win_points(round[1]) + move_points(round[1],round[0]) for round in l0]))

    
