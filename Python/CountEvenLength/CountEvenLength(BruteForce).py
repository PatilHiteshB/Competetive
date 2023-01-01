#User function Template for python3

class Solution:
    def countSetBits(self, n):
        ans = 0
        while n:
            ans += (1 if n&1 == 1 else 0)
            n = n>>1
        return ans
	def compute_value(self, n):
		# Code here
		mp = {}
		for i in range(2**n):
		    temp = self.countSetBits(i)
		    if temp in mp.keys():
		        mp[temp] += 1
            else:
                mp[temp] = 1
                
                
        
        ans = 0
        for i in mp.keys():
            ans += mp[i]*mp[i]
            
		return ans


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