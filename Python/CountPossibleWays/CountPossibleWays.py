#User function Template for python3

class Solution:
	def TotalWays(self, n):
	    self.mod = 1000000007
        a,b=2,3
        for i in range(3,n+1):
            b, a = (a+b)%self.mod, b
        return b**2%self.mod if n!=1 else a**2
#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		N = int(input())
		ob = Solution()
		ans = ob.TotalWays(N)
		print(ans)
# } Driver Code Ends