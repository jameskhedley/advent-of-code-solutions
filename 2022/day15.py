import regex
from pprint import pprint

def parse(lines):
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

def get_areas(lines, add_on=0):
    sensors = parse(lines)
    areas = {}
    beacons = set()
    for sensor, beacon in sensors.items():
        beacons.add(beacon)
        sx,sy = sensor
        distance = distance_to_beacon(beacon, sensor)+add_on
        #area = (left corner, right corner, bottom corner, top corner)
        new_area = ((sx-distance,sy), (sx+distance,sy), (sx,sy-distance), (sx,sy+distance))
        areas[sensor] = new_area
    return areas, beacons, sensors

def scan_exteriors(lines, imin, imax, debug=True):
    ### This works by the principle that as there can be only one possible location, it must be
    ### on the outside of one edge of one of the regions. So this looks at every perimeter point
    ### of every region and checks whether it is inside any other regions. Since the perimeters
    ### are far lesser in magnitude than the areas inside, this speeds things up a lot
    
    # blow up each region by one to 
    expanded_regions, _, _ = get_areas(lines,add_on=1)
    # same again but with original dimensions
    data, _, _ = get_areas(lines,add_on=0)

    perimeter = set()
    if debug:
        print(data)
    areas = list(expanded_regions.values())
    
    candidates = set()
    
    loops = 0
    
    while areas:
        loops+=1
        print(loops)
        area = areas.pop()	
        if debug:
            print(area)
        left, right, bottom, top = area

        #calculate the edges of the current (expanded by one) region
        top_right = list(zip(range(top[0],right[0]+1), reversed(range(right[1],top[1]+1))))
        top_left = list(zip(range(left[0],top[0]+1), range(left[1],top[1]+1)))
        bottom_left = list(zip(range(left[0],top[0]+1), reversed(range(bottom[1],left[1]+1))))
        bottom_right = list(zip(range(bottom[0],right[0]+1), range(bottom[1],right[1]+1)))

        #perimeter will have every point around the outside of this region        
        perimeter = set(top_right+top_left+bottom_left+bottom_right)
        if debug:
            print(perimeter)
        
        for point in perimeter:
            if point[0] < imin or point[0] > imax or point[1] < imin or point[1] > imax:
                continue
            inside_any = False
            for area_compare in data.values():
                if point_inside_area(point, area_compare):
                    inside_any = True
                    break
            if not inside_any:
                candidates.add(point)       
                
        if not inside_any:
            print("Found a point! At %s" % str(point))
            return
    if not candidates or len(candidates)>1:
        print("It's gone wrong :(") # should never happen
    if debug:
        print(candidates)
    return candidates.pop()
    
def scan_line(lines, validate_y, xmin, xmax, debug=True):
    ### This just looks across a given line and counts impossible positions
    areas, beacons, sensors = get_areas(lines)
            
    count, beacon_count = 0,0
    debug_string = ""
    debug_row ={}
    
    for xcheck in range(xmin, xmax):
        point = (xcheck, validate_y)
        for area in areas.values():
            if point_inside_area(point, area):
                if point in beacons:
                    beacon_count += 1
                    if debug:
                        debug_row[xcheck]='B'
                elif point in sensors.keys(): #yes we should count sensors
                    if debug:
                        debug_row[xcheck]='S'
                    count += 1
                else:
                    if debug:
                        debug_row[xcheck]='#'
                    count += 1
                break
            else:
                pass
        
        if debug and xcheck not in debug_row.keys():
            debug_row[xcheck]='.'

    if not debug: return count, beacon_count
    for k in sorted(debug_row.keys()):
        debug_string += debug_row[k]
    print("%s  - %d: %d" % (debug_string, validate_y, count))
    return count, beacon_count
    
ex_lines = [el.replace('\n','') for el in open("day15_ex.txt").readlines()]
lines = [el.replace('\n','') for el in open("day15.txt").readlines()]

if 0:
    #print the example grid
    for yval in range(-12,28):
        scan_line(ex_lines, yval, 0,50)

count, _ = scan_line(lines, 2_000_000, -400_000, 5_000_000, False)
print("Part one answer: %s" % count) #20 seconds, not great

#scan_exteriors(ex_lines, 0, 20, debug=True)
count = scan_exteriors(lines, 0, 4_000_000, debug=False)
print("Part tw0 answer: %s" % count) #about 7 minutes, really not so great


