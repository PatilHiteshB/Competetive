
import math

class Solution:
    
    def find(self, N):
        x = 0
        while 1 << x <= N:
            x += 1
            
        return x-1
        
    def countBits(self, N : int) -> int:
        # code here
        if N <= 1: return N
        
        x = self.find(N)
        return x * (2**(x-1)) + N - 2**x + 1 + self.countBits(N-2**x)
        



#{ 
 # Driver Code Starts
if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        N = int(input())
        
        obj = Solution()
        res = obj.countBits(N)
        
        print(res)
        

# } Driver Code Ends