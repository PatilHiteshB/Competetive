#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def isLoop(self, arr, start, loops):
        
        vis = [False for _ in range(len(arr))]
        
        while start < len(arr) and start >= 0:
            
            if vis[start] == False and loops[start] == False:
                vis[start] = True
            else: return True
            
            start += arr[start]
            
        return False
        
    def goodStones(self, n, arr) -> int:
        #code here
        loops = [False for _ in range(n)]
        ans = 0
        
        for i in range(n):
            
            if self.isLoop(arr, i, loops):
                loops[i] = True
            else:
                ans += 1
        
        return ans
        

#{ 
 # Driver Code Starts.

if __name__=="__main__":
    for _ in range(int(input())):
        n = int(input())
        arr = list(map(int, input().split()))
        obj=Solution()
        print(obj.goodStones(n, arr))
        
# } Driver Code Ends