#User function Template for python3
mod = 1000000007
class Solution:
    def arraySu(self, index, csum, fsum, arr, N):
        global mod
        
        if index == N:
            return 1 if csum == fsum else 0
        
        csum += arr[index]
        lans = self.arraySu(index+1, csum, fsum, arr, N)%mod
        
        csum -= arr[index]
        rans = self.arraySu(index+1, csum, fsum, arr, N)%mod
        
        return (lans+rans)%mod
        
	def perfectSum(self, arr, N, su):
		# code here
		return self.arraySu(0, 0, su, arr, N)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n,sum = input().split()
		n,sum = int(n),int(sum)
		arr = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.perfectSum(arr,n,sum)
		print(ans)

# } Driver Code Ends