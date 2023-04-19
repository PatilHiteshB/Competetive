#User function Template for python3
class Solution:
    
    def solve(self, ind, X, S):
        
        if ind < 0 or ind >= len(S) or X < 0:
            return
        
        S[ind] = '1'
        self.solve(ind+1, X-1, S)
        self.solve(ind-1, X-1, S)
            
            
    
    def wifiRange(self, N, S, X): 
        #code here
        
        Y = ['1' if i == '1' else '0' for i in S]
        
        for i in range(N):
            if S[i] == '1':
                self.solve(i, X, Y)
                
        return 0 if '0' in Y else 1
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        N,X = map(int,input().strip().split())
        S = input()
        ob = Solution()
        ans = ob.wifiRange(N, S, X)
        if ans:
            print(1)
        else:
            print(0)

# } Driver Code Ends