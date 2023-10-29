#User function Template for python3

class Solution:
    def setAllRangeBits(self, N , L , R):
        # code here 
        while (L<=R):
            N=N|(1<<L-1)
            L+=1
        return N


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N,L,R=map(int,input().split())
        
        ob = Solution()
        print(ob.setAllRangeBits(N,L,R))
# } Driver Code Ends