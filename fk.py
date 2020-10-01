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
                temp = arr[j]
                arr[j] = arr[k]
                arr[k] = temp
                temp1 = weights[j]
                weights[j] = weights[k]
                weights[k] = temp1
                temp2 = values[j]
                values[j] = values[k]
                values[k] = temp2

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
