#Uses python3

import sys
from itertools import chain, combinations


def get_subsets(fullset):
        listrep = list(fullset)
    subsets = []
    for i in range(2**len(listrep)):
        subset = []
        for k in range(len(listrep)):            
            if i & 1<<k:
                subset.append(listrep[k])
        subsets.append(subset)        
    return subsets
        
    return subsets

   

def lcs2(a, b):
    #lis = numpy.empty(shape=(len(a),len(b)),dtype='object') 
    cnt = 0
    #for i in range(len(s)+1):
     #   lis[i][0] = i
    #for j in range(len(t)+1):
     #   lis[0][j] = j
    sub1 = get_subsets(a)
    sub2 = get_subsets(b)
    
    for i in range(len(sub1)):
        for j in range(len(sub2)):
            if sub1[i] == sub2[j]:
                if cnt < len(sub1[i]):
                    cnt = len(sub1[j])


    return cnt

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    n = data[0]
    data = data[1:]
    a = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    b = data[:m]

    print(lcs2(a, b))
