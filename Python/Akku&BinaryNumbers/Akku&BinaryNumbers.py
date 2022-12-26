#User function Template for python3

class Solution:
    def tillN(self, N, index, count, k):
        
        if count == 3:
            return 1
        
        if index < 0:
            return 0
        
        ans = 0
        
        if self.isSet(N, index):
            ans += self.tillN(N, index-1, count+1, k&1)
            ans += self.tillN(N, index-1, count, 1)
        else:
            if k == 1:
                ans += self.tillN(N, index-1, count+1, k)
                ans += self.tillN(N, index-1, count, k)
            else:
                ans += self.tillN(N, index-1, count, k)
            
        return ans
            
    def isSet(self, n, ind):
        return n&(1<<ind)!=0
        
    def solve (self, L, R):
        # code here
        return self.tillN(R, 63, 0, 0) - self.tillN(L-1, 63, 0, 0)
        
    def precompute (self):
        pass
        # code here
        



#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__': 
    ob = Solution()
    ob.precompute()
    t = int (input ())
    for _ in range (t):
        L, R = map(int,input().split())
        ans = ob.solve(L, R);
        print(ans)




# } Driver Code Ends