#User function Template for python3


class Solution:
    def nextLargerElement(self, arr, N):
        #code here
        stck = []
        ans = []
        
        for i in range(N-1, -1, -1):
            
            while stck and stck[-1] <= arr[i]:
                stck.pop()
                
            ans.insert(0, -1 if stck == [] else stck[-1])
            stck.append(arr[i])
            
        return ans

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