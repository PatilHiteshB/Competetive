#User function Template for python3
#User function Template for python3

class Solution:
    def setBits(self, n):
        
        count = 0
        while n > 0:
            
            if n&1 == 1:
                count += 1
            
            n >>= 1
            
        return count
        
        
    def minVal(self, a, b):
        #code here
        
        a1 = self.setBits(a)
        b1 = self.setBits(b)
        
        answer = a
        
        if a1 == b1:
            pass
        elif a1 < b1:
            
            idx = 0
            while a1 != b1:
                
                if a&1 == 0:
                    
                    answer += 1<<idx
                    a1 += 1
                    
                idx += 1
                a //= 2
        else:
            
            idx = 0
            while a1 != b1:
                
                if a&1 == 1:
                    
                    answer -= 1<<idx
                    a1 -= 1
                    
                idx += 1
                a //= 2
                
        return answer
        
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