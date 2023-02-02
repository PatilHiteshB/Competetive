#User function Template for python3


class Solution():
    def solve(self, p, Edge):
        su = p
        s = p
        p = Edge[s]
        
        while p != s:
            
            su += p
            p = Edge[p]
            
        return su
        
    def largestSumCycle(self, N, Edge):
        #your code goes here
        visited = [False for i in range(N)]
        
        answer = 0
        
        for i in range(len(Edge)):
            
            if not visited[i]:
                
                mp = {}
                visited[i] = True
                
                mp[i] = 0
                p = Edge[i]
                flag = True
                
                while p not in mp.keys():
                    
                    if p == -1 or visited[p]:
                        
                        flag = False
                        break
                    
                    visited[p] = True
                    mp[p] = 0
                    p = Edge[p]
                    
                if flag:
                    answer  = max(self.solve(p, Edge), answer)
                    
                    
        if answer == 0:
            return -1
        return answer
                    
                


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    for _ in range(int(input())):
        N = int(input())
        Edge=[int(i) for i in input().split()]
        print(Solution().largestSumCycle(N, Edge))
# } Driver Code Ends