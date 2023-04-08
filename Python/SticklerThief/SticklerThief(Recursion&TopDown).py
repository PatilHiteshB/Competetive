#User function Template for python3

class Solution:  
    
    def solve(self, arr, N, ind, dp):
        
        if ind == 0: return arr[0]
        
        if ind < 0: return 0
        
        if dp[ind] != -1: return dp[ind]
        
        pick = arr[ind] + self.solve(arr, N, ind-2, dp)
        notpick = self.solve(arr, N, ind-1, dp)
        
        dp[ind] = max(pick, notpick)
        
        return dp[ind]
    
    #Function to find the maximum money the thief can get.
    def FindMaxSum(self, arr, n):
        # code here
        dp = [-1 for _ in range(n)]
        return self.solve(arr, n, n-1, dp)


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