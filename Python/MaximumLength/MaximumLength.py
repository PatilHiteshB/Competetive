#User function Template for python3

class Solution():
    
    def solve(self, a, b, c):
        #your code goes here
        ans = sorted([a, b, c])
        
        if ans[0] + ans[1] >= ((ans[2]+1)//2 - 1):
            return a+b+c
            
        return -1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

from collections import Counter
for _ in range(int(input())):
    a, b, c=map(int,input().split())
    obj = Solution()
    res = obj.solve(a, b, c)
    
    print(res)
# } Driver Code Ends