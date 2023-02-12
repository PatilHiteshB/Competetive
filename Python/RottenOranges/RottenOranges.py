class Solution:

        

    #Function to find minimum time required to rot all oranges. 
	def orangesRotting(self, arr):
		#Code here
		
		n = len(grid)
		m = len(grid[0])
		tarr = list(arr)
		
		qu = []
		
        for i in range(n):
            for j in range(m):
                
                if arr[i][j] == 2:
                    
                    qu.append((i, j, 0))
        # print(qu)            
        ans = 0
        
        while len(qu) > 0:
            
            i, j, k = qu.pop(0)
            
            for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                
                nx, ny = x+i, y+j
                
                if nx >=0 and nx < n and ny >= 0 and ny < m and tarr[nx][ny] == 1:
                    # print("{} {}".format(nx, ny))
                    tarr[nx][ny] = 2
                    qu.append((nx, ny, k+1))
                    ans = max(ans, k+1)
                    
            # print(qu)
            
        for i in range(n):
            for j in range(m):
                
                if tarr[i][j] == 1:
                    return -1
                    
        return ans
            

#{ 
 # Driver Code Starts
from queue import Queue

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n, m = map(int, input().split())
		grid = []
		for _ in range(n):
			a = list(map(int, input().split()))
			grid.append(a)
		obj = Solution()
		ans = obj.orangesRotting(grid)
		print(ans)

# } Driver Code Ends