#User function Template for python3
class Solution:


	def countSubarray(self, arr, N, K):
	    # code here
        ans = 0
        i = 0
        
        while i < N:
            
            if arr[i] > K:
                
                ans += N - i
                i += 1
                
            else:
                
                j = i + 1
                c = 0
                
                while j < N and arr[j] <= K:
                    j += 1
                    c += 1
                    
                if j >= N: break
                ans += N-j
                
                while c > 0:
                    
                    ans += N - j
                    c += -1
                    
                i = j
                
        return ans
                


#{ 
 # Driver Code Starts
#Initial Template for Python 3


# Driver code 
if __name__ == "__main__": 		
    tc=int(input())
    while tc > 0:
        n, k=map(int, input().strip().split())
        arr=list(map(int, input().strip().split()))
        ob = Solution()
        ans=ob.countSubarray(arr, n, k)
        print(ans)
        tc=tc-1
# } Driver Code Ends