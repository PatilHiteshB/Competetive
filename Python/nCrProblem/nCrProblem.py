#User function Template for python3

class Solution:
    
    def nCr(self, n, r):
        def fact(num):
            ans=1
            for i in range(1, num+1):
                ans*=i
            return ans
        return (fact(n)//(fact(r)*fact(n-r)))%(10**9+7)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, r = [int(x) for x in input().split()]
        
        ob = Solution()
        print(ob.nCr(n, r))
# } Driver Code Ends