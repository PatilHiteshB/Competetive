#User function Template for python3
class Solution:
    
    def wifiRange(self, N, S, X): 
        #code here
        
        visited=[0]*N
        
        for i in range(0,N):
           if(S[i]=='1'):
               visited[max(i-X,0)]+=1
               if i+X+1<N:
                 visited[i+X+1]+=-1
        
        for i in range(1,N):
            visited[i]+=visited[i-1]
        
        for val in visited:
            if val == 0:
                return False
        
        return True
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        N,X = map(int,input().strip().split())
        S = input()
        ob = Solution()
        ans = ob.wifiRange(N, S, X)
        if ans:
            print(1)
        else:
            print(0)

# } Driver Code Ends