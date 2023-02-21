#User function Template for python3

class Solution:
    def minIteration(self, N, M, x, y):
        #code here
        arr = [[0 for _ in range(M)] for _ in range(N)]
        qu = [(x-1, y-1, 0)]
        arr[x-1][y-1] = 1
        ans = 0
        
        while qu:
            
            # print(qu)
            i, j, k = qu.pop(0)
            for a, b in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                
                if a>=0 and a<N and b>=0 and b<M:
                    
                    if arr[a][b] == 0:
                        
                        qu.append((a, b, k+1))
                        arr[a][b] = 1
                        
                        ans = max(ans, k+1)
                        
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		N, M = map(int,input().split())
		x, y = map(int,input().split())
		ob = Solution()
		print(ob.minIteration(N, M, x, y))
# } Driver Code Ends