# Uses python3
import sys

def get_change(m):
    #write your code herez

    li = [0]*(m+1)
    li[0] = 0
    for i in range(m+1):
    	
    	
    	c = i
    	while(c > 0):
    		if(c % 4 == 0):
    			c = c - 4
    			li[i] = li[i] + 1
    		elif(c % 3 == 0):
    			c = c - 3
    			li[i] = li[i] + 1
    		else:
    			if(c > 4):
    				c = c - 4
    				li[i] = li[i] + 1
    			elif(c > 3):
    				c = c - 3
    				li[i] = li[i] + 1
    			else:
    				c = c - 1
    				li[i] = li[i] + 1
    		
    	

    c = len(li)
    

    return li[c-1]

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
