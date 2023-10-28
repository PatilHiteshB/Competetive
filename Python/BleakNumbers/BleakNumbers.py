#User function Template for python3
from math import log2
from math import ceil

class Solution:
    
    def countSetBits(self,n):
        
        res=0
        
        while n>0:
            res=res+n%2
            n=n//2
        
        return res
        
    
	def is_bleak(self, n):
		
		k=n-ceil(log2(n))
		
		while k<n:
		    if k+self.countSetBits(k)==n:
		        return 0
		    k=k+1
		
		return 1   

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		ob = Solution();
		ans = ob.is_bleak(n)
		print(ans)

# } Driver Code Ends