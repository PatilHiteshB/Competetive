#User function Template for python3

class Solution:
    def shortestXYDist(self, arr, N, M):
        # code here 
        
        vis = [[0 for _ in range(M)] for _ in range(N)]
        que = []
        
        for i in range(N):
            for j in range(M):
                
                if arr[i][j] == 'X':
                    que.append([[i, j], 0])
                    vis[i][j] = 1
                    
        dr = [0, 0, -1, 1]
        dc = [1, -1, 0, 0]
        
        
        while len(que) > 0:
            
            node = que.pop(0)
            cr = node[0][0]
            cc = node[0][1]
            
            gap = node[1]
            
            if arr[cr][cc] == 'Y':
                return gap
                
            for k in range(4):
                
                nr = cr+dr[k]
                nc = cc+dc[k]
                
                if 0 <= nr < N and 0 <= nc < M and vis[nr][nc] == 0:
                    que.append([[nr, nc], gap+1])
                    vis[nr][nc] = 1
                    
        return -1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N,M=map(int,input().split())
        grid = []
        for i in range(N):
            ch = list(map(str,input().split()))
            grid.append(ch)
            
        ob = Solution()
        print(ob.shortestXYDist(grid,N,M))
# } Driver Code Ends