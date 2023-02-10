#User function Template for python3
import sys
class Solution:
	def LongestBitonicSequence(self, arr):
		# Code here
		
		N = len(arr)
		
		incr = [0 for i in range(N)]
		decr = [0 for i in range(N)]


		for i in range(1, N):
            
            ma = 0
            for j in range(0, i):
                
                if arr[i] > arr[j]:
                    ma = max(ma, incr[j]+1)
            
            incr[i] = ma


        for i in range(N-2, -1, -1):
            
            ma = 0
            for j in range(N-1, i, -1):
                
                if arr[i] > arr[j]:
                    ma = max(ma, decr[j]+1)
                    
            decr[i] = ma


        
        ans = 0
        for i in range(N):
            ans = max(ans, incr[i]+decr[i]+1)
            
        return ans
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		nums = list(map(int, input().split()))
		ob = Solution()
		ans = ob.LongestBitonicSequence(nums)
		print(ans)
# } Driver Code Ends