#User function Template for python3

class Solution:
    def __init__(self):
        self.vertices = 0
        self.edges = 0
        
    def dfs(self, node, vis, adj):
        
        vis[node] = True
        self.edges += len(adj[node])
        
        for i in adj[node]:
            
            if vis[i] == False:
                self.vertices += 1
                self.dfs(i, vis, adj)
        
        
        
    def findNumberOfGoodComponent(self, V, adj):
        # code here
        
        vis = [False]*(V+1)
        full = 0
        
        for i in range(1, V+1):
            
            if vis[i] == False:
                
                self.edges = 0
                self.vertices = 1
                
                self.dfs(i, vis, adj)
                
                if self.vertices*(self.vertices-1) == self.edges:
                    full += 1
                
        return full


#{ 
 # Driver Code Starts
#Initial Template for Python 3

from sys import stdin, stdout
if __name__ == '__main__':
    test_cases = int(input())
    for _ in range (test_cases):
        E, V = map(int, input().split())
        adj = [[] for _ in range(V+1)]
        for _ in range(E):
            a,b = map(int, input().split())
            adj[a].append(b)
            adj[b].append(a)
            
        res = Solution().findNumberOfGoodComponent(V, adj)
        print(res)
# } Driver Code Ends