#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    
    def getTotal(self, bloomday, mid, K):
        result, count = 0, 0
        
        for i in range(len(bloomday)):
            if bloomday[i] <= mid:
                count+=1
            else:
                count=0
                
            if count==K:
                result+=1
                count=0
        return result
        
    def solve(self, M, K, bloomDay):
        # Code here
        if M*K > len(bloomDay):
            return -1
        
        low, high = 1, max(bloomDay)
        ans = -1
        
        while low<=high:
            
            mid = (low+high)//2
            total = self.getTotal(bloomDay, mid, K)
            
            if total>=M:
                ans = mid
                high = mid-1
            else:
                low = mid+1
        return ans
        

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        M, K = list(map(int, input().split()))
        bloomDay = list(map(int, input().split()))
        ob = Solution()
        res = ob.solve(M, K, bloomDay)
        print(res)
# } Driver Code Ends