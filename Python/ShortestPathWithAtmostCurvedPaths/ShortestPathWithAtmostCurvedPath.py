#User function Template for python3

import heapq

class Solution:
    def dijkstra(self, a, b, n, adj):
        dist = [float('inf')] * (n+1)
        pq = [(0, a)]
        dist[a] = 0

        while pq:
            dis, node = heapq.heappop(pq)

            for v, wt in adj[node]:
                if dist[v] > dist[node] + wt:
                    dist[v] = dist[node] + wt
                    heapq.heappush(pq, (dist[v], v))

        return dist

    def shortestPath(self, n, m, a, b, edges):
        adj = [[] for i in range(n+1)]
        curved = []

        for u, v, wt, cwt in edges:
            adj[u].append((v, wt))
            adj[v].append((u, wt))
            curved.append([u, v, cwt])

        dist1 = self.dijkstra(a, b, n, adj)
        dist2 = self.dijkstra(b, a, n, adj)

        ans = dist1[b]

        for u, v, cwt in curved:
            ans = min(ans, dist1[u]+cwt+dist2[v])
            ans = min(ans, dist1[v]+cwt+dist2[u])

        if ans >= float('inf'):
            return -1

        return ans




#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys 
sys.setrecursionlimit(10**6) 
from heapq import *

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n,m=map(int,input().split())
        a,b=map(int,input().split())
        edges = []
        for i in range(m):
            edge = list(map(int,input().split()))
            edges.append(edge)
        
        ob = Solution()
        print(ob.shortestPath(n,m,a,b,edges))
# } Driver Code Ends