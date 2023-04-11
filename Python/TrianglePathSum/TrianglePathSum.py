#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def solve(self, ind, arr, SUM):
        
        if ind == len(arr):
            return SUM
            
        MIN = float('inf')
        for i in arr[ind]:
            MIN = min(MIN, self.solve(ind+1, arr, SUM+i))
            
        return MIN
        
    def minimizeSum(self, n, triangle):
        # Code here
        
        return self.solve(0, triangle, 0)
        

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        n = int(input())
        triangle = [list(map(int, input().split())) for _ in range(n)]
        ob = Solution()
        res = ob.minimizeSum(n, triangle)
        print(res)
# } Driver Code Ends