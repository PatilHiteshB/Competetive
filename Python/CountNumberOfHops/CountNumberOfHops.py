#User function Template for python3

class Solution:
    #Function to count the number of ways in which frog can reach the top.
    def countWays(self,n):
        m=1000000007
        f=1
        s=2
        t=4

        if(n==3):
            return 4
            
        ans=0
        if(n<=2):
            return n
        for i in range(n-3):
            ans=(f+s+t)%m
            f=s
            s=t
            t=ans
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys
sys.setrecursionlimit(10**6)
# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        m = int(input())
        ob=Solution()
        print(ob.countWays(m))
# } Driver Code Ends