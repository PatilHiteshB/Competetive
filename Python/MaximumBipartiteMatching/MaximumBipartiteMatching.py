#User function Template for python3

class Solution:
    
    def __init__(self):
        self.ans = 0
        
        
    def solve(self, arr, N, M, assignedM, assignedN, depth):
        
        for i in range(M):
            
            if assignedM[i] == False:
                
                for j in range(N):
                    
                    if assignedN[j] == False and arr[i][j] == 1 :
                        
                        assignedM[i] = True
                        assignedN[j] = True
                        depth += 1
                        
                        self.ans = max(self.ans, depth)
                        self.solve(arr, N, M, assignedM, assignedN, depth)
                        
                        depth += -1
                        assignedM[i] = False
                        assignedN[j] = False
                    
        return depth
        
	def maximumMatch(self, arr):
		#code here
		M = len(arr)
		N = len(arr[0])
		self.solve(arr, N, M, [False for i in range(M)], [False for i in range(N)], 0)
		return self.ans
		


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		m, n = map(int, input().strip().split())
		G = []
		for i in range(m):
			G.append(list(map(int, input().strip().split())))
		obj = Solution()
		ans = obj.maximumMatch(G)
		print(ans)
# } Driver Code Ends