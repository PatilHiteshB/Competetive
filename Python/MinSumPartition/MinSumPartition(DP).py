#User function Template for python3
class Solution:
    
    
    def solve(self, ind, arr, target, dp):
        
        if ind < 0:
            return 1 if target == 0 else 0
            
        if dp[ind][target] != -1: return dp[ind][target]
        
        ans = notpick = self.solve(ind-1, arr, target, dp)
        
        if arr[ind] <= target:
            ans = max(ans, self.solve(ind-1, arr, target-arr[ind], dp))
            
        dp[ind][target] = ans
        return ans
        
        
            
        
	def minDifference(self, arr, n):
		# code here
		SUM = sum(arr)
		dp = [[-1 for _ in range(SUM)] for _ in range(n)]
		
		for i in range(SUM):
		    self.solve(n-1, arr, i, dp)
		    
        ans = float('inf')
        for i in range(SUM):
            
            if dp[n-1][i] == 1:
                ans = min(ans, abs(2*i-SUM))
                
        return ans
		
		


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		N = int(input())
		arr = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.minDifference(arr, N)
		print(ans)

# } Driver Code Ends