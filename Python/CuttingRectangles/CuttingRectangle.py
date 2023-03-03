#User function Template for python3

class Solution:
    def GCD(self, A, B):
        if A == 1 or B == 1:
            return 1
        if B == 0:
            return A
        if A == 0:
            return B
        
        if A > B: return self.GCD(B, A%B)
        return self.GCD(A, B%A)
        
    def minimumSquares(self, L, B):
        # code here
        
        ans = self.GCD(L, B)
                
        return [(L*B)//(ans*ans), ans]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        L, B = [int(x) for x in input().split()]
        
        ob = Solution();
        N, K = ob.minimumSquares(L, B)
        print(N,end=" ")
        print(K)
# } Driver Code Ends