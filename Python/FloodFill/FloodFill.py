class Solution:
    
    def floodFill(self, arr, sr, sc, newColor):
        #Code here
        qu = [(sr, sc)]
        n, m = len(arr), len(arr[0])
        start = arr[sr][sc]
        vis = [[False for _ in range(m)] for i in range(n)]
        
        while len(qu) > 0:
            
            i, j = qu.pop(0)
            arr[i][j] = newColor
            vis[i][j] = True
            
            for x, y in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                
                nx, ny = i+x, j+y
                
                if nx >= 0 and nx < n and ny >= 0 and ny < m and arr[nx][ny] == start and vis[nx][ny] == False:

                    qu.append((nx, ny))
                    vis[nx][ny] = True
                    arr[nx][ny] = newColor
                    
        return arr
                    


		            



#{ 
 # Driver Code Starts
import sys
sys.setrecursionlimit(10**7)
if __name__ == '__main__':

	T=int(input())
	for i in range(T):
		n, m = input().split()
		n = int(n)
		m = int(m)
		image = []
		for _ in range(n):
			image.append(list(map(int, input().split())))
		sr, sc, newColor = input().split()
		sr = int(sr); sc = int(sc); newColor = int(newColor);
		obj = Solution()
		ans = obj.floodFill(image, sr, sc, newColor)
		for _ in ans:
			for __ in _:
				print(__, end = " ")
			print()
# } Driver Code Ends