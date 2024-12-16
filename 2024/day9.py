import time
import itertools as itt
debug = 0
if debug:
    data = ''.join(open("./day9_ex.txt").readlines())
else:
    data = ''.join(open("./day9_data.txt").readlines())

print("data length: %d" % len(data))

def pt1(data):
    image = map_to_image(data)
    final = compress_blocks(image)
    res = checksum(final)
    return res

def pt2(data):
    image = map_to_image(data)
    final = compress_file(image)
    res = checksum(final)
    return res

def map_to_image(disk_map):
    print("building image...")
    image = []
    iid = 0
    ldm = list(disk_map)
    for idx, char in enumerate(ldm):
        if idx % 2 == 0:
            # data
            tmp = [str(iid)]*int(char)
            iid+=1
        else:
            # free space
            tmp = ['.']*int(char)
        image+=tmp
    return image

def contig(image, start):
    timer = 0
    if timer:
        t0 = time.time()
    first_dot, next_num = None, None
    image = image[start:]
    for idx, char in enumerate(image):
        if char == '.':
            if first_dot is None:
                first_dot = idx
        else:
            next_num = idx
        if first_dot is not None and first_dot < next_num:
            if timer:
                t1 = time.time()
                print("done in %f" % (t1-t0))
            return False, first_dot
    return True, 0

def compress_blocks(image):
    print("compressing blocks, image size %d..." % len(image))
    loops = 0
    last_break = 0 
    while True:
        is_contiguous, last_break = contig(image, last_break)
        if is_contiguous:
            break
        loops += 1
        if loops % 100 == 0:
            print(last_break)
        reversed = image[last_break:][::-1]
        for rev_last_idx, char in enumerate(reversed):
            if char != '.':
                break
        last_idx = len(image) - rev_last_idx - 1
        last = image[last_idx]
        first_free = image.index('.')
        image[first_free] = last
        image[last_idx] = '.'

    return image

def compress_file(image):
    print("compressing files, image size %d..." % len(image))
    file_id = max([int(x) for x in image if x != '.' ])
    while file_id >= 0:
        print(file_id)
        groups = [list(j) for i, j in itt.groupby(image)]
        files = [(idx,grp) for idx, grp in enumerate(groups) if not all(x == '.' for x in grp)]
        for file in files:
            if file_id in [int(x) for x in file[1]]:
                free_chunks = [(idx,grp) for idx, grp in enumerate(groups) if all(x == '.' for x in grp)]
                found_group = groups[file[0]]
                for (grp_idx, fc) in free_chunks:
                    if len(fc) >= len(found_group):
                        if grp_idx > file[0]:
                            break
                        old_len = len(found_group)
                        if len(fc) > len(found_group):
                            found_group+=['.']*(len(fc)-len(found_group))
                        groups[grp_idx] = found_group
                        groups[file[0]] = ['.']*old_len
                        image = list(itt.chain.from_iterable(groups))
                        break
        file_id -= 1
        
        if debug:
            time.sleep(0.5)
            print(''.join(image))
    return image

def checksum(image):
    sum = 0
    for idx, num in enumerate(image):
        if num != '.':
            sum += idx*int(num)
    return sum
    
def tests():
    if 1:
        image = map_to_image("12345")
        assert image == list("0..111....22222")
        image = map_to_image("2333133121414131402")
        assert image == list("00...111...2...333.44.5555.6666.777.888899")
        image = "0..111....22222"
        assert contig(image,0)[0] == False
        image = "02211122..2...."
        assert contig(image,0)[0] == False
        image = "022111222......"
        assert contig(image,0)[0] == True
    
    #pt1
    exp = list("022111222......")
    input = list("0..111....22222")
    actual = compress_blocks(input)
    assert exp==actual
    exp = list("0099811188827773336446555566..............")
    actual = compress_blocks(map_to_image("2333133121414131402"))
    assert exp==actual
    assert(checksum(list("0099811188827773336446555566.............."))==1928)
    #pt2
    exp = list("00992111777.44.333....5555.6666.....8888..")
    input = map_to_image("2333133121414131402")
    actual = compress_file(input)
    assert exp==actual

    print("*** tests passed ***")

tests()
#print("part 1: %d" % pt1(data))
print("part 2: %d" % pt2(data))