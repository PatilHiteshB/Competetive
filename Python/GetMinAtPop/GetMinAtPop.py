#User function Template for python3

#Function to push all the elements into the stack.
def _push(arr, n):
    # code here
    return arr


#Function to print minimum value in stack each time while popping.    
def _getMinAtPop(stack):
    # code here
    ans = [0] * len(stack)
    MIN = stack[0]
    
    for i in range(len(stack)):
        if MIN > stack[i]:
            MIN = stack[i]
        ans[i] = MIN
        
    for i in range(len(stack)-1, -1, -1):
        print(ans[i], end=" ")

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

#Contributed by : Nagendra Jha

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
        stack =  _push(a,n) # our stack to be used
        _getMinAtPop(stack) # print elements of stack as required
        print()

# } Driver Code Ends