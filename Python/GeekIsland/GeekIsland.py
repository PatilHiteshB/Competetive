#User function Template for python3

class Solution():
    def water_flow(self, mat, n, m):
        #your code goes here
        
        indian = [[False for i in range(m)] for i in range(n)]
        
        for i in range(n): self.dfs(mat, i, 0, -1, n, m, indian)
        for i in range(m): self.dfs(mat, 0, i, -1, n, m, indian)
        
        arabian = [[False for i in range(m)] for i in range(n)]
        
        for i in range(n): self.dfs(mat, i, m-1, -1, n, m, arabian)
        for i in range(m): self.dfs(mat, n-1, i, -1, n, m, arabian)
        
        cnt = 0
        
        for i in range(n):
            for j in range(m):
                
                if indian[i][j] and arabian[i][j]:
                    cnt += 1
                    
        return cnt
        
        
    def dfs(self, mat, i, j, prev, n, m, canTravel):
        
        dx = [0, 0, -1, 1 ]
	    dy = [-1, 1, 0, 0 ]
        
        if i<0 or j<0 or i>=n or j>=m or canTravel[i][j] or mat[i][j] < prev:
            return
        canTravel[i][j] = True
        
        for k in range(4): self.dfs(mat, i+dx[k], j+dy[k], mat[i][j], n, m, canTravel)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)
if __name__ == "__main__":
    for _ in range(int(input())):
        n,m = map(int, input().split())
        mat = []
        for i in range(n):
            tmp = [int(i) for i in input().split()]
            mat.append(tmp)
        print(Solution().water_flow(mat, n, m))
# } Driver Code Ends