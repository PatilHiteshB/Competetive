#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    
    def __init__(self):
        
        self.ans = 0
        
    def dfs(self, arr, vis, loop, n, i):
        
        if i<0 or i>=n:
            return True
        
        if vis[i]==True and loop[i]==False:
            return False
        
        if vis[i]==True and loop[i]==True:
            return True
        
        vis[i] = True
        
        if self.dfs(arr, vis, loop, n, arr[i]+i):
            
            self.ans += 1
            loop[i] = True
            
            return True
        
        return False

        
    def goodStones(self, n, arr) -> int:
        #code here
        
        vis = [False for _ in range(n)]
        loop = [False for _ in range(n)]
        
        self.ans = 0
        
        for i in range(n):
            
            if vis[i] == False:
                
                self.dfs(arr, vis, loop, n, i)
                
        return self.ans
        

#{ 
 # Driver Code Starts.

if __name__=="__main__":
    for _ in range(int(input())):
        n = int(input())
        arr = list(map(int, input().split()))
        obj=Solution()
        print(obj.goodStones(n, arr))
        
# } Driver Code Ends