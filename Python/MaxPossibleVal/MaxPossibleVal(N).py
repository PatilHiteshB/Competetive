#User function Template for python3

class Solution:
    def maxPossibleValue(self, N, A, B): 
        #code here
        minLen = float('inf')
        totalLen = totalCount = 0
        
        for i in range(N):
            
            if B[i] > 1:
                
                maxCount = B[i] // 2
                
                totalLen += maxCount * 2 * A[i]
                
                totalCount += maxCount
                
                if A[i] < minLen:
                    minLen = A[i]
                    
            
        if totalCount%2 == 1:
            totalLen -= minLen * 2
        
        return totalLen



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        N = int(input().strip())
        A = list(map(int, input().strip().split()))
        B = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.maxPossibleValue(N, A, B)
        print(ans)

# } Driver Code Ends