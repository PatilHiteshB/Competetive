#User function Template for python3

class Solution:	
	def wineSelling(self, arr, n):
		
		i, j= 0, 0
		ans = 0
		
		while True:
		    
		    while i<n and arr[i] <= 0:
		        i+=1
		        
            while j<n and arr[j] >= 0:
                j+=1
                
            if i==n or j==n:
                break
            
            change = min(arr[i], -arr[j])
            ans += abs((i-j)*change)
            arr[i] -= change
            arr[j] += change
            
        return ans
		


#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__=='__main__':
    t = int(input())
    for i in range(t):
        N = int(input())
        Arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.wineSelling(Arr,N)
        
        print(ans)

# } Driver Code Ends