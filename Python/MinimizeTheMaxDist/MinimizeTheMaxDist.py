#{ 
 # Driver Code Starts
#Initial Template for Python 3


# } Driver Code Ends
#User function Template for python3

class Solution:
    def findSmallestMaxDist(self, arr, K):
        # Code here
        
        start, end = 0, arr[-1] - arr[0]
        
        while end - start > 1e-5:
            
            mid = (end+start)/2
            
            if self.ispossible(arr, K, mid):
                end = mid
            else:
                start = mid
                
        
        return end
        
    
    def ispossible(self, arr, K, dist):
        
        count = 0
        for i in range(1, len(arr)):
            count += (arr[i]-arr[i-1])//dist
            
        return count <= K
        
        

#{ 
 # Driver Code Starts.
import math
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        stations = list(map(int, input().split()))
        K = int(input())
        ob = Solution()
        print('%.2f' % ob.findSmallestMaxDist(stations, K))
# } Driver Code Ends