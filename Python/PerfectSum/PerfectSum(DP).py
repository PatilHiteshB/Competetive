#User function Template for python3

mod = (10**9)+7
class Solution:
    def solve(self, arr, n, sum, dp):
        
        global mod
        
        if n < 0 and sum != 0:
            return 0
            
        if n < 0 and sum == 0:
            return 1
            
        if dp[n][sum] != -1:
            return dp[n][sum]%mod
            
        
        not_pick =   self.solve(arr, n-1, sum, dp)
        
        pick = 0
        if arr[n] <= sum:
            pick = self.solve(arr, n-1, sum-arr[n], dp) 
        
        # print(" {} {} {}".format(n, pick, not_pick))    
        dp[n][sum] = (pick%mod + not_pick%mod)%mod
        
        return dp[n][sum]
            
        
        
        
	def perfectSum(self, arr, n, sum):
		# code here
		dp = [[-1 for i in range(sum+1)] for i in range(n+1)]
		return self.solve(arr, n-1, sum, dp)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n,sum = input().split()
		n,sum = int(n),int(sum)
		arr = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.perfectSum(arr,n,sum)
		print(ans)

# } Driver Code Ends