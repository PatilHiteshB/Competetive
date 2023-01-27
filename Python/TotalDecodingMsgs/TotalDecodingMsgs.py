#User function Template for python3
mod = 1000000007
class Solution:
    def solve(self, st, n, dp):
        # print(st)
        global mod
        
        if n == 0 or n == 1:
            return 1
            
        if dp[n] != -1:
            return dp[n]
            
        cnt = 0
        
        if st[n-1] >= '1':
            cnt += self.solve(st, n-1, dp)%mod
        
        if st[n-2] == '1' or st[n-2] == '2' and st[n-1] <= '6':
            cnt += self.solve(st, n-2, dp)%mod
            
        dp[n] = cnt%mod
        return dp[n]
            
    def add(self, a, b):
        global mod
        return ((a%mod)+(b%mod))%mod
        
        
	def CountWays(self, st):
		# Code here
		if st[0] == '0':
		    return 0
		    
        return self.solve(st, len(st), [-1]*(len(st)+1))
		

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		str = input()
		ob = Solution()
		ans = ob.CountWays(str)
		print(ans)

# } Driver Code Ends