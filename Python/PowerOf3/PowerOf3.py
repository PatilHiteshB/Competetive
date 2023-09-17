#User function Template for python3
class Solution:
    def isPowerof3(self, N):
        # code here 
        
        x = 1
        while x <= N:
            
            if x == N:
                return "Yes"
            
            x = x*3
            
        return "No"


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        
        N=int(input())

        ob = Solution()
        print(ob.isPowerof3(N))
# } Driver Code Ends