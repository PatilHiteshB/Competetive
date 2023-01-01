#User function Template for python3

class Solution:
    
    def __init__(self):
        self.factN = 0
        self.factR = 0
        self.factNR = 0
            
    def countSetBits(self, n):
        ans = 0
        while n:
            ans += (1 if n&1 == 1 else 0)
            n = n>>1
        return ans
        
        
    def fact(self, n):
        if n < 0:
            return 0
        elif n == 0 or n == 1:
            return 1
        
        fact = 1
        while(n > 1):
            fact *= n
            n -= 1
            
        return fact

    def nCombination(self, n, r):
        # print("{} {}".format(self.factNR, r))
        if r == 0 or n == r:
            return 1
        return self.factN // (self.factNR * self.factR)
        
	def compute_value(self, n):
		# Code here
		self.factN = self.factNR = self.fact(n)
		self.factR = 1
		mod = 10**9+7
		ans = 0
		for i in range(n+1):
		    if i != 0:
		        self.factR *= i
		    temp = self.nCombination(n, i)
		    ans += ((temp%mod) * (temp%mod))%mod
		    if n != i:
                self.factNR = self.factNR // (n-i)
                
		return ans%mod


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		ob = Solution()
		ans = ob.compute_value(n)
		print(ans)
# } Driver Code Ends