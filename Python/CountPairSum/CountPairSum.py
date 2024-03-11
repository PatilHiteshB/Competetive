#User function Template for python3
class Solution:
	def countPairs(self, mat1, mat2, n, x):
		# code here
		
		mp = {}
		count = 0
		
		for i in range(n):
            for j in range(n):
                mp[mat1[i][j]] = True
        
        for i in range(n):
            for j in range(n):
                if x-mat2[i][j] in mp:
                    # print("{} {}".format(mat2[i][j], abs(x-mat2[i][j])))
                    count += 1
                    
        return count
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n , x = input().split()
		n,x = int(n), int(x)
		mat1 = []
		for _ in range(n):
			a = [int(x) for x in input().split()]
			mat1.append(a)

		mat2 = []
		for _ in range(n):
			a = [int(x) for x in input().split()]
			mat2.append(a)

		ob = Solution()
		ans = ob.countPairs(mat1, mat2, n, x)
		print(ans)

# } Driver Code Ends