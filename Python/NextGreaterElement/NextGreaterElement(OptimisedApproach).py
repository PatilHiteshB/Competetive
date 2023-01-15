#User function Template for python3


class Solution:
    def nextLargerElement(self, arr, N):
        #code here
        stck = []
        NGE = [-1] * N
        
        for index, value in enumerate(arr):
            
            l = len(stck)
            
            if l == 0:
                stck.append(index)
                
            try:
                nex = arr[index+1]
            except IndexError:
                break
            
            if nex <= arr[stck[-1]]:
                stck.append(index+1)
            else:
                
                while len(stck) > 0 and nex > arr[stck[-1]]:
                    i = stck.pop()
                    NGE[i] = nex
                else:
                    stck.append(index+1)
                    
        return NGE

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

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())

        a = list(map(int,input().strip().split()))
        obj = Solution()
        res = obj.nextLargerElement(a,n)
        for i in range (len (res)):
            print (res[i], end = " ")
        print ()
# } Driver Code Ends