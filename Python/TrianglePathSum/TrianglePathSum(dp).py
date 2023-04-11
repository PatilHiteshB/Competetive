#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def solve(self, r, c, arr, N, dp):
        
        if r >= N:
            return 0
            
        if dp[r][c] != -1: return dp[r][c]
        
        MIN = arr[r][c] + self.solve(r+1, c, arr, N, dp)
        
        if c+1 < len(arr[r]):
            MIN = min(MIN, arr[r][c+1] + self.solve(r+1, c+1, arr, N, dp))
            
        dp[r][c] = MIN
        return MIN
        
        
        
        
    def minimizeSum(self, n, triangle):
        # Code here
        dp = [[-1 for _ in i] for i in triangle]
        return self.solve(0, 0, triangle, n, dp)
        
        
        
        

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        n = int(input())
        triangle = [list(map(int, input().split())) for _ in range(n)]
        ob = Solution()
        res = ob.minimizeSum(n, triangle)
        print(res)
# } Driver Code Ends