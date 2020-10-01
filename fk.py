# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    
    value = 0.
    arr = []
    c = len(weights)-1
    
    for i in range(0,c+1):
        arr.append(values[i]/weights[i]) 
    
    for j in range(0,c):
        for k in range(j+1,c+1):
            point = arr[j]
            if(point > arr[k]):
                swap(arr[j],arr[k])
                swap(weights[j],weights[k])
                swap(values[j],values[k])

    while(capacity>0 and c>=0):
    

        if(weights[c] <= capacity):
            capacity = capacity - weights[c]
            value = value + values[c]
        
       
        else:
            d = (capacity*values[c])/weights[c]
            value+=d
            capacity = capacity - weights[c]
        c=c-1
    return value

if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    #data = list(map(int, input().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
