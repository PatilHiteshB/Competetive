#User function Template for python3

class Solution:
	def Count(self, matrix):
		# Code here
        m,n=len(matrix),len(matrix[0])
        def get(i,j):
            cnt=0
            for dx,dy in [(i+1,j),(i-1,j),(i,j-1),(i,j+1),(i+1,j+1),(i-1,j-1),(i+1,j-1),(i-1,j+1)]:
                if 0<=dx<m and 0<=dy<n and not matrix[dx][dy] :
                    cnt+=1
            return not cnt%2 if cnt else False
            
        return sum([True for i in range(m) for j in range(n) if(matrix[i][j] and get(i,j))])

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n, m = input().split()
		n = int(n); m = int(m);
		matrix = []
		for _ in range(n):
			matrix.append(list(map(int,input().split())))
		ob = Solution()
		ans = ob.Count(matrix)
		print(ans)

# } Driver Code Ends