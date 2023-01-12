#User function Template for python3

from queue import PriorityQueue
import heapq

class Solution:
    
        
    def minimizeSum(self, N, arr):
        # Code here
        heapq.heapify(arr)
        l=len(arr)
        op=0
        
        while l>1:
            
            x=heapq.heappop(arr)
            y=heapq.heappop(arr)
            heapq.heappush(arr,x+y)
            
            op=x+y+op
            
            l-=1
        return op


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    
    for _ in range(t):
        n = int(input())
        A = [int(x) for x in input().split()]
        ob=Solution()
        print(ob.minimizeSum(n, A))
# } Driver Code Ends