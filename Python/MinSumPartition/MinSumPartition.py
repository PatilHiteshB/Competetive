#User function Template for python3
class Solution:
    
    def __init__(self):
        self.ans = float('inf')
    
    def solve(self, ind, arr, N, sum1, sum2):
        
        if ind < 0:
            # print("{} {}".format(sum1, sum2))
            self.ans = min(self.ans, abs(sum1-sum2))
            return
        
        self.solve(ind-1, arr, N, sum1, sum2+arr[ind])
        self.solve(ind-1, arr, N, sum1+arr[ind], sum2)
            
        
	def minDifference(self, arr, n):
		# code here
		self.solve(N-1, arr, N, 0, 0)
		return self.ans


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