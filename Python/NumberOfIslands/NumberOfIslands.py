#User function Template for python3

import sys
sys.setrecursionlimit(10**8)
class Solution:
    def dfs(self, i, j, n, m, vis, grid):
        # print("{} {}".format(i, j))
        
        vis[i][j] = True
        
        for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1), (i+1, j+1), (i+1, j-1), (i-1, j+1), (i-1, j-1)]:
            # print(x, y)
            if x>=0 and x<n and y>=0 and y<m and vis[x][y] == False and grid[x][y]==1:
                self.dfs(x, y, n, m, vis, grid)
                
    def numIslands(self,grid):
        #code here
        
        N, M = len(grid), len(grid[0])
        vis = [[False for _ in range(m)] for _ in range(n)]
        
        ans = 0
        for i in range(n):
            for j in range(m):
                
                if vis[i][j] == False and grid[i][j] == 1:
                    self.dfs(i, j, N, M, vis, grid)
                    ans += 1
                    
                    
        return ans
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    for _ in range(int(input())):
        n,m=map(int,input().strip().split())
        grid=[]
        for i in range(n):
            grid.append([int(i) for i in input().strip().split()])
        obj=Solution()
        print(obj.numIslands(grid))
# } Driver Code Ends