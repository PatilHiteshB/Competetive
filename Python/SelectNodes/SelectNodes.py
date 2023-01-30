#User function Template for python3
from queue import PriorityQueue
class Solution:
    def dfs(self, adj, visited, node):
        
        visited[node] = 1
        select = False
        
        for i in adj[node]:
            
            if visited[i] == 0:
                
                isSelected = self.dfs(adj, visited, i)
                
                if isSelected == False:
                    
                    select = True
        
        if select:
            
            self.count += 1
        
        return select
        
    def countVertex(self, N, arr):
        #code here
        self.count = 0
        
        adj = [[] for i in range(N+1)]
        for i in arr:
            u = i[0]
            v = i[1]
            adj[v].append(u)
            adj[u].append(v)
            
        visited = [0 for i in range(N+1)]
        self.dfs(adj, visited, 1)
            
        return self.count
            
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        edges=[]
        for _ in range(N-1):
            arr = list(map(int,input().split()))
            edges.append(arr)

        ob = Solution()
        print(ob.countVertex(N, edges))
# } Driver Code Ends