#User function Template for python3

class Solution:
    
    def solve(self, index, vis, adj, ans):
        
        if vis[index] == True:
            return
        
        vis[index] = True
        ans.append(index)
        
        for i in adj[index]:
            self.solve(i, vis, adj, ans)
    
    #Function to return a list containing the DFS traversal of the graph.
    def dfsOfGraph(self, V, adj):
        # code here
        vis = [False for i in range(V)]
        ans = []
        
        for i in range(V):
            if not vis[i]:
                self.solve(i, vis, adj, ans)
                
        
        return ans


#{ 
 # Driver Code Starts

if __name__ == '__main__':
    T=int(input())
    while T>0:
        V,E=map(int,input().split())
        adj=[[] for i in range(V+1)]
        for i in range(E):
            u,v=map(int,input().split())
            adj[u].append(v)
            adj[v].append(u)
        ob=Solution()
        ans=ob.dfsOfGraph(V,adj)
        for i in range(len(ans)):
            print(ans[i],end=" ")
        print()
        T-=1
# } Driver Code Ends