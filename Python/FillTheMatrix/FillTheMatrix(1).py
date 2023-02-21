#User function Template for python3

class Solution:
    def minIteration(self, N, M, x, y):
        #code here
        ans = 0
        
        for a, b in [(1, 1), (1, M), (N, 1), (N, M)]:
            
            ans = max(ans, abs(x-a) + abs(y-b))
            
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		N, M = map(int,input().split())
		x, y = map(int,input().split())
		ob = Solution()
		print(ob.minIteration(N, M, x, y))
# } Driver Code Ends