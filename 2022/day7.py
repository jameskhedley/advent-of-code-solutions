#l0 = [el.replace('\n','') for el in open("day7_ex.txt").readlines()]
l0 = [el.replace('\n','') for el in open("day7.txt").readlines()]

path = []
all_paths = {}

#parse the input to a dict
for line in l0:
    if line[0]=='$':
        cmd=line[2:]
        print("cmd: %s" % cmd)
        parts = cmd.split(' ')
        if parts[0] == 'cd':
            if parts[1] == '..':
                path.pop()
            else:
                path.append(parts[1])
                all_paths['/'.join(path)]=0
    else:
        size, name = line.split(' ')
        if size == 'dir':
            print("subdir: %s" % (name))
        else:
            temp = '/'.join(path)
            print("Found file size: %s, name: %s, in path: %s" % (size, name, temp))
            all_paths['/'.join(path)]+=int(size)

#add all subdir sizes into parent
for k,v in all_paths.items():
    path = k.split('/')
    if len(path) <= 2:
        pass #has to be root
    else:
        while path:
            path.pop()
            if len(path)<=1: break
            all_paths['/'.join(path)] += v
        
print(all_paths)
res = 0
for k,v in all_paths.items():
    if v<=100000:
        res+=v

print("Part 1 answer: %d" % res)

total_usage = all_paths['/']
print("total usage: %d" % total_usage)

VOL_SIZE = 70000000
FS_REQ = 30000000
unused_space = VOL_SIZE-total_usage
print("unused space: %d" % unused_space)

additional_space_req = FS_REQ - unused_space
print("additional space required: %d" % additional_space_req)

candidates = {}
for k,v in all_paths.items():
    if v>= additional_space_req:
        candidates[k] = v

import pprint; pprint.pprint(candidates)
