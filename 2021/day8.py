from collections import defaultdict
import sys

#all_lines = open("day8-ex.txt").readlines()
all_lines = open("day8.txt").readlines()

#all_lines = ["acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf"]
#all_lines = ["be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe"]
#print(all_lines)
#sys.exit()

#all_lines = [all_lines[0]]

ZERO = {'a', 'b', 'c', 'e', 'f', 'g'}
ONE = {'c', 'f'}
TWO = {'a', 'c', 'd', 'e', 'g'}
THREE = {'a', 'c', 'd', 'f', 'g'}
FOUR = {'b', 'c', 'd', 'f'}
FIVE = {'a', 'b', 'd', 'f', 'g'}
SIX = {'a', 'b', 'd', 'e', 'f', 'g'}
SEVEN = {'a', 'c', 'f'}
EIGHT = {'a', 'b', 'c', 'd', 'e', 'f', 'g'}
NINE = {'a', 'b', 'c', 'd', 'f', 'g'}

all_nums = {0: ZERO, 1: ONE, 2: TWO, 3: THREE, 4: FOUR, 5: FIVE, 6: SIX, 7: SEVEN, 8: EIGHT, 9: NINE}
all_nums_inv = {tuple(v):k for k, v in all_nums.items()}

signals = [[set(x) for x in line.split(" | ")[0].split()] for line in all_lines]
outputs = [[set(x) for x in line.split(" | ")[1].strip().split()] for line in all_lines]
print(signals)
print("************************")
print(outputs)
print("************************")

def pt2(signals, outps):
    #print(inps)
    #print("************************")
    #print(outps)
    
    grand_total = 0
    
    for idx, sig_set in enumerate(signals):
        #print("Sig set: %s" % str(sig_set))
        inv_table = deduce(sig_set)
        for sig in sig_set:
            #print("Sig: %s" % str(sig))
            decoded = set([inv_table[x] for x in sig])

        result = ""
        for chars in outputs[idx]:
            #import pdb; pdb.set_trace()
            decoded = set([inv_table[x] for x in chars])
            for (num, num_set) in all_nums.items():
                if num_set == decoded:
                    DIGIT = str(num)
                    result += DIGIT
                    #print(DIGIT)
        print(result)
        grand_total += int(result)
    print(grand_total)
    
def deduce(signal_set):
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    #print(signal_set)
    signal_table = {}
    num_table = {}
    for signal in signal_set:
        #print(signal)
        if len(signal) == 2:
            signal_table[1] = signal
        elif len(signal) == 3:
            signal_table[7] = signal
        elif len(signal) == 4:
            signal_table[4] = signal
        elif len(signal) == 7:
            signal_table[8] = signal
    
    temp = signal_table[7] - signal_table[1]
    num_table["a"] = temp.pop()
    
    counts = defaultdict(int)
    for signal in signal_set:
        for letter in letters:
            if letter in signal:
                counts[letter]+=1
    
    
    sevens = [k for k,v in counts.items() if v==7]
    for candi in sevens:
        if candi in signal_table[4]:
            num_table["d"] = candi
        else:
            num_table["g"] = candi
    
    for signal in signal_set:
        if len(signal) == 6:
            if num_table["d"] not in signal:
                signal_table[0] = signal
            elif signal_table[4] - signal == set():
                signal_table[9] = signal
            else:
                signal_table[6] = signal



    counts = defaultdict(int)
    for signal in signal_set:
        if len(signal) != 5:
            continue
        #print(list(signal))
        for letter in letters:
            if letter in signal:
                counts[letter]+=1

    #import pdb; pdb.set_trace()
    singles = [(k,v) for k,v in counts.items() if v==1]
    for signal in signal_set:
        if len(signal) != 5:
            continue
        if singles[0][0] not in signal and singles[1][0] not in signal:
            #print("DEBUG %s" % str(singles[0][0]))
            signal_table[3] = signal
            break
    #print("Segments only in one five segment signal %s" % str(singles))
 
    for l in letters:
        if l not in signal_table[6]:
            num_table['c'] = l
            break
            
    for signal in signal_set:
        if len(signal) != 5:
            continue
        if signal in signal_table.values():
            #print("A known five segment signal: %s" % str(signal))    
            continue
        #print("A five segment signal: %s" % str(signal))
        if num_table['c'] in signal:
            signal_table[2] = signal
        else:
            signal_table[5] = signal
    
    temp = signal_table[1] - set(num_table['c'])
    num_table['f'] = temp.pop()
    
    temp = signal_table[4] - set(num_table['c']) - set(num_table['d']) - set(num_table['f'])
    num_table['b'] = temp.pop()
    
    temp = signal_table[2] - set(num_table['a']) - set(num_table['c']) - set(num_table['d']) - set(num_table['g'])
    num_table['e'] = temp.pop()
    
    #print(sorted(signal_table.keys()))
    #print(sorted(num_table.keys()))
    #print(num_table)
    #print(signal_table)

    inv = {v: k for k,v in num_table.items()}
    return inv

def junk():
    for signal in signal_set:
        if len(signal) == 5:
            temp = signal - signal_table[4]
            num_table["a"] = temp.pop()
            break        
    
def pt1(data):
    uniqs = [ONE, FOUR, SEVEN, EIGHT]
    count = 0
    for output in data:
        for group in output:
            print("***********************")
            print("Output group:" + str(group))
            for u in uniqs:
                print(u)
                if len(u) == len(group):
                    count+=1
            print(count)
            print("***********************")
    print(count)

#pt1(outputs)

pt2(signals, outputs)

