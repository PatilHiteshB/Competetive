#User function Template for python3

class Solution():
    def solve(self, N, K, GeekNum):
        #your code goes here
        if N <= K:
            return GeekNum[N-1]
            
        arr = [0 for _ in range(N)]
        
        for i in range(K):
            arr[i] = GeekNum[i]
        
        su = sum(GeekNum) 
        
        for i in range(K, N):
            
            arr[i] = su
            su = 2*arr[i] - arr[i-K]
            
        return arr[N-1]
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    for _ in range(int(input())):
        N,K=map(int,input().split())
        GeekNum = [int(i) for i in input().split()]
        print(Solution().solve(N, K, GeekNum))
        
    
# } Driver Code Ends