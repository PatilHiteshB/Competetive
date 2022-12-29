#User function Template for python3
class Solution:
    def solve(self, arr, k):
        count = 0
        for i in arr:
            if i%k == 0:
                count+= i//k
            else:
                count += (i//k)+1
        return count
        
    def smallestDivisor(self, nums, K):
        l, h = 1, max(nums)+1
        ans = 1
        
        while l<=h:
            
            mid = (l+h)//2
            
            temp = self.solve(nums, mid)
            
            if temp <= K:
                ans = mid
                h = mid-1
            else:
                l = mid+1
                
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        n, K = list(map(int, input().split()))
        nums = list(map(int, input().split()))
        ob = Solution()
        res = ob.smallestDivisor(nums, K)
        print(res)
# } Driver Code Ends