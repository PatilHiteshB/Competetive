import re

def contains_only_a_or_b(num, a, b):
    
    while num > 0:
        if num%10 in [a, b]:
            return True
        num //= 10
    
    return False


class Solution:
    
    def __init__(self):
        
        self.fact = [i for i in range(10**5 + 1)]
        self.fact[0] = 1
        
        for i in range(1, 10**5 + 1):
            self.fact[i] = (self.fact[i] *self.fact[i-1]) % (10**9 + 7)
            
            
        
    def bestNumbers(self, N : int, A : int, B : int, C : int, D : int) -> int:
        # code here
        if A == B:
            return 1 if contains_only_a_or_b(A*N, C, D) else 0
            
        count = 0
        mod = 10 ** 9 + 7
            
        for i in range(0, N+1):
            sum = A*i + B*(N-i)
            
            if contains_only_a_or_b(sum, C, D):
                
                n = self.fact[N]
                d = (self.fact[i] * self.fact[N-i]) % mod
                d = pow(d, mod-2, mod)
                # print("{} {}".format(n, d))
                # print(self.fact[:10])
                count += (n * d) % mod
                
        
        return count % mod
        





#{ 
 # Driver Code Starts


if __name__=="__main__":  
    t = int(input())
    for _ in range(t):
        N = int(input())
        A = int(input())
        B = int(input())
        C = int(input())
        D = int(input())
        obj = Solution()
        res = obj.bestNumbers(N, A, B, C, D)
        print(res)
# } Driver Code Ends