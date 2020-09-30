#Uses python3

import sys

def max_dot_product(a, b):
    #write your code here
    for j in range(len(a)):
        for k in range(j+1,len(a)):
            point = a[j]
            if(point > a[k]):
                temp = a[j]
                a[j] = a[k]
                a[k] = temp
    for j in range(len(a)):
        for k in range(j+1,len(a)):
            point = b[j]
            if(point > b[k]):
                temp = b[j]
                b[j] = b[k]
                b[k] = temp
                            
    res = 0
    for i in range(len(a)):
        res += a[i] * b[i]
    return res

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    #data = list(map(int, input().split()))
    n = data[0]
    a = data[1:(n + 1)]
    b = data[(n + 1):]
    print(max_dot_product(a, b))
    
