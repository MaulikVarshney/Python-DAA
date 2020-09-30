# Uses python3
import sys

def fast_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    #write your code here
    if (len(points) == 1):
    	for i in range(len(starts)):
    		if(starts[i] <= points[0] <= ends[i]):
    			cnt[0] = cnt[0] + 1

    mid = len(points) // 2 
    for i in range(len(starts)):
		cnt[i] = cnt[i] + fast_count_segments( starts, ends, points[0:mid])
    	cnt[i] = cnt[i] + fast_count_segments( starts, ends, points[mid:len(points)])
    
    return cnt

def naive_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends   = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]
    #use fast_count_segments
    cnt = fast_count_segments(starts, ends, points)
    for x in cnt:
        print(x, end=' ')
