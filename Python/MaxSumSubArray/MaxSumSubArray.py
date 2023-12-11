#User function Template for python3
class Solution:
    def maximumSumSubarray (self, K, arr, N):
        # code here 
        start = end = 0
        ans = 0
        count = 0
        
        while end < N:
            count += arr[end]
            
            if end - start >= K:
                count -= arr[start]
                start += 1
                
            if count > ans:
                ans = count
                
            end += 1
            
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        
        N,K = input().split()
        N = int(N)
        K = int(K)
        Arr = list( map(int,input().strip().split(" ")))

        ob = Solution()
        print(ob.maximumSumSubarray(K,Arr,N))
# } Driver Code Ends