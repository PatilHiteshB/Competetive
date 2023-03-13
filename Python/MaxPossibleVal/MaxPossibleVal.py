#User function Template for python3
from queue import PriorityQueue
class Solution:
    def maxPossibleValue(self, N, A, B): 
        #code here
        pq = PriorityQueue()
        for i in range(N):
            pq.put((-A[i], B[i]))
            
        ans = 0
        while len(pq.queue) > 0:
            
            length, count = pq.get()
            
            if count <= 1:
                continue
            
            if count >= 4:
                ans -= (length*4)
                pq.put((length, count-4))
                
            elif count >= 2:
                
                while len(pq.queue) > 0:
                    
                    l2, c2 = pq.get()
                    if c2 >= 2:
                        ans -= (l2*2+length*2)
                        pq.put((l2, c2-2))
                        break
                    
                pq.put((length, count-2))
                    
        
        return ans



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        N = int(input().strip())
        A = list(map(int, input().strip().split()))
        B = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.maxPossibleValue(N, A, B)
        print(ans)

# } Driver Code Ends