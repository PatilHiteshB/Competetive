#User function Template for python3
class Solution:

	def rowWithMax1s(self,arr, n, m):
		# code here
		k = 0
		l = m-1
		ans = -1
		
		while k<n and l >= 0:
		    
		    if arr[k][l] == 1:
		        ans = k
		        l += -1
		        
            if arr[k][l] == 0:
                k += 1
                
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, m = list(map(int, input().strip().split()))
        
        inputLine = list(map(int, input().strip().split()))
        arr = [[0 for j in range(m)] for i in range(n)]
        
        for i in range(n):
            for j in range(m):
                arr[i][j] = inputLine[i * m + j]
        ob = Solution()
        ans = ob.rowWithMax1s(arr, n, m)
        print(ans)
        tc -= 1

# } Driver Code Ends