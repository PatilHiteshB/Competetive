#User function Template for python3
class Solution:
	
	def findMaxSum(self, arr, n):
		# code here
		ma1 = ma2 = ans = 0
		
		for i in range(n):
		    
            ma1, ma2 = max(ma1, ma2), max(ma1+arr[i], ma2)
        
        return max(ma1, ma2)
		       


#{ 
 # Driver Code Starts
#Initial Template for Python 3




if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.findMaxSum(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends