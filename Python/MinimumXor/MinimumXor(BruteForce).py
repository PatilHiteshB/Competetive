#User function Template for python3
import sys

class Solution:
    
    def countSet(self, n):
        
        count = 0
        
        while n > 0:
            if n&1 == 1:
                count += 1
            n = n >> 1
            
        return count
        
    
        
    def minVal(self, a, b):
        #code here
        
        ma = 2 ** (len(bin(max(a, b))[2:]) + 1)
        
        arr = set()
        
        index = 0
        setB = self.countSet(b)
        
        
        while index < ma:
            
            if self.countSet(index) == setB and index not in arr:
                temp = index
            
                while temp < ma:
                    arr.add(temp)
                    temp *= 2
            
            index += 1
        
        answer = b
        xorma = sys.maxsize
        
        for i in arr:
            
            temp = a^i
            if temp < xorma:
                answer = i
                xorma = temp
        
        return answer


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        a = int(input())
        b = int(input())
        
        ob= Solution()
        print(ob.minVal(a,b))
# } Driver Code Ends