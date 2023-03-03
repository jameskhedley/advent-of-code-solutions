import regex
from pprint import pprint

def setup_cave(lines):
    pattern = "Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)"
    sensors = {}
    for line in lines:
        sx,sy, bx, by = [int(x) for x in regex.match(pattern, line).groups()]
        sensors[(sx,sy)] = (bx,by)
        
    return sensors

def point_inside_triangle(point, triangle):
    x1,y1 = triangle[0]
    x2,y2 = triangle[1]
    x3,y3 = triangle[2]
    xp,yp = point
    c1 = (x2-x1)*(yp-y1)-(y2-y1)*(xp-x1)
    c2 = (x3-x2)*(yp-y2)-(y3-y2)*(xp-x2)
    c3 = (x1-x3)*(yp-y3)-(y1-y3)*(xp-x3)
    #import pdb; pdb.set_trace()
    if (c1<=0 and c2<=0 and c3<=0) or (c1>=0 and c2>=0 and c3>=0):
        return True
    else:
        return False    
    
def point_inside_area(point, area):
    #area = (left corner, right corner, bottom corner, top corner)
    x,y = point
    #import pdb; pdb.set_trace()
    if x < area[0][0] or x > area[1][0]:
        return False
    if y < area[2][1] or y > area[3][1]:
        return False
    top_triangle = (area[0], area[1], area[3])
    bottom_triangle = (area[0], area[1], area[2])
    if point_inside_triangle(point, top_triangle):
        return True
    if point_inside_triangle(point, bottom_triangle):
        return True
    return False
    
def distance_to_beacon(beacon, sensor):
    bx,by = beacon
    sx,sy = sensor
    distance = abs(bx-sx) + abs(by-sy)
    return distance
    
def pt1(lines, validate_y, xmin, xmax, debug=True):
    sensors = setup_cave(lines)

    #sensors = {(8, 7): (2, 10)}
    areas = {}
    beacons = set()
    for sensor, beacon in sensors.items():
        beacons.add(beacon)
        sx,sy = sensor
        found = None
        distance = distance_to_beacon(beacon, sensor)
        new_area = ((sx-distance,sensor[1]), (sx+distance,sensor[1]), (sensor[0],sy-distance), (sensor[0],sy+distance))
        areas[sensor] = new_area
            
    count = 0
    debug_string = ""
    debug_row ={}
    
    for xcheck in range(xmin, xmax):
        for area in areas.values():
            #print("Checking area %s" % (str(area)))
            point = (xcheck, validate_y)
            if point_inside_area(point, area):
                #print("Point (%d,%d) is inside area %s" % (xcheck, validate_y, str(area)))
                if point in beacons:
                    #print("But it's a beacon, doesn't count")
                    if debug:
                        debug_row[xcheck]='B'
                elif point in sensors.keys():
                    #print("But it's a sensor, doesn't count")
                    if debug:
                        debug_row[xcheck]='S'
                    #count += 1
                else:
                    if debug:
                        debug_row[xcheck]='#'
                    count += 1
                break
            else:
                pass
                #print("Point (%d,%d) is outside area %s" % (xcheck, validate_y, str(area)))
        
        if debug and xcheck not in debug_row.keys():
            debug_row[xcheck]='.'
    if not debug:
        print("Pt1 answer at y val %d: %d" % (validate_y, count))
    #import pdb; pdb.set_trace()
    if not debug: return
    for k in sorted(debug_row.keys()):
        debug_string += debug_row[k]
    #print("%s  - %d" % (debug_string, count))
    print(count)

dbg_lines = [el.replace('\n','') for el in open("day15_debug.txt").readlines()]
ex_lines = [el.replace('\n','') for el in open("day15_ex.txt").readlines()]
lines = [el.replace('\n','') for el in open("day15.txt").readlines()]

#for yval in range(-2,22):
#    pt1(ex_lines, yval, -2,27)

for yval in range(0,50):
    pt1(dbg_lines, yval, -10,50)


#pt1(ex_lines, 9, -4,27)
#pt1(ex_lines, 10, -4,27)
#pt1(ex_lines, 11, -4,27)

#pt1(lines, 2000000, -4000000, 4000000, False)



