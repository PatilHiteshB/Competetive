#User function Template for python3

class Solution:
    def removeStudents(self, arr, n):
        # code here
        count = [1]*n
        
        
        ma = 0
        for i in range(n):
            for j in range(0, i):
                
                if arr[j] < arr[i] and count[j]+1 < count[i]:
                    count[j] = max(count[j], count[i]+1)
                    ma = max(count[j], ma)
                    
        return n-ma
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        H=list(map(int,input().split()))
        
        ob = Solution()
        print(ob.removeStudents(H,N))
# } Driver Code Ends