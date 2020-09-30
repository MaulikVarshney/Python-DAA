# Uses python3
import numpy
def edit_distance(s, t):
    #write your code here
    lis = numpy.empty(shape=(len(s)+1,len(t)+1),dtype='object') 
  
    for i in range(len(s)+1):
    	lis[i][0] = i
    for j in range(len(t)+1):
    	lis[0][j] = j

    for j in range(1, len(t)+1):
    	for i in range(1, len(s)+1):
    		insert = lis[i][j-1] + 1
    		deletion = lis[i-1][j] + 1
    		match = lis[i-1][j-1] 
    		mismatch = lis[i-1][j-1] + 1
    		if(s[i-1] == t[j-1]):
    			lis[i][j] = min(insert,deletion,match)
    		else:
    			lis[i][j] = min(insert,deletion,mismatch)

    
    return lis[len(s)][len(t)]

if __name__ == "__main__":
    print(edit_distance(input(), input()))
