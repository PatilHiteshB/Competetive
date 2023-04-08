#User function Template for python3

class Solution:  
    
    #Function to find the maximum money the thief can get.
    def FindMaxSum(self, arr, n):
        # code here
        
        dp = [0 for _ in range(n)]
        dp[0] = arr[0]
        
        
        for i in range(1, n):
            
            pick = arr[i]
            if i > 1: pick += dp[i-2]
            
            notpick = dp[i-1]
            dp[i] = max(pick, notpick)
            
        # print(dp)
            
        return dp[n-1]


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
        n = int(input())
        a = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.FindMaxSum(a,n))
# } Driver Code Ends