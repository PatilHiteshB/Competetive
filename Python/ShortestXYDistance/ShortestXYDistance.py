#User function Template for python3

class Solution:
    def shortestXYDist(self, arr, N, M):
        # code here 
        x = []
        y = []
        
        for i in range(N):
            for j in range(M):
                
                if arr[i][j] == 'X':
                    x.append((i, j))
                elif arr[i][j] == 'Y':
                    y.append((i, j))
                    
                    
        ans = float('inf')
        for i in x:
            for j in y:
                
                dist = abs(i[0] - j[0]) + abs(i[1] - j[1])
                ans = min(ans, dist)
                
        return ans
                


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