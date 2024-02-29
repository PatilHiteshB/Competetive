#User function Template for python3

class Solution:
    
	def sumBitDifferences(self,arr, n):
    	# code here
    	ans = 0
    	for i in range(31, -1, -1):
    	    one = 0
    	    zero = 0
    	    for j in range(n):
    	        bit = 1 << i
    	        if (arr[j] & bit) > 0:
    	            one += 1
    	        else:
    	            zero += 1
    	    ans += (one * zero) * 2
    	return ans



#{ 
 # Driver Code Starts

#Initial Template for Python 3


if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.sumBitDifferences(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends