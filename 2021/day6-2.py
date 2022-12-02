from collections import defaultdict
from pprint import pprint
data_ex = [3,4,3,1,2]

data = [4,3,3,5,4,1,2,1,3,1,1,1,1,1,2,4,1,3,3,1,1,1,1,2,3,1,1,1,4,1,1,2,1,2,2,1,1,1,1,1,5,1,1,2,1,1,1,1,1,1,1,1,1,3,1,1,1,1,1,1,1,1,5,1,4,2,1,1,2,1,3,1,1,2,2,1,1,1,1,1,1,1,1,1,1,4,1,3,2,2,3,1,1,1,4,1,1,1,1,5,1,1,1,5,1,1,3,1,1,2,4,1,1,3,2,4,1,1,1,1,1,5,5,1,1,1,1,1,1,4,1,1,1,3,2,1,1,5,1,1,1,1,1,1,1,5,4,1,5,1,3,4,1,1,1,1,2,1,2,1,1,1,2,2,1,2,3,5,1,1,1,1,3,5,1,1,1,2,1,1,4,1,1,5,1,4,1,2,1,3,1,5,1,4,3,1,3,2,1,1,1,2,2,1,1,1,1,4,5,1,1,1,1,1,3,1,3,4,1,1,4,1,1,3,1,3,1,1,4,5,4,3,2,5,1,1,1,1,1,1,2,1,5,2,5,3,1,1,1,1,1,3,1,1,1,1,5,1,2,1,2,1,1,1,1,2,1,1,1,1,1,1,1,3,3,1,1,5,1,3,5,5,1,1,1,2,1,2,1,5,1,1,1,1,2,1,1,1,2,1]

#DAYS = 18
#DAYS = 80
DAYS = 256


def main(fishes):
    agg = defaultdict(int)
    for fish in fishes:
        agg[fish] += 1
    pprint(dict(agg))
    for day in range(DAYS):
        new_agg = defaultdict(int)
        fry = 0
        print("day %d" % (day+1))
        #for k, v in agg.items():
        for k in range(0,9):
            if k==0:
                fry += agg[k]
                new_agg[6] = agg[k]
                if fry > 0:
                    print("SPAWNED, new fry=%d, new parents=%d" %(fry, new_agg[6]))
                    #import pdb; pdb.set_trace()
            else:
                #if k==7:
                #    import pdb; pdb.set_trace()
                new_agg[k-1] += agg[k]
        new_agg[8] = fry
        agg = new_agg
        
        pprint(dict(agg))
        print("***************")
    print(sum(agg.values()))


        
#main(data_ex)
main(data)
#1,738,377,086,345
#    2,109,914,057 #naive approach, 178 days


