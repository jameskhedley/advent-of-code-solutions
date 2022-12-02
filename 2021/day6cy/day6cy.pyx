#cython: language_level=3
import cython
from libc.stdlib cimport malloc, free


def main(fishes, cython.int days, print_fishes=False):
    idx: cython.int = 0
    fry: cython.int = 0
    len_f: cython.int = len(fishes)
    cdef int *my_ints
    fish: cython.int = 0
    
    cfishes = <int *>malloc(4000000000*cython.sizeof(int))
    
    if cfishes is NULL:
        raise MemoryError()
    for i in xrange(len_f):
        cfishes[i] = fishes[i]

    #p: cython.int[10000000]
    for day in range(days):
        fry = 0
        for idx in xrange(len_f):
            fish = cfishes[idx]
            if fish == 0:
                fry += 1
                cfishes[idx] = 6
            else:
                cfishes[idx] = fish - 1

        for idx in xrange(fry):
            cfishes[len_f+idx] = 8
        len_f = len_f + fry
        print("Day %d, %d fishes" % (day, len_f))
    print(len_f)

