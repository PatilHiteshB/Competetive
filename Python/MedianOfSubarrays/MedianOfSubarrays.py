#User function Template for python3
class Solution:
    
    def solve(self, A, N, M):
        map = {}
        cur = 0
        tot = 0
        ans = 0
        map[cur] = 1
        
        for i in range(N):
            x = 1 if A[i] >= M else -1
            
            if x == -1:
                tot -= map.get(cur-1, 0)
            else:
                tot += map.get(cur, 0)
                
            cur += x
            ans += tot
            map[cur] = map.get(cur, 0) + 1
        
        return ans
    
    def countSubarray(self, N, A, M):
        v1 = self.solve(A, N, M)
        v2 = self.solve(A, N, M+1)
        
        return v1 - v2




#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        N,M = map(int,input().strip().split())
        A = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.countSubarray(N, A, M)
        print(ans)

# } Driver Code Ends